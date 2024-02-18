#####################################
#
# simple script to create lcio files with single particle
# events - modify as needed
# @author F.Gaede, DESY
# @date 1/07/2014
#
# initialize environment:
#  export PYTHONPATH=${LCIO}/src/python:${ROOTSYS}/lib
#
#####################################
import math
import random
from array import array
import ROOT
from ROOT import TF1, TLorentzVector

# --- LCIO dependencies ---
from pyLCIO import UTIL, EVENT, IMPL, IO, IOIMPL

# ---- number of events ----------------------
nevt = 100000

outfile = "photonGun_gen.slcio"

# --------------------------------------------


wrt = IOIMPL.LCFactory.getInstance().createLCWriter()

wrt.open(outfile, EVENT.LCIO.WRITE_NEW)

random.seed()


# ========== particle properties ===================

# particles per event
npart = 1

genstat = 1

which_slice = 3
E_vec= [0.1, 50., 250., 1000., 5000.]

E_min = E_vec[which_slice]
E_max = E_vec[which_slice+1]

theta_min = 8./180.*math.pi
theta_max = 172./180.*math.pi

pdg = 22

decayLen = 1.e32

beamspot_sigma = 1.5 #mm

# =================================================


for j in range(0, nevt):

    col = IMPL.LCCollectionVec(EVENT.LCIO.MCPARTICLE)
    evt = IMPL.LCEventImpl()

    evt.setEventNumber(j)

    evt.addCollection(col, "MCParticle")

    print(j, "-----------------------------")

    for ipart in range(0, npart):

        energy = random.uniform(E_min, E_max) 
        p = math.sqrt(energy*energy)
        theta = random.uniform(theta_min, theta_max)
        phi = random.random() * math.pi * 2.

        px = p * math.sin(theta) * math.cos(phi)
        py = p * math.sin(theta) * math.sin(phi)
        pz = p * math.cos(theta)

        momentum = array('f', [px, py, pz])

        # --- endpoint
        epx = decayLen * math.cos( phi ) * math.sin( theta ) 
        epy = decayLen * math.sin( phi ) * math.sin( theta )
        epz = decayLen * math.cos( theta ) 

        endpoint = array('d',[ epx, epy, epz ] )  

        # --- production vertex

        vpx = 0.
        vpy = 0.
        vpz = random.gauss(0., beamspot_sigma)

        vertex = array('d', [vpx, vpy, vpz])

        time = 0.

# --------------- create MCParticle -------------------

        mcp = IMPL.MCParticleImpl()

        mcp.setGeneratorStatus(genstat)
        mcp.setMass(0.)
        mcp.setPDG(pdg)
        mcp.setMomentum(momentum)
        mcp.setCharge(0.)
        mcp.setVertex(vertex)
        mcp.setTime(time)

        if (decayLen < 1.e9):   # arbitrary ...
            mcp.setEndpoint(endpoint)

        print(" ", ipart, pdg, energy, phi, theta)

        if mcp.getEnergy() > E_max:
            print("Problem")
            print(" ", ipart, mcp.getPDG(), mcp.getEnergy())
            break

# -------------------------------------------------------

        col.addElement(mcp)

    wrt.writeEvent(evt)

print("Generated ", E_min, E_max, " slice")

wrt.close()
