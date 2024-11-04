Aqui estão as respostas para cada questão da lista:

---

## Lista de Exercícios 08 (Pesquisa)

1. **Em que tipo de lista a busca binária é mais eficiente?**  
   **Resposta**: b) Listas ordenadas  
   A busca binária só é eficaz em listas ordenadas, pois ela depende de uma ordem para descartar metade dos elementos em cada passo.

2. **Qual é a complexidade de tempo da busca binária?**  
   **Resposta**: b) O(log n)  
   A busca binária reduz o número de elementos pela metade a cada iteração, resultando em uma complexidade de `O(log n)`.

3. **Qual é a principal desvantagem da busca binária?**  
   **Resposta**: d) A lista precisa estar ordenada para funcionar corretamente.  
   A busca binária só funciona em listas ordenadas, o que pode ser uma limitação se os dados não estiverem organizados.

4. **Ao utilizar a pesquisa binária, qual condição leva ao término da recursão na busca?**  
   **Resposta**: c) Quando o índice de início é maior que o índice final.  
   Isso indica que o item não foi encontrado na lista, pois o intervalo pesquisado foi completamente reduzido.

5. **Dada uma lista desordenada `[10, 22, 5, 1, 7]`, qual o número de comparações feitas na pesquisa sequencial para encontrar o elemento 5?**  
   **Resposta**: 3  
   Na pesquisa sequencial, a busca percorre os elementos da lista um a um. Para encontrar o elemento 5, são feitas 3 comparações (10, 22, e então 5).

6. **Após quantas iterações a pesquisa binária encontra o elemento 8 na lista `[2, 4, 6, 8, 10]`?**  
   **Resposta**: 2  
   Primeira iteração: o meio é 6. Como 8 é maior, descarta-se a metade inferior.  
   Segunda iteração: o meio é 8, o que coincide com o item procurado.  
   Logo, são necessárias 2 iterações.

7. **Em uma lista ordenada de 1000 elementos, a pesquisa binária levará em média quantas comparações no pior caso?**  
   **Resposta**: Aproximadamente 10 comparações.  
   No pior caso, a busca binária necessita de `log₂(n)` comparações. `log₂(1000)` é aproximadamente 10.

8. **Em uma pesquisa sequencial, quantas iterações no máximo são necessárias para encontrar um elemento em uma lista de 100 elementos?**  
   **Resposta**: 100  
   No pior caso, se o elemento estiver no final ou não estiver presente, serão necessárias 100 comparações.

9. **Suponha que você tenha uma lista de strings ordenadas alfabeticamente. Como você adaptaria a busca binária para encontrar uma determinada string nessa lista?**  
   **Resposta**: Podemos usar o mesmo algoritmo de busca binária, comparando as strings de forma lexicográfica. Aqui está um exemplo em Python:

   ```python
   def busca_binaria_strings(lista, item_pesquisado):
       inicio = 0
       fim = len(lista) - 1
       while inicio <= fim:
           meio = (inicio + fim) // 2
           if lista[meio] == item_pesquisado:
               return True
           elif lista[meio] < item_pesquisado:
               inicio = meio + 1
           else:
               fim = meio - 1
       return False

   # Teste
   lista_strings = ["abacate", "banana", "caju", "laranja", "manga"]
   print(busca_binaria_strings(lista_strings, "laranja")) # True
   print(busca_binaria_strings(lista_strings, "uva")) # False
   ```

10. **Liste duas vantagens e duas desvantagens da busca sequencial em relação à busca binária.**  
    **Resposta**:  
    - **Vantagens**:  
      1. Funciona em listas desordenadas.  
      2. É mais simples de implementar e compreender.  
    - **Desvantagens**:  
      1. Menos eficiente em listas grandes (`O(n)`), pois precisa examinar cada elemento até encontrar o item.  
      2. Não se beneficia de uma lista ordenada como a busca binária.

11. **Apresente uma versão recursiva da busca binária em Python.**  
    **Resposta**:

    ```python
    def busca_binaria_recursiva(lista, item, inicio=0, fim=None):
        if fim is None:
            fim = len(lista) - 1
        if inicio > fim:
            return False
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return True
        elif lista[meio] > item:
            return busca_binaria_recursiva(lista, item, inicio, meio - 1)
        else:
            return busca_binaria_recursiva(lista, item, meio + 1, fim)

    # Teste
    lista_teste = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(busca_binaria_recursiva(lista_teste, 8))  # True
    print(busca_binaria_recursiva(lista_teste, 3))  # False
    ```

    A recursão reduz a lista pela metade em cada chamada, até que o item seja encontrado ou os índices de busca se invertam (início > fim).

12. **Crie uma função de pesquisa binária que retorne todos os índices de um número em uma lista ordenada que pode conter duplicatas.**  
    **Resposta**:

    ```python
    def busca_binaria_todos_indices(lista, item):
        indices = []
        inicio = 0
        fim = len(lista) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if lista[meio] == item:
                indices.append(meio)
                i = meio - 1
                while i >= 0 and lista[i] == item:
                    indices.append(i)
                    i -= 1
                i = meio + 1
                while i < len(lista) and lista[i] == item:
                    indices.append(i)
                    i += 1
                return sorted(indices)
            elif lista[meio] < item:
                inicio = meio + 1
            else:
                fim = meio - 1
        return indices

    # Teste
    lista_teste = [1, 2, 2, 2, 3, 4, 4, 5]
    print(busca_binaria_todos_indices(lista_teste, 2))  # [1, 2, 3]
    ```

13. **Implemente a busca binária usando recursividade sem o operador `slice`.**  
    **Resposta**:

    ```python
    def busca_binaria_recursiva_sem_slice(lista, item, inicio, fim):
        if inicio > fim:
            return False
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return True
        elif lista[meio] > item:
            return busca_binaria_recursiva_sem_slice(lista, item, inicio, meio - 1)
        else:
            return busca_binaria_recursiva_sem_slice(lista, item, meio + 1, fim)

    # Teste
    lista_teste = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(busca_binaria_recursiva_sem_slice(lista_teste, 8, 0, len(lista_teste) - 1))  # True
    print(busca_binaria_recursiva_sem_slice(lista_teste, 3, 0, len(lista_teste) - 1))  # False
    ```

14. **Gere uma lista de números aleatórios, ordene-os e verifique o desempenho dos seguintes algoritmos de busca:**
    - **Busca sequencial**
    - **Busca binária com `slice`**
    - **Busca binária sem `slice`**
   
   **Resposta**:
   Para este exercício, você pode usar a biblioteca `time` para medir o desempenho de cada função. Crie uma lista de números aleatórios com `random.sample`, ordene-a e meça o tempo de execução para cada tipo de busca.
