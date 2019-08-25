from random import randint as r
from random import choice as c

invetario = {}
personagem = {}

#abilidades
força = 1
destreza = 1
mira = 1
recuperação = 1
arcanidade = 1
sabedoria = 1
percepção = 1
carisma =  1
sorte = 1
altura = 4
#vidas
vp = 100 
ep = 0
#preços
ferrop = 50
açop = 50
ourop = 50
pratap = 50
pot = 10
#magia
mp = 50
#equipamentos
poção = 0
gold = 500
flechas = 0
dardos = 0
arma = "soco"
#outros
dmi = 1  #dano magico do item
ddi = 1  #dano a distancia do item
ddp = 1 # dano do projetil
cdd = 1  #chance de defesa
dnm = 1  #dano do material  
dni = 1  #dano do item
dnmi = 1 #dano do item
dfi = dni + dnm  #dano fisico do item
dne = 1  #dano do inimigo
ene = "aleatorio" #inimigo
goldr = 0 # gold roubado
#danos
dano_fisico = destreza + dfi
dano_magico = 0
dano_a_distacia = mira + ddi + ddp
#nivel
lv = 1
xp = 0
#listas
classes = ["barbaro","bardo","clérigo","mago","druida","ladino","paladino"]
raças = ["humano","anão","elfo","gnomo","halfling"]
armas_fisicas = ["adaga","clave","punhais","machado","escudo"]
armas_a_distancia = ["arco","besta","shuriken"]
armas_magicas = ["cajado","arco magico","livro magico","espada magica"]

#criação de personagem
print("criação de personagem")
personagem["raça"] = input(f"escolha uma das raças:\n{raças}\n")
personagem["classe"] = input(f"escolha uma das classes:\n{classes}\n")
personagem["nome"] = input("qual seu nome?\n")

perso = True
while perso:
    if personagem["raça"] not in raças:
        personagem["raça"] = input(f"escolha invalida\nescolha uma das raças:\n{raças}\n")
    else:
       break
perso2 = True
while perso2:
    if personagem["classe"] not in classes:
        personagem["classe"] = input(f"escolha invalida\nescolha uma das classes:\n{classes}\n")
    else:
        break



#regulando abilidades
if personagem["raça"] == "humano":
    força += 1
    destreza += 1
    mira += 1
elif personagem["raça"] == "anão":
    sorte += 2
    sabedoria += 1
    altura -= 1
elif personagem["raça"] == "elfo":
    mira += 1
    arcanidade += 1
    sabedoria += 1
elif personagem["raça"] == "gnomo":
    altura -= 2
    sorte += 3
    recuperação += 3
elif personagem["raça"] == "halfling":
    altura -= 1
    sorte += 3
    percepção += 1
if personagem["classe"] == "barbaro":
    força += 10
    destreza += 5
    recuperação += 5
    arcanidade += 1
    sabedoria += 5
    percepção += 3
    carisma += 5
elif  personagem["classe"] == "bardo":
    força += 5
    destreza += 10
    mira += 5
    recuperação += 5
    arcanidade += 5
    carisma += 10
    sorte =+ 5
elif  personagem["classe"] == "clérigo" or "clerigo":
    destreza += 5
    mira += 10
    recuperação += 10
    arcanidade += 10
    sabedoria += 5
    percepção += 5
    sorte += 10
elif  personagem["classe"] == "mago":
    força += 5
    destreza += 10
    mira += 5
    recuperação += 5
    arcanidade += 10
    sabedoria += 5
    percepção += 5
    sorte += 10
elif  personagem["classe"] == "druida":
    destreza += 5
    mira += 5
    recuperação += 5
    arcanidade += 9
    sabedoria += 10
    percepção += 5
    sorte += 9
elif  personagem["classe"] == "ladino":
    destreza += 10
    mira += 7
    recuperação += 5
    arcanidade += 1
    sabedoria += 10
    percepção += 5
    carisma += 5
    sorte += 10
elif  personagem["classe"] == "paladino":
    força += 5
    destreza += 10
    recuperação += 5
    arcanidade += 5
    sabedoria += 5
    percepção += 5
    carisma += 5
    sorte += 5

def batalha(ene,dne,goldr,dano_fisico,dano_magico,dano_a_distacia,arma,armas_magicas,armas_a_distancia,armas_fisicas,vp,mp,gold,poção,sorte,dni,cdd,destreza):
#define o inimigo
    inimigo = ("zumbi esqueleto ladrão").split()
    sorte1 = c(inimigo)
    if sorte1 == "zumbi":
        ene = "zumbi"
        ep = 100
        dne = r(1,15)
    elif sorte1 == "esqueleto":
        ene = "esqueleto"
        ep = 120
        dne = r(1,20)
    elif sorte1 == "ladrão":
        ene = "ladrão"
        ep = 100
        dne = r(1,15)
        goldr = r(1,5)
    jogo = True
    while jogo:
#define se você ganha ou perde
        if vp <= 0:
            print("Você perdeu\n")
            break
        elif ep <= 0:
            print("Parabens você ganhou\n")
            break
        print()

#mostra a vida e as escolhas
        print(f"sua vida: {vp}\nvida do {ene}: {ep}\nmoedas: {gold}\n")
        escolha =input("ATACAR DEFENDER MAGIA LOJA INVENTARIO \n").lower().strip()[:1]

#luta
        if escolha == "a":
            if arma == "soco":
                tec = input("você esta desarmado deja mesmo atacar? (s/n)\n")
                if tec == "n":
                    break
                else:
                    print(f"seu ataque foi de:{dano_fisico}\n")
                    ep -= dano_fisico
            elif arma in armas_fisicas:
                ep -= dano_fisico
                print(f"seu dano foi de {dano_fisico}\n")
            elif arma in armas_magicas:
                ep -= dano_magico
                print(f"seu dano foi de {dano_magico}\nagora você tem {mp} de mp\n ")
            elif arma in armas_a_distancia:
                ep -= dano_a_distacia
                print(f"seu dano foi de {dano_a_distacia}\n")
        
#magia
        if escolha == "m":
            print(f"você tem {mp} de mp\n")
            escolha_magia = input("CURA ATAQUE\n").lower().strip()[:1]
            if escolha_magia == "c":
                if mp <= 10:
                    print("você não tem mp suficiente")
                else:   
                    print("a cura custa 10mp e cura 15vp")
                    vp += 15
                    mp -= 10
                    print(f"agora você tem {mp} pontos de mp\n")
            if escolha_magia == "a":
                if mp <= 15:
                    print("você não tem mp suficiente")
                else:
                    print("o ataque custa 15 de mp e lança uma bola de fogo que da 10 pontos de dano magico\n")
                    ep -= 10
                    mp -= 15

#loja
        if escolha == "l":
            arma1 = c(armas_fisicas)
            arma2 = c(armas_a_distancia)
            arma3 = c(armas_magicas)
            print("todas as armas custão 50 moedas")
            escolha_loja = input(f"poção {arma1} {arma2} {arma3}\n").lower().strip()
            if escolha_loja == "p":
                print("a poção custa 15 moedas e cura 10 de vida")
                if gold <= 15:
                    print("você não tem moedas suficientes")
                else:
                    poção += 1
                    gold -= 15
            if escolha_loja == arma1:
                gold - 50
                if arma1 == "adaga":
                    arma = "adaga"
                    dni = 5
                    print("você adiquiriu adaga")
                if arma1 == "clave":
                    arma = "clave"
                    dni = 8
                    print("você adiquiriu clave")
                if arma1 == "punhais":
                    arma = "punhais"
                    dni = 6
                    sorte += 1
                    print("você adiquiriu punhais")
                if arma1 == "machado":
                    arma = "machado"
                    dni = 10
                    print("você adiquiriu machado")
                if arma1 == "escudo":
                    arma = "escudo"
                    print("você adiquiriu escudo")
                    dni =  5
                    cdd = 10
            print(arma)
            print(dni)
            print(destreza)
                
                    
            
                    
                    

#inimigo ataca
        print()
        print(f"Agora o {ene} ira atacar")
        if escolha == 'a':
            print(f"você recebeu {dne} de dano")
            if escolha == 'a':
                vp -= dne

#ganha ouro
        gold1 = r(1,15) + sorte
        gold += gold1

batalha(ene,dne,goldr,dano_fisico,dano_magico,dano_a_distacia,arma,armas_magicas,armas_a_distancia,armas_fisicas,vp,mp,gold,poção,sorte,dni,cdd,destreza)            
