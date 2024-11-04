def busca_binaria(uma_lista, item_pesquisado):
    inicio = 0
    fim = len(uma_lista) - 1
    encontrou = False
    while inicio <= fim and not encontrou:
        meio = (inicio + fim) // 2
        if uma_lista[meio] == item_pesquisado:
            encontrou = True
        else:
            if item_pesquisado < uma_lista[meio]:
                fim = meio - 1
            else:
                inicio = meio + 1
    return encontrou

# Teste
lista_teste = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(busca_binaria(lista_teste, 3))    # False
print(busca_binaria(lista_teste, 13))   # True
