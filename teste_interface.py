#importar biblioteca de sortear
import random
from colorama import Fore, Back, Style
#Função cria baralho
def cria_baralho():
    carta= ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    naipe= ["♠","♥","♦","♣"]
    baralho=[]
    for n in naipe:
        for c in carta:
            baralho.append(c+n)
    random.shuffle(baralho)
    return baralho
#Função extrai naipe
def extrai_naipe(x):
    y= x[-1]
    return y
#Função extrai valor da carta
def extrai_valor(v):
    v= v[:-1] + ""
    return v
#Função lista de movimentos possíveis
def lista_movimentos_possiveis(s,p):
    lista_mov= []
    if p == 0:
        return []
    if p > len(s):
        return []
    else:
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
    s[z]= s[y]
    del(s[y])
    return s
#Função possui movimentos possiveis
def possui_movimentos_possiveis(s):
    i= 0
    while i < len(s):
        mov_poss= lista_movimentos_possiveis(s, i)
        if mov_poss!= []:
            return True
        else:
            i= i+1
    return False

#Intruções do jogo:
print('Paciência Acordeão\n ============\n\n Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. \n ')
print('Existem apenas dois movimentos possíveis:\n\n 1. Empilhar uma carta sobre a carta imadiatamente anterior;\n 2. Empilhar uma carta sobre a terceira carta anterior.\n')
print('Para que o movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n')
print('1. As duas cartas possuem o mesmo valor ou\n2. as duas cartas possuem o mesmo naipe.\n')
print('Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n')
#Aperte [Enter] / Gerar cartas e numero
start= True
while start:
    comeca= input("Aperte [Enter] para iniciar o jogo...")
    if comeca == (""):
        baralho= cria_baralho()
        possui_movimentos= possui_movimentos_possiveis(baralho)
        while possui_movimentos:
            c_baralho= 0
            num= 1
            while c_baralho < len(baralho):
                naipe= extrai_naipe(baralho[c_baralho])
                if naipe == "♠":
                    print(Fore.CYAN + '{0}.  {1}'.format(num, baralho[c_baralho]))         #{0}: Numero da carta // {1}: Valor e estilo da carta
                if naipe == "♥":
                    print(Fore.RED + '{0}.  {1}'.format(num, baralho[c_baralho]))
                if naipe == "♦":
                    print(Fore.MAGENTA + '{0}.  {1}'.format(num, baralho[c_baralho]))
                if naipe == "♣":
                    print(Fore.GREEN + '{0}.  {1}'.format(num, baralho[c_baralho]))
                num = num+1 
                c_baralho = c_baralho+1
            w= True
            a = True
            while a:
                p =  int(input(Fore.WHITE + "Escolha uma carta (digite um número entre 1 e {}):  ".format(num-1)))
                if p >52 or p>=num:
                    print("Posição inválida. Por favor, digite um número entre 1 e {}:  ".format(num-1))
                a =False
                break
            possiveis_movimentos = lista_movimentos_possiveis(baralho, p-1)
            if p > len(baralho):
                print("")
            else:
                if possiveis_movimentos == []:
                    print ("A carta {0} não pode ser movida. Por favor, digite um número entre 1 e {1}:  ".format(baralho[p-1],num-1))
            if possiveis_movimentos == [1]:
                empilha(baralho, p-1, p-2)
            if possiveis_movimentos == [3]:
                empilha(baralho,p-1, p-4)
            if possiveis_movimentos == [1, 3]:
                b = True
                while b:
                    print('Sobre qual carta você quer empilhar o {0}?'.format(baralho[p-1]))
                    naipe_p2=extrai_naipe(baralho[p-2])
                    naipe_p4=extrai_naipe(baralho[p-4])
                    if naipe_p2 == "♠":
                        print(Fore.CYAN + "1.  {0}".format(baralho[p-2]))
                    if naipe_p2 == "♥":
                        print(Fore.RED + "1.  {0}".format(baralho[p-2]))
                    if naipe_p2 == "♦":
                        print(Fore.MAGENTA + "1.  {0}".format(baralho[p-2]))
                    if naipe_p2 == "♣":
                        print(Fore.GREEN + "1.  {0}".format(baralho[p-2]))
                    if naipe_p4 == "♠":
                        print(Fore.CYAN + "2.  {0}".format(baralho[p-4]))
                    if naipe_p4 == "♥":
                        print(Fore.RED + "2.  {0}".format(baralho[p-4]))
                    if naipe_p4 == "♦":
                        print(Fore.MAGENTA + "2.  {0}".format(baralho[p-4]))
                    if naipe_p4 == "♣":
                        print(Fore.GREEN + "2.  {0}".format(baralho[p-4]))
                    posicao_empilha = int(input(Fore.WHITE+'Digite o número de sua escolha(1-2):  '))
                    if posicao_empilha == 1:
                        empilha(baralho, p-1, p-2)
                        break
                    if posicao_empilha == 2:
                        empilha(baralho, p-1, p-4)
                        break
                    else:
                        print('Posição inválida, digite um número entre 1 e 2:')
                    break
        existe_movimentos = possui_movimentos_possiveis(baralho)
if len(baralho) >1:
    print(Fore.RED + "Você Perdeu")
else:
    print(Fore.GREEN + "Parabéns! Você ganhou")
estado_final=input(Fore.WHITE + "Você quer jogar de novo? (sim/nao) ")
if estado_final == "sim":
    start = True
if estado_final == "nao":
    start = False