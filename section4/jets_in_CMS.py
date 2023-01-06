# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events

jets, jetLabel = Handle("std::vector<:jet>"), "slimmedJets"
fatjets, fatjetLabel = Handle("std::vector<:jet>"), "slimmedJetsAK8"
vertices, vertexLabel = Handle("std::vector<:vertex>"), "offlineSlimmedPrimaryVertices"
verticesScore = Handle("edm::ValueMap")
seenIt = {} # list of things we've seen (so that we dump them in full only once)

# open file (you can use 'edmFileUtil -d /store/whatever.root' to get the physical file name)
events = Events('root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18MiniAOD/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/210000/DA20DC21-E781-C540-9FCD-7BCF2144CA4E.root' )

for iev,event in enumerate(events):
    if iev >= 10: break
    event.getByLabel(jetLabel, jets)
    event.getByLabel(fatjetLabel, fatjets)
    event.getByLabel(vertexLabel, vertices)
    event.getByLabel(vertexLabel, verticesScore)

    print "\nEvent %d: run %6d, lumi %4d, event %12d" % (iev,event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event())

    # Vertices
    if len(vertices.product()) == 0 or vertices.product()[0].ndof() < 4:
        print "Event has no good primary vertex."
        continue
    else:
        PV = vertices.product()[0]
        print "PV at x,y,z = %+5.3f, %+5.3f, %+6.3f, ndof: %.1f, score: (pt2 of clustered objects) %.1f" % (PV.x(), PV.y(), PV.z(), PV.ndof(),verticesScore.product().get(0))


    # Jets (AK4, CHS and Puppi)
    for jetLabel, algo in ("slimmedJets", "CHS"), ("slimmedJetsPuppi", "PUPPI"):
        event.getByLabel(jetLabel, jets)
        for i,j in enumerate(jets.product()):
            if j.pt() < 20: continue
            print "jet %s %3d: pt %5.1f (raw pt %5.1f, matched-calojet pt %5.1f), eta %+4.2f, btag CSVIVFv2 %.3f, CMVAv2 %.3f, pileup mva disc %+.2f" % (
                algo, i, j.pt(), j.pt()*j.jecFactor('Uncorrected'), j.userFloat("caloJetMap:pt") if algo == "CHS" else -99.0, j.eta(), max(0,j.bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags")), max(0,j.bDiscriminator("pfCombinedMVAV2BJetTags")), j.userFloat("pileupJetId:fullDiscriminant") if algo == "CHS" else -99)
            if 'jetAk4'+algo not in seenIt:
                constituents = [ j.daughter(i2) for i2 in xrange(j.numberOfDaughters()) ]
                constituents.sort(key = lambda c:c.pt(), reverse=True)
                for i2, cand in enumerate(constituents):
                    if i2 > 12:
                            print "         ....."
                            break
                    print "         constituent %3d: pt %6.2f, dz(pv) %+.3f, pdgId %+3d, hcal energy fraction %.2f, puppi weight %.3f " % (i2,cand.pt(),cand.dz(PV.position()),cand.pdgId(),cand.hcalFraction(),cand.puppiWeight())
                print "   btag discriminators:"
                for btag in j.getPairDiscri():
                    print  "\t%s %s" % (btag.first, btag.second)
                print "   userFloats:"
                for ufl in j.userFloatNames():
                    print  "\t%s %s" % (ufl, j.userFloat(ufl))
                seenIt['jetAk4'+algo] = True

    # Fat AK8 Jets
    for i,j in enumerate(fatjets.product()):
        print "jetAK8 %3d: pt %5.1f (raw pt %5.1f), eta %+4.2f, mass %5.1f ungroomed, %5.1f softdrop, %5.1f pruned CHS. " % (
            i, j.pt(), j.pt()*j.jecFactor('Uncorrected'), j.eta(), j.mass(), j.userFloat('ak8PFJetsPuppiSoftDropMass'), j.userFloat('ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass'))
        # If you use CMSSW_9_4_<=6 to read MiniAOD, to get the constituents of the AK8 jets, you have to loop over all of the
        # daughters recursively. To save space, the first two constituents are actually
        # the Soft Drop SUBJETS, which will then point to their daughters.
        # The remaining constituents are those constituents removed by soft drop but
        # still in the AK8 jet.
        if 'jetAk8' not in seenIt:
            constituents = []
            for ida in xrange( j.numberOfDaughters() ) :
                cand = j.daughter(ida)
                if cand.numberOfDaughters() == 0 :
                    constituents.append( cand )
                else : # only needed in CMSSW_9_4_<=6
                    for jda in xrange( cand.numberOfDaughters() ) : # only needed in CMSSW_9_4_<=6
                        cand2 = cand.daughter(jda) # only needed in CMSSW_9_4_<=6
                        constituents.append( cand2 ) # only needed in CMSSW_9_4_<=6
            constituents.sort(key = lambda c:c.pt(), reverse=True)
            for i2, cand in enumerate(constituents):
                if i2 >4:
                            print "         ....."
                            break
                print "         constituent %3d: pt %6.2f, pdgId %+3d, #dau %+3d" % (i2,cand.pt(),cand.pdgId(), cand.numberOfDaughters())
            print "   btag discriminators:"
            for btag in j.getPairDiscri():
                print  "\t%s %s" % (btag.first, btag.second)
            print "   userFloats:"
            for ufl in j.userFloatNames():
                print  "\t%s %s" % (ufl, j.userFloat(ufl))
            seenIt['jetAk8'] = True
        # Print Subjets
        if 'jetAk8SD' not in seenIt:
            sdSubjets = j.subjets('SoftDropPuppi')
            for isd,sdsub in enumerate( sdSubjets ) :
                print "   w subjet %3d: pt %5.1f (raw pt %5.1f), eta %+4.2f, mass %5.1f " % (
                    isd, sdsub.pt(), sdsub.pt()*sdsub.jecFactor('Uncorrected'), sdsub.eta(), sdsub.mass()
                    )
                print "   \tbtag discriminators:"
                for btag in sdsub.getPairDiscri():
                    print  "\t\t%s %s" % (btag.first, btag.second)
                print "   \tuserFloats:"
                for ufl in sdsub.userFloatNames():
                    print  "\t\t%s %s" % (ufl, sdsub.userFloat(ufl))
                seenIt['jetAk8SD'] = True

