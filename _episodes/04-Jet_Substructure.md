---
title: "Jet Substructure"
teaching: 40
exercises: 20
questions:
- "What is jet substructure?"
- "How to distinguished jets originating from W or top quarks?"
objectives:
- "Learn about high pt ak8jets (FatJet)"
- "Learn about the different substructure variables and taggers"
- "Learn ways to identify boosted W and top quarks"
keypoints:
- "Jet substructure is the field study the internakl structure of high pt jets, usually clustered with a bigger jet radius (AK8)."
- "Grooming algorithms like softdrop, and substructure variables like the nsubjettiness ratio help us to identify the origin of these jets."
- "Over the years more state-of-the-art taggers involving ML have been implemented in CMS. Those help us indentify more effectively boosted jets."
---

> ## After following the instructions in the setup:
>
> ~~~
> cd <YOUR WORKING DIRECTORY>/notebooks/DAS/
> source /cvmfs/sft.cern.ch/lcg/views/LCG_105/x86_64-el9-gcc11-opt/setup.sh
> jupyter notebook --no-browser --port=8888 --ip 127.0.0.1
> ~~~
> {: .language-bash}
>
> This will open a jupyter notebook tree with various notebooks. 
{: .callout}

## What is a jet? 

In the previous episodes we discussed that the jet is a physical object representing the
hadronization of quakrs and gluons. Perhaps we have encounter that a jet can be formed from random
noise or pileup particles in our detectors, not necessarily coming from hard scattered quarks and
gluons, but jets can be so much more:

<img src="../fig/episode4/jet_types.svg" alt="" style="width:70%">

The internal structure of the jet constituents help us to understand their origin.

<img src="../fig/episode4/jet_substructure.svg" alt="" style="width:50%">

## Boosted Objects

Heavy particles which are created not at rest but with some momentum are referred as boosted
objects. Let's analyze the example of a top quark. If the top quarks are boosted, e.g. when coming from a new massive particle, what happens?. Hadronic decay products collimated so then they can be reconstructed in the same final-state object! Hadronic final states now become accessible with a dijet final state (in this case)

<img src="../fig/episode4/boosted_top.svg" alt="" style="width:70%">

<img src="../fig/episode4/examples_of_boostedjets.svg" alt="" style="width:70%">

## Jet mass

QCD jet mass is a perturbative quantity. From the initial (almost) massless partons, pQCD gives rise to a jet mass of order:

$$\left< M^2 \right> \simeq C \cdot \frac{\alpha^2}{\pi} p_T^2 R^2$$

Jet mass is proportional to R and pT. C is a form factor related to originating parton and clustering algorithm. For non-cone algorithms:

$$ \left< M^2 \right> \simeq a \times \alpha_S p^2_T R^2 $$ 

where $a$ is 0.16 for quarks and 0.37 for gluons. For heavy objects, the LO mass scale is the heavy object mass. 

The mass of QCD jets changes as a function of momentum, but the mass of heavy particle jets is relatively stable. For a given mass and pT scale, choose an appropriate jet radius: 

$$\Delta R \sim \frac{2m}{p_T}$$

CMS uses R = 0.8 for heavy object reconstruction. That is merged W/Z at pT ~200 GeV and merged top at pT ~400 GeV.

<img src="../fig/episode4/jet_mass.png" alt="" style="width:40%">

### Rho parameter

A useful variable for massive, fat jets is the QCD scaling parameter $\rho$, defined as:

$\rho=\log(m^2/(p_{\mathrm{T}}R)^2)$.

(Sometimes $\rho$ is defined without the log). One useful feature of this variable is that QCD jet mass grows with $p_{\mathrm{T}}$, i.e. the two quantities are strongly correlated, while $\rho$ is much less correlated with $p_{\mathrm{T}}$.

<img src="../fig/episode4/rho.png" alt="" style="width:40%">

### Exercise 4.1

We can use jet mass to distinguish our boosted W and top jets from QCD. Let's compare the AK8 jet mass of the boosted top quarks from the RS KK sample and the jets from the QCD sample. Let's also look at the and the softdrop groomed jet mass combined with the PUPPI pileup subtraction algorithm for different samples.

> ## Open a notebook
>
> For this part, open the notebook called `Jet_Substructure.ipynb` and run Exercise 4.1.
{: .checklist}

> ## Question 4.1
>
> Do you think the jet mass alone can be used to identify boosted W and top jets? 
{: .challenge}

> ## Question 4.2
> After running Exercise 3, in which cases do you think the $\rho$ variable can be used? 
{: .challenge}

> ## Solution 4.2
> The following two plots show what QCD events look like in different $p_{T}$ ranges. It's clear that the mass depends very strongly on $p_{T}$, while the $\rho$ shape is fairly constant vs. $p_{T}$ (ignoring $\rho<7$ or so, which is the non-perturbative region). Having a stable shape is useful when studying QCD across a wide $p_{T}$ range.
> <img src="../fig/episode4/qcdpt_mass.png" width=600px/>
> <img src="../fig/episode4/qcdpt_rho.png" width=600px/>
{: .solution}


## Jet Substructure

Because boosted jets represent the hadronic products of a heavy particle produced with high momentum, some tools have been developed to study the internal structure of these jets. This topic is usually called Jet Substructure.

Jet substructure algorithms can be divided into three main tools:
 * **grooming algorithms** attempt to reduce the impact of *soft* contributions to clustering sequence by adding some other criteria. Examples of these algorimths are softdrop, trimming, pruning.
 * **subtructure variables** are observables that try to quantify how many cores or prongs can be identify within the structure of the boosted jet. Examples of these variables are n-subjetiness or energy correlation functions.
 * **taggers** are more sofisticated algorithms that attempt to identify the origin of the boosted jet. Currently taggers are based on sofisticated machine-learning techniques which try to use as much information as possible in order to efficiency identify boosted W/Z/Higgs/top jets. Examples of these taggers in CMS are deepAK8/ParticleNet or deepDoubleB.

For further reading, several measurements have been performed about jet substructure:
 * [Studies of jet mass in dijet and W/Z+jet events](http://arxiv.org/abs/1303.4811) (CMS).
 * [Jet mass and substructure of inclusive jets in sqrt(s) = 7 TeV pp collisions with the ATLAS experiment](http://arxiv.org/abs/1203.4606) (ATLAS).
 * [Theory slides](http://www.hri.res.in/~sangam/sangam18/talks/Marzani-2.pdf)
 * [More theory slides]( http://indico.hep.manchester.ac.uk/getFile.py/access?contribId=14&resId=0&materialId=slides&confId=4413)
 * [Talk from Phil Harris](https://web.pa.msu.edu/seminars/hep_seminars/abstracts/2018/Harris-HEPSeminar-Slides-4172018.pdf) on searching for boosted $W$ bosons.


### Jet Grooming Algorithms

There has been many different approaches to jet grooming during the years. The standard idea is to remove soft and wide-angle radiation from within the jet, then recluster with smaller R, remove subjets and then remove constituents during clustering.

The next cartoon provides a good summary of all these algorithms:

<img src="../fig/episode4/grooming.png" alt="" style="width:40%">

The softdrop algorithm is the one choosen at CMS by default. Softdrop recursively decluster jet. Remove the softer component unless the soft drop condition is
satisfied.

<img src="../fig/episode4/softdrop.png" alt="" style="width:70%">

Soft wide angle radiation fails the condition:
 * As $z_{cut}$ increases, then more aggressive grooming
 * As $\beta$ decreases, then more aggressive grooming

Example (zcut = 0.1) :
 * If $\beta =0$,  remove softer subjet if pT fraction < 0.1 (~equivalent to MMDT)
 * If $\beta > 0$,  remove softer subjet if pT fraction < x, where x increases with ΔR and has maximum value 0.1 
 * If $\beta \lim \infty$ no grooming
 * If $\beta <0$ soft drop becomes a tagger instead of a groomer (finds jets with hard, large angle subjets)

Jet grooming algorithms dramatically improves the separation of QCD and top quark jets. Merged top quarks can be identified with a window around the top quark mass.

<img src="../fig/episode4/grooming_comparison.svg" alt="" style="width:70%">

### Exercise 4.2

 In this part of the tutorial, we will compare different subtructure algorithms as well as some usually subtructure variables.

> ## Open a notebook
>
> For this part, open the notebook called `Jet_Substructure.ipynb` and run Exercise 4.2.
{: .checklist}

> ## Question 4.3
> Look at the following histogram, which compares ungroomed, pruned, soft drop (SD), PUPPI, and
> SD+PUPPI jets. 
> <img src="../fig/episode4/ex5_rsg_jetmass.png" width=400px/>
> Note that the histogram has two peaks. What do these correspond to? How do the algorithms affect the relative size of the two populations?
{: .challenge}

### Substructure variables

Knowing how many final state objects to expect from these decays we can look inside the jet for the expected substructure:
 * Top decays →  3 subjets
 * W/Z/H decays → 2 subjets
 *
A quantity called N-subjettiness is a measure of how consistent a jet is with a hypothesized number of subjets. N-subjetiness is defined as:

$$\tau_N = \frac{1}{\sum_i P_{T,i} \cdot R} \sum_i p_{T,i} \cdot min ( \Delta R_{1,i}, ... \Delta R_{N,i} )$$

The variable $\tau_N$ gives a sense of how many N prongs or cores can be find inside the jet. It is known that the n-subjetiness variables itself ($\tau_{N}$) do not provide good discrimination power, but its ratios do. Then, a $\tau_{MN} = \dfrac{\tau_M}{\tau_N}$ basically tests if the jet is more M-prong compared to N-prong. For instance, we expect 2 prongs for boosted jets originated from hadronic Ws, while we expect 1 prongs for high-pt jets from QCD multijet processes. The most common nsubjetiness ratio are $\tau_{21}$ and $\tau_{32}$. 

<img src="../fig/episode4/nsubjettiness.png" alt="" style="width:70%">

Another subtructure variable commonly used is the energy correlation function $N2$. Similarly than $\tau_{21}$, $N2$ tests if the boosted jet is compatible with a 2-prong jet hypothesis.

<img src="../fig/episode4/energy_correlations.svg" alt="" style="width:70%">

### Exercise 4.3

> ## Open a notebook
>
> For this part, open the notebook called `Jet_Substructure.ipynb` and run Exercise 4.3.
{: .checklist}


> ## Question 4.4
> Look at the histogram comparing $\tau_{21}$. What can you say about the histogram? Is $\tau_{21}$ telling you something about the nature of the boosted jets selected?
{: .challenge}

> ## Question 4.5
> Look at the histogram comparing $\tau_{32}$. What can you say about the histogram? Is $\tau_{32}$ telling you something about the nature of the boosted jets selected?
{: .challenge}


> ## Question 4.6
> Look at the histograms comparing $N2$ and $N3. What can you say about the histogram? Are these variables telling you something about the nature of the boosted jets selected?
{: .challenge}


## Taggers

In this part of the tutorial, we will look at how different substructure algorithms can be used to identify jets originating from boosted W's and tops. Specifically, we'll see how these identification tools are used to separate these boosted jets from those originating from Standard Model QCD, a dominant process at the LHC.

### W tagging

<img src="../fig/episode4/wtagging.svg" alt="" style="width:70%">

### top tagging

<img src="../fig/episode4/toptagging.svg" alt="" style="width:70%">

### Tagging with machine learning

W/Top tagging was one of the first places where ML was adopted in CMS. We have study several of these algorithms (JME-18-002), being “deepAK8/ParticleNet” the most used within CMS. 

<img src="../fig/episode4/mltagging.svg" alt="" style="width:70%">

### Exercise 4.4

> ## Open a notebook
>
> For this part, open the notebook called `Jet_Substructure.ipynb` and run Exercise 4.4.
{: .checklist}

> ## Question 4.7
>
> * Why can we use a ttbar sample to talk about W-tagging?
> * What cuts would you place on these variables to distinguish W bosons from QCD?
> * So far, which variable looks more promising?
{: .challenge}

> ## Question 4.8
> * What cut would you apply to select boosted top quarks?
> * For both the W and top selections, what other variable(s) could we cut on in addition?
{: .challenge}

### Go Further

 * You can learn more about jet grooming from the jet substructure exercise and PUPPI from the pileup mitigation exercise.
 * We briefly mentioned that you can combine variables for even better discrimination. In CMS, we do this to build our jet taggers. For the simple taggers, we often combine cuts on jet substructure variables and jet mass. The more sophisticated taggers, which are used more and more widely within CMS, use deep neural networks. To learn about building a machine learning tagger, check out the [machine learning short exercise](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolCERN2020MLShortExercise). (FIXME)

> ## What about boosted Higgs?
>
> CMS has also a rich program for booted Higgs to bb/cc taggers, however they are usually studied by
> the btagging group (BTV). Look at their documentation for more information.
{: .callout}

{% include links.md %}

