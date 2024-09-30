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

def verifica_parenteses_balanceados(expressao):
    pilha = Pilha()
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expressao:
        if char in '([{':  # Se for um parêntese de abertura
            pilha.empilhar(char)
        elif char in ')]}':  # Se for um parêntese de fechamento
            if pilha.esta_vazia() or pilha.desempilhar() != pares[char]:
                return False
        # Ignora outros caracteres
    return pilha.esta_vazia()

# Teste com expressões contendo outros caracteres
expressao1 = "a + (b * [c / {d - e}])"
expressao2 = "(a + b] * {c - d})"
expressao3 = "Texto sem nenhum parêntese!"

print(verifica_parenteses_balanceados(expressao1))  # Saída: True
print(verifica_parenteses_balanceados(expressao2))  # Saída: False
print(verifica_parenteses_balanceados(expressao3))  # Saída: True

'''
Explicação:

    Ignorando outros caracteres: A função apenas se preocupa com os caracteres (), [], e {}, ignorando letras, números e operadores aritméticos.
    Teste 1: A expressão a + (b * [c / {d - e}]) está balanceada, então retorna True.
    Teste 2: A expressão (a + b] * {c - d}) não está balanceada, porque há um parêntese aberto ( que não corresponde ao fechamento com ], então retorna False.
    Teste 3: A expressão Texto sem nenhum parêntese! é considerada balanceada, já que não contém parênteses, colchetes ou chaves.

Isso garante que a verificação seja focada apenas nos símbolos de parênteses e ignore qualquer outro caractere na string.
'''
