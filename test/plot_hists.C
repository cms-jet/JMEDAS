// root [0] .L plot_hists.C+
// root [1] run()

#include <vector>
#include <string>
#include <algorithm> 
#include <iostream>
#include <cmath>
#include "TStyle.h"
#include "TFile.h"
#include "TH1.h"
#include "TCanvas.h"
#include "TLegend.h"
using namespace std;

void DrawHists(std::string, std::string, std::string, TFile*, TFile*, std::string, std::string); 

void run(){
  gStyle->SetOptStat(0);
  TFile *Fzp    = new TFile("histoszp.root");
  TFile *Fqcd   = new TFile("histosqcd.root");

  DrawHists("testGroomAK12","h_ak12chs_mass", "h_ak12chs_softDropMass", Fzp, Fzp, "Fat jet mass", "soft drop mass" );
  DrawHists("testGroomAK12","h_ak12chs_mass", "h_ak12chs_prunedMass"  , Fzp, Fzp, "Fat jet mass", "pruned mass"    );
  DrawHists("testGroomAK12","h_ak12chs_mass", "h_ak12chs_trimedMass"  , Fzp, Fzp, "Fat jet mass", "trimed mass"    );
  DrawHists("testGroomAK12","h_ak12chs_mass", "h_ak12chs_filteredMass", Fzp, Fzp, "Fat jet mass", "filtered mass"  );


  DrawHists("compareTtbarQCD","h_ak12chs_mass", "h_ak12chs_mass", Fzp, Fqcd, "Fat jet mass - ttbar", "Fat jet mass - qcd" );
  DrawHists("compareTtbarQCD","h_ak12chs_softDropMass", "h_ak12chs_softDropMass", Fzp, Fqcd, "Soft drop jet mass - ttbar", "Soft drop jet mass - qcd" );
}

void DrawHists(std::string savelabel, std::string histoname1, std::string histoname2, TFile* f1, TFile* f2, std::string L1, std::string L2  ){ 
  string shistoname1 = "ana/"+histoname1 ;
  string shistoname2 = "ana/"+histoname2 ;
  TH1D *h1  = (TH1D*)f1->Get(shistoname1.c_str());
  TH1D *h2  = (TH1D*)f2->Get(shistoname2.c_str());
  if (h1 && h2){
    TCanvas *c1 = new TCanvas("c1","my canvas",200,10,900,700);
    double m1=h1->GetMaximum();
    double m2=h2->GetMaximum();    
    vector<double> v;
    v.push_back(m1);
    v.push_back(m2);
    vector<double>::const_iterator largest = max_element(v.begin(),v.end());
    double max  = *largest;
        
    h1->SetLineColor(1);
    h2->SetLineColor(2);
    
    h1->SetLineWidth(2);
    h2->SetLineWidth(2);

    h1->SetFillColor(0);
    h2->SetFillColor(0);
        
    h1->SetTitle("");
    h2->SetTitle("");

    if(m1==max){
      h1->Draw();
      h2->Draw("same");
    } 
    if(m2==max){
      h2->Draw();
      h1->Draw("same");
    }
    h1->Draw("same");
    h2->Draw("same");

    TLegend leg(0.6,0.76,0.82,0.88);
    leg.SetBorderSize(0);
    leg.SetFillColor(0);
    leg.AddEntry(h1,L1.c_str(),"L");
    leg.AddEntry(h2,L2.c_str(),"L");
    leg.Draw("same");
    
    c1->Update();
    string savename = savelabel+"_"+histoname1+"_"+histoname2+".pdf";
    c1->SaveAs(savename.c_str());
    delete c1;
    delete h1;
    delete h2;
  }
  else {cout<<"DID NOT GET HISTOS"<<endl;}
}

