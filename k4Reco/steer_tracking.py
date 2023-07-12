from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *
algList = []

CONSTANTS = {
}

parseConstants(CONSTANTS)

from Configurables import k4DataSvc, PodioInput, ToolSvc, EDM4hep2LcioTool, Lcio2EDM4hepTool

evtsvc = k4DataSvc('EventDataSvc')
evtsvc.input = 'cippa.edm4hep.root'

inp = PodioInput('InputReader')
inp.collections = [
  'EventHeader',
  'MCParticles',
  'VertexBarrelCollection',
  'VertexEndcapCollection',
  'InnerTrackerBarrelCollection',
  'OuterTrackerBarrelCollection',
  'InnerTrackerEndcapCollection',
  'OuterTrackerEndcapCollection',
]
inp.OutputLevel = DEBUG

Config = MarlinProcessorWrapper("Config")
Config.OutputLevel = WARNING 
Config.ProcessorType = "CLICRecoConfig" 
Config.Parameters = {
                     "Overlay": ["False"],
                     "OverlayChoices": ["False", "BIB"],
                     "Tracking": ["Conformal"],
                     "TrackingChoices": ["Truth", "Conformal"],
                     "VertexUnconstrained": ["OFF"],
                     "VertexUnconstrainedChoices": ["ON", "OFF"]
                     }

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = WARNING 
EventNumber.ProcessorType = "Statusmonitor" 
EventNumber.Parameters = {
                          "HowOften": ["1"]
                          }

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = WARNING 
MyAIDAProcessor.ProcessorType = "AIDAProcessor" 
MyAIDAProcessor.Parameters = {
                              "Compress": ["1"],
                              "FileName": ["histograms_hits"],
                              "FileType": ["root"]
                              }

edmConvTool = EDM4hep2LcioTool("EDM4hep2lcio")
edmConvTool.convertAll = False
edmConvTool.collNameMapping = {
  "MCParticles": "MCParticles_LCIO",
  "VertexBarrelCollection": "VertexBarrelCollection_LCIO",
  "VertexEndcapCollection": "VertexEndcapCollection_LCIO",
  "InnerTrackerBarrelCollection": "InnerTrackerBarrelCollection_LCIO",
  "OuterTrackerBarrelCollection": "OuterTrackerBarrelCollection_LCIO",
  "InnerTrackerEndcapCollection": "InnerTrackerEndcapCollection_LCIO",
  "OuterTrackerEndcapCollection": "OuterTrackerEndcapCollection_LCIO"
}
edmConvTool.OutputLevel = DEBUG

lcioConvTool = Lcio2EDM4hepTool("LCIO2EDM4hep")
lcioConvTool.convertAll = False
lcioConvTool.collNameMapping = {
    "Tracks": "Tracks"
}
lcioConvTool.OutputLevel = DEBUG

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = WARNING 
InitDD4hep.ProcessorType = "InitializeDD4hep" 
InitDD4hep.Parameters = {
                         "DD4hepXMLFile": ["../detector-simulation/geometries/MuColl_10TeV_v0A/MuColl_10TeV_v0A.xml"],
                         "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
                         }
InitDD4hep.EDM4hep2LcioTool=edmConvTool

VXDBarrelDigitiser = MarlinProcessorWrapper("VXDBarrelDigitiser")
VXDBarrelDigitiser.OutputLevel = WARNING 
VXDBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor" 
VXDBarrelDigitiser.Parameters = {
                                 "CorrectTimesForPropagation": ["true"],
                                 "IsStrip": ["false"],
                                 "ResolutionT": ["0.03"],
                                 "ResolutionU": ["0.005"],
                                 "ResolutionV": ["0.005"],
                                 "SimTrackHitCollectionName": ["VertexBarrelCollection_LCIO"],
                                 "SimTrkHitRelCollection": ["VBTrackerHitsRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TimeWindowMax": ["0.09"],
                                 "TimeWindowMin": ["-0.09"],
                                 "TrackerHitCollectionName": ["VBTrackerHits"],
                                 "UseTimeWindow": ["true"]
                                 }

VXDEndcapDigitiser = MarlinProcessorWrapper("VXDEndcapDigitiser")
VXDEndcapDigitiser.OutputLevel = WARNING 
VXDEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor" 
VXDEndcapDigitiser.Parameters = {
                                 "CorrectTimesForPropagation": ["true"],
                                 "IsStrip": ["false"],
                                 "ResolutionT": ["0.03"],
                                 "ResolutionU": ["0.005"],
                                 "ResolutionV": ["0.005"],
                                 "SimTrackHitCollectionName": ["VertexEndcapCollection_LCIO"],
                                 "SimTrkHitRelCollection": ["VETrackerHitsRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TimeWindowMax": ["0.09"],
                                 "TimeWindowMin": ["-0.09"],
                                 "TrackerHitCollectionName": ["VETrackerHits"],
                                 "UseTimeWindow": ["true"]
                                 }

InnerPlanarDigiProcessor = MarlinProcessorWrapper("InnerPlanarDigiProcessor")
InnerPlanarDigiProcessor.OutputLevel = WARNING 
InnerPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor" 
InnerPlanarDigiProcessor.Parameters = {
                                       "CorrectTimesForPropagation": ["true"],
                                       "IsStrip": ["false"],
                                       "ResolutionT": ["0.06"],
                                       "ResolutionU": ["0.007"],
                                       "ResolutionV": ["0.090"],
                                       "SimTrackHitCollectionName": ["InnerTrackerBarrelCollection_LCIO"],
                                       "SimTrkHitRelCollection": ["IBTrackerHitsRelations"],
                                       "SubDetectorName": ["InnerTrackers"],
                                       "TimeWindowMax": ["0.18"],
                                       "TimeWindowMin": ["-0.18"],
                                       "TrackerHitCollectionName": ["IBTrackerHits"],
                                       "UseTimeWindow": ["true"]
                                       }

InnerEndcapPlanarDigiProcessor = MarlinProcessorWrapper("InnerEndcapPlanarDigiProcessor")
InnerEndcapPlanarDigiProcessor.OutputLevel = WARNING 
InnerEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor" 
InnerEndcapPlanarDigiProcessor.Parameters = {
                                             "CorrectTimesForPropagation": ["true"],
                                             "IsStrip": ["false"],
                                             "ResolutionT": ["0.06"],
                                             "ResolutionU": ["0.007"],
                                             "ResolutionV": ["0.090"],
                                             "SimTrackHitCollectionName": ["InnerTrackerEndcapCollection_LCIO"],
                                             "SimTrkHitRelCollection": ["IETrackerHitsRelations"],
                                             "SubDetectorName": ["InnerTrackers"],
                                             "TimeWindowMax": ["0.18"],
                                             "TimeWindowMin": ["-0.18"],
                                             "TrackerHitCollectionName": ["IETrackerHits"],
                                             "UseTimeWindow": ["true"]
                                             }

OuterPlanarDigiProcessor = MarlinProcessorWrapper("OuterPlanarDigiProcessor")
OuterPlanarDigiProcessor.OutputLevel = WARNING 
OuterPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor" 
OuterPlanarDigiProcessor.Parameters = {
                                       "CorrectTimesForPropagation": ["true"],
                                       "IsStrip": ["false"],
                                       "ResolutionT": ["0.06"],
                                       "ResolutionU": ["0.007"],
                                       "ResolutionV": ["0.090"],
                                       "SimTrackHitCollectionName": ["OuterTrackerBarrelCollection_LCIO"],
                                       "SimTrkHitRelCollection": ["OBTrackerHitsRelations"],
                                       "SubDetectorName": ["OuterTrackers"],
                                       "TimeWindowMax": ["0.18"],
                                       "TimeWindowMin": ["-0.18"],
                                       "TrackerHitCollectionName": ["OBTrackerHits"],
                                       "UseTimeWindow": ["true"]
                                       }

OuterEndcapPlanarDigiProcessor = MarlinProcessorWrapper("OuterEndcapPlanarDigiProcessor")
OuterEndcapPlanarDigiProcessor.OutputLevel = WARNING 
OuterEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor" 
OuterEndcapPlanarDigiProcessor.Parameters = {
                                             "CorrectTimesForPropagation": ["true"],
                                             "IsStrip": ["false"],
                                             "ResolutionT": ["0.06"],
                                             "ResolutionU": ["0.007"],
                                             "ResolutionV": ["0.090"],
                                             "SimTrackHitCollectionName": ["OuterTrackerEndcapCollection_LCIO"],
                                             "SimTrkHitRelCollection": ["OETrackerHitsRelations"],
                                             "SubDetectorName": ["OuterTrackers"],
                                             "TimeWindowMax": ["0.18"],
                                             "TimeWindowMin": ["-0.18"],
                                             "TrackerHitCollectionName": ["OETrackerHits"],
                                             "UseTimeWindow": ["true"]
                                             }

OverlayFalse = MarlinProcessorWrapper("OverlayFalse")
OverlayFalse.OutputLevel = WARNING 
OverlayFalse.ProcessorType = "OverlayTimingGeneric" 
OverlayFalse.Parameters = {
                           "BackgroundFileNames": ["/dev/null"],
                           "Collection_IntegrationTimes": ["VertexBarrelCollection_LCIO", "-0.36", "0.48", "VertexEndcapCollection_LCIO", "-0.36", "0.48", "InnerTrackerBarrelCollection_LCIO", "-0.36", "0.48", "InnerTrackerEndcapCollection_LCIO", "-0.36", "0.48", "OuterTrackerBarrelCollection_LCIO", "-0.36", "0.48", "OuterTrackerEndcapCollection_LCIO", "-0.36", "0.48"],
                           "Delta_t": ["1"],
                           "IntegrationTimeMin": ["-0.36"],
                           "MCParticleCollectionName": ["MCParticle_LCIO"],
                           "MCPhysicsParticleCollectionName": ["MCPhysicsParticles"],
                           "MergeMCParticles": ["false"],
                           "NBunchtrain": ["0"],
                           "NumberBackground": ["0."],
                           "PhysicsBX": ["1"],
                           "Poisson_random_NOverlay": ["false"],
                           "RandomBx": ["false"],
                           "TPCDriftvelocity": ["0.05"]
                           }

OverlayBIB = MarlinProcessorWrapper("OverlayBIB")
OverlayBIB.OutputLevel = WARNING 
OverlayBIB.ProcessorType = "OverlayTimingGeneric" 
OverlayBIB.Parameters = {
                         "AllowReusingBackgroundFiles": ["false"],
                         "BackgroundFileNames": ["/data/BIB/sim_mumi-1e3x500-26m-lowth-excl_c00.slcio", "100%", "4282MB", "15.9MB/s", "04:29", "/data/BIB/sim_mupl-1e3x500-26m-lowth-excl_c00.slcio"],
                         "Collection_IntegrationTimes": ["VertexBarrelCollection", "-0.36", "0.48", "VertexEndcapCollection", "-0.36", "0.48", "InnerTrackerBarrelCollection", "-0.36", "0.48", "InnerTrackerEndcapCollection", "-0.36", "0.48", "OuterTrackerBarrelCollection", "-0.36", "0.48", "OuterTrackerEndcapCollection", "-0.36", "0.48"],
                         "Delta_t": ["1"],
                         "IntegrationTimeMin": ["-0.36"],
                         "MCParticleCollectionName": ["MCParticle"],
                         "MCPhysicsParticleCollectionName": ["MCPhysicsParticles"],
                         "MergeMCParticles": ["false"],
                         "NBunchtrain": ["1"],
                         "NumberBackground": ["2993"],
                         "PhysicsBX": ["1"],
                         "Poisson_random_NOverlay": ["false"],
                         "RandomBx": ["false"],
                         "StartBackgroundFileIndex": ["0"],
                         "TPCDriftvelocity": ["0.05"]
                         }

MyCKFTracking = MarlinProcessorWrapper("MyCKFTracking")
MyCKFTracking.OutputLevel = INFO
MyCKFTracking.ProcessorType = "ACTSSeededCKFTrackingProc" 
MyCKFTracking.Parameters = {
                            "CKF_Chi2CutOff": ["1"],
                            "CKF_NumMeasurementsCutOff": ["1"],
                            "MatFile": ["data/material-maps.json"],
                            "RunCKF": ["True"],
                            "SeedFinding_CollisionRegion": ["75"],
                            "SeedFinding_DeltaRMax": ["80"],
                            "SeedFinding_DeltaRMin": ["5"],
                            "SeedFinding_MinPt": ["500"],
                            "SeedFinding_RMax": ["150"],
                            "SeedFinding_RadLengthPerSeed": ["0.1"],
                            "SeedFinding_SigmaScattering": ["50"],
                            "SeedingLayers": ["13", "2", "13", "6", "13", "10", "13", "14", "14", "2", "14", "6", "14", "10", "14", "14", "15", "2", "15", "6", "15", "10", "15", "14"],
                            "TGeoFile": ["data/MuColl_v1.root"],
                            "TrackCollectionName": ["AllTracks"],
                            "TrackerHitCollectionNames": ["VBTrackerHits", "IBTrackerHits", "OBTrackerHits", "VETrackerHits", "IETrackerHits", "OETrackerHits"]
                            }

MyTrackDeduper = MarlinProcessorWrapper("MyTrackDeduper")
MyTrackDeduper.OutputLevel = INFO 
MyTrackDeduper.ProcessorType = "ACTSDuplicateRemoval" 
MyTrackDeduper.Parameters = {
                             "InputTrackCollectionName": ["AllTracks"],
                             "OutputTrackCollectionName": ["Tracks"]
                             }
MyTrackDeduper.Lcio2EDM4hepTool=lcioConvTool 

MergeHits = MarlinProcessorWrapper("MergeHits")
MergeHits.OutputLevel = INFO 
MergeHits.ProcessorType = "MergeCollections" 
MergeHits.Parameters = {
                        "InputCollections": ["VBTrackerHits", "IBTrackerHits", "OBTrackerHits", "VETrackerHits", "IETrackerHits", "OETrackerHits"],
                        "OutputCollection": ["HitsCollection"]
                        }

MyTrackTruth = MarlinProcessorWrapper("MyTrackTruth")
MyTrackTruth.OutputLevel = INFO 
MyTrackTruth.ProcessorType = "TrackTruthProc" 
MyTrackTruth.Parameters = {
                           "MCParticleCollection": ["MCParticle_LCIO"],
                           "Particle2TrackRelationName": ["MCParticle_Tracks"],
                           "TrackCollection": ["Tracks"],
                           "TrackerHit2SimTrackerHitRelationName": ["VBTrackerHitsRelations", "IBTrackerHitsRelations", "OBTrackerHitsRelations", "VETrackerHitsRelations", "IETrackerHitsRelations", "OETrackerHitsRelations"]
                           }


# Write output to EDM4hep
from Configurables import PodioOutput
out = PodioOutput("PodioOutput", filename = "my_output.edm4hep.root")
out.outputCommands = ["keep *"]

MyAIDAProcessor.OutputLevel = DEBUG

algList.append(inp)
algList.append(MyAIDAProcessor)
algList.append(EventNumber)
algList.append(Config)
algList.append(InitDD4hep)
# algList.append(OverlayBIB)  # Config.OverlayBIB
algList.append(OverlayFalse)  # Config.OverlayFalse
algList.append(VXDBarrelDigitiser)
algList.append(VXDEndcapDigitiser)
algList.append(InnerPlanarDigiProcessor)
algList.append(InnerEndcapPlanarDigiProcessor)
algList.append(OuterPlanarDigiProcessor)
algList.append(OuterEndcapPlanarDigiProcessor)
algList.append(MyCKFTracking)
algList.append(MyTrackDeduper)
algList.append(MyTrackTruth)
algList.append(out)

from Configurables import ApplicationMgr
ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = -1,
                ExtSvc = [evtsvc],
                OutputLevel=WARNING
              )
