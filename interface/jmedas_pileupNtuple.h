//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Jan 16 15:35:42 2014 by ROOT version 5.32/00
// from TTree t/t
//////////////////////////////////////////////////////////

#ifndef pileupNtuple_h
#define pileupNtuple_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include "TTree.h"
#include "TTreeReader.h"
#include "TTreeReaderValue.h"
#include "TTreeReaderArray.h"

// Header file for the classes stored in the TTree if any.
#include <string>
#include <vector>
#include <utility>

// Fixed size dimensions of array or collections stored in the TTree if any.

using std::string;
using std::vector;
using std::pair;

typedef vector<pair<string, float> > JECInfo;

class pileupNtuple {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Declaration of leaf types
   vector<int>*    npus;
   vector<float>*  tnpus;
   vector<int>*    bxns;
   Float_t         rho;
   Float_t         beta;
   Float_t         betaStar;
   Long64_t        npv;
   Long64_t        run;
   Long64_t        lumi;
   Long64_t        evt;
   //UChar_t         nref;
   //vector<int>*    refrank;
   vector<int>*    refpdgid;
   vector<int>*    refpdgid_algorithmicDef;
   vector<int>*    refpdgid_physicsDef;
   vector<float>*  refe;
   vector<float>*  refpt;
   vector<float>*  refeta;
   vector<float>*  refphi;
   vector<float>*  refy;
   vector<float>*  refdrjt;
   vector<float>*  refarea;
   vector<float>*  jte;
   vector<float>*  jtpt;
   vector<float>*  jteta;
   vector<float>*  jtphi;
   vector<float>*  jty;
   //vector<float>*  jtjec;
   vector<JECInfo>*  jtjec;
   vector<float>*  jtarea;
   vector<float>*  jtchf;
   vector<float>*  jtnhf;
   vector<float>*  jtnef;
   vector<float>*  jtcef;
   vector<float>*  jtmuf;
   vector<float>*  jthfhf;
   vector<float>*  jthfef;
   vector<float>*  mupt;
   vector<float>*  mueta;
   vector<float>*  muphi;
   vector<float>*  mue;
   vector<float>*  muIso_PuppiCombined;
   vector<float>*  muIso_PuppiCombined_CH;
   vector<float>*  muIso_PuppiCombined_NH;
   vector<float>*  muIso_PuppiCombined_PH;
   vector<float>*  muIso_PuppiWithLep;
   vector<float>*  muIso_PuppiWithLep_CH;
   vector<float>*  muIso_PuppiWithLep_NH;
   vector<float>*  muIso_PuppiWithLep_PH;
   vector<float>*  muIso_PuppiWithoutLep;
   vector<float>*  muIso_PuppiWithoutLep_CH;
   vector<float>*  muIso_PuppiWithoutLep_NH;
   vector<float>*  muIso_PuppiWithoutLep_PH;
   vector<float>*  metpt;
   vector<float>*  meteta;
   vector<float>*  metphi;
   vector<float>*  mete;
   vector<float>*  metNoHFpt;
   vector<float>*  metNoHFeta;
   vector<float>*  metNoHFphi;
   vector<float>*  metNoHFe;
   vector<float>*  metPUPPIpt;
   vector<float>*  metPUPPIeta;
   vector<float>*  metPUPPIphi;
   vector<float>*  metPUPPIe;

   // List of branches
   TBranch        *b_npus;   //!
   TBranch        *b_tnpus;   //!
   TBranch        *b_bxns;   //!
   TBranch        *b_rho;   //!
   TBranch        *b_beta;   //!
   TBranch        *b_betaStar;   //!
   TBranch        *b_npv;   //!
   TBranch        *b_run;   //!
   TBranch        *b_lumi;   //!
   TBranch        *b_evt;   //!
   TBranch        *b_nref;   //!
   TBranch        *b_refrank;   //!
   TBranch        *b_refpdgid;   //!
   TBranch        *b_refpdgid_algorithmicDef;   //!
   TBranch        *b_refpdgid_physicsDef;   //!
   TBranch        *b_refe;   //!
   TBranch        *b_refpt;   //!
   TBranch        *b_refeta;   //!
   TBranch        *b_refphi;   //!
   TBranch        *b_refy;   //!
   TBranch        *b_refdrjt;   //!
   TBranch        *b_refarea;   //!
   TBranch        *b_jte;   //!
   TBranch        *b_jtpt;   //!
   TBranch        *b_jteta;   //!
   TBranch        *b_jtphi;   //!
   TBranch        *b_jty;   //!
   TBranch        *b_jtjec;   //!
   TBranch        *b_jtarea;   //!
   TBranch        *b_jtchf;   //!
   TBranch        *b_jtnhf;   //!
   TBranch        *b_jtnef;   //!
   TBranch        *b_jtcef;   //!
   TBranch        *b_jtmuf;   //!
   TBranch        *b_jthfhf;   //!
   TBranch        *b_jthfef;   //!
   TBranch        *b_mupt;   //!
   TBranch        *b_mueta;   //!
   TBranch        *b_muphi;   //!
   TBranch        *b_mue;   //!
   TBranch        *b_muIso_PuppiCombined;   //!
   TBranch        *b_muIso_PuppiCombined_CH;   //!
   TBranch        *b_muIso_PuppiCombined_NH;   //!
   TBranch        *b_muIso_PuppiCombined_PH;   //!
   TBranch        *b_muIso_PuppiWithLep;   //!
   TBranch        *b_muIso_PuppiWithLep_CH;   //!
   TBranch        *b_muIso_PuppiWithLep_NH;   //!
   TBranch        *b_muIso_PuppiWithLep_PH;   //!
   TBranch        *b_muIso_PuppiWithoutLep;   //!
   TBranch        *b_muIso_PuppiWithoutLep_CH;   //!
   TBranch        *b_muIso_PuppiWithoutLep_NH;   //!
   TBranch        *b_muIso_PuppiWithoutLep_PH;   //!
   TBranch        *b_metpt;   //!
   TBranch        *b_meteta;   //!
   TBranch        *b_metphi;   //!
   TBranch        *b_mete;   //!
   TBranch        *b_metNoHFpt;   //!
   TBranch        *b_metNoHFeta;   //!
   TBranch        *b_metNoHFphi;   //!
   TBranch        *b_metNoHFe;   //!
   TBranch        *b_metPUPPIpt;   //!
   TBranch        *b_metPUPPIeta;   //!
   TBranch        *b_metPUPPIphi;   //!
   TBranch        *b_metPUPPIe;   //!

   pileupNtuple(TTree *tree=0, bool newTree = false);
   virtual ~pileupNtuple();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
   virtual void     MakeTree(TTree *tree);
   virtual void     MakeVectors();
   virtual void     clear();

   int itIndex();
   double sumEOOT();
   double sumLOOT();
   bool CheckValue(ROOT::TTreeReaderValueBase* value);
   void printJEC(Long64_t entry = -1, Long64_t jet = -1);
};

#endif

#ifdef pileupNtuple_cxx
pileupNtuple::pileupNtuple(TTree *tree, bool newTree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if(newTree) {
      MakeTree(tree);
   }
   else {
      Init(tree);
   }
}

pileupNtuple::~pileupNtuple()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t pileupNtuple::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t pileupNtuple::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void pileupNtuple::MakeTree(TTree *tree)
{
   gROOT->ProcessLine("#include <vector>");

   // Set vector pointers
   MakeVectors();

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->Branch("npus", "vector<Int_t>", &npus);
   fChain->Branch("tnpus", "vector<Float_t>", &tnpus);
   fChain->Branch("bxns", "vector<Int_t>", &bxns);
   fChain->Branch("rho", &rho, "rho/F");
   fChain->Branch("beta", &beta, "beta/F");
   fChain->Branch("betaStar", &betaStar, "betaStar/F");
   fChain->Branch("npv", &npv, "npv/L");
   fChain->Branch("run", &run, "run/L");
   fChain->Branch("lumi", &lumi, "lumi/L");
   fChain->Branch("evt", &evt, "evt/L");
   //fChain->Branch("nref", &nref, "nref/b");
   //fChain->Branch("refrank", refrank, "refrank[nref]/I");
   fChain->Branch("refpdgid", "vector<Int_t>", &refpdgid);
   fChain->Branch("refpdgid_algorithmicDef", "vector<Int_t>", &refpdgid_algorithmicDef);
   fChain->Branch("refpdgid_physicsDef", "vector<Int_t>", &refpdgid_physicsDef);
   fChain->Branch("refe", "vector<Float_t>", &refe);
   fChain->Branch("refpt", "vector<Float_t>", &refpt);
   fChain->Branch("refeta", "vector<Float_t>", &refeta);
   fChain->Branch("refphi", "vector<Float_t>", &refphi);
   fChain->Branch("refy", "vector<Float_t>", &refy);
   fChain->Branch("refdrjt", "vector<Float_t>", &refdrjt);
   fChain->Branch("refarea", "vector<Float_t>", &refarea);
   fChain->Branch("jte", "vector<Float_t>", &jte);
   fChain->Branch("jtpt", "vector<Float_t>", &jtpt);
   fChain->Branch("jteta", "vector<Float_t>", &jteta);
   fChain->Branch("jtphi", "vector<Float_t>", &jtphi);
   fChain->Branch("jty", "vector<Float_t>", &jty);
   //fChain->Branch("jtjec", "vector<Float_t>", &jtjec);
   fChain->Branch("jtjec", &jtjec);
   fChain->Branch("jtarea", "vector<Float_t>", &jtarea);
   fChain->Branch("jtchf", "vector<Float_t>", &jtchf);
   fChain->Branch("jtnhf", "vector<Float_t>", &jtnhf);
   fChain->Branch("jtnef", "vector<Float_t>", &jtnef);
   fChain->Branch("jtcef", "vector<Float_t>", &jtcef);
   fChain->Branch("jtmuf", "vector<Float_t>", &jtmuf);
   fChain->Branch("jthfhf", "vector<Float_t>", &jthfhf);
   fChain->Branch("jthfef", "vector<Float_t>", &jthfef);
   fChain->Branch("mupt", "vector<Float_t>", &mupt);
   fChain->Branch("mueta", "vector<Float_t>", &mueta);
   fChain->Branch("muphi", "vector<Float_t>", &muphi);
   fChain->Branch("mue", "vector<Float_t>", &mue);
   fChain->Branch("muIso_PuppiCombined", "vector<Float_t>", &muIso_PuppiCombined);
   fChain->Branch("muIso_PuppiCombined_CH", "vector<Float_t>", &muIso_PuppiCombined_CH);
   fChain->Branch("muIso_PuppiCombined_NH", "vector<Float_t>", &muIso_PuppiCombined_NH);
   fChain->Branch("muIso_PuppiCombined_PH", "vector<Float_t>", &muIso_PuppiCombined_PH);
   fChain->Branch("muIso_PuppiWithLep", "vector<Float_t>", &muIso_PuppiWithLep);
   fChain->Branch("muIso_PuppiWithLep_CH", "vector<Float_t>", &muIso_PuppiWithLep_CH);
   fChain->Branch("muIso_PuppiWithLep_NH", "vector<Float_t>", &muIso_PuppiWithLep_NH);
   fChain->Branch("muIso_PuppiWithLep_PH", "vector<Float_t>", &muIso_PuppiWithLep_PH);
   fChain->Branch("muIso_PuppiWithoutLep", "vector<Float_t>", &muIso_PuppiWithoutLep);
   fChain->Branch("muIso_PuppiWithoutLep_CH", "vector<Float_t>", &muIso_PuppiWithoutLep_CH);
   fChain->Branch("muIso_PuppiWithoutLep_NH", "vector<Float_t>", &muIso_PuppiWithoutLep_NH);
   fChain->Branch("muIso_PuppiWithoutLep_PH", "vector<Float_t>", &muIso_PuppiWithoutLep_PH);
   fChain->Branch("metpt", "vector<Float_t>", &metpt);
   fChain->Branch("meteta", "vector<Float_t>", &meteta);
   fChain->Branch("metphi", "vector<Float_t>", &metphi);
   fChain->Branch("mete", "vector<Float_t>", &mete);
   fChain->Branch("metNoHFpt", "vector<Float_t>", &metNoHFpt);
   fChain->Branch("metNoHFeta", "vector<Float_t>", &metNoHFeta);
   fChain->Branch("metNoHFphi", "vector<Float_t>", &metNoHFphi);
   fChain->Branch("metNoHFe", "vector<Float_t>", &metNoHFe);
   fChain->Branch("metPUPPIpt", "vector<Float_t>", &metPUPPIpt);
   fChain->Branch("metPUPPIeta", "vector<Float_t>", &metPUPPIeta);
   fChain->Branch("metPUPPIphi", "vector<Float_t>", &metPUPPIphi);
   fChain->Branch("metPUPPIe", "vector<Float_t>", &metPUPPIe);
   Notify();
}

void pileupNtuple::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set vector pointers
   MakeVectors();

   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("npus", &npus, &b_npus);
   fChain->SetBranchAddress("tnpus", &tnpus, &b_tnpus);
   fChain->SetBranchAddress("bxns", &bxns, &b_bxns);
   fChain->SetBranchAddress("rho", &rho, &b_rho);
   fChain->SetBranchAddress("beta", &beta, &b_beta);
   fChain->SetBranchAddress("betaStar", &betaStar, &b_betaStar);
   fChain->SetBranchAddress("npv", &npv, &b_npv);
   fChain->SetBranchAddress("run", &run, &b_run);
   fChain->SetBranchAddress("lumi", &lumi, &b_lumi);
   fChain->SetBranchAddress("evt", &evt, &b_evt);
   //fChain->SetBranchAddress("nref", &nref, &b_nref);
   //fChain->SetBranchAddress("refrank", refrank, &b_refrank);
   fChain->SetBranchAddress("refpdgid", &refpdgid, &b_refpdgid);
   fChain->SetBranchAddress("refpdgid_algorithmicDef", &refpdgid_algorithmicDef, &b_refpdgid_algorithmicDef);
   fChain->SetBranchAddress("refpdgid_physicsDef", &refpdgid_physicsDef, &b_refpdgid_physicsDef);
   fChain->SetBranchAddress("refe", &refe, &b_refe);
   fChain->SetBranchAddress("refpt", &refpt, &b_refpt);
   fChain->SetBranchAddress("refeta", &refeta, &b_refeta);
   fChain->SetBranchAddress("refphi", &refphi, &b_refphi);
   fChain->SetBranchAddress("refy", &refy, &b_refy);
   fChain->SetBranchAddress("refdrjt", &refdrjt, &b_refdrjt);
   fChain->SetBranchAddress("refarea", &refarea, &b_refarea);
   fChain->SetBranchAddress("jte", &jte, &b_jte);
   fChain->SetBranchAddress("jtpt", &jtpt, &b_jtpt);
   fChain->SetBranchAddress("jteta", &jteta, &b_jteta);
   fChain->SetBranchAddress("jtphi", &jtphi, &b_jtphi);
   fChain->SetBranchAddress("jty", &jty, &b_jty);
   fChain->SetBranchAddress("jtjec", &jtjec, &b_jtjec);
   fChain->SetBranchAddress("jtarea", &jtarea, &b_jtarea);
   fChain->SetBranchAddress("jtchf", &jtchf, &b_jtchf);
   fChain->SetBranchAddress("jtnhf", &jtnhf, &b_jtnhf);
   fChain->SetBranchAddress("jtnef", &jtnef, &b_jtnef);
   fChain->SetBranchAddress("jtcef", &jtcef, &b_jtcef);
   fChain->SetBranchAddress("jtmuf", &jtmuf, &b_jtmuf);
   fChain->SetBranchAddress("jthfhf", &jthfhf, &b_jthfhf);
   fChain->SetBranchAddress("jthfef", &jthfef, &b_jthfef);
   fChain->SetBranchAddress("mupt", &mupt, &b_mupt);
   fChain->SetBranchAddress("mueta", &mueta, &b_mueta);
   fChain->SetBranchAddress("muphi", &muphi, &b_muphi);
   fChain->SetBranchAddress("mue", &mue, &b_mue);
   fChain->SetBranchAddress("muIso_PuppiCombined", &muIso_PuppiCombined, &b_muIso_PuppiCombined);
   fChain->SetBranchAddress("muIso_PuppiCombined_CH", &muIso_PuppiCombined_CH, &b_muIso_PuppiCombined_CH);
   fChain->SetBranchAddress("muIso_PuppiCombined_NH", &muIso_PuppiCombined_NH, &b_muIso_PuppiCombined_NH);
   fChain->SetBranchAddress("muIso_PuppiCombined_PH", &muIso_PuppiCombined_PH, &b_muIso_PuppiCombined_PH);
   fChain->SetBranchAddress("muIso_PuppiWithLep", &muIso_PuppiWithLep, &b_muIso_PuppiWithLep);
   fChain->SetBranchAddress("muIso_PuppiWithLep_CH", &muIso_PuppiWithLep_CH, &b_muIso_PuppiWithLep_CH);
   fChain->SetBranchAddress("muIso_PuppiWithLep_NH", &muIso_PuppiWithLep_NH, &b_muIso_PuppiWithLep_NH);
   fChain->SetBranchAddress("muIso_PuppiWithLep_PH", &muIso_PuppiWithLep_PH, &b_muIso_PuppiWithLep_PH);
   fChain->SetBranchAddress("muIso_PuppiWithoutLep", &muIso_PuppiWithoutLep, &b_muIso_PuppiWithoutLep);
   fChain->SetBranchAddress("muIso_PuppiWithoutLep_CH", &muIso_PuppiWithoutLep_CH, &b_muIso_PuppiWithoutLep_CH);
   fChain->SetBranchAddress("muIso_PuppiWithoutLep_NH", &muIso_PuppiWithoutLep_NH, &b_muIso_PuppiWithoutLep_NH);
   fChain->SetBranchAddress("muIso_PuppiWithoutLep_PH", &muIso_PuppiWithoutLep_PH, &b_muIso_PuppiWithoutLep_PH);
   fChain->SetBranchAddress("metpt", &metpt, &b_metpt);
   fChain->SetBranchAddress("meteta", &meteta, &b_meteta);
   fChain->SetBranchAddress("metphi", &metphi, &b_metphi);
   fChain->SetBranchAddress("mete", &mete, &b_mete);
   fChain->SetBranchAddress("metNoHFpt", &metNoHFpt, &b_metNoHFpt);
   fChain->SetBranchAddress("metNoHFeta", &metNoHFeta, &b_metNoHFeta);
   fChain->SetBranchAddress("metNoHFphi", &metNoHFphi, &b_metNoHFphi);
   fChain->SetBranchAddress("metNoHFe", &metNoHFe, &b_metNoHFe);
   fChain->SetBranchAddress("metPUPPIpt", &metPUPPIpt, &b_metPUPPIpt);
   fChain->SetBranchAddress("metPUPPIeta", &metPUPPIeta, &b_metPUPPIeta);
   fChain->SetBranchAddress("metPUPPIphi", &metPUPPIphi, &b_metPUPPIphi);
   fChain->SetBranchAddress("metPUPPIe", &metPUPPIe, &b_metPUPPIe);

   Notify();
}

Bool_t pileupNtuple::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void pileupNtuple::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t pileupNtuple::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
void pileupNtuple::MakeVectors()
{
   npus                     = new vector<int>;
   tnpus                    = new vector<float>;
   bxns                     = new vector<int>;
   refpdgid                 = new vector<int>;
   refpdgid_algorithmicDef  = new vector<int>;
   refpdgid_physicsDef      = new vector<int>;
   refe                     = new vector<float>;
   refpt                    = new vector<float>;
   refeta                   = new vector<float>;
   refphi                   = new vector<float>;
   refy                     = new vector<float>;
   refdrjt                  = new vector<float>;
   refarea                  = new vector<float>;
   jte                      = new vector<float>;
   jtpt                     = new vector<float>;
   jteta                    = new vector<float>;
   jtphi                    = new vector<float>;
   jty                      = new vector<float>;
   //jtjec                    = new vector<float>;
   jtjec                    = new vector<JECInfo>;
   jtarea                   = new vector<float>;
   jtchf                    = new vector<float>;
   jtnhf                    = new vector<float>;
   jtnef                    = new vector<float>;
   jtcef                    = new vector<float>;
   jtmuf                    = new vector<float>;
   jthfhf                   = new vector<float>;
   jthfef                   = new vector<float>;
   mupt                     = new vector<float>;
   mueta                    = new vector<float>;
   muphi                    = new vector<float>;
   mue                      = new vector<float>;
   muIso_PuppiCombined      = new vector<float>;
   muIso_PuppiCombined_CH   = new vector<float>;
   muIso_PuppiCombined_NH   = new vector<float>;
   muIso_PuppiCombined_PH   = new vector<float>;
   muIso_PuppiWithLep       = new vector<float>;
   muIso_PuppiWithLep_CH    = new vector<float>;
   muIso_PuppiWithLep_NH    = new vector<float>;
   muIso_PuppiWithLep_PH    = new vector<float>;
   muIso_PuppiWithoutLep    = new vector<float>;
   muIso_PuppiWithoutLep_CH = new vector<float>;
   muIso_PuppiWithoutLep_NH = new vector<float>;
   muIso_PuppiWithoutLep_PH = new vector<float>;
   metpt                    = new vector<float>;
   meteta                   = new vector<float>;
   metphi                   = new vector<float>;
   mete                     = new vector<float>;
   metNoHFpt                = new vector<float>;
   metNoHFeta               = new vector<float>;
   metNoHFphi               = new vector<float>;
   metNoHFe                 = new vector<float>;
   metPUPPIpt               = new vector<float>;
   metPUPPIeta              = new vector<float>;
   metPUPPIphi              = new vector<float>;
   metPUPPIe                = new vector<float>;
}
void pileupNtuple::clear()
{
   npus->clear();
   tnpus->clear();
   bxns->clear();
   refpdgid->clear();
   refpdgid_algorithmicDef->clear();
   refpdgid_physicsDef->clear();
   refe->clear();
   refpt->clear();
   refeta->clear();
   refphi->clear();
   refy->clear();
   refdrjt->clear();
   refarea->clear();
   jte->clear();
   jtpt->clear();
   jteta->clear();
   jtphi->clear();
   jty->clear();
   jtjec->clear();
   jtarea->clear();
   jtchf->clear();
   jtnhf->clear();
   jtnef->clear();
   jtcef->clear();
   jtmuf->clear();
   jthfhf->clear();
   jthfef->clear();
   mupt->clear();
   mueta->clear();
   muphi->clear();
   mue->clear();
   muIso_PuppiCombined->clear();
   muIso_PuppiCombined_CH->clear();
   muIso_PuppiCombined_NH->clear();
   muIso_PuppiCombined_PH->clear();
   muIso_PuppiWithLep->clear();
   muIso_PuppiWithLep_CH->clear();
   muIso_PuppiWithLep_NH->clear();
   muIso_PuppiWithLep_PH->clear();
   muIso_PuppiWithoutLep->clear();
   muIso_PuppiWithoutLep_CH->clear();
   muIso_PuppiWithoutLep_NH->clear();
   muIso_PuppiWithoutLep_PH->clear();
   metpt->clear();
   meteta->clear();
   metphi->clear();
   mete->clear();
   metNoHFpt->clear();
   metNoHFeta->clear();
   metNoHFphi->clear();
   metNoHFe->clear();
   metPUPPIpt->clear();
   metPUPPIeta->clear();
   metPUPPIphi->clear();
   metPUPPIe->clear();
}
#endif // #ifdef pileupNtuple_cxx
