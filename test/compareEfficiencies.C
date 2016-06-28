void compareEfficiencies(string filename1, string filename2, string variable, int nbins, float min, float max, string DenomCut = "", string NumCut = ""){


	if (filename2 == "") filename2 = filename1;


	gStyle->SetOptStat(0);
	gROOT->SetStyle("Plain");

	TFile *inputFile1 = new TFile(filename1.c_str());
	TFile *inputFile2 = new TFile(filename2.c_str());

	TTree *jetTree1 = (TTree *) inputFile1->Get("varTree");
	TTree *jetTree2 = (TTree *) inputFile2->Get("varTree");

	TH1F *var1NumH = new TH1F("var1NumH", "var1NumH", nbins, min, max);
	TH1F *var2NumH = new TH1F("var2NumH", "var2NumH", nbins, min, max);
	TH1F *var1DenH = new TH1F("var1DenH", "var1DenH", nbins, min, max);
	TH1F *var2DenH = new TH1F("var2DenH", "var2DenH", nbins, min, max);
	

	cout << variable << endl;	

	jetTree1->Draw(Form("%s>>var1NumH",variable.c_str()), Form("%s && %s", NumCut.c_str(), DenomCut.c_str()), "goff");
	jetTree2->Draw(Form("%s>>var2NumH",variable.c_str()), Form("%s && %s", NumCut.c_str(), DenomCut.c_str()), "goff");
	jetTree1->Draw(Form("%s>>var1DenH",variable.c_str()), DenomCut.c_str(), "goff");
	jetTree2->Draw(Form("%s>>var2DenH",variable.c_str()), DenomCut.c_str(), "goff");




	TH1F *ratio1H = (TH1F *) var1NumH->Clone("ratio1H");
	ratio1H->Sumw2();
	ratio1H->Divide(var1NumH, var1DenH, 1, 1, "B");
	TH1F *ratio2H = (TH1F *) var2NumH->Clone("ratio2H");
	ratio2H->Sumw2();
	ratio2H->Divide(var2NumH, var2DenH, 1, 1, "B");

	ratio1H->SetLineWidth(2);
	ratio2H->SetLineWidth(2);

	ratio1H->SetLineColor(kRed);
	ratio2H->SetLineColor(kBlue);
	
	ratio1H->SetMaximum( TMath::Max(ratio1H->GetMaximum(), ratio2H->GetMaximum()) * 1.25 );

	ratio1H->GetXaxis()->SetTitle(variable.c_str());
	ratio1H->GetYaxis()->SetTitle("Tagging Rate");


	ratio1H->Draw("E");
	ratio2H->Draw("E same");
	

	TLegend *leg = new TLegend(0.1,0.9,0.9,0.99);
	leg->SetFillColor(0);
	leg->SetNColumns(2);
	leg->AddEntry(ratio1H, filename1.c_str(), "l");
	leg->AddEntry(ratio2H, filename2.c_str(), "l");
	leg->Draw("same");

}


