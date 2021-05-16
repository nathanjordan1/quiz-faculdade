#QUIZ RELACIONADO A 1º AULA DE DESENVOLVIMENTO DE SOFTWARE DA FACULDADE

print('''                       QUIZ    
===== PROCESSO DE DESENVOLVIMENTO DE SOFTWARE =====''')

print('''\n1) O que é um Software?

[ A ] Componente de um computador
[ B ] Programa de computador
[ C ] Linguagem Binária
[ D ] Linguagem de Programação\n''')

Resp1 = str(input("Insira sua resposta: ")).upper() #1º Resposta do Usuário

Cont = 0 
if Resp1 == "B": #1º Estrutura IF
    print('''\nResposta correta, o software é a conversão de uma linguagem de programação
para uma linguagem binária e se criando um programa\n''')
    Cont += 10
elif Resp1 == "A":
    print('''\nA resposta correta é 'B', um software é um programa que exerce
uma linguagem de programação convertida para uma linguagem binária\n''')
elif Resp1== "C":
    print('''\nA resposta correta é 'B', um software é um programa que exerce
uma linguagem de programação convertida para uma linguagem binária\n''')
TotCont = Cont
print("+10 Pontos")
print(f"Seus pontos são: {TotCont}\n")

print("================================================================")
    
print('''\n2) Quais são os modo de organização atual das linguagens?

[ A ] Orientada a Objeto
[ B ] Linguagem Binária
[ C ] Imperativo
[ D ] Linguagem Humana\n''')
    
Resp2 = str(input("Insira sua resposta: ")).upper() #2º Resposta do Usuário

Cont = TotCont #2º Estrutura IF
if Resp2 == "A":
    print('''\nResposta correta, atualmente as linguagens utilizam 
o meio de Orientada a Objeto para instruções compostas e organizadas\n''')
    Cont += 10
elif Resp2 == "B":
    print('''\nA resposta correta é "A", atualmente as linguagens utilizam 
o meio de Orientada a Objeto para instruções compostas e organizadas\n''')
elif Resp2 == "C":
    print('''A resposta correta é "A", atualmente as linguagens utilizam 
o meio de Orientada a Objeto para instruções compostas e organizadas\n''')
elif Resp2 == "D":
    print('''\nA resposta correta é "A", atualmente as linguagens utilizam 
a Orientada a Objeto para instruções compostas e organizadas\n''')
TotCont = Cont
print("+10 Pontos")
print(f"Seus pontos são {TotCont} pontos\n")

print("================================================================")

print('''\n3) Quais são as fases de um Processo de Desenvolvimento de Software?

[ A ] Requisitos, Homologação, Testes, Codificação, Projeto, Implatanção, Concepção, Manutenção e Análise
[ B ] Homologação, Requisitos, Codificação, Projeto, Concepção, Manutenção, Análise, Testes e Implantação
[ C ] Concepção, Requisitos, Projeto, Análise, Codificação, Testes, Implatanção, Homologação e Manutenção
[ D ] Concepção, Requisitos, Análise, Projeto, Codificação, Testes, Homologação, Implantação e Manutenção\n''')

Resp3 = str(input("Insira sua resposta: ")).upper() #3ºResposta do Usuário

Cont = TotCont #3º Estrutura IF
if Resp3 == "D":
    print("\nResposta correta, estas são as fases certas para um desenvolvimento de software\n")
    Cont += 10
elif Resp3 == "A":
    print('''\nA resposta correta é a "D"
Concepção, Requisitos, Análise, Projeto, Codificação, Testes, Homologação, Implantação e Manutenção\n''')
elif Resp3 == "B":
    print('''\nA resposta correta é a "D"
Concepção, Requisitos, Análise, Projeto, Codificação, Testes, Homologação, Implantação e Manutenção\n''')
elif Resp3 == "C":
    print('''\nA resposta correta é a "D"
Concepção, Requisitos, Análise, Projeto, Codificação, Testes, Homologação, Implantação e Manutenção\n''')
TotCont = Cont
print("+10 Pontos")
print(f"Seus pontos são {TotCont} pontos\n")

print("================================================================")
print('''\n4) Qual é a classificação de um software?

[ A ] Hardware, Software, Usuário e Sistema Operacional
[ B ] Usuário, Software, Sistema Operacional e hardware
[ C ] Hardware, Sistema Operacional, Software e Usuário
[ D ] Sistema Operacional, Hardware, Software e Usuário\n''')

Resp4 = str(input("Insira sua resposta: ")).upper()

Cont = TotCont #4º Estrutura IF
if Resp4 == "C":
    print("\nResposta Correta\n")
elif Resp4 == "A":
    print('''\nA resposta correta é a "C"\nHardware, Sistema Operacional, Software e Usuário\n''')
elif Resp4 == "B":
    print('''\nA resposta correta é a "C"\nHardware, Sistema Operacional, Software e Usuário\n''')
elif Resp4 == "D":
    print('''\nA resposta correta é a "C"\nHardware, Sistema Operacional, Software e Usuário\n''')
Cont = TotCont
print("+10 pontos")
print(f"Seus pontos são {TotCont} pontos\n")

if TotCont > 0:
    print("================================================================")
    print("                           PARABÉNS                             ")
    print(f"                  Você conseguiu {TotCont} pontos!             ")
else:
    print("================================================================")
    print("                           Tente Novamente                      ")
    print(f"                      Você conseguiu {TotCont} pontos!         ")