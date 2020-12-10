#Find the largest palindrome made from the product of two 3-digit numbers.
def reverte(numero):
    revertido = 0 
    while (numero > 0):  
        resto = numero % 10  
        revertido = (revertido * 10) + resto
        numero = numero // 10
    return revertido

maior = 0
for i in range (999,1,-1):
    for j in range (999,1,-1):
        soma = i*j
        x = soma
        if reverte(soma) == soma:
            if soma > maior:
                maior = soma
print(maior)