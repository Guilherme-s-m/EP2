#importar biblioteca de sortear
import random
#Função cria baralho
def cria_baralho():
    carta= ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    naipe= ["♠","♥","♦","♣"]
    baralho=[]
    for n in naipe:
        for c in carta:
            carta= c+n
            baralho.append(carta)
    return baralho


Função extrai naipe
  def extrai_naipe(x):
    y = x[-1]
    return y

