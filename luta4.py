from random import randint as r
from random import choice as c

#preços
esp1 = 50
ado = 75
#vida
vida = 250
zombi = 500
#euipamentos
gold = 0
poção = 0
#status
dano = 1
adp = 1

def luta(esp1,ado,vida,zombi,gold,poção,dano,adp):

    print("Você encontrou um zombi lute contra ele")

    defesa = ('fracassou sucesso fracassou').split()
    sorte = c(defesa)
    jogo = True
    while jogo:
        if vida <= 0:
            print("Você perdeu")
            break
        elif zombi <= 0:
            print("Parabens você ganhou")
            break
        print()

        print(f"sua vida: {vida}\nvida do zombi: {zombi}\nmoedas: {gold}\n")
        escolha =input("ATACAR DEFENDER ITENS POÇÕES\n").lower().strip()[:1]
        
        if escolha == 'a':
            escolha_atacar = input('Para girar o dado aperte (D): ')
            print()
            if escolha_atacar == 'd':
                dado = r(1,20)
                print(f"Seu ataque foi de {dado * dano}pts")
                if escolha_atacar == 'd':
                    zombi -= dado
                
            else:
                print("Você usou o comando errado e morreu")
                break
    #aqui que eu mexi
        if escolha == 'i':
            print(f"você tem {gold} moedas\n")
            compra = (input(f"poção = 10g (1)\nespada = {esp1}g (2)\nadorar os deuses = {ado}g (3)\n"))
            if compra == "p":
                print("a poção cura 15 pts de vida e custa 10 moedas\n")
                if gold >= 10:
                    gold = gold - 10
                    print("você comprou uma poção\n")   
                    poção = poção + 1
                else:
                    print("você não tem moedas suficientes\n")
            elif compra == "e":
                print(f"a espada aumenta o dano em 1pt e custa {esp1} moedas\n")
                if gold >= esp1:
                    gold = gold - esp1
                    print("agora seu dano esta aumentado\n")
                    dano = dano + 1
                    esp1 = esp1 + 25
                else:
                    print("você não tem moedas suficientes\n")
            elif compra == "a":
                print(f"adorar os deuses aumenta a taxa de ouro\n dropado em 1 e custa {ado}\n")
                if gold >= ado:
                    gold = gold - ado
                    print("agora dropara mais ouro dos inimigos\n")
                    adp = adp + 1
                    ado = ado + 50
                else:
                    print("você não tem moedas suficientes\n")
            else:
                escolha = "a"
        if escolha == 'p':
            if poção >= 1:
                vida = vida + 15
                poção = poção - 1
                print(f"você tomou uma poçâo agora sua vida esta em {vida}\ne você tem {poção} poções")
            else:
                print("você não tem poções")
        
        else:
            dano_contra_ataque = r(1,5)
            if sorte == 'sucesso':
                print(f'voce conseguio defender e lançar um contra ataque de {dano_contra_ataque}pts')
                if sorte == 'sucesso':
                    zombi -= dano_contra_ataque
            else:
                print('sua defesa fracassou\nvocê recebera dano x2 no proximo ataque')

        print()
        print('Agora o zombi ira atacar')
        ataque_zombi = r(1,20)
        if escolha == 'a':
            print(f'você recebeu {ataque_zombi} de dano')
            if escolha == 'a':
                vida -= ataque_zombi
        else:
            if sorte == 'sucesso':
                print('defendeu')
                continue
            else:
                print(f'você recebeu {ataque_zombi*2} de dano')
                if sorte == 'fracassou':
                    vida -= ataque_zombi*2

        gold1 = r(1,10)
        gold2 = gold1 * adp
        gold = gold + gold2

        
        print(f"com essa batalha você conseguio mais {gold1} moedas \n ")

        print()

valor1 = input("deseja lutar?(s/n)\n")
if valor1 == "s":
    luta(esp1,ado,vida,zombi,gold,poção,dano,adp)
