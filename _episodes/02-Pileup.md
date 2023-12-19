---
title: "Pileup"
teaching: 0
exercises: 0
questions:
- "What is pileup and how does it afffect to jets?"
objectives:
- "Learn about the pileup mitigation techniques used at CMS."
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
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

{% include links.md %}

