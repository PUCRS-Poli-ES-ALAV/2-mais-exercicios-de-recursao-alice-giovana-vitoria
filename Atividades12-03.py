import sys
sys.stdout.reconfigure(encoding='utf-8')

# 1. Modele e implemente um método recursivo que calcule o fatorial de um número n passado como parâmetro.
    #Modelagem: n!=n×(n−1)×(n−2)×...×1

    #Implementação:
def fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.") #O raise no python auxilia no lançamento de exceções
    if n == 0 or n == 1: #Esse é o nosso caso base
        return 1
    return n * fatorial(n - 1)

    #Execução:
num = 4
print(f"O fatorial de {num} é {fatorial(num)}")


# 2. Modele e implemente um método recursivo que calcule o somatório de um número n (passado como parâmetro) até 0.
    #Modelagem: S(n)=n+S(n−1),se n>0 e S(n)=n+S(n+1),se n<0

    # Implementação:
def somatorio(n):
    if n == 0: # caso base
        return 0
    elif n > 0:
        return n + somatorio(n - 1)
    else:  # Caso n seja negativo
        return n + somatorio(n + 1)

    #Execução:
num = 3
print(f"O somatório de {num} até 0 é {somatorio(num)}")


# 3. Modele e implemente um método recursivo que calcule o n-ésimo número da sequência de fibonacci.
    # Modelagem: Se n = 0, retorna 0 ; Se n = 1, retorna 1 e  F(n-1) + F(n-2), se n>=2

    # Implementação:
def fibonacci(n):
    if n < 0:
        raise ValueError("O índice de Fibonacci não pode ser negativo.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

    #Execução:
num = 7
print(f"O {num}-ésimo número de Fibonacci é {fibonacci(num)}")


# 4. Modele e implemente um método recursivo que calcule o somatório dos números inteiros entre os números k e j, passados como parâmetro.
    # Modelagem: k, se k = j ; k + S(k +1,j), se k<j e k + S(k-1,j), se k>j

    # Implementação:
def somatorio(k,j):
    if k ==j:
        return k
    elif k<j:
        return k + somatorio(k +1,j)
    else:
        return k + somatorio(k-1,j)

    # Execução:
k = 5
j = 8
print(f"O somátório dos números entre {k} e {j} é {somatorio(k,j)}")


