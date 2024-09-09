def fatorial_duplo(N):
    if N == 1:
        return 1
    else:
        return N * fatorial_duplo(N - 2)

# Exemplo de uso:
print(fatorial_duplo(5))  # Saída: 15
