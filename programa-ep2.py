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
def extrai_valor(v):
    v = v[:-1] + ""
    return v
#Função lista de movimentos possíveis
def lista_movimentos_possiveis(s,p):
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
def empilha(s,y,z):
    s[z] = s[y]
    del(s[y])
    return s
#Função possui movimentos possiveis
def possui_movimentos_possiveis(s):
    i = 0
    while i < len(s):
        mov_poss = lista_movimentos_possiveis(s, i)
        if mov_poss != []:
            return True
        else:
            i += 1
    return False

#Intruções do jogo:
print('Paciência Acordeão\n ============\n\n Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. \n ')
print('Existem apenas dois movimentos possíveis:\n\n 1. Empilhar uma carta sobre a carta imadiatamente anterior;\n 2. Empilhar uma carta sobre a terceira carta anterior.\n')
print('Para que o movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n')
print('1. As duas cartas possuem o mesmo valor ou\n2. as duas cartas possuem o mesmo naipe.\n')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n\nAperte [Enter] para iniciar o jogo... ')


