def fibonacci_sequence(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
    if b == n:
        return True
    else:
        return False

numero = int(input("Digite um número: "))

if fibonacci_sequence(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
