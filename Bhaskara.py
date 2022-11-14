import re
import math
'''
Formula: Δ= b²-4.a.c
         x= (-b±√Δ)/(2.a)
'''

def check(x): # Verifica se X é positivo ou negativo 
    if x == '' or x == '+': return int(1)
    if x == '-': return int(-1)
    return x

def fCoeficientes(equação): # Encontra os coeficientes
    coeficientes = re.search('([+-]?\d*)x\^2([+-]\d*)x+([+-]\d+)', equação) # procurar os coeficientes
    if coeficientes: # Se achar os coeficientes, defina-os
        a = check(coeficientes.group(1))
        b = check(coeficientes.group(2)) # Classificando os coeficientes
        c = coeficientes.group(3)
        return [int(a),int(b),int(c)]

    return

def mdc(n,d): # Encontra o MDC
    while d != 0: # Descobre o MDC de n e d
        r = n%d
        n = d
        d = r
    return n

def calcX(coeficientes, delta, op): # Calcula o X' ou X"
    a,b,c = coeficientes # Define os coeficientes
    raizDelta = int(math.sqrt(delta)) # calcula a raiz quadrada do delta

    if op == 1: n = (-b+raizDelta) # se op = 1, calcule o x', se não, calcule o x"
    else: n = (-b-raizDelta)

    d = (2*a) # Calcula o denominador
    X = n/d # Divide o numerador pelo denominador
    if not X//1 == X : # Se o resultado não for um numero inteiro, deixe-o como fração
        m = mdc(n,d) # Calcula o Minimo Multiplo Comum do numerador e do denominador
        X = f'{n//m}/{d//m}' # Divide a fração pelo mdc(para simplificá-la)
    else: X = int(X) # Se X não for fracão, defina-o como inteiro(pois "n/d" retorna um float)

    return X

def bhaskara(equação): # Junta tudo e calcula o valor de X
    
    coeficientes = fCoeficientes(equação)
    if not coeficientes: 
        return print("Equação invalida!\nUse o formato: ax^2±bx±c\nExemplo:x^2+12x-13")

    a,b,c = coeficientes # define os coeficientes
    delta = b**2-4*a*c

    if delta < 0:
        S = '{Esta equação não possui raizes reais!}'
    else:
        x1 = calcX(coeficientes, delta, 1) # Encontra o valor de x'
        x2 = calcX(coeficientes, delta, 2) # Encontra o valor de x"
        S = '{' + f'{x1},{x2}' +'}' # Define a solução da formula
        if x1 == x2: S = '{' + f'{x1}' +'}'

    print(f'Equação: {equação}\nCoeficientes: a = {a}, b = {b}, c = {c}\nDelta: {delta}\nResultado: S={S}')
