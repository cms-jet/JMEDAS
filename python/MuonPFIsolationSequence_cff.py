import FWCore.ParameterSet.Config as cms

from CommonTools.ParticleFlow.Isolation.tools_cfi import *

def load_muonPFiso_sequence(proc, seq_name, algo, coneR, src, src_charged_hadron='', src_neutral_hadron='', src_photon='', src_charged_pileup=''):

    doCH, doNH, doPh, doPU = False, False, False, False
    if src_charged_hadron != '': doCH = True
    if src_neutral_hadron != '': doNH = True
    if src_photon         != '': doPh = True
    if src_charged_pileup != '': doPU = True

    iso_seq = cms.Sequence()

    if doCH:
        setattr(proc, 'muPFIsoDepositCH'+algo, isoDepositReplace(src, src_charged_hadron))
        iso_seq += getattr(proc, 'muPFIsoDepositCH'+algo)

    if doNH:
        setattr(proc, 'muPFIsoDepositNH'+algo, isoDepositReplace(src, src_neutral_hadron))
        iso_seq += getattr(proc, 'muPFIsoDepositNH'+algo)

    if doPh:
        setattr(proc, 'muPFIsoDepositPh'+algo, isoDepositReplace(src, src_photon))
        iso_seq += getattr(proc, 'muPFIsoDepositPh'+algo)

    if doPU:
        setattr(proc, 'muPFIsoDepositPU'+algo, isoDepositReplace(src, src_charged_pileup))
        iso_seq += getattr(proc, 'muPFIsoDepositPU'+algo)

    iso_vals_seq = cms.Sequence()

    if doCH:
        setattr(proc, 'muPFIsoValueCH'+algo,
          cms.EDProducer('CandIsolatorFromDeposits',
            deposits = cms.VPSet(
              cms.PSet(
                src = cms.InputTag('muPFIsoDepositCH'+algo),
                deltaR = cms.double(coneR),
                weight = cms.string('1'),
                vetos = cms.vstring('0.0001','Threshold(0.0)'),
                skipDefaultVeto = cms.bool(True),
                mode = cms.string('sum')
              )
            )
          )
        )
        iso_vals_seq += getattr(proc, 'muPFIsoValueCH'+algo)

    if doNH:
        setattr(proc, 'muPFIsoValueNH'+algo,
          cms.EDProducer('CandIsolatorFromDeposits',
            deposits = cms.VPSet(
              cms.PSet(
                src = cms.InputTag('muPFIsoDepositNH'+algo),
                deltaR = cms.double(coneR),
                weight = cms.string('1'),
                vetos = cms.vstring('0.01','Threshold(0.5)'),
                skipDefaultVeto = cms.bool(True),
                mode = cms.string('sum')
              )
            )
          )
        )
        iso_vals_seq += getattr(proc, 'muPFIsoValueNH'+algo)

    if doPh:
        setattr(proc, 'muPFIsoValuePh'+algo,
          cms.EDProducer('CandIsolatorFromDeposits',
            deposits = cms.VPSet(
              cms.PSet(
                src = cms.InputTag('muPFIsoDepositPh'+algo),
                deltaR = cms.double(coneR),
                weight = cms.string('1'),
                vetos = cms.vstring('0.01','Threshold(0.5)'),
                skipDefaultVeto = cms.bool(True),
                mode = cms.string('sum')
              )
            )
          )
        )
        iso_vals_seq += getattr(proc, 'muPFIsoValuePh'+algo)

    if doPU:
        setattr(proc, 'muPFIsoValuePU'+algo,
          cms.EDProducer('CandIsolatorFromDeposits',
            deposits = cms.VPSet(
              cms.PSet(
                src = cms.InputTag('muPFIsoDepositPU'+algo),
                deltaR = cms.double(coneR),
                weight = cms.string('1'),
                vetos = cms.vstring('0.01','Threshold(0.5)'),
                skipDefaultVeto = cms.bool(True),
                mode = cms.string('sum')
              )
            )
          )
        )
        iso_vals_seq += getattr(proc, 'muPFIsoValuePU'+algo)

    iso_seq *= iso_vals_seq

    setattr(proc, seq_name, iso_seq)
