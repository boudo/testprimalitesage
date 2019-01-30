#!/usr/bin/env sage

import sys

from sage.all import *


def fermat(n, it) :
	print("fermat")
	expo = n - 1
	modul = n

	for i in range(0, it) : 
		#print("debut  rand")
		a = randrange(3, n)
		
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
a = 2^216091 - 1
b = 1
print(fermat(a , b))
print("fin pgcd = ")
print(gcd(4, 4))
print("fin squar")
print(power_mod(6,30,31))
