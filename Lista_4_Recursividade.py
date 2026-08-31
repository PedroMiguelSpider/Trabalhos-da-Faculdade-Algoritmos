# 1. Escreva uma função recursiva que calcule o máximo divisor comum (MDC) de dois números inteiros a e b.
def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)
mdc_numeros = mdc(48, 18)
print(mdc_numeros)

# 2. Escreva uma função recursiva que calcule a potência de um número x elevado a um expoente n.
def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)
num = potencia(2, 10)
print(num)

# 3. Escreva uma função recursiva que inverta uma string. Por exemplo, se a entrada for "python", a função deve retornar "nohtyp".
def inverter(s):
    if len(s) <= 1:
        return s
    return inverter(s[1:]) + s[0]
inverso = inverter("python")
print(inverso)


# 4. Escreva uma função recursiva que verifique se uma string é um palíndromo. Um palíndromo é uma palavra ou frase que se lê da mesma forma de trás para frente, ignorando espaços, maiúsculas e minúsculas. Por exemplo, "arara" é um palíndromo.
def palindromo(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindromo(s[1:-1])
palavra = palindromo("arara")
print(palavra)

# 5. Escreva uma função recursiva que calcule a soma dos dígitos de um número inteiro positivo.
def soma_digitos(n):
    if n < 10:
        return n
    return n % 10 + soma_digitos(n // 10)
soma = soma_digitos(12345)
print(soma)


# 6. Escreva uma função recursiva que encontre todos os anagramas de uma string.
def anagramas(s):
    if len(s) <= 1:
        return [s]
    resultado = []
    for i, char in enumerate(s):
        restante = s[:i] + s[i+1:]
        for sub in anagramas(restante):
            resultado.append(char + sub)
    return resultado
anag = anagramas("abc")
print(anag)


