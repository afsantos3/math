import matplotlib.pyplot as plt
import math
def f(x):
	return 1. / float(1 + 25*(x**2))

def fp(x):
	return (50. * x) / ((25*x**2 + 1)**2)
def get_x(x0, minJ, maxJ, h):
	xList = []

	xList.append(x0)

	for j in range(minJ, maxJ + 1):
		xList.append(x0 + (j * h))
	
	print(xList)
	return xList
#Newton's Form of the Interpolant
#p10(x) = a0 + a1(x - x0) + ... + a10(x - x0_)...(x-xn-1)

#Lagrange Polynomial Interpolation
def divide_diff(x):
	fs = [[0 for i in range(len(x))] for j in range(len(x))]
	coeffs = []

	for i in range(0, len(x)):
		fs[i][0] = f(x[i])
	
	coeffs.append(fs[0][0])
	
	for i in range(1, len(x)):
		for j in range(1, i+1):
			fs[i][j] = (fs[i][j - 1] - fs[i - 1][j - 1]) / (x[i] - x[i - j])
			
			if(i == j):
				coeffs.append(fs[i][j])
	
	#print(coeffs)
	return coeffs

def horner(coeffs, n, x, xList):
	b = coeffs[n]
	
	for i in reversed(range(0, n)):
		b = coeffs[i]  + (x - xList[i]) * b
	
	return b

def cubic_hermite(x1, x2, x):
	mid = (f(x2) - f(x1)) / (x2 - x1) 
	aj = (mid - fp(x1)) / (x2 - x1)
	bj = (fp(x2) - mid) / (x2 - x1)
	cj = (bj - aj) / (x2 - x1)
	
	l = f(x1) + fp(x1)*(x - x1) + aj*((x - x1)**2) + cj*((x-x1)**2)*(x-x2)
	return l

def evall(xList, minI, maxI, t):
	dist = abs(minI - maxI)
	dist /= 250
	xss = []
	points = []
	num = -1
	count = 0

	for i in range(0, 250):
		new_x = minI + i * (dist)
		xss.append(new_x)
	
	for j, i in enumerate(xss):
		if(j % 25 == 0):
				num += 1
		
		if(num+1 > len(xList)-1):
			continue
		
		count += 1

		if(t == 'c'):
			points.append(cubic_hermite(xList[num], xList[num+1], i))
		else:
			points.append(p_linear(xList[num], xList[num+1], i))

	print (len(points), len(xss))
	return points, xss
			
def p_linear(x1, x2, x):
	l = f(x1) * ((x - x2) / (x1 - x2)) + f(x2) * ((x - x1) / (x2 - x1))
	return l

def get_points(coeffs, n, minI, maxI, xList):
	xs = []
	points = []
	
	dist = abs(minI - maxI)
	
	dist /= 250
	
	for i in range(0, 250):
		new_x = minI + i * (dist)
		xs.append(new_x)
	
	for i in xs:
		points.append(horner(coeffs, n, i, xList))	
	
	return points, xs

def get_ys(xList):
	points = []

	for i in xList:
		points.append(f(i))

	return points

def error(applied, original):
	e = 0
	for i in range(0, len(applied)):
		temp = abs(original[i] - applied[i])
		
		if e < temp:
			e = temp
	
	return e
xs = get_x(-1., 1, 10, float(1/5))
cs = divide_diff(xs)
ans = horner(cs, len(xs)-1, -1, xs)

yPoints, xPoints = get_points(cs, len(xs)-1, -1, 1, xs)

actual = get_ys(xPoints)

ynew_points, xnew_points = evall(xs, -1, 1, 'c')
plt.plot(xPoints, actual, 'g-', label='f(x)')
plt.plot(xPoints, yPoints, 'ro-', label='f_app(x)')
plt.xlim(-1, 1)
plt.xlabel("x")
plt.ylabel('y')
plt.title('Lagrange Polynomial Interpolation')
plt.legend(loc='upper right')
plt.savefig('lagrange')

plt.plot(xPoints, actual,'g-', label='f(x)')
plt.plot(xnew_points, ynew_points,'ro-', label='f_app(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Piecewise Cubic Hermite Interpolation')
plt.legend(loc='upper right')
plt.xlim(-1, 1)
plt.show()

y2points, x2points = evall(xs, -1, 1, 'l')
plt.plot(x2points, actual, 'g-', label='f(x)')
plt.plot(x2points, y2points, 'ro-', label='f_app(x)')
plt.xlim(-1, 1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Piecewise linear interpolation')
plt.legend(loc='upper right')
plt.show()

print(len(x2points), len(xPoints), len(xnew_points))

e1 = error(yPoints, actual)
print("Lagrange poly: ", e1)
e2 = error(ynew_points, actual)
print("hermite: ", e2)
e3 = error(y2points, actual)
print("linear inter: ", e3)

