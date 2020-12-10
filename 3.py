#What is the largest prime factor of the number 600851475143 ?
n = 600851475143
div = 2
while n > 1:
    if n%div == 0:
        n = n/div
        print(n)
    else:
        div+=1