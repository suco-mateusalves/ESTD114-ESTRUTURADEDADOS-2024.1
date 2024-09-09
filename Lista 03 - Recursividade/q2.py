def inverter_palavra(palavra):
    if palavra == "":
        return palavra
    else:
        return inverter_palavra(palavra[1:]) + palavra[0]

# Exemplo de uso:
print(inverter_palavra("Python"))  # Saída: "nohtyP"
