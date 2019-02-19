#!/usr/bin/env sage

import sys

from sage.all import *


def Fermat(n, it) :
	print("fermat")
	expo = n - 1
	modul = n

	for i in range(0, it) : 
		#print("debut  rand")
		a = randrange(2, n) # ici
		
		#print("random = ")
		#print(a)
		if gcd(modul, a) != 1 :
			#print("ici pgcd = ")
			#print(gcd(modul, a))
			return 0
		
		elif gcd(modul, a) == 1 :
			#print("squart")
			#print("elif pgcd = ")
			#print(gcd(modul, a))
			if power_mod(a,expo,modul) != 1 :
				return 0
	#print("ici pgcd = ")
	#print(gcd(modul, a))
	return 1


print("debut*******************")
a = 2^521-1
b = 5
print(Fermat(a , b))


