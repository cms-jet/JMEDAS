#
# Taken from https://github.com/kpedro88/TreeMaker/blob/upgrade2016/TreeMaker/python/JetDepot.py
# Written by: Kevin Pedro
# Modified by: Alexx Perloff
#

import FWCore.ParameterSet.Config as cms

def JetDepot(process, sequence, JetTag, JetType, jecUncDir=0, doSmear=True, jerUncDir=0):
    if hasattr(process,sequence):
        theSequence = getattr(process,sequence)
    else:
        print "Unknown sequence: "+sequence
        return

    # starting value
    # for now, assume JECs have already been updated
    JetTagOut = JetTag
    
    ## ----------------------------------------------------------------------------------------------
    ## JEC uncertainty variations
    ## ----------------------------------------------------------------------------------------------

    if jecUncDir!=0:
        #JEC unc up or down
        patJetsJEC = cms.EDProducer('JetUncertaintyProducer',
            JetTag = JetTagOut,
            JetType = cms.string(JetType),
            jecUncDir = cms.int32(jecUncDir)
        )
        dir = "up" if jecUncDir>0 else "down"
        JetTagOut = cms.InputTag(JetTagOut.value()+"JEC"+dir)
        setattr(process,JetTagOut.value(),patJetsJEC)
        theSequence = getattr(process,JetTagOut.value()) * theSequence

    ## ----------------------------------------------------------------------------------------------
    ## JER smearing + uncertainty variations
    ## ----------------------------------------------------------------------------------------------
    
    if doSmear:
        patSmearedJets = cms.EDProducer("SmearedPATJetProducer",
            src = JetTagOut,
            enabled = cms.bool(True),
            rho = cms.InputTag("fixedGridRhoFastjetAll"),
            skipGenMatching = cms.bool(False),
            # Read from GT
            algopt = cms.string('AK4PFchs_pt'),
            algo = cms.string('AK4PFchs'),
            # Gen jet matching
            genJets = cms.InputTag("slimmedGenJets"),
            dRMax = cms.double(0.2),
            dPtMaxFactor = cms.double(3),
            variation = cms.int32(jerUncDir),
            seed = cms.uint32(37428479),
        )
        dir = "" if jerUncDir==0 else ("up" if jerUncDir>0 else "down")
        JetTagOut = cms.InputTag(JetTagOut.value()+"JER"+dir)
        setattr(process,JetTagOut.value(),patSmearedJets)
        theSequence = getattr(process,JetTagOut.value()) * theSequence
    
    return (process, JetTagOut)