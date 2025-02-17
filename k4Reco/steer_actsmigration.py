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
read.Files = ["muonGun_sim_v0A.slcio"]
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
    "FileName": ["lctuple_muonGun"],
    "FileType": ["root"]
}

Output_REC = MarlinProcessorWrapper("Output_REC")
Output_REC.OutputLevel = INFO
Output_REC.ProcessorType = "LCIOOutputProcessor"
Output_REC.Parameters = {
    "DropCollectionNames": [],
    "DropCollectionTypes": [],
    "FullSubsetCollections": ["EfficientMCParticles", "InefficientMCParticles"],
    "KeepCollectionNames": ["MCParticle_SiTracks_Refitted"],
    "LCIOOutputFile": ["muonGun_reco_v0A.slcio"],
    "LCIOWriteMode": ["WRITE_NEW"]
}

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = INFO
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
    "DD4hepXMLFile": ["/data/detector-simulation/geometries/MuColl_10TeV_v0A/MuColl_10TeV_v0A.xml"],
    "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
}

VXDBarrelRealisticDigi = MarlinProcessorWrapper("VXDBarrelRealisticDigi")
VXDBarrelRealisticDigi.OutputLevel = VERBOSE
VXDBarrelRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
VXDBarrelRealisticDigi.Parameters = {
                                     "ChargeDigitizeBinning": ["1"],
                                     "ChargeDigitizeNumBits": ["4"],
                                     "ChargeMaximum": ["15000."],
                                     "CollectionName": ["VertexBarrelCollection"],
                                     "CutOnDeltaRays": ["0.030"],
                                     "Diffusion": ["0.07"],
                                     "DigitizeCharge": ["1"],
                                     "DigitizeTime": ["0"],
                                     "ElectronicEffects": ["1"],
                                     "ElectronicNoise": ["80"],
                                     "ElectronsPerKeV": ["270.3"],
                                     "EnergyLoss": ["280.0"],
                                     "MaxEnergyDelta": ["100.0"],
                                     "MaxTrackLength": ["10.0"],
                                     "OutputCollectionName": ["VBTrackerHits"],
                                     "PixelSizeX": ["0.025"],
                                     "PixelSizeY": ["0.025"],
                                     "PoissonSmearing": ["1"],
                                     "RelationColName": ["VBTrackerHitsRelations"],
                                     "SegmentLength": ["0.005"],
                                     "StoreFiredPixels": ["1"],
                                     "SubDetectorName": ["VertexBarrel"],
                                     "TanLorentz": ["0.8"],
                                     "TanLorentzY": ["0.0"],
                                     "Threshold": ["500"],
                                     "ThresholdSmearSigma": ["25"],
                                     "TimeDigitizeBinning": ["0"],
                                     "TimeDigitizeNumBits": ["10"],
                                     "TimeMaximum": ["15.0"],
                                     "TimeSmearingSigma": ["0.05"]
                                     }

VXDEndcapRealisticDigi = MarlinProcessorWrapper("VXDEndcapRealisticDigi")
VXDEndcapRealisticDigi.OutputLevel = WARNING
VXDEndcapRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
VXDEndcapRealisticDigi.Parameters = {
                                     "ChargeDigitizeBinning": ["1"],
                                     "ChargeDigitizeNumBits": ["4"],
                                     "ChargeMaximum": ["15000."],
                                     "CollectionName": ["VertexEndcapCollection"],
                                     "CutOnDeltaRays": ["0.030"],
                                     "Diffusion": ["0.07"],
                                     "DigitizeCharge": ["1"],
                                     "DigitizeTime": ["0"],
                                     "ElectronicEffects": ["1"],
                                     "ElectronicNoise": ["80"],
                                     "ElectronsPerKeV": ["270.3"],
                                     "EnergyLoss": ["280.0"],
                                     "MaxEnergyDelta": ["100.0"],
                                     "MaxTrackLength": ["10.0"],
                                     "OutputCollectionName": ["VETrackerHits"],
                                     "PixelSizeX": ["0.025"],
                                     "PixelSizeY": ["0.025"],
                                     "PoissonSmearing": ["1"],
                                     "RelationColName": ["VETrackerHitsRelations"],
                                     "SegmentLength": ["0.005"],
                                     "StoreFiredPixels": ["1"],
                                     "SubDetectorName": ["VertexEndcap"],
                                     "TanLorentz": ["0.0"],
                                     "TanLorentzY": ["0.0"],
                                     "Threshold": ["500"],
                                     "ThresholdSmearSigma": ["25"],
                                     "TimeDigitizeBinning": ["0"],
                                     "TimeDigitizeNumBits": ["10"],
                                     "TimeMaximum": ["15.0"],
                                     "TimeSmearingSigma": ["0.05"]
                                     }

InnerPlanarRealisticDigi = MarlinProcessorWrapper("InnerPlanarRealisticDigi")
InnerPlanarRealisticDigi.OutputLevel = WARNING
InnerPlanarRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
InnerPlanarRealisticDigi.Parameters = {
                                       "ChargeDigitizeBinning": ["1"],
                                       "ChargeDigitizeNumBits": ["4"],
                                       "ChargeMaximum": ["60000."],
                                       "CollectionName": ["InnerTrackerBarrelCollection"],
                                       "CutOnDeltaRays": ["0.030"],
                                       "Diffusion": ["0.07"],
                                       "DigitizeCharge": ["1"],
                                       "DigitizeTime": ["0"],
                                       "ElectronicEffects": ["1"],
                                       "ElectronicNoise": ["80"],
                                       "ElectronsPerKeV": ["270.3"],
                                       "EnergyLoss": ["280.0"],
                                       "MaxEnergyDelta": ["100.0"],
                                       "MaxTrackLength": ["10.0"],
                                       "OutputCollectionName": ["IBTrackerHits"],
                                       "PixelSizeX": ["0.050"],
                                       "PixelSizeY": ["1.0"],
                                       "PoissonSmearing": ["1"],
                                       "RelationColName": ["IBTrackerHitsRelations"],
                                       "SegmentLength": ["0.005"],
                                       "StoreFiredPixels": ["1"],
                                       "SubDetectorName": ["InnerTrackerBarrel"],
                                       "TanLorentz": ["0.8"],
                                       "TanLorentzY": ["0.0"],
                                       "Threshold": ["1000."],
                                       "ThresholdSmearSigma": ["25"],
                                       "TimeDigitizeBinning": ["0"],
                                       "TimeDigitizeNumBits": ["10"],
                                       "TimeMaximum": ["15.0"],
                                       "TimeSmearingSigma": ["0.060"]
                                       }

InnerEndcapRealisticDigi = MarlinProcessorWrapper("InnerEndcapRealisticDigi")
InnerEndcapRealisticDigi.OutputLevel = WARNING
InnerEndcapRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
InnerEndcapRealisticDigi.Parameters = {
                                       "ChargeDigitizeBinning": ["1"],
                                       "ChargeDigitizeNumBits": ["4"],
                                       "ChargeMaximum": ["60000."],
                                       "CollectionName": ["InnerTrackerEndcapCollection"],
                                       "CutOnDeltaRays": ["0.030"],
                                       "Diffusion": ["0.07"],
                                       "DigitizeCharge": ["1"],
                                       "DigitizeTime": ["0"],
                                       "ElectronicEffects": ["1"],
                                       "ElectronicNoise": ["80"],
                                       "ElectronsPerKeV": ["270.3"],
                                       "EnergyLoss": ["280.0"],
                                       "MaxEnergyDelta": ["100.0"],
                                       "MaxTrackLength": ["10.0"],
                                       "OutputCollectionName": ["IETrackerHits"],
                                       "PixelSizeX": ["0.050"],
                                       "PixelSizeY": ["1.0"],
                                       "PoissonSmearing": ["1"],
                                       "RelationColName": ["IETrackerHitsRelations"],
                                       "SegmentLength": ["0.005"],
                                       "StoreFiredPixels": ["1"],
                                       "SubDetectorName": ["InnerTrackerEndcap"],
                                       "TanLorentz": ["0.0"],
                                       "TanLorentzY": ["0.0"],
                                       "Threshold": ["1000."],
                                       "ThresholdSmearSigma": ["25"],
                                       "TimeDigitizeBinning": ["0"],
                                       "TimeDigitizeNumBits": ["10"],
                                       "TimeMaximum": ["15.0"],
                                       "TimeSmearingSigma": ["0.060"]
                                       }

OuterPlanarRealisticDigi = MarlinProcessorWrapper("OuterPlanarRealisticDigi")
OuterPlanarRealisticDigi.OutputLevel = WARNING
OuterPlanarRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
OuterPlanarRealisticDigi.Parameters = {
                                       "ChargeDigitizeBinning": ["1"],
                                       "ChargeDigitizeNumBits": ["4"],
                                       "ChargeMaximum": ["60000."],
                                       "CollectionName": ["OuterTrackerBarrelCollection"],
                                       "CutOnDeltaRays": ["0.030"],
                                       "Diffusion": ["0.07"],
                                       "DigitizeCharge": ["1"],
                                       "DigitizeTime": ["0"],
                                       "ElectronicEffects": ["1"],
                                       "ElectronicNoise": ["80"],
                                       "ElectronsPerKeV": ["270.3"],
                                       "EnergyLoss": ["280.0"],
                                       "MaxEnergyDelta": ["100.0"],
                                       "MaxTrackLength": ["10.0"],
                                       "OutputCollectionName": ["OBTrackerHits"],
                                       "PixelSizeX": ["0.050"],
                                       "PixelSizeY": ["10.0"],
                                       "PoissonSmearing": ["1"],
                                       "RelationColName": ["OBTrackerHitsRelations"],
                                       "SegmentLength": ["0.005"],
                                       "StoreFiredPixels": ["1"],
                                       "SubDetectorName": ["OuterTrackerBarrel"],
                                       "TanLorentz": ["0.8"],
                                       "TanLorentzY": ["0.0"],
                                       "Threshold": ["1000."],
                                       "ThresholdSmearSigma": ["25"],
                                       "TimeDigitizeBinning": ["0"],
                                       "TimeDigitizeNumBits": ["10"],
                                       "TimeMaximum": ["15.0"],
                                       "TimeSmearingSigma": ["0.060"]
                                       }

OuterEndcapRealisticDigi = MarlinProcessorWrapper("OuterEndcapRealisticDigi")
OuterEndcapRealisticDigi.OutputLevel = WARNING
OuterEndcapRealisticDigi.ProcessorType = "MuonCVXDDigitiser"
OuterEndcapRealisticDigi.Parameters = {
                                       "ChargeDigitizeBinning": ["1"],
                                       "ChargeDigitizeNumBits": ["4"],
                                       "ChargeMaximum": ["60000."],
                                       "CollectionName": ["OuterTrackerEndcapCollection"],
                                       "CutOnDeltaRays": ["0.030"],
                                       "Diffusion": ["0.07"],
                                       "DigitizeCharge": ["1"],
                                       "DigitizeTime": ["0"],
                                       "ElectronicEffects": ["1"],
                                       "ElectronicNoise": ["80"],
                                       "ElectronsPerKeV": ["270.3"],
                                       "EnergyLoss": ["280.0"],
                                       "MaxEnergyDelta": ["100.0"],
                                       "MaxTrackLength": ["10.0"],
                                       "OutputCollectionName": ["OETrackerHits"],
                                       "PixelSizeX": ["0.050"],
                                       "PixelSizeY": ["10.0"],
                                       "PoissonSmearing": ["1"],
                                       "RelationColName": ["OETrackerHitsRelations"],
                                       "SegmentLength": ["0.005"],
                                       "StoreFiredPixels": ["1"],
                                       "SubDetectorName": ["OuterTrackerEndcap"],
                                       "TanLorentz": ["0.0"],
                                       "TanLorentzY": ["0.0"],
                                       "Threshold": ["1000."],
                                       "ThresholdSmearSigma": ["25"],
                                       "TimeDigitizeBinning": ["0"],
                                       "TimeDigitizeNumBits": ["10"],
                                       "TimeMaximum": ["15.0"],
                                       "TimeSmearingSigma": ["0.060"]
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
    "MatFile": ["/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/actstracking/porting_v32-erbr2i/share/ACTSTracking/data/material-maps.json"],
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
                      "15", "2", "15", "6", "15", "10", "15", "14"],
    "TGeoFile": ["/opt/spack/opt/spack/x86_64-almalinux9-gcc11.4.1-opt/actstracking/porting_v32-erbr2i/share/ACTSTracking/data/MuColl_v1.root"],
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
    "MinClustersOnTrackAfterFit": ["6"],
    "MultipleScatteringOn": ["true"],
    # "NHitsCuts": ["1,2", "1", "3,4", "1", "5,6", "0"],
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

OverlayMIX = MarlinProcessorWrapper("OverlayMIX")
OverlayMIX.OutputLevel = INFO
OverlayMIX.ProcessorType = "OverlayTimingRandomMix"
OverlayMIX.Parameters = {
    "BackgroundFileNamesMuPlus": ["/data/MuCData/BIB10/HiStat/sim_mm/BIB_sim_100.slcio", "/data/MuCData/BIB10/HiStat/sim_mm/BIB_sim_101.slcio"],
    "BackgroundFileNamesMuMinus": ["/data/MuCData/BIB10/HiStat/sim_mp/BIB_sim_102.slcio", "/data/MuCData/BIB10/HiStat/sim_mp/BIB_sim_103.slcio"],
    "Collection_IntegrationTimes": ["VertexBarrelCollection", "-0.5", "15.",
                                    "VertexEndcapCollection", "-0.5", "15.",
                                    "InnerTrackerBarrelCollection", "-0.5", "15.",
                                    "InnerTrackerEndcapCollection", "-0.5", "15.",
                                    "OuterTrackerBarrelCollection", "-0.5", "15.",
                                    "OuterTrackerEndcapCollection", "-0.5", "15.",
                                    "ECalBarrelCollection", "-0.5", "15.",
                                    "ECalEndcapCollection", "-0.5", "15.",
                                    "HCalBarrelCollection", "-0.5", "15.",
                                    "HCalEndcapCollection", "-0.5", "15.",
                                    "YokeBarrelCollection", "-0.5", "15.",
                                    "YokeEndcapCollection", "-0.5", "15."],
    "IntegrationTimeMin": ["-0.5"],
    "MCParticleCollectionName": ["MCParticle"],
    "MergeMCParticles": ["false"],
    "NumberBackground": ["2"]
}

OverlayIP = MarlinProcessorWrapper("OverlayIP")
OverlayIP.OutputLevel = INFO
OverlayIP.ProcessorType = "OverlayTimingGeneric"
OverlayIP.Parameters = {
    "AllowReusingBackgroundFiles": ["true"],
    "BackgroundFileNames": ["pairs_10v1_5T_sim.slcio"],
    "Collection_IntegrationTimes": [
        "VertexBarrelCollection", "-0.5", "15.",
        "VertexEndcapCollection", "-0.5", "15.",
        "InnerTrackerBarrelCollection", "-0.5", "15.",
        "InnerTrackerEndcapCollection", "-0.5", "15.",
        "OuterTrackerBarrelCollection", "-0.5", "15.",
        "OuterTrackerEndcapCollection", "-0.5", "15.",
        "ECalBarrelCollection", "-0.5", "15.",
        "ECalEndcapCollection", "-0.5", "15.",
        "HCalBarrelCollection", "-0.5", "15.",
        "HCalEndcapCollection", "-0.5", "15.",
        "YokeBarrelCollection", "-0.5", "15.",
        "YokeEndcapCollection", "-0.5", "15."
    ],
    "Delta_t": ["10000"],
    "IntegrationTimeMin": ["-0.5"],
    "MCParticleCollectionName": ["MCParticle"],
    "MCPhysicsParticleCollectionName": ["MCPhysicsParticles_IP"],
    "MergeMCParticles": ["true"],
    "NBunchtrain": ["1"],
    "NumberBackground": ["1"],
    "PhysicsBX": ["1"],
    "Poisson_random_NOverlay": ["false"],
    "RandomBx": ["false"],
    "StartBackgroundFileIndex": ["0"],
    "TPCDriftvelocity": ["0.05"]
}


algList.append(MyAIDAProcessor)
algList.append(EventNumber)
algList.append(InitDD4hep)
# algList.append(OverlayMIX)
#algList.append(OverlayIP)

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

algList.append(Output_REC)

ApplicationMgr(TopAlg=algList,
               EvtSel='NONE',
               EvtMax=1,
               ExtSvc=[evtsvc],
               OutputLevel=INFO
               )
