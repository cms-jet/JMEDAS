---
layout: lesson
root: .  # Is the only page that doesn't follow the pattern /:path/index.html
permalink: index.html  # Is the only page that doesn't follow the pattern /:path/index.html
---

This tutorial is intended to provide you with the basic you need in order to deal with jets in your analysis. We start with the basics of what is a jet, how are they reconstructed, what algorithms are used, etc. Then we give examples with scripts on how to access jets and use them in your analysis frameworks, including corrections and systematics. In the second part of the exercise, we examine jet substructure algorithms, which have many uses including identification of hadronic decays of heavy SM particles like top quarks, W, Z, and H bosons, as well as mitigation of pileup and others.

The tutorial is designed to be executed at cmslpc and followed in the JMEDAS 2023 twiki page, where you find links to instructional slides and (read-only) notebooks that walk you through the exercises.

_For general questions, problems, debugs, or asking for help from experts on jets and missing ET:_ [CMS Talk JetMET category](https://cms-talk.web.cern.ch/c/pog/jetmet/51)

_Follow the CMS workbook on jet analysis:_  [WorkBookJetAnalysis](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetAnalysis)

### What is this set of exercises is trying to do ?

Give you a hands-on experience on how to access jet collection in an event, plot basic jet quantities, and apply jet energy correction.

 * A 101 on how to access jets in the CMS framework without assuming prior knowledge of jet analysis.
 * Make you familiar with basic jet types and algorithms and how to use them in your analysis.
 * Illustrate each exercise using real life example scripts.
 * Give you a comprehensive reference to more advanced workbook examples, additional resources, and pedagogical documentation in one place.

### What are these exercises NOT meant for ?

To give a comprehensive summary of the CMS JetMET software machinery or of the jet analyses being performed at CMS.

### What do we expect from you ?

 * You should have followed all the pre-exercises and have cmslpc account, grid certificate, and a current web browser at hand.
 * You should work through the notebooks, making sure to understand every step and every plot.
 * The exercises are prepared to be run directly from a cmslpc node, with also non-interactive notebooks to follow and discuss the exercises.

### Facilitators CMSDAS LPC 2024

 * Alejandro Gomez Espinosa	
 * Martin Kwok	
 * Clemens Lange	
 * Chris Madrid	
 * Connor Moore	
 * Grace Cummings	
 * Henning Kirschenmann

### Introductory slides

We will start with this version of slides: [CMSDAS_Jets_intro_2023.pdf]().


### Support

Join the [ShortExJets Mattermost channel](https://mattermost.web.cern.ch/cmsdaslpc2024/channels/shortexjets) and don't hesitate to ask for help from the facilitators in the room.

### Setup

Follow the setup [here](setup.md).

<!-- this is an html comment -->
{% comment %} This is a comment in Liquid {% endcomment %}

> ## Prerequisites
>
> FIXME
[CMS DAS Pre-exercises](https://fnallpc.github.io/cms-das-pre-exercises/) {: .prereq}

{% include links.md %}
