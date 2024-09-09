def fatorial(N):
    if N == 0:
        return 1
    else:
        return N * fatorial(N - 1)

# Exemplo de uso:
print(fatorial(4))  # Saída: 24
