# Lista de Exercícios 03 (Recursividade) 
## Instruções: 
### Desenvolva seu algoritmo para os problemas abaixo. 

Crie suas próprias funções, utilize o mínimo de funções preexistentes da linguagem. 

1. Escreva uma função recursiva que calcule e retorne o fatorial de um número inteiro N. Fat(4) = 4 * 3 * 2 * 1

2. Escreva uma função recursiva que permita inverter uma palavra N. "Python" -->> "nohtyP"

3. Escreva uma função recursiva que determine quantas vezes uma letra K ocorre em uma Palavra P. Por exemplo, a letra 'u' ocorre 2 vezes em "estrutura" 

4. Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente. 

5. Escreva uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente. 

6. Escreva uma função recursiva que calcule o Nésimo 10 termo da sequencia de Fibonacci. A sequência de Fibonacci é 0,1, 1, 2, 3, 5, 8, 13, 21,... 

7. Escreva uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número. O fatorial duplo é definido como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! == 1 * 3 * 5 = 15 

8. Escreva uma função recursiva que informa se uma String é palíndroma ou não. Um palíndromo é uma string que é lida da mesma maneira da esquerda para a direita e da direita para a esquerda. Alguns exemplos de palíndromo são "E até o papa poeta é" (se os espaços, pontuação e acentos forem ignorados). 

9. O MDC de dois números inteiros é o maior número inteiro que divide ambos sem deixar resto. O MDC pode ser calculado através do algoritmo de Euclides. Abaixo uma função iterativa que calcula o MDC. Reescreva a função abaixo de forma recursiva. 

````python
def MDC(a, b): 
while (b != 0): 
r = a % b 
a = b 
b = r 
return a
````
