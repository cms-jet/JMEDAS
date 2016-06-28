void compare2DQuantities(string filename1, string var1, string var2, int nbins, float min, float max, int nbinsY, float minY, float maxY, string cut){

	gStyle->SetOptStat(0);
	gROOT->SetStyle("Plain");

	TFile *inputFile1 = new TFile(filename1.c_str());

	TTree *jetTree1 = (TTree *) inputFile1->Get("varTree");

	TH2F *var1H = new TH2F("var1H", "var1H", nbins, min, max, nbinsY, minY, maxY);
	

	cout << var1 << "  " << var2 << endl;	

	jetTree1->Draw(Form("%s:%s>>var1H",var1.c_str(), var2.c_str()), cut.c_str(), "goff");





	//var1H->SetMaximum( TMath::Max(var1H->GetMaximum(), var2H->GetMaximum()) * 1.25 );

	

  TCanvas *c1236= new TCanvas("c1236","",200,10,800,700);

	var1H->GetXaxis()->SetTitle(var2.c_str());
	var1H->GetYaxis()->SetTitle(var1.c_str());
	var1H->DrawNormalized("colz");
	
 string savename = "plots2/hist2d_"+var1+"_"+var2+"_"+filename1+".pdf";

  c1236->SaveAs(savename.c_str ());


}


