#importar biblioteca de sortear
import random
#Função cria baralho
def cria_baralho():
    carta= ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    naipe= ["♠","♥","♦","♣"]
    baralho=[]
    for n in naipe:
        for c in carta:
            baralho.append(c+n)
    return baralho
#print(cria_baralho())

#Função extrai naipe
def extrai_naipe(x):
    y = x[-1]
    return y
#Função estrai valor da carta
def extrai_valor(x):
    x = x[:-1] + ""
    return x
