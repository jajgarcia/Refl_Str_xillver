#!/usr/bin/python
#
# rf_xillver.py
#
# Estimates and prints the reflection strength
# in a xillver model for different parameters
#
# Requires: xspec
#
import sys 
from xspec import *
from optparse import OptionParser
from astropy.io import fits as pyfits
import os,os.path
import glob
#
# ------------------------------------------------------------------------------
#
# MAIN PROGRAM
#
#
#
version='0.1a'
date='- Mon Jul 18 22:13:58 EDT 2016 -'
author='Javier Garcia'
#
#-----

# No chatter
Xset.chatter = 0

Xset.abund = "wilm"
Xset.xsect = "vern"

# Ecut values
gammavals=['1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0','2.1','2.2','2.3','2.4','2.5','2.6','2.7','2.8','2.9','3.0']

# Query
Fit.query = 'yes'

# Load local models
AllModels.lmod("relxill")

for gamma in gammavals:

    # Define the Model
    m1 = Model("xillver")

    m1(1).values = gamma	# Gamma
    m1(2).values = "1"		# Afe
    m1(3).values = "200"	# Ecut
    m1(4).values = "3.0"	# logXi
    m1(5).values = "0"		# z
    m1(6).values = "20"		# Incl
    m1(7).values = "-1"		# refl_frac
    m1(8).values = "1"		# norm

    # Calculate 20-40 keV flux
    AllModels.calcFlux("20. 40.")
    flux_ref=AllModels(1).flux[0]

    m1(7).values = "0"		# refl_frac
    AllModels.calcFlux("20. 40.")
    flux_pl=AllModels(1).flux[0]

    print gamma,flux_ref/flux_pl

    # Unload the model
    AllModels.clear()

# Output
#
#
sys.exit()
# ------------------------------------------------------------------------------
