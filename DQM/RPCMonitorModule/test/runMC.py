import FWCore.ParameterSet.Config as cms

process = cms.Process("AGRAnalyzer")

# process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load('Configuration.Geometry.GeometryExtended2015Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2015_cff')
#process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
#process.load("Geometry.CSCGeometry.cscGeometry_cfi")
#process.load("Geometry.DTGeometry.dtGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("DQMServices.Components.MEtoEDMConverter_cfi")
process.load("DQMServices.Core.DQM_cfg")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.autoCond import autoCond
#process.GlobalTag.globaltag = autoCond['mc']
process.GlobalTag.globaltag = 'GR_P_V44::All'#'MC_70_V4::All'#'GR_E_V37::All'#'GR_P_V32::All'#START50_V14::All'



#### Camillo's Muon Tools ##########################################
# process.load("MuonTools.StandardSequences.RecoStandAloneMuon_cff")
# # have stareco use hlt digis
# process.load("MuonTools.Configuration.HltMuonDigis_cff")
# # have stareco use hlt segments (1)
# process.load("MuonTools.Configuration.HltMuonSegments_cff")
# keep stareco from using rpcs
# process.load("MuonTools.Configuration.StandAloneNoRpc_cff")
####################################################################


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",

   fileNames = cms.untracked.vstring(
#MC
#'root://eoscms//eos/cms/store/user/mileva/grApril/SingleMuPt10_2015_cfi_RECO_nobadcsc.root'

#data from eos
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/886/00000/0C83F675-3BC0-E311-AF86-02163E00B05B.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/737/00000/BE7647E3-3BC0-E311-A825-02163E00C4FC.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/848/00000/BEF94C1A-21C1-E311-96C5-02163E00E621.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/854/00000/F41019F8-29C1-E311-A840-02163E00E610.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/3EE3399E-7DC1-E311-9DFF-02163E00CD88.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/88789BF4-8BC1-E311-BA12-02163E00E64D.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/A60449D9-8BC1-E311-8267-02163E00F36F.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/B03F65EA-78C1-E311-B9B1-0025904B2018.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/B4B60B29-8CC1-E311-ADB7-02163E00E656.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/C26CC6D2-86C1-E311-9860-02163E00E770.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/C2EEF4E4-78C1-E311-A372-002590494DD2.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/C669288D-7DC1-E311-B4B3-02163E00F1E5.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/D4B0C225-D7C1-E311-96AC-02163E00E674.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/F47B6647-7CC1-E311-9EE3-02163E00EA50.root',
#'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/878/00000/F6585DE4-8BC1-E311-802E-02163E00E650.root'
##'root://eoscms//eos/cms/store/data/Commissioning2014/Cosmics/RECO/PromptReco-v1/000/220/886/00000/0C83F675-3BC0-E311-AF86-02163E00B05B.root'

#data skim from Alberto
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220737_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220848_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220854_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220855_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220878_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220878_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220878_3.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220878_4.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220878_5.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220878_6.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220885_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220885_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220886_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220889_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220891_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220896_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220896_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220896_3.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220896_4.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220900_1.root',
#'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220909_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220935_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220948_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220960_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220960_10.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220960_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220960_3.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220960_4.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220960_5.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220960_6.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220960_7.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220960_8.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220960_9.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220963_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220965_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220966_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220966_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220966_3.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220969_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220987_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220987_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220987_3.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220987_4.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_220987_5.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221001_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221027_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221036_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221043_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221073_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221083_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221083_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221083_3.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221083_4.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221086_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221086_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221104_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221104_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_10.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_11.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_3.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_4.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_5.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_6.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_7.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_8.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221113_9.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221120_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221121_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221122_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221136_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221139_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221139_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221144_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221144_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221144_3.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221150_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221153_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221164_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221198_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221215_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221215_2.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221227_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221237_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221238_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221239_1.root',
'root://eoscms//eos/cms/store/group/comm_rpc/LS-I/AGR/Tree_221240_1.root'



)
)

#### Switch off requirement to use only Segments used in Tracks --- AGR will not have useful tracks #######
# process.dTandCSCSegmentsinTracks = cms.EDProducer("DTandCSCSegmentsinTracks",
#                                                   cscSegments = cms.InputTag("hltCscSegments"),
#                                                   dt4DSegments = cms.InputTag("hltDt4DSegments"),
#                                                   tracks = cms.InputTag("standAloneMuons","UpdatedAtVtx")
#                                                   )
###########################################################################################################


process.rpcPointProducer = cms.EDProducer('RPCPointProducer',
  incldt = cms.untracked.bool(True),
  inclcsc = cms.untracked.bool(True),
  incltrack =  cms.untracked.bool(False),
  debug = cms.untracked.bool(False),
  rangestrips = cms.untracked.double(4.),
  rangestripsRB4 = cms.untracked.double(4.),
  MinCosAng = cms.untracked.double(0.85),
  MaxD = cms.untracked.double(80.0),	#for CSC
  MaxDrb4 = cms.untracked.double(150.0), #for DT
  ExtrapolatedRegion = cms.untracked.double(0.6), #in stripl/2 in Y and stripw*nstrips/2 in X
  # cscSegments = cms.InputTag('dTandCSCSegmentsinTracks','SelectedCscSegments','OwnParticles'),
  # dt4DSegments = cms.InputTag('dTandCSCSegmentsinTracks','SelectedDtSegments','OwnParticles'),
  cscSegments = cms.InputTag('cscSegments', '', 'RECO'),
  dt4DSegments = cms.InputTag('dt4DSegments', '', 'RECO'),
  tracks = cms.InputTag("standAloneMuons"),
  TrackTransformer = cms.PSet(
      DoPredictionsOnly = cms.bool(False),
      Fitter = cms.string('KFFitterForRefitInsideOut'),
      TrackerRecHitBuilder = cms.string('WithTrackAngle'),
      Smoother = cms.string('KFSmootherForRefitInsideOut'),
      MuonRecHitBuilder = cms.string('MuonRecHitBuilder'),
      RefitDirection = cms.string('alongMomentum'),
      RefitRPCHits = cms.bool(False),
      Propagator = cms.string('SmartPropagatorAnyRKOpposite')
  )
)

process.museg = cms.EDAnalyzer("MuonSegmentEff",

    incldt = cms.untracked.bool(True),
    incldtMB4 = cms.untracked.bool(True),
    inclcsc = cms.untracked.bool(True),
    debug = cms.untracked.bool(False),
    inves = cms.untracked.bool(True),
    DuplicationCorrection = cms.untracked.int32(1),
    manualalignment = cms.untracked.bool(False),
    AliFileName = cms.untracked.string('/afs/cern.ch/user/c/carrillo/endcap/CMSSW_3_0_0_pre10/src/DQM/RPCMonitorModule/data/Alignment69912.dat'),
    rangestrips = cms.untracked.double(4.),
    # cscSegments = cms.untracked.InputTag('hltCscSegments'),
    # dt4DSegments = cms.untracked.InputTag('hltDt4DSegments'),
    # rpcRecHits = cms.InputTag("hltRpcRecHits"),
    cscSegments = cms.untracked.InputTag('cscSegments'),
    dt4DSegments = cms.untracked.InputTag('dt4DSegments'),
    rpcRecHits = cms.InputTag("rpcRecHits"),

    rpcDTPoints = cms.InputTag("rpcPointProducer","RPCDTExtrapolatedPoints"),
    rpcCSCPoints = cms.InputTag("rpcPointProducer","RPCCSCExtrapolatedPoints"),

    EffSaveRootFile = cms.untracked.bool(True),
    EffRootFileName = cms.untracked.string('efficiency.root'),
    EffSaveRootFileEventsInterval = cms.untracked.int32(100)
)

# process.normfilter = cms.EDFilter("HLTHighLevel",
#     TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
#     HLTPaths = cms.vstring("AlCa_RPCMuonNormalisation*"),
#     eventSetupPathsKey = cms.string(''),
#     andOr = cms.bool(True),
#     throw = cms.bool(True)
# )
# process.load("TriggerFilter.TriggerFilter.triggerFilter_cfi")
# process.p = cms.Path(process.normfilter*process.triggerFilter*process.muonstandalonereco*process.dTandCSCSegmentsinTracks*process.rpcPointProducer*process.museg)
process.p = cms.Path(process.rpcPointProducer*process.museg)

process.DQM.collectorHost = ''
process.DQM.collectorPort = 9090
process.DQM.debug = False


