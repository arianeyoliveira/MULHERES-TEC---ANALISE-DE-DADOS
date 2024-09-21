"""print("Qual a sua idade?")
idade = int(input())

if idade >= 18:
    print("ACESSO LIBERADO! BOA FESTA")
else:
    print("ACESSO NEGADO! VOCÊ É MENOR DE IDADE")"""

    # CODIGO PARA LIBERAR ACESSO SOMENTE PARA MAIORES DE 19 ANOS

"""print("Qual a sua idade?")
idade = int(input())

if idade < 18:
    print("ACESSO NEGADO! VOCÊ É MENOR DE IDADE")

elif idade == 18:
    print("VOCÊ ESTÁ QUASE LÁ!MAIS UM NAO E VOCÊ TERÁ ACESSO!")
    
else:
    print("ACESSO LIBERADO! BOA FESTA!")"""


# CÓDIGO PARA VERIFICAR SE ALUNO FOI APROVADO!

"""print("Digite a nota do primeiro bimestre:")
B1 = float(input())                          # aqui pedimos para o codigo entender que o valor que pedimos para o usuario digita, seja interpretado como valor inteiro
print("Digite a nota do segundo bimestre: ")
B2 = float(input())
print("Digite a nota do terceiro bimestre:")
B3 = float(input())
print("Digite a nota do quarto bimestre: ")
B4 = float(input())
media = (B1 + B2 + B3 + B4) / 4
print("a media e ", media)"""


"""if media >= 7:
    print("APROVADO!")

elif media < 7 = 5:
    print("RECUPERAÇÃO!")

else:
    print("REPROVADO!")


print("Qual seu gênero ? (F OU M)")                  #Perguntando ao usuário o seu gênero
genero = input().upper()
print("Qual município você mora? ")                  # Criando variavel gener
municipio = input().lower()

if genero == "F" and municipio  == "rio de janeiro":
    print("VOCÊ PODE PARTICIPAR DO MULHERES TECH")
else:
    print("VOCÊ NÃO PODE PARTICIPAR DO MULHERTES TECH")"""






# CÓDIGO PARA LIBERAR O ACESSO DE UM FILME ONDE SÓ É PERMITIDO A ENTRADA DE MAIORES DE 18 ANOS E ADOLESCENTES COM 16 ANOS OU MAIS, ACOMPANHADO DE UM RESPOSNÁVEL. CÓDIGOS: SRT/ INT / FLOART 


print("*" *30 , "BEM VINDO AO CINEMA CINÉPOLIS", "*" * 30 )
print(" ")
print("Qual sua idade?")
idade = int(input())

if idade >= 18:
    print("ACESSO LIBERADO! BOM FILME\nBOM FILME\nAPROVEITE NOSSOS COMBOS DE PIPOCA COM REFRIGERANTE DE 1L")

elif idade >= 16:
    print("O FILME SELECIONADO É PARAM MAIORES DE 18 ANOS\nPARA ACESSAR AS DEPENDÊNCIAS DO CINEMA,VOCÊ ESTÁ ACOMPANHADO DE UM RESPONSÁVEL?")
    responsavel = input().upper()
    if responsavel == "SIM":
        print ("ACESSO LIBERADO! BOM FILME\nAPROVEITE NOSSOS COMBOS DE PIPOCA.") 
    else: 
        print("VOCÊ SO PODE VER O FILME ACOMPANHADO DE UM RESPONSÁVEL")

else:
    print("ACESSO NEGADO!\nVOCÊ É MENOR DE IDADE")