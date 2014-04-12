import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")
# process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')

process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

process.MessageLogger = cms.Service("MessageLogger")

process.demo = cms.EDAnalyzer("RPCMonitorEfficiency",
    fileName = cms.untracked.string(
#'efficiency.root'
'file:/afs/cern.ch/work/m/mileva/CMSSW_7_0_3_patch2/src/efficiency.root'


),
    fileOut = cms.untracked.string('efficiencyAnalyzed.root'),

    BlackListFile = cms.untracked.string('blacklist.dat'),

    debug = cms.untracked.bool(False),
    makehtml = cms.untracked.bool(False),
    prodimages = cms.untracked.bool(False),
    statistics = cms.untracked.bool(True),
    threshold = cms.untracked.double(50.0),
                              
    barrel = cms.untracked.bool(True),
    endcap = cms.untracked.bool(True)
)

process.p = cms.Path(process.demo)
