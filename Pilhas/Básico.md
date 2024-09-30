# Pilhas

### Nível Básico

#### O que é uma Pilha?

Uma **pilha** é uma estrutura de dados que segue o princípio **LIFO** (Último a Entrar, Primeiro a Sair), ou seja, o último item inserido é o primeiro a ser removido. Imagine uma pilha de pratos: o último prato colocado no topo é o primeiro a ser retirado.

Em Python, podemos implementar uma pilha usando uma lista (`list`), já que a lista oferece suporte aos principais métodos necessários: `append()` e `pop()`.

#### Operações Básicas
1. **push**: Adiciona um elemento no topo da pilha.
2. **pop**: Remove o elemento do topo da pilha.
3. **top/peek**: Olha o elemento no topo sem removê-lo.
4. **is_empty**: Verifica se a pilha está vazia.

#### Exemplo de Implementação:

```python
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
```

### Desafio básico:

1. Crie uma pilha e adicione três números.
2. Remova o número do topo.
3. Mostre o número atual do topo.

Pratique isso e, em seguida, avançaremos para o nível intermediário com mais funcionalidades e otimizações!
