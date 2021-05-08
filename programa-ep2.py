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

#Função extrai naipe
def extrai_naipe(x):
    y = x[-1]
    return y

#Função extrai valor da carta
def extrai_valor(x):
    x = x[:-1] + ""
    return x

#Função lista de movimentos possíveis
def lista_movimentos_possiveis (s,p):
    lista_mov= []
    if p == 0:
        return []
    if extrai_naipe(s[p]) == extrai_naipe(s[p-1]):
        lista_mov.append(1)
    elif extrai_valor (s[p]) == extrai_valor(s[p-1]):
        lista_mov.append(1)
    if extrai_naipe(s[p]) == extrai_naipe(s[p-3]) and (p-3) >=0:
        lista_mov.append(3)
    elif extrai_valor(s[p]) == extrai_valor(s[p-3]) and (p-3)>=0:
        lista_mov.append(3)
    return lista_mov


#Função empilha
def empilha(x,y,z):
    x.remove(x[z]) 
    x.insert(x[z],x[y])
    x.remove(x[y])
    return x
print(empilha(['6♥', 'J♥', '9♣', '9♥'],1,0))
