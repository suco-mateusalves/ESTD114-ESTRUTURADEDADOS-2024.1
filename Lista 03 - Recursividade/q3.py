def contar_letra(palavra, letra):
    if palavra == "":
        return 0
    else:
        return (1 if palavra[0] == letra else 0) + contar_letra(palavra[1:], letra)

# Exemplo de uso:
print(contar_letra("estrutura", 'u'))  # Saída: 2
