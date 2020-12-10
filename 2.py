#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
t1 = 0 #termo 1
t2 = 1 #termo 2
soma = 0 #Fib
soma_even = 0 #Resposta

while soma < 4000000:
    soma = t1+t2
    t1=t2
    t2=soma
    if soma%2 == 0:
        soma_even+=soma
        
print(soma_even)