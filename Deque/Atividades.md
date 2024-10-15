# Lista de Exercícios 06 (Deque)
### Instruções:

- Desenvolva seu algoritmo para os problemas abaixo.

- Crie suas próprias funções, utilize o mínimo de funções reexistentes da linguagem.

#### 1. Qual os valores retornados durante a seguinte série de operações em uma deque "d" inicialmente inicialmente vazio? add_first(4), add_last(8), add_last(9), add_first(5), back(), delete_first(), delete_last(), add_last(7), first(), last(), add_last(6),
delete_first(), delete_first(). .

#### 2. Suponha que você tem um deque D contendo os números (1,2,3,4,5,6,7,8), nesta ordem. Suponha também que você tem inicialmente uma fila F vazia. Apresente o código que usa SOMENTE D e F (e nenhuma outra variável) e armazena em F os elementos de na ordem (1,2,3,4,5,6,7,8).

#### 3. João tem 4 vacas que ele deseja levar para o outro lado de um ponto, mas somente uma canga que permite colocar duas vagas, lado a lado, amarradas na canga. A canga é muito pesada pela ele carregar pela ponte, mas ele consegue prender (e soltar) as vacas na canga a qualquer momento sem gastar muito tempo (tempo 0). Das suas vacas:
-Malhada pode atravessar a ponte em 2 minutos
- Estrelinha pode atravessar em 4 minutos
- Celeste pode atravessar em 10 minutos
- Pintada pode atravessar em 20 minutos.
Claro, quando duas vagas são unidas a canga, elas se andam na velocidade da vaca mais lenta. Descreva como João pode levar todas as vacas pela ponte em 34 minutos ou menos.

canga = peça de madeira usada para atrelar bois a carroça ou arado, para que andem no mesmo compasso; jugo.

#### 4. Descreva como implementar um deque através da utilização de duas pilhas. Qual seria o tempo de execução dos métodos?

#### 5. Implemente o TAD deque a partir de FilaArray visto em sala de aula.

#### 6. Escreva um programa que usa um Deque para verificar se uma string é um palíndromo. O programa pode ignorar espaços e pontuações. Qual seria o tempo de execução do método (Big O)?

#### 7. Escreva a função deque_sum que retorna a soma dos elementos de um Deque implementado com listas.

#### 8. Qual o desempenho da função deque_sum [questão 7]? Há como melhorar? Explique!

#### 9. Explique a principal diferença entre um Deque e uma lista simples em Python em termos de complexidade de operações.

#### 10. Imagine que você tenha um deque circular implementado com listas, com um limite fixo de capacidade. O deque deve ser capaz de armazenar elementos até o limite especificado e, caso o deque esteja cheio, novos elementos inseridos do lado direito removem o elemento mais antigo do lado esquerdo (FIFO). Especifique como seria a implementação de tal deque com capacidade fixa e justifique como cada operação ( add_first , add_last , delete_first , delete_last ) deve ser ajustada para garantir o comportamento descrito. Quais são os tempos de execução dessas operações e como a lista subjacente é manipulada para manter a estrutura circular?

#### 11. Escreva uma função add para inserir um elemento em uma posição específica no meio do deque. Discuta o desempenho da sua função.
