from Configurables import ApplicationMgr
from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *
algList = []
evtsvc = EventDataSvc()

CONSTANTS = {
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = INFO
read.Files = ["/dataMuC/sim/TYPEEVENT/TYPEEVENT_sim_INFILENAME.slcio"]
algList.append(read)

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = INFO
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {
    "HowOften": ["1"]
}

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = INFO
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
    "FileName": ["lctuple_TYPEEVENT_actsseededckf_INFILENAME"],
    "FileType": ["root"]
}

Output_REC = MarlinProcessorWrapper("Output_REC")
Output_REC.OutputLevel = INFO
Output_REC.ProcessorType = "LCIOOutputProcessor"
Output_REC.Parameters = {
    "DropCollectionNames": [],
    "DropCollectionTypes": [],
    "FullSubsetCollections": ["EfficientMCParticles", "InefficientMCParticles", "SiTracks"],
    "KeepCollectionNames": ["MCParticle_SiTracks", "MCParticle_SiTracks_Refitted"],
    "LCIOOutputFile": ["/dataMuC/reco/TYPEEVENT/TYPEEVENT_reco_INFILENAME.slcio"],
    "LCIOWriteMode": ["WRITE_NEW"]
}

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = INFO
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
    "DD4hepXMLFile": ["/code/detector-simulation/geometries/MuColl_10TeV_v0A/MuColl_10TeV_v0A.xml"],
    "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
}

VXDBarrelDigitiser = MarlinProcessorWrapper("VXDBarrelDigitiser")
VXDBarrelDigitiser.OutputLevel = INFO
VXDBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDBarrelDigitiser.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.03"],
    "ResolutionU": ["0.005"],
    "ResolutionV": ["0.005"],
    "SimTrackHitCollectionName": ["VertexBarrelCollection"],
    "SimTrkHitRelCollection": ["VBTrackerHitsRelations"],
    "SubDetectorName": ["Vertex"],
    "TimeWindowMax": ["0.15"],
    "TimeWindowMin": ["-0.09"],
    "TrackerHitCollectionName": ["VBTrackerHits"],
    "UseTimeWindow": ["true"]
}

VXDEndcapDigitiser = MarlinProcessorWrapper("VXDEndcapDigitiser")
VXDEndcapDigitiser.OutputLevel = INFO
VXDEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDEndcapDigitiser.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.03"],
    "ResolutionU": ["0.005"],
    "ResolutionV": ["0.005"],
    "SimTrackHitCollectionName": ["VertexEndcapCollection"],
    "SimTrkHitRelCollection": ["VETrackerHitsRelations"],
    "SubDetectorName": ["Vertex"],
    "TimeWindowMax": ["0.15"],
    "TimeWindowMin": ["-0.09"],
    "TrackerHitCollectionName": ["VETrackerHits"],
    "UseTimeWindow": ["true"]
}

InnerPlanarDigiProcessor = MarlinProcessorWrapper("InnerPlanarDigiProcessor")
InnerPlanarDigiProcessor.OutputLevel = INFO
InnerPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["InnerTrackerBarrelCollection"],
    "SimTrkHitRelCollection": ["IBTrackerHitsRelations"],
    "SubDetectorName": ["InnerTrackers"],
    "TimeWindowMax": ["0.3"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["IBTrackerHits"],
    "UseTimeWindow": ["true"]
}

InnerEndcapPlanarDigiProcessor = MarlinProcessorWrapper(
    "InnerEndcapPlanarDigiProcessor")
InnerEndcapPlanarDigiProcessor.OutputLevel = INFO
InnerEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerEndcapPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["InnerTrackerEndcapCollection"],
    "SimTrkHitRelCollection": ["IETrackerHitsRelations"],
    "SubDetectorName": ["InnerTrackers"],
    "TimeWindowMax": ["0.3"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["IETrackerHits"],
    "UseTimeWindow": ["true"]
}

OuterPlanarDigiProcessor = MarlinProcessorWrapper("OuterPlanarDigiProcessor")
OuterPlanarDigiProcessor.OutputLevel = INFO
OuterPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["OuterTrackerBarrelCollection"],
    "SimTrkHitRelCollection": ["OBTrackerHitsRelations"],
    "SubDetectorName": ["OuterTrackers"],
    "TimeWindowMax": ["0.3"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["OBTrackerHits"],
    "UseTimeWindow": ["true"]
}

OuterEndcapPlanarDigiProcessor = MarlinProcessorWrapper(
    "OuterEndcapPlanarDigiProcessor")
OuterEndcapPlanarDigiProcessor.OutputLevel = INFO
OuterEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterEndcapPlanarDigiProcessor.Parameters = {
    "CorrectTimesForPropagation": ["true"],
    "IsStrip": ["false"],
    "ResolutionT": ["0.06"],
    "ResolutionU": ["0.007"],
    "ResolutionV": ["0.090"],
    "SimTrackHitCollectionName": ["OuterTrackerEndcapCollection"],
    "SimTrkHitRelCollection": ["OETrackerHitsRelations"],
    "SubDetectorName": ["OuterTrackers"],
    "TimeWindowMax": ["0.3"],
    "TimeWindowMin": ["-0.18"],
    "TrackerHitCollectionName": ["OETrackerHits"],
    "UseTimeWindow": ["true"]
}

CKFTracking = MarlinProcessorWrapper("CKFTracking")
CKFTracking.OutputLevel = INFO
CKFTracking.ProcessorType = "ACTSSeededCKFTrackingProc"
CKFTracking.Parameters = {
    "CKF_Chi2CutOff": ["10"],
    "CKF_NumMeasurementsCutOff": ["1"],
    "MatFile": ["/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/actstracking-1.3.1-klkmpye5nmu4ep6z5fh66nz3x3zgvf5e/share/ACTSTracking/data/material-maps.json"],
    "PropagateBackward": ["False"],
    "RunCKF": ["True"],
    "SeedFinding_CollisionRegion": ["5"],
    "SeedFinding_DeltaRMax": ["80"],
    "SeedFinding_DeltaRMin": ["5"],
    "SeedFinding_ImpactMax": ["3"],
    "SeedFinding_MinPt": ["500"],
    "SeedFinding_RMax": ["150"],
    "SeedFinding_RadLengthPerSeed": ["0.1"],
    "SeedFinding_SigmaScattering": ["50"],
    "SeedingLayers": ["13", "2", "13", "6", "13", "10", "13", "14", 
                      "14", "2", "14", "6", "14", "10", "14", "14", 
                      "15", "2", "15", "6", "15", "10", "15", "14",
                      "8", "2",
                      "17", "2",
                      "18", "2"],
    "TGeoFile": ["/opt/spack/opt/spack/linux-almalinux9-x86_64/gcc-11.5.0/actstracking-1.3.1-klkmpye5nmu4ep6z5fh66nz3x3zgvf5e/share/ACTSTracking/data/MuColl_v1.root"],
    "TrackCollectionName": ["AllTracks"],
    "TrackerHitCollectionNames": ["VBTrackerHits", "IBTrackerHits", "OBTrackerHits", "VETrackerHits", "IETrackerHits", "OETrackerHits"]
}

TrackDeduper = MarlinProcessorWrapper("TrackDeduper")
TrackDeduper.OutputLevel = INFO
TrackDeduper.ProcessorType = "ACTSDuplicateRemoval"
TrackDeduper.Parameters = {
    "InputTrackCollectionName": ["AllTracks"],
    "OutputTrackCollectionName": ["SiTracks"]
}

Refit = MarlinProcessorWrapper("Refit")
Refit.OutputLevel = INFO
Refit.ProcessorType = "RefitFinal"
Refit.Parameters = {
    "DoCutsOnRedChi2Nhits": ["true"],
    "EnergyLossOn": ["true"],
    "InputRelationCollectionName": ["SiTrackRelations"],
    "InputTrackCollectionName": ["SiTracks"],
    "Max_Chi2_Incr": ["1.79769e+30"],
    "MinClustersOnTrackAfterFit": ["3"],
    "MultipleScatteringOn": ["true"],
    #"NHitsCuts": ["1,2", "1", "3,4", "1", "5,6", "0"],
    "OutputRelationCollectionName": ["SiTracks_Refitted_Relation"],
    "OutputTrackCollectionName": ["SiTracks_Refitted"],
    "ReducedChi2Cut": ["3."],
    "ReferencePoint": ["-1"],
    "SmoothOn": ["false"],
    "extrapolateForward": ["true"]
}

MyTrackTruth = MarlinProcessorWrapper("MyTrackTruth")
MyTrackTruth.OutputLevel = INFO
MyTrackTruth.ProcessorType = "TrackTruthProc"
MyTrackTruth.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "Particle2TrackRelationName": ["MCParticle_SiTracks_Refitted"],
    "TrackCollection": ["SiTracks_Refitted"],
    "TrackerHit2SimTrackerHitRelationName": ["VBTrackerHitsRelations", "IBTrackerHitsRelations", "OBTrackerHitsRelations", "VETrackerHitsRelations", "IETrackerHitsRelations", "OETrackerHitsRelations"]
}

MyTrackTruthSiTracks = MarlinProcessorWrapper("MyTrackTruthSiTracks")
MyTrackTruthSiTracks.OutputLevel = INFO
MyTrackTruthSiTracks.ProcessorType = "TrackTruthProc"
MyTrackTruthSiTracks.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "Particle2TrackRelationName": ["MCParticle_SiTracks"],
    "TrackCollection": ["SiTracks"],
    "TrackerHit2SimTrackerHitRelationName": ["VBTrackerHitsRelations", "IBTrackerHitsRelations", "OBTrackerHitsRelations", "VETrackerHitsRelations", "IETrackerHitsRelations", "OETrackerHitsRelations"]
}

MyEcalBarrelDigi = MarlinProcessorWrapper("MyEcalBarrelDigi")
MyEcalBarrelDigi.OutputLevel = INFO
MyEcalBarrelDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalBarrelDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["0.0001575"],
    "inputHitCollections": ["ECalBarrelCollection"],
    "outputHitCollections": ["EcalBarrelCollectionDigi"],
    "outputRelationCollections": ["EcalBarrelRelationsSimDigi"],
    "threshold": ["5e-05"],
    "thresholdUnit": ["GeV"],
    "timingCorrectForPropagation": ["1"],
    "timingCut": ["1"],
    "timingResolution": ["0"],
    "timingWindowMax": ["10"],
    "timingWindowMin": ["-0.5"],
    "elec_range_mip": ["15000"]
}

MyEcalBarrelReco = MarlinProcessorWrapper("MyEcalBarrelReco")
MyEcalBarrelReco.OutputLevel = INFO
MyEcalBarrelReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalBarrelReco.Parameters = {
    "CellIDLayerString": ["layer"],
    #    "calibration_factorsMipGev": ["0.00641222630095"],
    "calibration_factorsMipGev": ["0.0066150"],
    "calibration_layergroups": ["50"],
    "inputHitCollections": ["EcalBarrelCollectionDigi"],
    "inputRelationCollections": ["EcalBarrelRelationsSimDigi"],
    "outputHitCollections": ["EcalBarrelCollectionRec"],
    "outputRelationCollections": ["EcalBarrelRelationsSimRec"]
}

MyEcalEndcapDigi = MarlinProcessorWrapper("MyEcalEndcapDigi")
MyEcalEndcapDigi.OutputLevel = INFO
MyEcalEndcapDigi.ProcessorType = "RealisticCaloDigiSilicon"
MyEcalEndcapDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["0.0001575"],
    "inputHitCollections": ["ECalEndcapCollection"],
    "outputHitCollections": ["EcalEndcapCollectionDigi"],
    "outputRelationCollections": ["EcalEndcapRelationsSimDigi"],
    "threshold": ["5e-05"],
    "thresholdUnit": ["GeV"],
    "timingCorrectForPropagation": ["1"],
    "timingCut": ["1"],
    "timingResolution": ["0"],
    "timingWindowMax": ["10"],
    "timingWindowMin": ["-0.5"],
    "elec_range_mip": ["15000"]
}

MyEcalEndcapReco = MarlinProcessorWrapper("MyEcalEndcapReco")
MyEcalEndcapReco.OutputLevel = INFO
MyEcalEndcapReco.ProcessorType = "RealisticCaloRecoSilicon"
MyEcalEndcapReco.Parameters = {
    "CellIDLayerString": ["layer"],
    #    "calibration_factorsMipGev": ["0.00641222630095"],
    "calibration_factorsMipGev": ["0.0066150"],
    "calibration_layergroups": ["50"],
    "inputHitCollections": ["EcalEndcapCollectionDigi"],
    "inputRelationCollections": ["EcalEndcapRelationsSimDigi"],
    "outputHitCollections": ["EcalEndcapCollectionRec"],
    "outputRelationCollections": ["EcalEndcapRelationsSimRec"]
}

MyHcalBarrelDigi = MarlinProcessorWrapper("MyHcalBarrelDigi")
MyHcalBarrelDigi.OutputLevel = INFO
MyHcalBarrelDigi.ProcessorType = "RealisticCaloDigiScinPpd"
MyHcalBarrelDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["0.0004925"],
    "inputHitCollections": ["HCalBarrelCollection"],
    "outputHitCollections": ["HcalBarrelCollectionDigi"],
    "outputRelationCollections": ["HcalBarrelRelationsSimDigi"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.5"],
    "thresholdUnit": ["MIP"],
    #"timingCorrectForPropagation": ["1"],
    "timingCut": ["1"],
    #"timingResolution": ["0"],
    #"timingWindowMax": ["10"],
    #"timingWindowMin": ["-0.5"]
}

MyHcalBarrelReco = MarlinProcessorWrapper("MyHcalBarrelReco")
MyHcalBarrelReco.OutputLevel = INFO
MyHcalBarrelReco.ProcessorType = "RealisticCaloRecoScinPpd"
MyHcalBarrelReco.Parameters = {
    "CellIDLayerString": ["layer"],
    #    "calibration_factorsMipGev": ["0.0287783798145"],
    "calibration_factorsMipGev": ["0.024625"],
    "calibration_layergroups": ["100"],
    "inputHitCollections": ["HcalBarrelCollectionDigi"],
    "inputRelationCollections": ["HcalBarrelRelationsSimDigi"],
    "outputHitCollections": ["HcalBarrelCollectionRec"],
    "outputRelationCollections": ["HcalBarrelRelationsSimRec"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"]
}

MyHcalEndcapDigi = MarlinProcessorWrapper("MyHcalEndcapDigi")
MyHcalEndcapDigi.OutputLevel = INFO
MyHcalEndcapDigi.ProcessorType = "RealisticCaloDigiScinPpd"
MyHcalEndcapDigi.Parameters = {
    "CellIDLayerString": ["layer"],
    "calibration_mip": ["0.0004725"],
    "inputHitCollections": ["HCalEndcapCollection"],
    "outputHitCollections": ["HcalEndcapCollectionDigi"],
    "outputRelationCollections": ["HcalEndcapRelationsSimDigi"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"],
    "ppd_npix_uncert": ["0"],
    "ppd_pix_spread": ["0"],
    "threshold": ["0.5"],
    "thresholdUnit": ["MIP"],
    #"timingCorrectForPropagation": ["1"],
    "timingCut": ["1"],
    #"timingResolution": ["0"],
    #"timingWindowMax": ["10"],
    #"timingWindowMin": ["-0.5"]
}

MyHcalEndcapReco = MarlinProcessorWrapper("MyHcalEndcapReco")
MyHcalEndcapReco.OutputLevel = INFO
MyHcalEndcapReco.ProcessorType = "RealisticCaloRecoScinPpd"
MyHcalEndcapReco.Parameters = {
    "CellIDLayerString": ["layer"],
    #   "calibration_factorsMipGev": ["0.0285819096797"],
    "calibration_factorsMipGev": ["0.024625"],
    "calibration_layergroups": ["100"],
    "inputHitCollections": ["HcalEndcapCollectionDigi"],
    "inputRelationCollections": ["HcalEndcapRelationsSimDigi"],
    "outputHitCollections": ["HcalEndcapCollectionRec"],
    "outputRelationCollections": ["HcalEndcapRelationsSimRec"],
    "ppd_mipPe": ["15"],
    "ppd_npix": ["2000"]
}

MyEcalBarrelConer = MarlinProcessorWrapper("MyEcalBarrelConer")
MyEcalBarrelConer.OutputLevel = INFO
MyEcalBarrelConer.ProcessorType = "CaloConer"
MyEcalBarrelConer.Parameters = {
    "MCParticleCollectionName": ["MCParticle"],
    "CaloHitCollectionName": ["EcalBarrelCollectionRec"],
    "CaloRelationCollectionName": ["EcalBarrelRelationsSimRec"],
    "GoodHitCollection": ["EcalBarrelCollectionConed"],
    "GoodRelationCollection": ["EcalBarrelRelationsSimConed"],
    "ConeWidth": ["0.02"]
}

MyEcalEndcapConer = MarlinProcessorWrapper("MyEcalEndcapConer")
MyEcalEndcapConer.OutputLevel = INFO
MyEcalEndcapConer.ProcessorType = "CaloConer"
MyEcalEndcapConer.Parameters = {
    "MCParticleCollectionName": ["MCParticle"],
    "CaloHitCollectionName": ["EcalEndcapCollectionRec"],
    "CaloRelationCollectionName": ["EcalEndcapRelationsSimRec"],
    "GoodHitCollection": ["EcalEndcapCollectionConed"],
    "GoodRelationCollection": ["EcalEndcapRelationsSimConed"],
    "ConeWidth": ["0.02"]
}

MyHcalBarrelConer = MarlinProcessorWrapper("MyHcalBarrelConer")
MyHcalBarrelConer.OutputLevel = INFO
MyHcalBarrelConer.ProcessorType = "CaloConer"
MyHcalBarrelConer.Parameters = {
    "MCParticleCollectionName": ["MCParticle"],
    "CaloHitCollectionName": ["HcalBarrelCollectionRec"],
    "CaloRelationCollectionName": ["HcalBarrelRelationsSimRec"],
    "GoodHitCollection": ["HcalBarrelCollectionConed"],
    "GoodRelationCollection": ["HcalBarrelRelationsSimConed"],
    "ConeWidth": ["0.02"]
}

MyHcalEndcapConer = MarlinProcessorWrapper("MyHcalEndcapConer")
MyHcalEndcapConer.OutputLevel = INFO
MyHcalEndcapConer.ProcessorType = "CaloConer"
MyHcalEndcapConer.Parameters = {
    "MCParticleCollectionName": ["MCParticle"],
    "CaloHitCollectionName": ["HcalEndcapCollectionRec"],
    "CaloRelationCollectionName": ["HcalEndcapRelationsSimRec"],
    "GoodHitCollection": ["HcalEndcapCollectionConed"],
    "GoodRelationCollection": ["HcalEndcapRelationsSimConed"],
    "ConeWidth": ["0.02"]
}


MyEcalBarrelSelector = MarlinProcessorWrapper("MyEcalBarrelSelector")
MyEcalBarrelSelector.OutputLevel = INFO
MyEcalBarrelSelector.ProcessorType = "CaloHitSelector"
MyEcalBarrelSelector.Parameters = {
    "CaloHitCollectionName": ["EcalBarrelCollectionConed"],
    "CaloRelationCollectionName": ["EcalBarrelRelationsSimConed"],
    "GoodHitCollection": ["EcalBarrelCollectionSel"],
    "GoodRelationCollection": ["EcalBarrelRelationsSimSel"],
    "ThresholdsFilePath": ["/code/CaloSelector/ECAL_Thresholds_10TeV.root"],
    "Nsigma": ["0"],
    "DoBIBsubtraction": ["false"]
}

MyEcalEndcapSelector = MarlinProcessorWrapper("MyEcalEndcapSelector")
MyEcalEndcapSelector.OutputLevel = INFO
MyEcalEndcapSelector.ProcessorType = "CaloHitSelector"
MyEcalEndcapSelector.Parameters = {
    "CaloHitCollectionName": ["EcalEndcapCollectionConed"],
    "CaloRelationCollectionName": ["EcalEndcapRelationsSimConed"],
    "GoodHitCollection": ["EcalEndcapCollectionSel"],
    "GoodRelationCollection": ["EcalEndcapRelationsSimSel"],
    "ThresholdsFilePath": ["/code/CaloSelector/ECAL_Thresholds_10TeV.root"],
    "Nsigma": ["0"],
    "DoBIBsubtraction": ["false"]
}

DDMarlinPandora = MarlinProcessorWrapper("DDMarlinPandora")
DDMarlinPandora.OutputLevel = INFO
DDMarlinPandora.ProcessorType = "DDPandoraPFANewProcessor"
DDMarlinPandora.Parameters = {
    "ClusterCollectionName": ["PandoraClusters"],
    "CreateGaps": ["false"],
    "CurvatureToMomentumFactor": ["0.00015"],
    "D0TrackCut": ["200"],
    "D0UnmatchedVertexTrackCut": ["5"],
    "DigitalMuonHits": ["0"],
    "ECalBarrelNormalVector": ["0", "0", "1"],
    "ECalCaloHitCollections": ["EcalBarrelCollectionSel", "EcalEndcapCollectionSel"],
    "ECalMipThreshold": ["0.5"],
    "ECalScMipThreshold": ["0"],
    "ECalScToEMGeVCalibration": ["1"],
    "ECalScToHadGeVCalibrationBarrel": ["1"],
    "ECalScToHadGeVCalibrationEndCap": ["1"],
    "ECalScToMipCalibration": ["1"],
    "ECalSiMipThreshold": ["0"],
    "ECalSiToEMGeVCalibration": ["1"],
    "ECalSiToHadGeVCalibrationBarrel": ["1"],
    "ECalSiToHadGeVCalibrationEndCap": ["1"],
    "ECalSiToMipCalibration": ["1"],
    "ECalToEMGeVCalibration": ["1.02373335516"],
    "ECalToHadGeVCalibrationBarrel": ["1.17344504717"],
    "ECalToHadGeVCalibrationEndCap": ["1.17344504717"],
    "ECalToMipCalibration": ["181.818"],
    "EMConstantTerm": ["0.01"],
    "EMStochasticTerm": ["0.17"],
    "FinalEnergyDensityBin": ["110."],
    "HCalBarrelNormalVector": ["0", "0", "1"],
    "HCalCaloHitCollections": ["HcalBarrelCollectionConed", "HcalEndcapCollectionConed"],
    "HCalMipThreshold": ["0.3"],
    "HCalToEMGeVCalibration": ["1.0"],
    "HCalToHadGeVCalibration": ["1.02821419758"],
    "HCalToMipCalibration": ["37.1747"],
    "HadConstantTerm": ["0.03"],
    "HadStochasticTerm": ["0.6"],
    "KinkVertexCollections": ["KinkVertices"],
    "LayersFromEdgeMaxRearDistance": ["250"],
    "MCParticleCollections": ["MCParticle"],
    "MaxBarrelTrackerInnerRDistance": ["200"],
    "MaxClusterEnergyToApplySoftComp": ["2000."],
    "MaxHCalHitHadronicEnergy": ["1000000"],
    "MaxTrackHits": ["5000"],
    "MaxTrackSigmaPOverP": ["0.15"],
    "MinBarrelTrackerHitFractionOfExpected": ["0"],
    "MinCleanCorrectedHitEnergy": ["0.1"],
    "MinCleanHitEnergy": ["0.5"],
    "MinCleanHitEnergyFraction": ["0.01"],
    "MinFtdHitsForBarrelTrackerHitFraction": ["0"],
    "MinFtdTrackHits": ["0"],
    "MinMomentumForTrackHitChecks": ["0"],
    "MinTpcHitFractionOfExpected": ["0"],
    "MinTrackECalDistanceFromIp": ["0"],
    "MinTrackHits": ["0"],
#    "MuonBarrelBField": ["5.0"],
    "MuonBarrelBField": ["0.0001"],
    "MuonCaloHitCollections": ["MUON"],
#    "MuonEndCapBField": ["5.0"],
    "MuonEndCapBField": ["0.0001"],
    "MuonHitEnergy": ["0.5"],
    "MuonToMipCalibration": ["19607.8"],
    "NEventsToSkip": ["0"],
    "NOuterSamplingLayers": ["3"],
    "PFOCollectionName": ["PandoraPFOs"],
    "PandoraSettingsXmlFile": ["/code/SteeringMacros/PandoraSettings/PandoraSettingsDefault.xml"],
    "ProngVertexCollections": ["ProngVertices"],
    "ReachesECalBarrelTrackerOuterDistance": ["-100"],
    "ReachesECalBarrelTrackerZMaxDistance": ["-50"],
    "ReachesECalFtdZMaxDistance": ["1"],
    "ReachesECalMinFtdLayer": ["0"],
    "ReachesECalNBarrelTrackerHits": ["0"],
    "ReachesECalNFtdHits": ["0"],
    "RelCaloHitCollections": ["EcalBarrelRelationsSimSel", "EcalEndcapRelationsSimSel", "HcalBarrelRelationsSimConed", "HcalEndcapRelationsSimConed", "RelationMuonHit"],
    "RelTrackCollections": ["SiTracks_Refitted_Relation"],
    "ShouldFormTrackRelationships": ["1"],
    "SoftwareCompensationEnergyDensityBins": ["0", "2.", "5.", "7.5", "9.5", "13.", "16.", "20.", "23.5", "28.", "33.", "40.", "50.", "75.", "100."],
    "SoftwareCompensationWeights": ["1.61741", "-0.00444385", "2.29683e-05", "-0.0731236", "-0.00157099", "-7.09546e-07", "0.868443", "1.0561", "-0.0238574"],
    # ECAL corrections w/o BIB w/cell selection
    #"ECALInputEnergyCorrectionPoints": ["0.1", 
    #                                    "35.871", "38.327", "41.386", "45.812", "50.01", "53.71", "58.548", "63.903", "66.884", "68.92", 
    #                                    "75.776", "79.581", "85.142", "91.092", "97.439", "103.42", "108.42", "112.653", "121.198", "133.57", 
    #                                    "142.56", "152.919", "163.913", "192.116", "242.636", "292.002", "342.592", "392.635", "446.347", 
    #                                    "495.021", "544.526", "597.864", "671.43", "774.283", "874.801", "983.224", "1082.058", "1186.351", 
    #                                    "1288.68", "1412.564", "1528.811", "1834.117", "2298.427", "2820.119", "3588.558", "4565.85", "5073.16"],
    #"ECALOutputEnergyCorrectionPoints": ["0.1",  
    #                                     "16.0", "18.5", "22.5", "27.5", "32.5", "37.5", "42.5", "47.5", "52.5", "57.5", "62.5", "67.5", 
    #                                     "72.5", "77.5", "82.5", "87.5", "92.5", "97.5", "105.0", "115.0", "125.0", "135.0", "145.0", 
    #                                     "175.0", "225.0", "275.0", "325.0", "375.0", "425.0", "475.0", "525.0", "575.0", "650.0", "750.0", 
    #                                     "850.0", "950.0", "1050.0", "1150.0", "1250.0", "1350.0", "1450.0", "1750.0", "2250.0", "2750.0", 
    #                                     "3500.0", "4500.0", "5000."],
    # HCAL corrections w/o BIB w/cell selection
    #"InputEnergyCorrectionPoints": ["1.166", "1.772", "1.468", "1.844", "2.384", "2.737", "3.085", "3.886", "3.97", "4.999",
    #                                 "5.64", "6.328", "6.909", "7.352", "7.893", "9.211", "8.783", "10.494", "9.644", "10.263", 
    #                                 "10.754", "10.283", "12.955", "14.203", "15.32", "15.285", "17.759", "24.1", "34.602", "45.971", 
    #                                 "66.333", "85.715", "100.868", "121.045", "141.793", "160.122", "190.229", "236.062", "272.852", 
    #                                 "324.34", "367.599", "456.216", "508.0", "591.241", "677.222", "864.469", "1110.301", "1378.305", 
    #                                 "1763.056", "2135.02", "2372.24"],
    #"OutputEnergyCorrectionPoints": ["5.0", "11.0", "13.0", "15.0", "17.0", "19.0", "22.5", "27.5", "32.5", "37.5", 
    #                                 "42.5", "47.5", "52.5", "57.5", "62.5", "67.5", "72.5", "77.5", "82.5", "87.5", 
    #                                 "92.5", "97.5", "105.0", "115.0", "125.0", "135.0", "145.0", "175.0", "225.0", 
    #                                 "275.0", "325.0", "375.0", "425.0", "475.0", "525.0", "575.0", "650.0", "750.0", 
    #                                 "850.0", "950.0", "1050.0", "1150.0", "1250.0", "1350.0", "1450.0", "1750.0", "2250.0", "2750.0", 
    #                                 "3500.0", "4500.0", "5000."],
    #"OutputEnergyCorrectionPoints": ["5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", 
    #                                 "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", 
    #                                 "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", 
    #                                 "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", 
    #                                 "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", 
    #                                 "5000.0", "5000.0", "5000."],
    "InputEnergyCorrectionPoints": [],
    "OutputEnergyCorrectionPoints": [],
    "SplitVertexCollections": ["SplitVertices"],
    "StartVertexAlgorithmName": ["PandoraPFANew"],
    "StartVertexCollectionName": ["PandoraStartVertices"],
    "StripSplittingOn": ["0"],
    "TrackCollections": ["SiTracks_Refitted"],
    "TrackCreatorName": ["DDTrackCreatorCLIC"],
    "TrackStateTolerance": ["0"],
    "TrackSystemName": ["DDKalTest"],
    "UnmatchedVertexTrackMaxEnergy": ["5"],
    "UseEcalScLayers": ["0"],
    "UseNonVertexTracks": ["1"],
    "UseOldTrackStateCalculation": ["0"],
    "UseUnmatchedNonVertexTracks": ["0"],
    "UseUnmatchedVertexTracks": ["1"],
    "V0VertexCollections": ["V0Vertices"],
    "YokeBarrelNormalVector": ["0", "0", "1"],
    "Z0TrackCut": ["200"],
    "Z0UnmatchedVertexTrackCut": ["5"],
    "ZCutForNonVertexTracks": ["250"]
}

'''
DDMarlinPandora = MarlinProcessorWrapper("DDMarlinPandora")
DDMarlinPandora.OutputLevel = INFO
DDMarlinPandora.ProcessorType = "DDPandoraPFANewProcessor"
DDMarlinPandora.Parameters = {
    "ClusterCollectionName": ["PandoraClusters"],
    "CreateGaps": ["false"],
    "CurvatureToMomentumFactor": ["0.00015"],
    "D0TrackCut": ["200"],
    "D0UnmatchedVertexTrackCut": ["5"],
    "DigitalMuonHits": ["0"],
    "ECalBarrelNormalVector": ["0", "0", "1"],
    "ECalCaloHitCollections": ["EcalBarrelCollectionRec", "EcalEndcapCollectionRec"],
    "ECalMipThreshold": ["0.5"],
    "ECalScMipThreshold": ["0"],
    "ECalScToEMGeVCalibration": ["1"],
    "ECalScToHadGeVCalibrationBarrel": ["1"],
    "ECalScToHadGeVCalibrationEndCap": ["1"],
    "ECalScToMipCalibration": ["1"],
    "ECalSiMipThreshold": ["0"],
    "ECalSiToEMGeVCalibration": ["1"],
    "ECalSiToHadGeVCalibrationBarrel": ["1"],
    "ECalSiToHadGeVCalibrationEndCap": ["1"],
    "ECalSiToMipCalibration": ["1"],
    "ECalToEMGeVCalibration": ["1.02373335516"],
    "ECalToHadGeVCalibrationBarrel": ["1.17344504717"],
    "ECalToHadGeVCalibrationEndCap": ["1.17344504717"],
    "ECalToMipCalibration": ["181.818"],
    "EMConstantTerm": ["0.01"],
    "EMStochasticTerm": ["0.17"],
    "FinalEnergyDensityBin": ["110."],
    "HCalBarrelNormalVector": ["0", "0", "1"],
    "HCalCaloHitCollections": ["HcalBarrelCollectionRec", "HcalEndcapCollectionRec"],
    "HCalMipThreshold": ["0.3"],
    "HCalToEMGeVCalibration": ["1.0"],
    "HCalToHadGeVCalibration": ["1.02821419758"],
    "HCalToMipCalibration": ["37.1747"],
    "HadConstantTerm": ["0.03"],
    "HadStochasticTerm": ["0.6"],
    "KinkVertexCollections": ["KinkVertices"],
    "LayersFromEdgeMaxRearDistance": ["250"],
    "MCParticleCollections": ["MCParticle"],
    "MaxBarrelTrackerInnerRDistance": ["200"],
    "MaxClusterEnergyToApplySoftComp": ["2000."],
    "MaxHCalHitHadronicEnergy": ["1000000"],
    "MaxTrackHits": ["5000"],
    "MaxTrackSigmaPOverP": ["0.15"],
    "MinBarrelTrackerHitFractionOfExpected": ["0"],
    "MinCleanCorrectedHitEnergy": ["0.1"],
    "MinCleanHitEnergy": ["0.5"],
    "MinCleanHitEnergyFraction": ["0.01"],
    "MinFtdHitsForBarrelTrackerHitFraction": ["0"],
    "MinFtdTrackHits": ["0"],
    "MinMomentumForTrackHitChecks": ["0"],
    "MinTpcHitFractionOfExpected": ["0"],
    "MinTrackECalDistanceFromIp": ["0"],
    "MinTrackHits": ["0"],
#    "MuonBarrelBField": ["5.0"],
    "MuonBarrelBField": ["0.0001"],
    "MuonCaloHitCollections": ["MUON"],
#    "MuonEndCapBField": ["5.0"],
    "MuonEndCapBField": ["0.0001"],
    "MuonHitEnergy": ["0.5"],
    "MuonToMipCalibration": ["19607.8"],
    "NEventsToSkip": ["0"],
    "NOuterSamplingLayers": ["3"],
    "PFOCollectionName": ["PandoraPFOs"],
    "PandoraSettingsXmlFile": ["/code/SteeringMacros/PandoraSettings/PandoraSettingsDefault.xml"],
    "ProngVertexCollections": ["ProngVertices"],
    "ReachesECalBarrelTrackerOuterDistance": ["-100"],
    "ReachesECalBarrelTrackerZMaxDistance": ["-50"],
    "ReachesECalFtdZMaxDistance": ["1"],
    "ReachesECalMinFtdLayer": ["0"],
    "ReachesECalNBarrelTrackerHits": ["0"],
    "ReachesECalNFtdHits": ["0"],
    "RelCaloHitCollections": ["EcalBarrelRelationsSimRec", "EcalEndcapRelationsSimRec", "HcalBarrelRelationsSimRec", "HcalEndcapRelationsSimRec", "RelationMuonHit"],
    "RelTrackCollections": ["SiTracks_Refitted_Relation"],
    "ShouldFormTrackRelationships": ["1"],
    "SoftwareCompensationEnergyDensityBins": ["0", "2.", "5.", "7.5", "9.5", "13.", "16.", "20.", "23.5", "28.", "33.", "40.", "50.", "75.", "100."],
    "SoftwareCompensationWeights": ["1.61741", "-0.00444385", "2.29683e-05", "-0.0731236", "-0.00157099", "-7.09546e-07", "0.868443", "1.0561", "-0.0238574"],
    # ECAL corrections w/o BIB w/cell selection
    #"ECALInputEnergyCorrectionPoints": ["0.1", 
    #                                    "35.871", "38.327", "41.386", "45.812", "50.01", "53.71", "58.548", "63.903", "66.884", "68.92", 
    #                                    "75.776", "79.581", "85.142", "91.092", "97.439", "103.42", "108.42", "112.653", "121.198", "133.57", 
    #                                    "142.56", "152.919", "163.913", "192.116", "242.636", "292.002", "342.592", "392.635", "446.347", 
    #                                    "495.021", "544.526", "597.864", "671.43", "774.283", "874.801", "983.224", "1082.058", "1186.351", 
    #                                    "1288.68", "1412.564", "1528.811", "1834.117", "2298.427", "2820.119", "3588.558", "4565.85", "5073.16"],
    #"ECALOutputEnergyCorrectionPoints": ["0.1",  
    #                                     "16.0", "18.5", "22.5", "27.5", "32.5", "37.5", "42.5", "47.5", "52.5", "57.5", "62.5", "67.5", 
    #                                     "72.5", "77.5", "82.5", "87.5", "92.5", "97.5", "105.0", "115.0", "125.0", "135.0", "145.0", 
    #                                     "175.0", "225.0", "275.0", "325.0", "375.0", "425.0", "475.0", "525.0", "575.0", "650.0", "750.0", 
    #                                     "850.0", "950.0", "1050.0", "1150.0", "1250.0", "1350.0", "1450.0", "1750.0", "2250.0", "2750.0", 
    #                                     "3500.0", "4500.0", "5000."],
    # HCAL corrections w/o BIB w/cell selection
    #"InputEnergyCorrectionPoints": ["1.166", "1.772", "1.468", "1.844", "2.384", "2.737", "3.085", "3.886", "3.97", "4.999",
    #                                 "5.64", "6.328", "6.909", "7.352", "7.893", "9.211", "8.783", "10.494", "9.644", "10.263", 
    #                                 "10.754", "10.283", "12.955", "14.203", "15.32", "15.285", "17.759", "24.1", "34.602", "45.971", 
    #                                 "66.333", "85.715", "100.868", "121.045", "141.793", "160.122", "190.229", "236.062", "272.852", 
    #                                 "324.34", "367.599", "456.216", "508.0", "591.241", "677.222", "864.469", "1110.301", "1378.305", 
    #                                 "1763.056", "2135.02", "2372.24"],
    #"OutputEnergyCorrectionPoints": ["5.0", "11.0", "13.0", "15.0", "17.0", "19.0", "22.5", "27.5", "32.5", "37.5", 
    #                                 "42.5", "47.5", "52.5", "57.5", "62.5", "67.5", "72.5", "77.5", "82.5", "87.5", 
    #                                 "92.5", "97.5", "105.0", "115.0", "125.0", "135.0", "145.0", "175.0", "225.0", 
    #                                 "275.0", "325.0", "375.0", "425.0", "475.0", "525.0", "575.0", "650.0", "750.0", 
    #                                 "850.0", "950.0", "1050.0", "1150.0", "1250.0", "1350.0", "1450.0", "1750.0", "2250.0", "2750.0", 
    #                                 "3500.0", "4500.0", "5000."],
    #"OutputEnergyCorrectionPoints": ["5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", 
    #                                 "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", 
    #                                 "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", 
    #                                 "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", 
    #                                 "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", "5000.", 
    #                                 "5000.0", "5000.0", "5000."],
    "InputEnergyCorrectionPoints": [],
    "OutputEnergyCorrectionPoints": [],
    "SplitVertexCollections": ["SplitVertices"],
    "StartVertexAlgorithmName": ["PandoraPFANew"],
    "StartVertexCollectionName": ["PandoraStartVertices"],
    "StripSplittingOn": ["0"],
    "TrackCollections": ["SiTracks_Refitted"],
    "TrackCreatorName": ["DDTrackCreatorCLIC"],
    "TrackStateTolerance": ["0"],
    "TrackSystemName": ["DDKalTest"],
    "UnmatchedVertexTrackMaxEnergy": ["5"],
    "UseEcalScLayers": ["0"],
    "UseNonVertexTracks": ["1"],
    "UseOldTrackStateCalculation": ["0"],
    "UseUnmatchedNonVertexTracks": ["0"],
    "UseUnmatchedVertexTracks": ["1"],
    "V0VertexCollections": ["V0Vertices"],
    "YokeBarrelNormalVector": ["0", "0", "1"],
    "Z0TrackCut": ["200"],
    "Z0UnmatchedVertexTrackCut": ["5"],
    "ZCutForNonVertexTracks": ["250"]
}
'''

FastJetProcessor = MarlinProcessorWrapper("FastJetProcessor")
FastJetProcessor.OutputLevel = INFO
FastJetProcessor.ProcessorType = "FastJetProcessor"
FastJetProcessor.Parameters = {
    "algorithm": ["antikt_algorithm", "0.4"],
    "clusteringMode": ["Inclusive", "5"],
    "jetOut": ["JetOut"],
    "recParticleIn": ["PandoraPFOs"],
    "recombinationScheme": ["E_scheme"]
}

ValenciaJetProcessor = MarlinProcessorWrapper("ValenciaJetProcessor")
ValenciaJetProcessor.OutputLevel = INFO
ValenciaJetProcessor.ProcessorType = "FastJetProcessor"
ValenciaJetProcessor.Parameters = {
    "algorithm": ["ValenciaPlugin", "1.2", "1.0", "0.7"],
    "clusteringMode": ["ExclusiveNJets", "2"],
    "jetOut": ["ValenciaJetOut"],
    "recParticleIn": ["PandoraPFOs"],
    "recombinationScheme": ["E_scheme"]
}

MyDDSimpleMuonDigi = MarlinProcessorWrapper("MyDDSimpleMuonDigi")
MyDDSimpleMuonDigi.OutputLevel = INFO
MyDDSimpleMuonDigi.ProcessorType = "DDSimpleMuonDigi"
MyDDSimpleMuonDigi.Parameters = {
    "CalibrMUON": ["70.1"],
    "MUONCollections": ["YokeBarrelCollection", "YokeEndcapCollection"],
    "MUONOutputCollection": ["MUON"],
    "MaxHitEnergyMUON": ["2.0"],
    "MuonThreshold": ["1e-06"],
    "RelationOutputCollection": ["RelationMuonHit"]
}

algList.append(MyAIDAProcessor)
algList.append(EventNumber)
algList.append(InitDD4hep)
algList.append(VXDBarrelDigitiser)
algList.append(VXDEndcapDigitiser)
algList.append(InnerPlanarDigiProcessor)
algList.append(InnerEndcapPlanarDigiProcessor)
algList.append(OuterPlanarDigiProcessor)
algList.append(OuterEndcapPlanarDigiProcessor)
algList.append(CKFTracking)
algList.append(TrackDeduper)
algList.append(Refit)
algList.append(MyTrackTruth)
algList.append(MyTrackTruthSiTracks)
algList.append(MyEcalBarrelDigi)
algList.append(MyEcalBarrelReco)
algList.append(MyEcalEndcapDigi)
algList.append(MyEcalEndcapReco)
algList.append(MyHcalBarrelDigi)
algList.append(MyHcalBarrelReco)
algList.append(MyHcalEndcapDigi)
algList.append(MyHcalEndcapReco)
algList.append(MyEcalBarrelConer)
algList.append(MyEcalEndcapConer)
algList.append(MyHcalBarrelConer)
algList.append(MyHcalEndcapConer)
algList.append(MyEcalBarrelSelector)
algList.append(MyEcalEndcapSelector)
algList.append(MyDDSimpleMuonDigi)
algList.append(DDMarlinPandora)
algList.append(FastJetProcessor)
algList.append(ValenciaJetProcessor)
algList.append(Output_REC) 

ApplicationMgr(TopAlg=algList,
               EvtSel='NONE',
               EvtMax=-1,
               ExtSvc=[evtsvc],
               OutputLevel=INFO
               )
