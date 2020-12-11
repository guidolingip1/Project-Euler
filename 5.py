#Péssima Otimização
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def divide(num,div):
    soma = 0
    for i in range(1,div):
        if num%i != 0:
            return 1
        soma+=num%i
    return soma

i = 1
while 1:
    if divide(i,20) == 0:
        print(i)
        break;
    i+=1