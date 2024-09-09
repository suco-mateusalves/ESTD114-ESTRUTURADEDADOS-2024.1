'''
Função limpar_string(s, index=0):
Objetivo: Cria uma nova string contendo apenas os caracteres alfanuméricos e em minúsculas.
Recursão: Processa a string caractere por caractere. Se o caractere é alfanumérico, é adicionado à nova string. Caso contrário, é ignorado.
Caso Base: Quando o índice é maior ou igual ao comprimento da string, a função retorna uma string vazia.

Função verificar_palindromo(s):
Objetivo: Verifica se a string é um palíndromo.
Recursão: Compara o primeiro e o último caractere da string. Se forem iguais, a função é chamada recursivamente com a string reduzida (sem o primeiro e o último caractere). Se o comprimento da string for 1 ou 0, ela é um palíndromo.
Caso Base: Se a string tiver comprimento 1 ou 0, é um palíndromo.

Função eh_palindromo(s):
Objetivo: Limpa a string de entrada e verifica se ela é um palíndromo usando as funções auxiliares.
'''

def eh_palindromo(s):
    def limpar_string(s, index=0):
        if index >= len(s):
            return ""
        char = s[index].lower()
        if char.isalnum():  # Verifica se o caractere é alfanumérico
            return char + limpar_string(s, index + 1)
        else:
            return limpar_string(s, index + 1)

    def verificar_palindromo(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return verificar_palindromo(s[1:-1])
    
    s_limpo = limpar_string(s)
    return verificar_palindromo(s_limpo)

# Exemplo de uso:
print(eh_palindromo("E até o papa poeta é"))  # Saída: True
