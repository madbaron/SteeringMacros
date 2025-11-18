from Configurables import ApplicationMgr
from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *

import os

from k4FWCore.parseArgs import parser

parser.add_argument("--enableBIB", action="store_true", default=False, help="Enable BIB overlay")
parser.add_argument("--enableIP", action="store_true", default=False, help="Enable IP overlay")
parser.add_argument("--TypeEvent", type=str, default="muonGun_pT_0_50", help="Type of event to process")
parser.add_argument("--InFileName", type=str, default="0", help="Input file name for the simulation")
parser.add_argument("--code", type=str, default="/code", help="Top-level directory for code")
parser.add_argument("--data", type=str, default="/dataMuC", help="Top-level directory for data")
parser.add_argument("--skipReco", action="store_true", default=False, help="Skip reconstruction")
the_args = parser.parse_args()

algList = []
evtsvc = EventDataSvc()

CONSTANTS = {
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = INFO
read.Files = ["nuGun_MAIA_v0_tracks_30_70.slcio"]
#read.Files = ["/dataMuC/reco/muonGun_pT_0_50/muonGun_pT_0_50_reco_0.slcio"]
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
    "FileName": ["lctuple_"+the_args.TypeEvent+"_actsseededckf_"+the_args.InFileName],
    "FileType": ["root"]
}

Output_REC = MarlinProcessorWrapper("Output_REC")
Output_REC.OutputLevel = INFO
Output_REC.ProcessorType = "LCIOOutputProcessor"
if not the_args.enableBIB:
    Output_REC.Parameters = {
        "DropCollectionTypes": [],
        "DropCollectionNames": [],
        "FullSubsetCollections": [],
        "KeepCollectionNames": ["MCParticle_SiTracks", "MCParticle_SiTracks_Refitted", "MCParticle_SelectedTracks"],
        #"LCIOOutputFile": ["nuGun_tests.slcio"],
        "LCIOOutputFile": ["zummaddumma.slcio"],
        "LCIOWriteMode": ["WRITE_NEW"]
    }
else:
    Output_REC.Parameters = {
        "DropCollectionTypes": [
            "SimTrackerHit", "SimCalorimeterHit",
            "CalorimeterHit", "TrackerHitPlane",
            "LCRelation"
        ],
        "DropCollectionNames": [
            "AllTracks", "SeedTracks", "SiTracks",
            "MCPhysicsParticles", "MCPhysicsParticles_IP"
        ],
        "FullSubsetCollections": [
            "EcalBarrelCollectionSel", "EcalEndcapCollectionSel",
            "HcalBarrelCollectionSel", "HcalEndcapCollectionSel",
            "IBTrackerHitsSplit", "IETrackerHitsSplit",
            "OBTrackerHitsSplit", "OETrackerHitsSplit", 
            "VBTrackerHitsSplit", "VETrackerHitsSplit",
            "VBTrackerHitsRelationsSplit", "VETrackerHitsRelationsSplit",
            "IBTrackerHitsRelationsSplit", "IETrackerHitsRelationsSplit",
            "OBTrackerHitsRelationsSplit", "OETrackerHitsRelationsSplit",
            "VertexBarrelCollectionSplit", "VertexEndcapCollectionSplit",
            "InnerTrackerBarrelCollectionSplit", "InnerTrackerEndcapCollectionSplit",
            "OuterTrackerBarrelCollectionSplit", "OuterTrackerEndcapCollectionSplit",
            "SiTracks_Refitted"
        ],
        "KeepCollectionNames": [
            "EcalBarrelCollectionSel", "EcalEndcapCollectionSel",
            "HcalBarrelCollectionSel", "HcalEndcapCollectionSel",
            "IBTrackerHitsSplit", "IETrackerHitsSplit",
            "OBTrackerHitsSplit", "OETrackerHitsSplit", 
            "VBTrackerHitsSplit", "VETrackerHitsSplit",
            "VBTrackerHitsRelationsSplit", "VETrackerHitsRelationsSplit",
            "IBTrackerHitsRelationsSplit", "IETrackerHitsRelationsSplit",
            "OBTrackerHitsRelationsSplit", "OETrackerHitsRelationsSplit",
            "VertexBarrelCollectionSplit", "VertexEndcapCollectionSplit",
            "InnerTrackerBarrelCollectionSplit", "InnerTrackerEndcapCollectionSplit",
            "OuterTrackerBarrelCollectionSplit", "OuterTrackerEndcapCollectionSplit",
            "SiTracks_Refitted", "MCParticle_SiTracks_Refitted"
        ],
        "LCIOOutputFile": [f"{the_args.TypeEvent}_trktests_{the_args.InFileName}.slcio"],
        "LCIOWriteMode": ["WRITE_NEW"]
    }

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = INFO
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
    "DD4hepXMLFile": [os.environ['k4geo_DIR']+"/MuColl/MAIA/compact/MAIA_v0/MAIA_v0.xml"],
    "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
}

MyTrackSelectorHoles = MarlinProcessorWrapper("MyTrackSelectorHoles")
MyTrackSelectorHoles.OutputLevel = INFO
MyTrackSelectorHoles.ProcessorType = "FilterTracks"
MyTrackSelectorHoles.Parameters = {
    "InputTrackCollectionName": ["SiTracksDeduped"],
    "OutputTrackCollectionName": ["SiTracks"],
    "BarrelOnly": ["false"],
    "HasCaloState": ["false"],
    "NHitsTotal": ["3"],
    "NHitsVertex": ["0"],
    "NHitsInner": ["0"],
    "NHitsOuter": ["0"],
    "MinPt": ["0.5"],
    "Chi2Spatial": ["999"],
    "MaxHoles": ["1"],
    "MaxD0": ["999"],
    "MaxZ0": ["999"]
}

MyTrackTruth = MarlinProcessorWrapper("MyTrackTruth")
MyTrackTruth.OutputLevel = INFO
MyTrackTruth.ProcessorType = "TrackTruthProc"
MyTrackTruth.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "Particle2TrackRelationName": ["MCParticle_SiTracks"],
    "TrackCollection": ["SiTracks"],
    "TrackerHit2SimTrackerHitRelationName": ["VBTrackerHitsRelationsSplit", "IBTrackerHitsRelationsSplit", "OBTrackerHitsRelationsSplit", "VETrackerHitsRelationsSplit", "IETrackerHitsRelationsSplit", "OETrackerHitsRelationsSplit"]
}

Refit = MarlinProcessorWrapper("Refit")
Refit.OutputLevel = WARNING
Refit.ProcessorType = "RefitFinal"
Refit.Parameters = {
    "InputTrackCollectionName": ["SiTracks"],
    "InputRelationCollectionName": ["SiTrackRelations"],
    "OutputTrackCollectionName": ["SiTracks_Refitted"],
    "OutputRelationCollectionName": ["SiTracks_Refitted_Relation"],
    "MultipleScatteringOn": ["true"],
    "EnergyLossOn": ["true"],
    "SmoothOn": ["false"],
    "Max_Chi2_Incr": ["10."],
    "ReferencePoint": ["-1"],
    "extrapolateForward": ["true"],
    "MinClustersOnTrackAfterFit": ["3"],
    "MaxOutliersAllowed": ["2"],
    "ReducedChi2Cut": ["10."]
}

MyTrackTruthRefitted = MarlinProcessorWrapper("MyTrackTruthRefitted")
MyTrackTruthRefitted.OutputLevel = INFO
MyTrackTruthRefitted.ProcessorType = "TrackTruthProc"
MyTrackTruthRefitted.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "Particle2TrackRelationName": ["MCParticle_SiTracks_Refitted"],
    "TrackCollection": ["SiTracks_Refitted"],
    "TrackerHit2SimTrackerHitRelationName": ["VBTrackerHitsRelationsSplit", "IBTrackerHitsRelationsSplit", "OBTrackerHitsRelationsSplit", "VETrackerHitsRelationsSplit", "IETrackerHitsRelationsSplit", "OETrackerHitsRelationsSplit"]
}

MyTrackSelector = MarlinProcessorWrapper("MyTrackSelector")
MyTrackSelector.OutputLevel = INFO
MyTrackSelector.ProcessorType = "FilterTracks"
MyTrackSelector.Parameters = {
    "BarrelOnly": ["false"],
    "HasCaloState": ["true"],
    "NHitsTotal": ["8"],
    "NHitsVertex": ["0"],
    "NHitsInner": ["0"],
    "NHitsOuter": ["0"],
    "MinPt": ["0.5"],
    "Chi2Spatial": ["3"],
    "MaxHoles": ["5"],
    "InputTrackCollectionName": ["SiTracks_Refitted"],
    "OutputTrackCollectionName": ["SelectedTracks"],
    "MaxD0": ["999"],
    "MaxZ0": ["999"]
}


MyTrackTruthSelected = MarlinProcessorWrapper("MyTrackTruthSelected")
MyTrackTruthSelected.OutputLevel = INFO
MyTrackTruthSelected.ProcessorType = "TrackTruthProc"
MyTrackTruthSelected.Parameters = {
    "MCParticleCollection": ["MCParticle"],
    "Particle2TrackRelationName": ["MCParticle_SelectedTracks"],
    "TrackCollection": ["SelectedTracks"],
    "TrackerHit2SimTrackerHitRelationName": ["VBTrackerHitsRelationsSplit", "IBTrackerHitsRelationsSplit", "OBTrackerHitsRelationsSplit", "VETrackerHitsRelationsSplit", "IETrackerHitsRelationsSplit", "OETrackerHitsRelationsSplit"]
}


algList.append(MyAIDAProcessor)
algList.append(EventNumber)
algList.append(InitDD4hep)

algList.append(MyTrackSelectorHoles)
algList.append(MyTrackTruth)
algList.append(Refit)
algList.append(MyTrackTruthRefitted)
algList.append(MyTrackSelector)
algList.append(MyTrackTruthSelected)

algList.append(Output_REC)

ApplicationMgr(TopAlg=algList,
               EvtSel='NONE',
               EvtMax=-1,
               ExtSvc=[evtsvc],
               OutputLevel=INFO
               )
