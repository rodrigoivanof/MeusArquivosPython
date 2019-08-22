personagem = {}
pp =0
personagem["nome"] = input("qual o nome do seu personagem?\n")
classes = ["barbaro","bardo","clérigo","druida","paladino","ladino","mago"]
personagem["classe"] = input(f"escolha uma das classes:\n{classes}\n")
raças = ["humano","anão","elfo","gnomo","meio-elfo","meio-orc","halfling",]
personagem["raça"] = input(f"escolha uma das classes:\n{raças}\n")
abilidades = ["força","destreza","Constituição","Inteligência","Sabedoria","Carisma"]
pontos_de_abilidade = 2
pp = 1
print(f"você tem direito a duas dessas abilidades:\n{abilidades}\n")
abl1 = input("escolha a primeira abilidade:\n")
if pp == 1:
    pp = 0
    pontos_de_abilidade = 1
abl2 = input("escolha a segunda abilidade:\n")
pp = 1
if pp == 1:
    pp = 0
    pontos_de_abilidade = 0
abl= abl1 +" e "+ abl2
personagem["abilidades são"] = abl
personagem["pontos de abilidade"] = 0

print(personagem)