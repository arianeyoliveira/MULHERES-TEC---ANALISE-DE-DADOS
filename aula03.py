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
    print("ACESSO NEGADO!\nVOCÊ É MENOR DE IDADE")19