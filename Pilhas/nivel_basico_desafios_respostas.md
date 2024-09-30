### 1. **Empilhar e Desempilhar Números:**

Aqui, vamos criar uma pilha e empilhar os números de 1 a 5 nela. Depois, desempilharemos esses números e exibiremos o resultado.

```python
# Criar a pilha (inicialmente vazia)
pilha = []

# Empilhar os números de 1 a 5
for i in range(1, 6):
    pilha.append(i)

print("Pilha após empilhar números de 1 a 5:", pilha)

# Desempilhar os números e exibir
print("Desempilhando os números:")
while pilha:
    print(pilha.pop())  # Desempilha e exibe o topo da pilha
```

**Saída esperada:**
```
Pilha após empilhar números de 1 a 5: [1, 2, 3, 4, 5]
Desempilhando os números:
5
4
3
2
1
```

---

### 2. **Verificar se uma Pilha está Vazia:**

Agora, vamos escrever uma função que verifica se a pilha está vazia e retorna `True` ou `False`.

```python
def esta_vazia(pilha):
    return len(pilha) == 0  # Se a pilha tem tamanho 0, está vazia

# Testando com uma pilha vazia e uma não vazia
pilha_vazia = []
pilha_com_elementos = [1, 2, 3]

print("Pilha vazia está vazia?", esta_vazia(pilha_vazia))  # Esperado: True
print("Pilha com elementos está vazia?", esta_vazia(pilha_com_elementos))  # Esperado: False
```

**Saída esperada:**
```
Pilha vazia está vazia? True
Pilha com elementos está vazia? False
```

---

### 3. **Reverter uma String com Pilha:**

Usaremos uma pilha para reverter uma string. Vamos empilhar cada caractere e depois desempilhá-los.

```python
def reverter_string(texto):
    pilha = []
    
    # Empilhar cada caractere da string
    for char in texto:
        pilha.append(char)
    
    # Desempilhar e criar a string invertida
    texto_invertido = ''
    while pilha:
        texto_invertido += pilha.pop()
    
    return texto_invertido

# Testando a função com a string "Python"
texto_original = "Python"
texto_revertido = reverter_string(texto_original)
print("Texto original:", texto_original)  # Saída: Python
print("Texto revertido:", texto_revertido)  # Saída: nohtyP
```

**Saída esperada:**
```
Texto original: Python
Texto revertido: nohtyP
```

---

### 4. **Checar Parênteses Balanceados:**

Vamos verificar se os parênteses de uma expressão estão balanceados. Usaremos uma pilha para garantir que cada `(` tem um `)` correspondente.

```python
def verifica_parenteses_balanceados(expressao):
    pilha = []
    
    for char in expressao:
        if char == '(':  # Empilha se for parêntese de abertura
            pilha.append(char)
        elif char == ')':  # Desempilha se for parêntese de fechamento
            if len(pilha) == 0:  # Se tentar desempilhar uma pilha vazia, não está balanceado
                return False
            pilha.pop()
    
    return len(pilha) == 0  # No final, a pilha deve estar vazia se estiver balanceado

# Testando a função com uma expressão com parênteses balanceados
expressao = "(2 + 3) * (4 + 5)"
print(verifica_parenteses_balanceados(expressao))  # Esperado: True
```

**Saída esperada:**
```
True
```

---

### 5. **Simular uma Pilha de Livros:**

Aqui, vamos criar uma função para empilhar, desempilhar e exibir o livro no topo de uma pilha de livros.

```python
def empilhar_livro(pilha, livro):
    pilha.append(livro)
    print(f"Empilhou: {livro}")

def desempilhar_livro(pilha):
    if pilha:
        return pilha.pop()
    else:
        return "Pilha de livros vazia"

def exibir_topo(pilha):
    if pilha:
        return pilha[-1]
    else:
        return "Pilha de livros vazia"

# Testando a simulação da pilha de livros
pilha_livros = []
empilhar_livro(pilha_livros, "Livro A")
empilhar_livro(pilha_livros, "Livro B")
empilhar_livro(pilha_livros, "Livro C")

print("Livro no topo:", exibir_topo(pilha_livros))  # Esperado: Livro C

print("Desempilhando:", desempilhar_livro(pilha_livros))  # Esperado: Livro C
print("Livro no topo agora:", exibir_topo(pilha_livros))  # Esperado: Livro B
```

**Saída esperada:**
```
Empilhou: Livro A
Empilhou: Livro B
Empilhou: Livro C
Livro no topo: Livro C
Desempilhando: Livro C
Livro no topo agora: Livro B
```

---

### 6. **Soma de Números Empilhados:**

Vamos empilhar números e depois desempilhá-los somando o resultado.

```python
def soma_numeros_empilhados(numeros):
    pilha = []
    
    # Empilhando os números
    for numero in numeros:
        pilha.append(numero)
    
    soma = 0
    # Desempilhando e somando
    while pilha:
        soma += pilha.pop()
    
    return soma

# Testando com a lista de números [1, 2, 3, 4]
numeros = [1, 2, 3, 4]
print(soma_numeros_empilhados(numeros))  # Esperado: 10
```

**Saída esperada:**
```
10
```

---

### 7. **Converter Decimal para Binário com Pilha:**

Vamos converter um número decimal em binário usando uma pilha.

```python
def decimal_para_binario(decimal):
    pilha = []
    
    # Empilhando os restos da divisão por 2
    while decimal > 0:
        resto = decimal % 2
        pilha.append(resto)
        decimal //= 2
    
    binario = ''
    # Desempilhando para formar o número binário
    while pilha:
        binario += str(pilha.pop())
    
    return binario

# Testando com o número 10
numero_decimal = 10
print(decimal_para_binario(numero_decimal))  # Esperado: "1010"
```

**Saída esperada:**
```
1010
```

