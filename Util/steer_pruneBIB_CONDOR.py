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
read.Files = ["/nfs/dust/atlas/user/fmeloni/DataMuC/BIB10TeV/sim_TYPEEVENT/BIB_sim_INFILENAME.slcio"]
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
    "LCIOOutputFile": ["/nfs/dust/atlas/user/fmeloni/DataMuC/BIB10TeV/sim_TYPEEVENT_pruned/BIB_sim_INFILENAME.slcio"],
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
