from Configurables import ApplicationMgr
from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper
from k4MarlinWrapper.parseConstants import *

from k4FWCore.parseArgs import parser
parser.add_argument("--data", type=str, default="/dataMuC", help="Top-level directory for data")
the_args = parser.parse_args()

algList = []
evtsvc = EventDataSvc()

CONSTANTS = {
}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = INFO
read.Files = [f"{the_args.data}/BIB10TeV/sim_TYPEEVENT/BIB_sim_INFILENAME.slcio"]
algList.append(read)

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = INFO
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {
    "HowOften": ["1"]
}

Output_LCIO = MarlinProcessorWrapper("Output_LCIO")
Output_LCIO.OutputLevel = INFO
Output_LCIO.ProcessorType = "LCIOOutputProcessor"
Output_LCIO.Parameters = {
    "DropCollectionNames": ["MCParticle"],
    "DropCollectionTypes": [],
    "FullSubsetCollections": [],
    "KeepCollectionNames": [],
    "LCIOOutputFile": [f"{the_args.data}/BIB10TeV/sim_TYPEEVENT_pruned/BIB_sim_INFILENAME.slcio"],
    "LCIOWriteMode": ["WRITE_NEW"]
}

algList.append(EventNumber)
algList.append(Output_LCIO)

ApplicationMgr(TopAlg=algList,
               EvtSel='NONE',
               EvtMax=-1,
               ExtSvc=[evtsvc],
               OutputLevel=INFO
               )
