---
title: "Jet Substructure"
teaching: 0
exercises: 0
questions:
- "What is jet substructure?"
objectives:
- "Learn how to identify the origin of jets with high pt"
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

Full set of intro slides: Slides 58-76 (FIXME)

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

 In this part of the tutorial, we will compare different subtructure algorithms as well as some usually subtructure variables.

> ## Open a notebook
>
> For this part, open the notebook called `Jet_Substructure.ipynb` and run Exercise 1.
{: .checklist}

> ## Question 4.1
> Look at the following histogram, which compares ungroomed, pruned, soft drop (SD), PUPPI, and
> SD+PUPPI jets. 
> <img src="../fig/ex5_rsg_jetmass.png" width=400px/>
> Note that the histogram has two peaks. What do these correspond to? How do the algorithms affect the relative size of the two populations?
{: .challenge}


{% include links.md %}

