# The following comments couldn't be translated into the new config version:

#keep the logging output to a nice level

import FWCore.ParameterSet.Config as cms

process = cms.Process("RPCSegmentEff")

process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
process.load("Geometry.CSCGeometry.cscGeometry_cfi")
process.load("Geometry.DTGeometry.dtGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("DQMServices.Components.MEtoEDMConverter_cfi")
process.load("DQMServices.Core.DQM_cfg")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'MC_31X_V1::All'

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('//store/data/Commissioning09/RPCMonitor/RAW/v3/000/106/019/FC80F355-6972-DE11-8AD4-001D09F2AD7F.root')
)

process.museg = cms.EDFilter("MuonSegmentEff",

    incldt = cms.untracked.bool(True),
    incldtMB4 = cms.untracked.bool(True),
    inclcsc = cms.untracked.bool(True),

    debug = cms.untracked.bool(True),
    inves = cms.untracked.bool(True),
    
    DuplicationCorrection = cms.untracked.int32(1),

    manualalignment = cms.untracked.bool(False),
    AliFileName = cms.untracked.string('/afs/cern.ch/user/c/carrillo/endcap/CMSSW_3_0_0_pre10/src/DQM/RPCMonitorModule/data/Alignment69912.dat'),
	
    rangestrips = cms.untracked.double(4.),
    rangestripsRB4 = cms.untracked.double(4.),
    MinCosAng = cms.untracked.double(0.85),
    MaxD = cms.untracked.double(80.0),
    MaxDrb4 = cms.untracked.double(150.0),

    cscSegments = cms.untracked.string('hltCscSegments'),
    dt4DSegments = cms.untracked.string('hltDt4DSegments'),

    EffSaveRootFile = cms.untracked.bool(True),
    EffRootFileName = cms.untracked.string('eff106019.FC80F355-6972-DE11-8AD4-001D09F2AD7F.root'),
    EffSaveRootFileEventsInterval = cms.untracked.int32(100)
)

process.normfilter = cms.EDFilter("HLTHighLevel",
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    HLTPaths = cms.vstring("AlCa_RPCMuonNormalisation"),
    eventSetupPathsKey = cms.string(''),
    andOr = cms.bool(True),
    throw = cms.bool(True)
)

process.p = cms.Path(process.normfilter*process.museg)

process.DQM.collectorHost = ''
process.DQM.collectorPort = 9090
process.DQM.debug = False


