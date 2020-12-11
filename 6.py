#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def sum_squares(n):
	sum = 0
	for i in range(1,n):
		sum+= i*i
	return sum

def square_sum(n):
	sum = 0
	for i in range(1,n):
		sum+= i
	return sum*sum

print(square_sum(101) - sum_squares(101))