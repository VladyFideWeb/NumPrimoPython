def muestra_resultado(x):
    y = calcula_factorial(x-1)+1
    if y%x == 0:
        print('Número Primo')
    else: 
        print('Número no Primo')   


def calcula_factorial(numero):
    factorial =1
    for i in range(1,numero+1):
        factorial = factorial * numero
        numero = numero -1
    return factorial    

def run():
    x =int(input('Ingrese Número: '))
    if x == 1:
        print('Número no Primo')
    else:    
        Resultado =muestra_resultado(x)      


if __name__ == '__main__': 
    run()