def imprimir_decrescente(N):
    if N >= 0:
        print(N)
        imprimir_decrescente(N - 1)

# Exemplo de uso:
imprimir_decrescente(5)  # Saída: 5 4 3 2 1 0
