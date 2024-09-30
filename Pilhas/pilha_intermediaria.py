class PilhaVaziaError(Exception):
    pass

class Pilha:
    def __init__(self):
        self.pilha = []

    def esta_vazia(self):
        return len(self.pilha) == 0

    def empilhar(self, item):
        self.pilha.append(item)

    def desempilhar(self):
        if self.esta_vazia():
            raise PilhaVaziaError("Não é possível desempilhar, a pilha está vazia!")
        return self.pilha.pop()

    def topo(self):
        if self.esta_vazia():
            raise PilhaVaziaError("A pilha está vazia, não há elemento no topo!")
        return self.pilha[-1]

    def tamanho(self):
        return len(self.pilha)

# Exemplo de uso com tratamento de exceção
minha_pilha = Pilha()

try:
    minha_pilha.desempilhar()  # Tentando desempilhar de uma pilha vazia
except PilhaVaziaError as e:
    print(e)  # Saída: Não é possível desempilhar, a pilha está vazia!
