def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
def pow(num, r):
	if r == 0:
		return 1
	else:
		return num * pow(num, r-1)

def choose(n, k):
	return factorial(n)/(factorial(k) * factorial(n-k))

def calcOnto(i, o):
	val = 0
	for k in range(0, o):
		val += (pow(-1, k) * choose(o, o-k) * pow(o-k, i))
	return val


INPUT = int(raw_input("Choose how many inputs in the function:"))

try:
	if not (0 < INPUT):
		raise ValueError()
except ValueError:
	print "Invalid Option, input has to be greater than 0"

OUTPUT = int(raw_input("Choose how many outputs in the function:"))

try:
	if not (0 < OUTPUT):
		raise ValueError()
except ValueError:
	print "Invalid Option, output has to be greater than 0"


nOntos = calcOnto(INPUT, OUTPUT)
print nOntos
