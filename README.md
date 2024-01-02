# Jet CMSDAS Exercise repository

This repository contains code use for several years for each CMS Data Analysis School, and therefore there is one branch for the specific CMSDAS school. 

## For students

If you want to follow the CMSDAS short jet exercise check the website: [http://cms-jet.github.io/JMEDAS/](http://cms-jet.github.io/JMEDAS)

The latest version of the school is on January 2024 and therefore use the branch `DASJan2024`:

```
git clone git@github.com:cms-jet/JMEDAS.git -b DASJan2024
```


## For contributors

This is the master branch which contains all the code used in several CMSDAS schools. This means that many of the code is obsolete or uses tools that are not longer recommended by CMS. 

### To update the website

The website uses the [carpentry software](https://github.com/carpentries/styles/). If you want to modify it, use the `gh-pages` branch and follow the recommendations from the carpentry style.

### To update the exercises

The latest version of the exercises, for Jan 2024, use `jupyter notebooks`, `nanoAOD` and `coffea`. This is located under `notebooks/master/`.

All the previous notebooks are stored under `notebooks/obsolete/`.

The code in `interface/`, `plugins/`, `scripts/` and `src/`, is the code use under CMSSW using miniAOD. These scripts are not longer used by kept here for documentation.


## CMSDAS Jet Short Exercise - January  2024
  
### Introduction
This tutorial is intended to provide you with the basic you need in order to deal with jets in your analysis. We start with the basics of what is a jet, how are they reconstructed, what algorithms are used, etc. Then we give examples with scripts on how to access jets and use them in your analysis frameworks, including corrections and systematics. In the second part of the exercise, we examine jet substructure algorithms, which have many uses including identification of hadronic decays of heavy SM particles like top quarks, W, Z, and H bosons, as well as mitigation of pileup and others.

The tutorial is designed to be executed at cmslpc and followed in the [JMEDAS 2024 website](http://cms-jet.github.io/JMEDAS), where you find links to instructional slides and instructions that walk you through the exercises.
