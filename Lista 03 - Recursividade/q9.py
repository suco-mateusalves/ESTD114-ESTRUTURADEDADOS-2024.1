def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# Exemplo de uso:
print(mdc(48, 18))  # Saída: 6
