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

# --- LCIO dependencies ---
from pyLCIO import UTIL, EVENT, IMPL, IO, IOIMPL

#---- number of events ----------------------
nevt = 10000

outfile = "muonGun_gen.slcio"

#--------------------------------------------


wrt = IOIMPL.LCFactory.getInstance().createLCWriter( )

wrt.open( outfile , EVENT.LCIO.WRITE_NEW ) 

random.seed()


#========== particle properties ===================

# particles per event
npart = 1

genstat  = 1

which_slice = 3
pt_vec= [0.1, 50., 250., 1000., 5000.]

pt_min = pt_vec[which_slice]
pt_max = pt_vec[which_slice+1]

theta_min = 8./180.*math.pi
theta_max = 172./180.*math.pi

pdg = 13

mass =  0.105658 
charge = -1.

decayLen = 1.e32

beamspot_sigma = 1.5 #mm

#=================================================


for j in range( 0, nevt ):

    col = IMPL.LCCollectionVec( EVENT.LCIO.MCPARTICLE ) 
    evt = IMPL.LCEventImpl() 

    evt.setEventNumber( j ) 

    evt.addCollection( col , "MCParticle" )

    print (j, "-----------------------------")
    
    for ipart in range( 0, npart ):
    
        pt = random.uniform(pt_min, pt_max)
        theta = random.uniform(theta_min, theta_max) 
        phi =  random.random() * math.pi * 2.

        p = pt/math.sin( theta )
        energy   = math.sqrt( mass*mass  + p * p ) 

        if energy > 5000:
            continue
        
        px = pt * math.cos( phi )
        py = pt * math.sin( phi )
        pz = p * math.cos( theta )

        momentum  = array('f',[ px, py, pz ] )  

        
        # --- endpoint
        
        epx = decayLen * math.cos( phi ) * math.sin( theta ) 
        epy = decayLen * math.sin( phi ) * math.sin( theta )
        epz = decayLen * math.cos( theta ) 

        endpoint = array('d',[ epx, epy, epz ] )  


        # --- production vertex

        vpx = 0.
        vpy = 0.
        vpz = random.gauss(0., beamspot_sigma)

        vertex = array('d',[ vpx, vpy, vpz ] )

        time = 0.


        # --- particle charge
        
        if ipart % 2 == 1:
            pdg = -pdg
            charge = -charge
        

        
#--------------- create MCParticle -------------------
        
        mcp = IMPL.MCParticleImpl() 

        mcp.setGeneratorStatus( genstat ) 
        mcp.setMass( mass )
        mcp.setPDG( pdg ) 
        mcp.setMomentum( momentum )
        mcp.setCharge( charge ) 
        mcp.setVertex( vertex )
        mcp.setTime( time )

        if( decayLen < 1.e9 ) :   # arbitrary ...
            mcp.setEndpoint( endpoint ) 

        print ("  ", ipart, pdg, charge, pt, phi, theta)
    

#-------------------------------------------------------


        col.addElement( mcp )

        
    wrt.writeEvent( evt ) 

print("Generated ", pt_min, pt_max, " slice")

wrt.close() 
