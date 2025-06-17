# Jet CMSDAS Exercise repository

This repository contains code used for several CMS Data Analysis Schools
There is one branch for each CMSDAS school.

## For students

To follow the CMSDAS short jet exercise check the website: [http://cms-jet.github.io/JMEDAS/](http://cms-jet.github.io/JMEDAS)

This version of the school is June 2025 and therefore use the branch `DASJune2025`:

```shell
git clone git@github.com:cms-jet/JMEDAS.git -b DASJan2025
```

## For contributors

The master branch contains the history of all code used in several CMSDAS schools.
This means that some code might be obsolete or use tools that are not longer recommended by CMS.

### To update the website

The website uses the [carpentry software](https://github.com/carpentries/styles/). If you want to modify it, use the `gh-pages` branch and follow the recommendations from the carpentry style.

### To update the exercises

The latest version of the exercises use `jupyter notebooks`, `nanoAOD` and `coffea`. This is located under `notebooks/master/`.

All the previous notebooks are stored under `notebooks/obsolete/`.

The code in `interface/`, `plugins/`, `scripts/` and `src/`, is the code use under CMSSW using miniAOD.
These scripts are not longer used by kept here for documentation.

## CMSDAS Jet Short Exercise - June 2025
  
### Introduction

This tutorial is intended to provide you with the basic you need in order to deal with jets in your analysis.
We start with the basics of what is a jet, how are they reconstructed, what algorithms are used, etc.
Then we give examples with scripts on how to access jets and use them in your analysis frameworks,
including corrections and systematics.
In the second part of the exercise, we examine jet substructure algorithms,
which have many uses including identification of hadronic decays of heavy SM particles like top quarks,
W, Z, and H bosons, as well as mitigation of pileup and others.

The tutorial is designed to be executed on LXPLUS and followed in the
[JMEDAS 2025 website](http://cms-jet.github.io/JMEDAS),
where you find links to instructional slides and instructions that walk you through the exercises.
