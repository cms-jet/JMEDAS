---
title: "Pileup and jetID"
teaching: 0
exercises: 0
questions:
- "What is pileup and how does it afffect to jets?"
- "What is the basic jet quality criteria?"
objectives:
- "Learn about the pileup mitigation techniques used at CMS."
- "Learn about about the basic jet quality criteria."
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
- "The so-called jetID is the basic jet quality criteria to remove fake jets."
---

Full set of intro slides: Slides 30-44 (FIXME)


> ## After following the instructions in the setup (if you have not done it yet) :
>
> ~~~
> cd <YOUR WORKING DIRECTORY>/notebooks/
> source /cvmfs/sft.cern.ch/lcg/views/LCG_103/x86_64-centos7-gcc11-opt/setup.sh
> jupyter notebook --no-browser --port=8888 --ip 127.0.0.1
> ~~~
> {: .language-bash}
>
> This will open a jupyter notebook tree with various notebooks. 
{: .callout}

## Measuring pileup

Before we get into mitigating pileup effects, let's first examine measures of pileup in more detail. We will discuss event-by-event variables that can be used to characterize the pileup and this will give us some hints into thinking about how to deal with it.

> ## Open a notebook
>
> For the first part of this introduction open the notebook called `Pileup.ipynb`.
{: .checklist}

> ## Question 2.1
> Why are there a different amount of pileup interactions than primary vertices?
{: .challenge}

> ## Solution 2.1
> There is a vertex finding efficiency, which in Run I was about 72%. This means that $N_{PV}\simeq0.72{\cdot}N_{PU}$
{: .solution}

{% comment %} THIS I DIDN"T KNOW HOW TO DO WITH NANO
<font color='red'>Question 2: How many pileup interactions are simulated before and after the in-time bunch crossing?</font><details>
<summary><font color='blue'>Hint</font></summary>
Try running the command `t.Scan("bxns:tnpu:npu")`
</details><details>
<summary><font color='blue'>Show answer...</font></summary>
There are 12 interactions before and 3 after.
</details>
{% endcomment %}

> ## Question 2.2
> Rho is the measure of the density of the pileup in the event. It's measured in terms of GeV per unit area. Can you think of ways we can use this information the correct for the effects of pileup?
{: .challenge}

> ## Solution 2.2 
> From the jet $p_{T}$ simply subtract off the average amount of pileup expected in a jet of that size. Thus $p_{T}^{corr}{\simeq}p_{T}^{reco}-\rho{\cdot}area$
{: .solution}

> ## Question 2.3
> This plot shows the jet composition. Generally, why do we see the mixture of photons, neutral hadrons and charged hadrons that we see?</font>
> <img src="../fig/composition_combo_pt_pfpaper_final_v2.png" alt="Jet Composition Vs. Pt" width="400px" />
{: .challenge}

> ## Solution 2.3
> A majority of the constituents in a jet come from pions. Pions come in neutral ($\pi^{0}$) and charged ($\pi^{\pm}$) varieties. Naively you would expect the composition to be two thirds charged hadrons and one third neutral hadrons. However, we know that $\pi^{0}$ decays to two photons, which leads to a large photon fraction.
> <img src="../fig/efracs_particles_8TeV.png" alt="Jet Composition MC" width="380px" />
{: .solution}

## Pileup reweighting

(FIXME)



## Jet ID

In order to avoid using fake jets, which can originate from a hot calorimeter cell or electronic read-out box, we need to require some basic quality criteria for jets. These criteria are collectively called "jet ID". Details on the jet ID for PFJets can be found in the following twiki:

[https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID](https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID)

The JetMET POG recommends a single jet ID for most physics analysess in CMS, which corresponds to what used to be called the tight Jet ID. Some important observations from the above twiki:

 - Jet ID is defined for uncorrected jets only. Never apply jet ID on corrected jets. This means that in your analysis you should apply jet ID first, and then apply JECs on those jets that pass jet ID.
 - Jet ID is fully efficient (>99%) for real, high-$p_{\mathrm{T}}$ jets used in most physics analysis. Its background rejection power is similarly high.


> ## Open a notebook
>
> For this part open the notebook called `Jet_Types_and_Algorithms.ipynb` and run the Exercise 3.
{: .checklist}

In nanoAOD is trivial to apply jetID. They are stored as Flags, where `events.Jet.jetId>=2` corresponds to *tightID* and `events.Jet.jetId>=6` corresponds to *tightLepVetoID*. 

If you want to know how this flags are stored in nanoAOD, the next block shows the implementation in
C++ from a miniAOD file:
> ## Implementation in c++
> There are several ways to apply jet ID. In our above exercises, we have run the cuts "on-the-fly" in our python FWLite macro (the first option here). Others are listed for your convenience.
>
> The following examples use somewhat out of date numbers. See the above link to the JetID twiki for the current numbers.
>
> To apply the cuts on pat::Jet (like in miniAOD) in python then you can do :
>
> ~~~
> # Apply jet ID to uncorrected jet
> nhf = jet.neutralHadronEnergy() / uncorrJet.E()
> nef = jet.neutralEmEnergy() / uncorrJet.E()
> chf = jet.chargedHadronEnergy() / uncorrJet.E()
> cef = jet.chargedEmEnergy() / uncorrJet.E()
> nconstituents = jet.numberOfDaughters()
> nch = jet.chargedMultiplicity()
> goodJet = \
>   nhf < 0.99 and \
>   nef < 0.99 and \
>   chf > 0.00 and \
>   cef < 0.99 and \
>   nconstituents > 1 and \
>   nch > 0
> ~~~
> {: .code}
> 
> To apply the cuts on pat::Jet (like in miniAOD) in C++ then you can do:
> 
> ~~~
> // Apply jet ID to uncorrected jet
> double nhf = jet.neutralHadronEnergy() / uncorrJet.E();
> double nef = jet.neutralEmEnergy() / uncorrJet.E();
> double chf = jet.chargedHadronEnergy() / uncorrJet.E();
> double cef = jet.chargedEmEnergy() / uncorrJet.E();
> int nconstituents = jet.numberOfDaughters();
> int nch = jet.chargedMultiplicity();
> bool goodJet =
>   nhf < 0.99 &&
>   nef < 0.99 &&
>   chf > 0.00 &&
>   cef < 0.99 &&
>   nconstituents > 1 &&
>   nch > 0;
> ~~~
> {: .code}
> 
> To create selected jets in cmsRun:
> ~~~
> from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
> process.tightPatJetsPFlow = cms.EDFilter("PFJetIDSelectionFunctorFilter",
>                                          filterParams = pfJetIDSelector.clone(quality=cms.string("TIGHT")),
>                                          src = cms.InputTag("slimmedJets")
>                                          )
> ~~~
> {: .code}
> 
> It is also possible to use the `PFJetIDSelectionFunctor` C++ selector (actually, either in C++ or python), but this was primarily developed in the days before PF when applying CaloJet ID was not possible very easily. Nevertheless, the functionality of more complicated selection still exists for PFJets, but is almost never used other than the few lines above. If you would still like to use that C++ class, it is documented as an example here.
{: .solution}

> ## Discussion 1.4
>
> What do the jets with jetId represent? Were you expecting more or less jets with jetId==0?
{: .discussion}
{% include links.md %}

