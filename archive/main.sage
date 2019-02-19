#!/usr/bin/env sage

import sys

from sage.all import *
from testProbabilistes.testProbabilistes import *

# pour 3 < n < +00

for i in range(4, 100):
	#expo = i
	#n = 2^expo - 1  # si executer via sage
	n = i
	iter = 100
	print( 'Fermat = %s' % (Fermat( n, iter )) )
	print( 'Miller-Rabin = %s' % MillerRabin(n, iter) )