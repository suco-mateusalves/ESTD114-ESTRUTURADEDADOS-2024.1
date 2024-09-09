def fibonacci(N):
    if N <= 1:
        return N
    else:
        return fibonacci(N - 1) + fibonacci(N - 2)

# Exemplo de uso:
print(fibonacci(10))  # Saída: 55
