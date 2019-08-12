calc = False
while calc == False:

    valor1= int(input("digite o primeiro valor: "))
    variavel= input("digite a variavel: ")
    valor2=int(input("digite o segundl valor: "))
    
    if variavel == "+":
        resultado= (valor1 + valor2)
    elif variavel == "-":
        resultado = (valor1 - valor2)
    elif variavel == "*":
        resultado = (valor1 * valor2)
    elif variavel == "/":
        resultado = (valor1 / valor2)
    elif variavel == "**":
        resultado = (valor1 ** valor2)
    print(resultado)

    c = input("Deseja sair? (s/n)\n")
    if c == "s":
        calc = True
    
