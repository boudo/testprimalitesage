#!/usr/bin/env sage

import sys

from sage.all import *


#print(************  TEST DE MILLER-RABIN  ************")

def decoupNmoins1(nMoins1) : #n - 1 > 4
	print("decoupage de nMoins1")
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
	print("temoin de composition")

	nMoins1 = n - 1
	s = decoupNmoins1(nMoins1)

	if s != 0 :
		d = nMoins1 // s

	if s == 0 :
		d = nMoins1


	modul = power_mod(a, d, n)
	print(a)
	print(d)
	print(n)
	if modul == 1 or modul == nMoins1 :
		print("ce nombre est compose 1")
		#return 0

	for i in range(1, s):
		tmp = 2^i
		modul = power_mod(a, d*tmp, n)
		if modul == 1 or modul == nMoins1 :
			print("ce nombre est compose 2")
			return 0

	if power_mod(a, d*(2^s), n) != 1 :
		print("ce nombre est compose3")
		print(d)
		print(s)

		print(power_mod(a, d*(2^s), n))
		return 0

	print("ce nom est premier")
	return 1

print("************* debut du TEST *******************")

print( temoinDeComposition(6, 2^521-1) )

print("************* fin du TEST *******************")