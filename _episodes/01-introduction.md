---
title: "Jets 101"
teaching: 0
exercises: 0
questions:
- "What is a jet?"
objectives:
- "Learn about jets, their different origin, types and reclustering algorithms."
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

In your cmslpc ssh session that was opened in the preliminary step in the README instructions, navigate to directory section1 and follow the instructions in the below notebooks.
Please note that the code shown in the notebooks is just for you to understand what each python script is doing and there's minor differences in the actual scripts that you will execute and sometimes modify in your ssh session. 

Covered notebooks: Basics (Ex 1.1) and Jet Types and Algorithms (Ex 1.2)

Full set of intro slides: Slides 1-24 

---

> ## After following the instructions in the setup:
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

## Jet Basics

> ## Open a notebook
>
> For the first part of this introduction open the notebook called `Basics.ipynb`.
{: .checklist}

This preliminary exercise will illustrate some of the basic properties of jets, like the four momentum quantiies: pt, eta, phi, mass.  We will use nanoAOD files, which are currently widely used with the CMS Collaborators. For more information about nanoAOD follow [this link](https://gitlab.cern.ch/cms-nanoAOD/nanoaod-doc/-/wikis/home). At the end of the notebook you will be able to see all the quantities stored in the `Jet` collection.

> ## Question 1.1
>
> Have you seen these jet quantities before? Where you expecting something different?
{: .challenge}

> ## Question 1.2
>
> Did you plot other jet quantities stored in nanoAOD? Do you understand the meaning of them?
{: .challenge}

## # Jet Types and Algorithms

The jet algorithms take as input a set of 4-vectors. At CMS, the most popular jet type is the "Particle Flow Jet", which attempts to use the entire detector at once and derive single four-vectors representing specific particles.For this reason it is very comparable (ideally) to clustering generator-level four-vectors also.

### Particle Flow Jets (PFJets)

Particle Flow candidates (PFCandidates) combine information from various detectors to make a combined estimation of particle properties based on their assigned identities (photon, electron, muon, charged hadron, neutral hadron).

PFJets are created by clustering PFCandidates into jets, and contain information about contributions of every particle class: Electromagnetic/hadronic, Charged/neutral etc.

The jet response is high. The jet pT resolution is good: starting at 15--20% at low pT and asymptotically reaching 5% at high pT.

### Monte Carlo Generator-level Jets (GenJets)

GenJets are pure Monte Carlo simulated jets. They are useful for analysis with MC samples. GenJets are formed by clustering the four-momenta of Monte Carlo truth particles. This may include “invisible” particles (muons, neutrinos, WIMPs, etc.).

As there are no detector effects involved, the jet response (or jet energy scale) is 1, and the jet resolution is perfect, by definition.

GenJets include information about the 4-vectors of the constituent particles, the hadronic and electromagnetic components of the energy etc.

### Calorimeter Jets (CaloJets)

CaloJets are formed from energy deposits in the calorimeters (hadronic and electromagnetic), with no tracking information considered. In the barrel region, a calorimeter tower consists of a single HCAL cell and the associated 5x5 array of ECAL crystals (the HCAL-ECAL association is similar but more complicated in the endcap region). The four-momentum of a tower is assigned from the energy of the tower, assuming zero mass, with the direction corresponding to the tower position from the interaction point.

In CMS, CaloJets are used less often than PFJets. Examples of their use include performance studies to disentangle tracker and calorimeter effects, and trigger-level analyses where the tracker is neglected to reduce the event processing time. ATLAS makes much more use of CaloJets, as their version of particle flow is not as mature as CMS's.

> ## Open a notebook
>
> For the first part of this introduction open the notebook called `Jet_Types_and_Algorithms.ipynb`.
{: .checklist}

> ## Question 1.3
>
> After running the _Reconstructed vs. Generator-Level Jets_ part of the notebook. As you can see, the agreement between calo, gen and pfjet isn't very good! Can you guess why?
{: .challenge}

> ## Solution 1.3
> We need to apply the jet energy corrections (JEC), which are described in the next exercise. But before we do that, we'll go over the jet clustering algorithms used in CMS.
{: .solution}

## Jet Clustering Algorithms

{% include links.md %}

