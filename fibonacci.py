def fibonacci(numero):
    # função que calcula a sequência de Fibonacci
    a, b = 0, 1 # os dois primeiros números devem ser 0 e 1
    while b < numero:
        a, b = b, a + b
    return numero == b
    
numero = int(input("informe um número: "))
if fibonacci(numero):
    print(f"o número informado '{numero}' pertence a sequência de Fibonacci")
else:
    print(f"o número informado '{numero}' não pertence a sequência de Fibonacci")