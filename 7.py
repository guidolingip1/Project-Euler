#What is the 10 001st prime number?
#primo é somente os números que são divisiveis apenas por 1 e por eles mesmos
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

primos = 0
n = 1
obj = 0
while primos < 10002:
	if checa(n) == n:
		print(n)
		primos+=1

	n+=1