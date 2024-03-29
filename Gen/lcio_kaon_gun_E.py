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

outfile = "kaonGun_gen.slcio"

# --------------------------------------------


wrt = IOIMPL.LCFactory.getInstance().createLCWriter()

wrt.open(outfile, EVENT.LCIO.WRITE_NEW)

random.seed()


# ========== particle properties ===================

# particles per event
npart = 1

genstat = 1

E_min = 2
E_max = 100

theta_min = 8./180.*math.pi
theta_max = 172./180.*math.pi

pdg = 130

mass = 0.497611   # k0 mass
charge = 0.

decayLen = 15.34 # m
#decayLen = 1.e22

beamspot_sigma = 1.5  # mm

# =================================================


for j in range(0, nevt):

    col = IMPL.LCCollectionVec(EVENT.LCIO.MCPARTICLE)
    evt = IMPL.LCEventImpl()

    evt.setEventNumber(j)

    evt.addCollection(col, "MCParticle")

    print(j, "-----------------------------")

    for ipart in range(0, npart):

        energy = random.uniform(E_min, E_max) 
        p = math.sqrt(energy*energy - mass*mass)
        theta = random.uniform(theta_min, theta_max)
        phi = random.random() * math.pi * 2.

        px = p * math.sin(theta) * math.cos(phi)
        py = p * math.sin(theta) * math.sin(phi)
        pz = p * math.cos(theta)

        momentum = array('f', [px, py, pz])

        # --- endpoint

        myKaon = TLorentzVector()
        myKaon.SetPxPyPzE(px,py,pz,energy)

        denominator = decayLen * myKaon.Gamma() * myKaon.Beta()
        exponential = TF1("myExp", "(1/[0])*TMath::Exp(-1*x/[0])")
        exponential.SetParameter(0, denominator)
        flight = exponential.GetRandom()

        epx = flight * math.cos(phi) * math.sin(theta)
        epy = flight * math.sin(phi) * math.sin(theta)
        epz = flight * math.cos(theta)

        endpoint = array('d', [epx, epy, epz])

        # --- production vertex

        vpx = 0.
        vpy = 0.
        vpz = random.gauss(0., beamspot_sigma)

        vertex = array('d', [vpx, vpy, vpz])

        time = 0.

        # --- particle charge

        if ipart % 2 == 1:
            pdg = -pdg
            charge = -charge


# --------------- create MCParticle -------------------

        mcp = IMPL.MCParticleImpl()

        mcp.setGeneratorStatus(genstat)
        mcp.setMass(mass)
        mcp.setPDG(pdg)
        mcp.setMomentum(momentum)
        mcp.setCharge(charge)
        mcp.setVertex(vertex)
        mcp.setTime(time)

        if (decayLen < 1.e9):   # arbitrary ...
            mcp.setEndpoint(endpoint)

        print("  ", ipart, pdg, charge, energy, phi, theta)


# -------------------------------------------------------

        col.addElement(mcp)

    wrt.writeEvent(evt)

print("Generated ", E_min, E_max, " slice")

wrt.close()
