class Pilha:
    def __init__(self):
        self.pilha = []

    def esta_vazia(self):
        return len(self.pilha) == 0

    def empilhar(self, item):
        self.pilha.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.pilha.pop()
        return "Pilha vazia"

    def topo(self):
        if not self.esta_vazia():
            return self.pilha[-1]
        return "Pilha vazia"

    def tamanho(self):
        return len(self.pilha)

# Exemplo de uso
minha_pilha = Pilha()
minha_pilha.empilhar(5)
minha_pilha.empilhar(10)
print(minha_pilha.topo())  # Saída: 10
print(minha_pilha.desempilhar())   # Saída: 10
print(minha_pilha.desempilhar())   # Saída: 5
print(minha_pilha.esta_vazia())  # Saída: True
