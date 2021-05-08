#Função cria baralho
def cria_baralho():
    carta= ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    naipe= ["♠","♥","♦","♣"]
    baralho=[]
    for n in naipe:
        for c in carta:
            baralho.append(c+n)
    return baralho

print (cria_baralho())       
