#=========================================================================
# Choose PyMTL or Verilog version
#=========================================================================
# Set this variable to 'pymtl' if you are using PyMTL for your RTL design
# (i.e., your design is in IntMultBasePRTL) or set this variable to
# 'verilog' if you are using Verilog for your RTL design (i.e., your
# design is in IntMulBaseVRTL).

rtl_language = 'verilog'

#-------------------------------------------------------------------------
# Do not edit below this line
#-------------------------------------------------------------------------

# PyMTL wrappers for the corresponding Verilog RTL models.

from os import path
from pymtl3 import *
from pymtl3.passes.backends.verilog import *
from pymtl3.stdlib.stream.ifcs import RecvIfcRTL, SendIfcRTL

class synchronizer(Component):
    def construct(s):
        s.inp = InPort()
        s.outp = OutPort()

        s.value = Wire(Bits3)

# For to force testing a specific RTL language
import sys
if hasattr( sys, '_called_from_test' ):
  if sys._pymtl_rtl_override:
    rtl_language = sys._pymtl_rtl_override

# Import the appropriate version based on the rtl_language variable

if rtl_language == 'pymtl':
  from .ArbitratorPRTL import ArbitratorPRTL as ArbitratorRTL
elif rtl_language == 'verilog':
  ArbitratorRTL = ArbitratorVRTL
else:
  raise Exception("Invalid RTL language!")
