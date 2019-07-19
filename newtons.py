#Adriano Santos
#CS 471
#Project 1
#Newton's Method

import math

def f(x):
	fx = .5 + .25*(x**2) - x*math.sin(x) - .5*math.cos(2*x)
	return fx

def fp(x):
	fpx = .5*x - math.sin(x) - x*math.cos(x) + 2*math.sin(x)*math.cos(x)
	return fpx

tol = 10**-5
e = 1
x = math.pi / 2
n = 0


while(tol < e):
	print(e)
	print("n: {0:2d}\tx(n): {1:4f}) ".format(n, x))
	
	xn = x - (f(x) / fp(x)) 
	en = math.fabs(xn - x)
	x = xn
	e = en
	n += 1	

print(e)
