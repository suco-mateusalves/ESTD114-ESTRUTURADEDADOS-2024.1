def imprimir_crescente(N):
    if N >= 0:
        imprimir_crescente(N - 1)
        print(N)

# Exemplo de uso:
imprimir_crescente(5)  # Saída: 0 1 2 3 4 5
