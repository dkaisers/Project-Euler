import math

print("x by y")
x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

def bico(x, y):
	if y == x:
		return 1
	elif y == 1:
		return x
	elif y > x:
		return 0
	else:
		a = math.factorial(x)
		b = math.factorial(y)
		c = math.factorial(x - y)
		return (a // (b * c))

print("Number of lattice paths:")
print(bico(x + y, x))
