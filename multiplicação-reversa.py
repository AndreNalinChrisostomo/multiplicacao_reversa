#codigo pensado e escrito por: André Nalin Chrisostomo
#Este programa basicamente faz uma multiplicação inversa, ou seja, ao invés de dar dois numeros para multiplicar e retornar um resultado, o programa permite você dar um resultado e o programa mostrar todas as multiplicações possíveis para retornar o número
from random import randint 


def comecar(valor):

    #define quais serão os valores da direita e da esquerda da multiplicação
    direita  =  randint(1, valor)
    esquerda =  randint(1, valor)

    #loop para checar se os valores aleatórios quando multiplicados resultam no valor definido
    while True:
        if direita * esquerda == valor:
            print(f'{direita} * {esquerda} = {valor}')
            direita  =  randint(1, valor)
            esquerda =  randint(1, valor)    
        else:
            direita  =  randint(1, valor)
            esquerda =  randint(1, valor)            


comecar(int(input("Insira o valor a ser trabalhado: ")))


