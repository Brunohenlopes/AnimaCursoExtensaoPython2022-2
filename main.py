#Aula 1
# Meu primeiro projeto Python!!
#
# print() = comando de saida 
#print("Hello world!")
# Quando quiser guardar uma String!(frase)
#nome = "Bruno Henrique"
#idade = 21
#print(nome)
#print("minha idade é " +str(idade))
#Aula 2
nome = input("Digite seu nome: ")
print(f"Boa noite {nome}")
idade = int(input("Digite sua idade:"))
print("Sua idade é {}" .format (idade))
soma = idade*2
print("idade ao dobro é: {}".format(soma))
if (idade >= 18):
  print("Você pode dirigir ou  beber")

 
else:
  print("Você não pode beber e nem dirigir")
genero = input("Informe seu gênero: \nM:Masculino e F=Femnino: ")
if idade >= 18 and genero == "M":
  print("Você precisa prestar serviço militar obrigatório")
else:
  print("Seu gênero é feminino")
  
 
 













