def tobin(number): # Converte um decimal em binario
    bin = []
    if number == 0 or number == 1:
        return number

    while number != 0:
        bin.append(str(number%2))
        number = number//2
    
    return str().join(bin[::-1]) 

def todec(number): # Converte um binario em decimal
    number = str(number)
    dec = 0
    for n in number:
        dec = dec*2 + int(n)

    return dec

# Não me pergunte como funciona, fiz a muito tempo atrás.
 