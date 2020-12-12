#What is the 10 001st prime number?
#works but very slow
def checa(n):
	primo = 0
	for i in range(2,n-1):
		if n%i == 0:
			primo = 1
			break;

	if primo == 0:
		return n
	if primo == 1:
		return 0

soma = 0
n = 1
obj = 0
while n < 2000000:
	if checa(n) == n:
		print(n)
		soma+=n
	n+=1

print(soma-1)