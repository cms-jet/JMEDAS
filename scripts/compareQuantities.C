void compareQuantities(string filename1, string filename2, string var1, string var2, int nbins, float min, float max, string cut = ""){

  TCanvas *c1236= new TCanvas("c1236","",200,10,800,700);

	if (filename2 == "") filename2 = filename1;

	gStyle->SetOptStat(0);
	gROOT->SetStyle("Plain");

	TFile *inputFile1 = new TFile(filename1.c_str());
	TFile *inputFile2 = new TFile(filename2.c_str());

	TTree *jetTree1 = (TTree *) inputFile1->Get("varTree");
	TTree *jetTree2 = (TTree *) inputFile2->Get("varTree");

	TH1F *var1H = new TH1F("var1H", "", nbins, min, max);
	TH1F *var2H = new TH1F("var2H", "", nbins, min, max);
	

	cout << var1 << "  " << var2 << endl;	

	jetTree1->Draw(Form("%s>>var1H",var1.c_str()), cut.c_str(), "goff");
	jetTree2->Draw(Form("%s>>var2H",var2.c_str()), cut.c_str(), "goff");

	cout << var1H->GetEntries() << " " << var2H->GetEntries() << endl;

	var1H->SetLineWidth(2);
	var2H->SetLineWidth(2);

	var1H->SetLineColor(kRed);
	var2H->SetLineColor(kBlue);


	var1H->SetMaximum( TMath::Max(var1H->GetMaximum(), var2H->GetMaximum())  );

	var1H->GetXaxis()->SetTitle("Quantity");
	var1H->GetYaxis()->SetTitle("Fraction of Events");

  string savename = "plots/"+var1+"_"+var2+"_"+filename1+"_"+filename2+".pdf";

    if (var1==var2) 
    {
        var1H->GetXaxis()->SetTitle(var1.c_str());
        var1 = filename1;
        var2 = filename2;
    }

	var1H->DrawNormalized();
	var2H->DrawNormalized("same");
	

	TLegend *leg = new TLegend(0.1,0.9,0.9,0.99);
	leg->SetFillColor(0);
	leg->SetNColumns(2);
	leg->AddEntry(var1H, var1.c_str(), "l");
	leg->AddEntry(var2H, var2.c_str(), "l");
	leg->Draw("same");

  c1236->SaveAs(savename.c_str ());
  inputFile1->Close();
inputFile2->Close();
}


