from random import randint as r

vida = 100
zombie = 150

luta = input("você encontrou um zumbi\ndeseja lutar? (s/n)\n")
if luta == "n":
    dado = r(1,20)
    if dado < 2:
        print ("você consegiu fugir\n")
    else:
        print ("você nâo consegue escapar\n ")

ks = input("para começar a batalha rode o dado apertando d:\n")
if ks == "d":
    dado = r(1,20)
    print(f"dado foi igual a {dado}")
if dado < 2:
    print("você errou")
else :
    zombie = (zombie - dado)
    print(f"zombie levou {dado} de dano")
    print(f"vida do zumbi esta em {zombie}")

kr = input("zumbi ataca, rode o dado aperando d:\n")
if kr == "d":
    dado = r(1,20)
    print (f"dado foi igual a {dado}")
if dado < 5:
    print("zombie errou")
else :
    vida = (vida - dado)
    print(f"você levou {dado} de dano")
print(f"sua vida esta em {vida}")
