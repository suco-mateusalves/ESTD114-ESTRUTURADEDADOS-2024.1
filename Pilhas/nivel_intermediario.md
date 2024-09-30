# Pilhas

### Nível Intermediário

Agora que você já entendeu os conceitos básicos de pilha, vamos explorar mais funcionalidades e otimizar a implementação. Vamos também aplicar o uso de exceções e trabalhar com um exemplo mais prático.

#### 1. Exceções para Operações Inválidas

No exemplo anterior, quando tentamos desempilhar ou verificar o topo de uma pilha vazia, retornamos uma string dizendo que a pilha está vazia. Porém, em uma aplicação real, o ideal é lançar uma exceção para que o código saiba que houve um erro.

```python
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
```

#### 2. Exemplo Prático: Verificação de Parênteses Balanceados

Um uso comum de pilhas é a verificação de expressões matemáticas ou de código para garantir que os parênteses estão corretamente balanceados. Vamos criar um código que verifica se uma expressão com parênteses, colchetes e chaves está correta.

**Exemplo**: 
- A expressão `(([]{}))` está balanceada.
- A expressão `([)]` não está balanceada.

```python
def verifica_parenteses_balanceados(expressao):
    pilha = Pilha()
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expressao:
        if char in '([{':  # Se for um parêntese de abertura
            pilha.empilhar(char)
        elif char in ')]}':  # Se for um parêntese de fechamento
            if pilha.esta_vazia() or pilha.desempilhar() != pares[char]:
                return False
    return pilha.esta_vazia()

# Teste
expressao1 = "(([]{}))"
expressao2 = "([)]"

print(verifica_parenteses_balanceados(expressao1))  # Saída: True
print(verifica_parenteses_balanceados(expressao2))  # Saída: False
```

### Desafio Intermediário:

1. Modifique a função de verificação de parênteses balanceados para incluir suporte a strings que possam ter outros caracteres além de parênteses, colchetes ou chaves. Ou seja, a função só deve verificar os parênteses e ignorar outros caracteres.

Agora que avançamos para um uso prático da pilha, podemos continuar para o nível avançado, onde exploraremos a otimização de performance e a implementação de pilhas com capacidade limitada.
