from random import randint as r
from random import choice as s
a = ' '
b = ' '
c = ' '
d = ' '
e = ' '
f = ' '
g = ' '
h = ' '
i = ' '

escolha = input("Escolha entre\nX ou O: ").strip().upper()
escolha_maquina = ''
if escolha == 'X':
    escolha_maquina = 'O'
elif escolha == 'O':
    escolha_maquina = 'X'
else:
    print("Esta opçao não existe")
print(f"Sua escolha: {escolha}\nEscolha da maquina {escolha_maquina}")
casas_livres = ["a","b","c","d","e","f","g","h","i"]
letras = ["a","b","c","d","e","f","g","h","i"]
casas_cheias = []

while True:
    while True:
        jogada = input("Escolha sua casa: ")
        if jogada in casas_cheias:
            print("esta casa ja esta ocupada")
        else:
            break

    if jogada == "a":
        casas_livres[0] = "1"
        casas_cheias.insert(0,"a")
        a = escolha
    elif jogada == "b":
        casas_livres[1] = "2"
        casas_cheias.insert(1,"b")
        b = escolha
    elif jogada == "c":
        casas_livres[2] = "3"
        casas_cheias.insert(2,"c")
        c = escolha
    elif jogada == "d":
        casas_livres[3] = "4"
        casas_cheias.insert(3,"d")
        d = escolha
    elif jogada == "e":
        casas_livres[4] = "5"
        casas_cheias.insert(4,"e")
        e = escolha
    elif jogada == "f":
        casas_livres[5] = "6"
        casas_cheias.insert(5,"f")
        f = escolha
    elif jogada == "g":
        casas_livres[6] = "7"
        casas_cheias.insert(6,"g")
        g = escolha
    elif jogada == "h":
        casas_livres[7] = "8"
        casas_cheias.insert(7,"h")
        h = escolha
    elif jogada == "i":
        casas_livres[8] = "9"
        casas_cheias.insert(8,"g")
        i = escolha

    tabela2=( 
    f'      |     |      \n'
    f'    {a} |  {b}  |  {c}\n'
    f'  ____|_____|____  \n'
    f'      |     |      \n'
    f'    {d} |  {e}  |  {f}\n'
    f'  ____|_____|____  \n'
    f'      |     |      \n'
    f'    {g} |  {h}  |  {i}\n'
    f'      |     |      \n' 
    )

    print(casas_livres)
    print(tabela2)
    print("agora a vez da maquina")

    while True:
        jogada_maquina = s(casas_livres)
        if jogada_maquina in letras:
            if jogada_maquina not in casas_cheias:
                break

    if jogada_maquina == "a":
        casas_livres[0] = "1"
        casas_cheias.insert(0,"a")
        a = escolha_maquina
    elif jogada_maquina == "b":
        casas_livres[1] = "2"
        casas_cheias.insert(1,"b")
        b = escolha_maquina
    elif jogada_maquina == "c":
        casas_livres[2] = "3"
        casas_cheias.insert(2,"c")
        c = escolha_maquina
    elif jogada_maquina == "d":
        casas_livres[3] = "4"
        casas_cheias.insert(3,"d")
        d = escolha_maquina
    elif jogada_maquina == "e":
        casas_livres[4] = "5"
        casas_cheias.insert(4,"e")
        e = escolha_maquina
    elif jogada_maquina == "f":
        casas_livres[5] = "6"
        casas_cheias.insert(5,"f")
        f = escolha_maquina
    elif jogada_maquina == "g":
        casas_livres[6] = "7"
        casas_cheias.insert(6,"g")
        f = escolha_maquina
    elif jogada_maquina == "h":
        casas_livres[7] = "8"
        casas_cheias.insert(7,"h")
        h = escolha_maquina
    elif jogada_maquina == "i":
        casas_livres[8] = "9"
        casas_cheias.insert(8,"i")
        i = escolha_maquina

    tabela2=( 
    f'      |     |      \n'
    f'    {a} |  {b}  |  {c}\n'
    f'  ____|_____|____  \n'
    f'      |     |      \n'
    f'    {d} |  {e}  |  {f}\n'
    f'  ____|_____|____  \n'
    f'      |     |      \n'
    f'    {g} |  {h}  |  {i}\n'
    f'      |     |      \n' 
    )

    print(casas_livres)
    print(tabela2)

'''
    if a and b and c == escolha:
        print("você ganhou")
        break
    elif a and b and c == escolha_maquina:
        print("você perdeu")
        break
    elif a and e and i == escolha:
        print("você ganhou")
        break
    elif a and e and i == escolha_maquina:
        print("você perdeu")
        break
    elif a and d and g == escolha:
        print("você ganhou")
        break
    elif a and d and g == escolha_maquina:
        print("você perdeu")
        break
    elif b and e and h == escolha:
        print("você perdeu")
        break
    elif b and e and h == escolha_maquina:
        print("você perdeu")
        break
    elif c and f and i == escolha:
        print("você ganhou")
        break
    elif c and f and i == escolha_maquina:
        print("você perdeu")
        break
    elif d and e and f == escolha:
        print("você ganhou")
        break
    elif d and e and f == escolha_maquina:
        print("você perdeu")
        break
    elif g and h and i == escolha:
        print("você ganhou")
        break
    elif g and h and i == escolha_maquina:
        print("você perdeu")
        break
    elif g and e and c == escolha:
        print("você ganhou")
        break
    elif g and e and c == escolha_maquina:
        print("você perdeu")
        break
'''
