#define pileupNtuple_cxx
#include "Analysis/JMEDAS/interface/jmedas_pileupNtuple.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>

void pileupNtuple::Loop()
{
//   In a ROOT session, you can do:
//      Root > .L pileupNtuple.C
//      Root > pileupNtuple t
//      Root > t.GetEntry(12); // Fill t data members with entry number 12
//      Root > t.Show();       // Show values of entry 12
//      Root > t.Show(16);     // Read and show values of entry 16
//      Root > t.Loop();       // Loop on all entries
//

//     This is the loop skeleton where:
//    jentry is the global entry number in the chain
//    ientry is the entry number in the current Tree
//  Note that the argument to GetEntry must be:
//    jentry for TChain::GetEntry
//    ientry for TTree::GetEntry and TBranch::GetEntry
//
//       To read only selected branches, Insert statements like:
// METHOD1:
//    fChain->SetBranchStatus("*",0);  // disable all branches
//    fChain->SetBranchStatus("branchname",1);  // activate branchname
// METHOD2: replace line
//    fChain->GetEntry(jentry);       //read all branches
//by  b_branchname->GetEntry(ientry); //read only this branch
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;
   }
}

//______________________________________________________________________________
int pileupNtuple::itIndex() {
   for(unsigned int ibx=0; ibx<(*bxns).size(); ibx++) {
      if((*bxns)[ibx]==0) return ibx;
   }
   return -1;
}

//______________________________________________________________________________
double pileupNtuple::sumEOOT() {
   int iIT = itIndex();
   if(iIT>(int)(*npus).size()-1) return 0;
   double sum = 0;
   for(int ipu=0; ipu<iIT; ipu++) {
      sum+=(*npus)[ipu];
   }
   return sum;
}

//______________________________________________________________________________
double pileupNtuple::sumLOOT() {
   int iIT = itIndex();
   if(iIT>(int)(*npus).size()-1) return 0;
   double sum = 0;
   for(int ipu=(*npus).size()-1; ipu>iIT; ipu--) {
      sum+=(*npus)[ipu];
   }
   return sum;
}

//______________________________________________________________________________
bool CheckValue(ROOT::Internal::TTreeReaderValueBase* value) {
   if (value->GetSetupStatus() < 0) {
      std::cerr << "Error " << value->GetSetupStatus()
                << "setting up reader for " << value->GetBranchName() << '\n';
      return false;
   }
   return true;
}

//______________________________________________________________________________
void pileupNtuple::printJEC(Long64_t entry, Long64_t jet) {
   // The TTreeReader gives access to the TTree to the TTreeReaderValue and
   // TTreeReaderArray objects. It knows the current entry number and knows
   // how to iterate through the TTree.
   TTreeReader reader(fChain);
   // Read a single float value in each tree entries:
   TTreeReaderArray<JECInfo> r_jtjec(reader, "jtjec");
   //if (!CheckValue(r_jtjec)) {
   //   std::cout << "ERROR::pileupNtuple::printJEC Can't read information from the jtjec branch" << std::endl;
   //   return;
   //}

   // Now iterate through the TTree entries and print
   while (reader.Next()) {
      if(entry>-1)
         reader.SetEntry(entry);

      if (reader.GetEntryStatus() == TTreeReader::kEntryValid) {
         std::cout << "Loaded entry " << reader.GetCurrentEntry() << '\n';
      }
      else {
         return;
      }

      unsigned int min = (jet>-1) ? jet : 0;
      unsigned int max = (jet>-1) ? jet+1 : r_jtjec.GetSize();
      for(unsigned int ijet=min; ijet<max; ijet++) {
         std::cout << "\tJet " << ijet << ":" << std::endl;
         for(unsigned int ijec=0; ijec<r_jtjec[ijet].size(); ijec++) {
            std::cout << "\t\tJEC level: " << r_jtjec[ijet][ijec].first << "\tJEC Factor: " << r_jtjec[ijet][ijec].second << std::endl;
         }
      }

      if(entry>-1)
         break;
   } // TTree entry / event loop
}
