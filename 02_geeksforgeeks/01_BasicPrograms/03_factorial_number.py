
# Python 3 program to find 
def factorial(n):
	
	# single line to find factorial
	return 1 if (n==1 or n==0) else n * factorial(n - 1) 

# Driver Code
num = 5
x = factorial(num)
print("Factorial of",num,"is", x)


