#!/usr/bin/env sage

import sys

from sage.all import *

#_____________________________________________________________________________________________________
#___________________________________Test de Fermat____________________________________________________
def Fermat(n, it) :
	#print("fermat")
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

#_____________________________________________________________________________________________________
#___________________________________Test de Miller-Rabin______________________________________________


def decoupNmoins1(nMoins1) : #n - 1 > 4
	#print("decoupage de nMoins1")
	s = 0
	tmp = nMoins1
	while tmp > 1 :
		if (tmp % 2) == 0 :
			s = s + 1
			tmp = tmp / 2

		else :
			break

	return s



def temoinDeComposition(a, n) :
	#print("temoin de composition")
	s = 0
	d = 0
	modul = 0
	tmp = 0
	nMoins1 = n - 1
	s = decoupNmoins1(nMoins1) # nMoins1 = 2^s * d
	tmp = 2**s
	d = nMoins1 / tmp

	modul = power_mod(a, d, n)

	if modul == 1 or modul == nMoins1 :
		#print("ce nombre n'est pas un temoin de composition 1")
		return 0

	for i in range(1, s):
		tmp = 2**i
		modul = power_mod(a, d*tmp, n)
		if modul == nMoins1 :
			#print("ce nombre n'est pas un temoin de composition 2")
			return 0

		if modul == 1 :
			#print("ce nombre est un temoin de composition 2")
			return 1

	if power_mod(a, d*(2**s), n) == 1 :
		#print("ce nombre n'est pas un temoin de composition 3")
		#print(power_mod(a, d*(2^s), n))
		return 0

	#print("ce nombre est un temoin de composition")
	return 1

def MillerRabin(n, iter) :
	#print("Miller_Rabin")
	if n < 4:
		print("Ce nombre doit etre superieur ou egal a 4")
		return -1;

	nMoins1 = n - 1

	for i in range(0, iter) : 
		a = randrange(2, nMoins1,1) # 1 < a < nMoins1

		if temoinDeComposition(a, n) :
			#print("ce nombre est compose")
			return 0

	#print("ce nombre est premier")
	return 1

#_____________________________________________________________________________________________________
#___________________________________Test de Solovay-Strassen__________________________________________

def jacobi(a, n):
	#print("jacobi")
	
	if n % 2 == 0 : 				# si n est pair
		return 0
	
	if gcd(a, n) != 1 :				# pro 2
		#print('pro 2')
		return 0

	if a > n:
		modul = a % n
		#print('pro 1')
		return jacobi( modul, n) # pro 1

	if a == 2 :						# pro 5
		#print('pro 5')
		modul1 = n % 8
		if modul1 == 1 or modul1 == 7 :
			return 1

		if modul1 == 3 or modul1 == 5 :
			return -1

	if a % 2 == 0 :
		#print('pro 3')
		return jacobi(a/2, n) * jacobi(2, n) # pro 3

	if a == 1 :						# pro 4
		#print('pro 4')
		return 1

	if gcd(a, n) == 1 : 			# pro suit 2 et 6
		#print('pro 2 et 6')
		modul2 = n % 4
		modul3 = a % 4
		if modul2 == 1 or modul3 == 1 :
			return jacobi(n, a)

		if modul2 == modul3 and modul3 == 3 :
			return - jacobi(n, a)



def SolovayTrassen(n, iter):
	#print("Solovay-Strassen")
	if n < 4:
		print("Ce nombre doit etre superieur ou egal a 4")
		return -1;

	nMoins1 = n - 1

	for i in range(0, iter):
		a = randrange(2, nMoins1, 1)
		#print('a = %s' %a)
		r = jacobi(a, n)
		#print('jacobi = %s' %r)
		modul = power_mod(a, nMoins1 / 2, n)
		#print('modul = %s' %modul)

		if r == 0 or (modul != 1 and modul != nMoins1) : # r = 0 ou 1 ou -1 = n-1
			return 0

	return 1