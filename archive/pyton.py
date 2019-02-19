#!/usr/bin/env sage

import sys

from sage.all import *


#print(************  TEST DE MILLER-RABIN  ************")

def decoupNmoins1(nMoins1) : #n - 1 > 4
	#print("decoupage de nMoins1")
	s = 0
	tmp = nMoins1
	while tmp > 1 :
		if (tmp % 2) == 0 :
			s = s +1
			tmp = tmp // 2

		else :
			break

	return s



def temoinDeComposition(a, n) :
	#print("temoin de composition")
	s = 0
	d = 0
	modul = 0;
	nMoins1 = n - 1
	s = decoupNmoins1(nMoins1)
	tmp = 2^s

	if s != 0 :
		d = nMoins1 // tmp

	if s == 0 :
		d = nMoins1

	modul = power_mod(a, d, n)

	if modul == 1 or modul == nMoins1 :
		#print("ce nombre n'est pas un temoin de composition 1")
		return 0

	for i in range(1, s):
		tmp = 2^i
		modul = power_mod(a, d*tmp, n)
		if modul == nMoins1 :
			#print("ce nombre n'est pas un temoin de composition 2")
			return 0

		if modul == 1 :
			#print("ce nombre est un temoin de composition 2")
			return 1

	if power_mod(a, d*(2^s), n) == 1 :
		#print("ce nombre n'est pas un temoin de composition 3")
		#print(power_mod(a, d*(2^s), n))
		return 0

	#print("ce nombre est un temoin de composition")
	return 1

def MillerRabin(n, iter) :
	print("Miller_Rabin")
	nMoins1 = n - 1

	for i in range(0, iter) :
		a = randrange(2, nMoins1)

		if temoinDeComposition(a, n) :
			print("ce nombre est compose")
			return 0

	print("ce nombre est premier")
	return 1


print("************* debut du TEST *******************")

iter = 5
n = 2^5-1
print( MillerRabin(n, iter) )

print(" ************* fin du TEST ******************* ")