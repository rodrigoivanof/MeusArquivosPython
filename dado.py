tink = False
while tink == False:

    from random import randint as r
    dado = r(1,20)
    print(dado)

    tink2 = input("deseja rodar o dado? (s/n)\n")
    if tink2 == "n":
        tink = True
