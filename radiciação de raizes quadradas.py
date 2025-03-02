import numpy

primos = [2, 3, 5, 7]

def gprimes(r):
    
    for n in range(2, r+1):
        if n == 1: continue
        for d in primos:
            if n%d == 0:
                break
            
            if d == 7: primos.append(n)

def fatorar(n):
    gprimes(n)
    termos = []
    while not int(n) == 1:
        for d in primos:
            while n%d == 0:
                n = n/d
                termos.append(d)
    
    termos = agrupar(termos)
    return termos

def agrupar(termos):
    print(f'Resultado da fatoração: {(termos)}')
    lista = []
    r = []
    last = False
    numeros = sorted(set(termos))

    for i in range(len(termos)):
        if last == True: 
            last = False
            continue

        if i+1 >= len(termos):
            r.append(str(termos[i]))
            break

        if termos[i] == termos[i+1]:
            lista.append(termos[i])
            last = True
        else:
            r.append(str(termos[i]))
    
    return lista, r

def raiz(num):
    sla = fatorar(int(num))

    radicando = sla[1]
    if len(radicando) >= 1: radicando = '√'+"⋅".join(radicando)
    else: radicando = ''

    fora = sla[0]
    fora = int(numpy.prod(fora))
    if fora == 1: fora = ''

    if fora == radicando: fora = '1'
    return f'{fora}{radicando}'

def start():
    num = int(input('Que número você gostaria de obter a raiz quadrada?\n'))
    result = raiz(num)
    return print(f'A raiz quadrada de {num} é {result}') 

start()
