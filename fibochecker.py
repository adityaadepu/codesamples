import gmpy
def isFibo(d):
	if (gmpy.is_square(5*d*d+4)==1 or  gmpy.is_square(5*d*d-4)==1):
		print "IsFibo"
	else:
		print "IsNotFibo"
	

num1 = input()
for i in range(num1):
	num2 = input()
	isFibo(num2)
