# armazenando condicoes
ingressos = 50
compradores = 250
tem_ingresso_sulficiente = (ingressos >= compradores)
print(tem_ingresso_sulficiente)

#dados
nome = "Iago Alan"
idade = 20
peso = 60.5
print(nome)
print(idade)
print(peso)

nome = input ("Digite seu nome:")
idade = int ( input ("Digite sua Idade:") ) #int - numeros inteiros #inp - para digitar algo
peso = float ( input ("Digite seu Peso:") ) #float - numeros decimais
print(nome)
print(type (idade) )
print(type (peso) )

#Operadores

soma = 1 + 1 #Soma dos Doces
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2
print("doces", soma) #Primeiro STRING(nome que sera dado), depois variavel
print("multiplicacao", multiplicacao)
print("divisao", divisao)
print("potencia", potencia) 



#Se você pode entrar na balada ou não  (IF/ELSE)
Idade = int( input ("Informe sua Idade Para a Entrada:") )

if idade >= 18: 
    print("PERMITIDO!")
else: 
  print("BLOQUEADO")
  

  #Salários - Junior, Pleno, Senior (IF,ELSE,ELIF)
  
  salario = float(input ("Informe seu salário:") )

  if salario <= 3000: 
     print("Programador Júnior")
  elif salario > 3000 and salario <= 6000:
     print("Programador Pleno")
  elif salario > 6000 and salario <= 15000:
     print("Programador Sênior")
  else: 
     print("Progrador Gerente")
