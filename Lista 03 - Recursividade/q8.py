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
