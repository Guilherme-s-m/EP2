#importar biblioteca de sortear
import random
#função cria baralho
def cria_baralho():
    carta= ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    naipe= ["♠","♥","♦","♣"]
    baralho=[]
    for n in naipe:
        for c in carta:
            carta= c+n
            baralho.append(carta)
    return baralho

print cria_baralho()
print baralho


"""#função extrair naipe da carta
def extrai_naipe():
def criar_baralho():
#função extrair naipe da carta
def extrair_naipe(carta):
  def extrai_naipe(x):
    y = x[-1]
    return y
#função extrair valor da carta
def extrair_valor():"""
