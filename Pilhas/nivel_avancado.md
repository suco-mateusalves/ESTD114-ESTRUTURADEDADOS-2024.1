# Pilhas

### Nível Avançado

Agora vamos avançar para otimizações, pilhas com capacidade limitada e problemas mais complexos que envolvem pilhas. Também exploraremos como podemos implementar uma pilha sem usar a estrutura de lista do Python, mas sim uma estrutura personalizada.

#### 1. Pilha com Capacidade Limitada

Em alguns casos, podemos precisar de uma pilha com capacidade limitada. Vamos implementar uma pilha que não permita adicionar mais elementos do que um tamanho pré-determinado.

```python
class PilhaComLimite:
    def __init__(self, limite):
        self.pilha = []
        self.limite = limite

    def esta_vazia(self):
        return len(self.pilha) == 0

    def esta_cheia(self):
        return len(self.pilha) == self.limite

    def empilhar(self, item):
        if self.esta_cheia():
            raise Exception("Pilha está cheia! Não é possível empilhar mais itens.")
        self.pilha.append(item)

    def desempilhar(self):
        if self.esta_vazia():
            raise Exception("Pilha está vazia! Não é possível desempilhar.")
        return self.pilha.pop()

    def topo(self):
        if self.esta_vazia():
            raise Exception("A pilha está vazia, não há elemento no topo!")
        return self.pilha[-1]

    def tamanho(self):
        return len(self.pilha)

# Exemplo de uso
pilha_com_limite = PilhaComLimite(3)
pilha_com_limite.empilhar(1)
pilha_com_limite.empilhar(2)
pilha_com_limite.empilhar(3)

# Tentando adicionar mais itens do que o limite
try:
    pilha_com_limite.empilhar(4)
except Exception as e:
    print(e)  # Saída: Pilha está cheia! Não é possível empilhar mais itens.
```

#### 2. Implementação de Pilha com Estrutura de Nós (Linked List)

Em vez de usar uma lista do Python, podemos construir uma pilha utilizando uma lista ligada (*linked list*). Isso pode ser útil para controlar a memória de maneira mais eficiente, dependendo do uso.

Cada elemento da pilha será representado por um **nó**, que contém um valor e uma referência para o próximo nó.

```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaListaLigada:
    def __init__(self):
        self.topo_pilha = None
        self.tamanho_pilha = 0

    def esta_vazia(self):
        return self.topo_pilha is None

    def empilhar(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.topo_pilha
        self.topo_pilha = novo_no
        self.tamanho_pilha += 1

    def desempilhar(self):
        if self.esta_vazia():
            raise Exception("Pilha está vazia! Não é possível desempilhar.")
        valor = self.topo_pilha.valor
        self.topo_pilha = self.topo_pilha.proximo
        self.tamanho_pilha -= 1
        return valor

    def topo(self):
        if self.esta_vazia():
            raise Exception("A pilha está vazia, não há elemento no topo!")
        return self.topo_pilha.valor

    def tamanho(self):
        return self.tamanho_pilha

# Exemplo de uso
pilha_ligada = PilhaListaLigada()
pilha_ligada.empilhar(5)
pilha_ligada.empilhar(10)
print(pilha_ligada.topo())  # Saída: 10
print(pilha_ligada.desempilhar())  # Saída: 10
print(pilha_ligada.desempilhar())  # Saída: 5
```

### 3. Aplicação Complexa: Avaliação de Expressões Pós-fixadas (Notação Polonesa Inversa)

Um problema clássico que envolve pilhas é a **avaliação de expressões pós-fixadas** (ou Notação Polonesa Inversa - RPN). Neste tipo de expressão, os operadores vêm depois dos operandos, e a pilha é usada para avaliar a expressão.

**Exemplo**:
A expressão infixa: `(3 + 4) * 5`
Se converte em pós-fixa: `3 4 + 5 *`

#### Avaliação da Expressão Pós-fixada:

1. Quando encontramos um número, o empilhamos.
2. Quando encontramos um operador, desempilhamos os dois últimos números, aplicamos o operador e empilhamos o resultado.

```python
def avalia_expressao_posfixa(expressao):
    pilha = Pilha()
    operadores = {'+', '-', '*', '/'}
    
    for elemento in expressao.split():
        if elemento.isdigit():
            pilha.empilhar(int(elemento))
        elif elemento in operadores:
            b = pilha.desempilhar()
            a = pilha.desempilhar()
            if elemento == '+':
                pilha.empilhar(a + b)
            elif elemento == '-':
                pilha.empilhar(a - b)
            elif elemento == '*':
                pilha.empilhar(a * b)
            elif elemento == '/':
                pilha.empilhar(a / b)
    
    return pilha.topo()

# Exemplo de uso
expressao_posfixa = "3 4 + 5 *"
print(avalia_expressao_posfixa(expressao_posfixa))  # Saída: 35
```

### Desafio Avançado:
1. Implemente uma função que converta uma expressão infixa (como `(3 + 4) * 5`) em uma expressão pós-fixa (como `3 4 + 5 *`).
2. Modifique a função de avaliação pós-fixada para suportar números decimais e mais operadores (como potência `^`).

Essa é uma aplicação poderosa e bastante utilizada em compiladores e calculadoras. Quando você estiver confortável com isso, estará preparado para aplicar pilhas em problemas reais e complexos!
