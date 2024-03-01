# Python3 code to recursively find
# the power of a number

# Recursive function to find N^P.
def power(N, P):

	# If power is 0 then return 1
	# if condition is true
	# only then it will enter it,
	# otherwise not
	if P == 0:
		return 1

	# Recurrence relation
	return (N*power(N, P-1))


# Driver code
if __name__ == '__main__':
	
	N = 5
	P = 2

	print(power(N, P))
