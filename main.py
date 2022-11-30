#Aula 1
#Meu primeiro projeto Python!!

'''print() = comando de saida 
print("Hello world!")
Quando quiser guardar uma String!(frase)
nome = "Bruno Henrique"
idade = 21
print(nome)
print("minha idade é " +str(idade))'''

#Aula 2
'''nome = input("Digite seu nome: ")
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
  print("Seu gênero é feminino")'''

'''nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota: "))
if (nota==10):
  print(f"{nome} você é o bichão mesmo ")
elif (nota < 10 and nota >= 6):
  print("Você ficou na média")
else:
  print("Sua nota foi abaixo da média")'''
# Aula 3

'''contador = 1
while(contador <= 10):
  print(contador)
  contador = contador + 1'''

'''frutas = ["morango","laranja","maçã","manga"]'''
#print(frutas[2])
#print(len(frutas))
#frutas.append("manga")
'''i = 0
while (i<4):    
  print(frutas[i])
  i = i + 1'''
'''for frutas in frutas:
  print(frutas)'''

#criação de funções 

'''preco = 1999.90
imposto = preco * 0.05
print(imposto)

preco2 = 100
imposto2 = preco2 * 0.05
print(imposto2)'''

'''https://www.w3schools.com/python/python_functions.asp'''

def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.07
  return imposto

#Aqui é o uso... aqui é imposto a calcular.. e exibir na tela
preco = 299
imposto = calcular_imposto(preco)
print(imposto)

valores = [1.99,24.50,78.27,1515.5]
for valor in valores:
 print(f"O imposto de {valores} é {calcular_imposto(valor)}")
#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
poyatos = Pessoa(1, "Henrique Poyatos")
print(poyatos)

#Quero mostrar só o nome
print(poyatos.nome)

print("DAQUI PRA FRENTE É ACESSO AO BANCO...")

#Chama o objeto de banco de dados
db = Database()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)


#Criar um objeto com qualquer ator/atriz/diretor/diretora
novo = Pessoa(0, "Denzel Washington")

#Olha que simples...
novo = pessoaDAO.save(novo)

#consulta o banco de novo..
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)
#faz um ajuste estratégico no dao/PessoaDAO.py
from model.Pessoa import Pessoa 

class PessoaDAO:
  conexao = None
  cursor = None

  def __init__(self, con, cur):
    self.conexao = con
    self.cursor = cur

  def getAll(self, orderBy = False):
    sql = "SELECT id, nome FROM pessoa "
    if orderBy == True:
      sql = sql + " ORDER BY nome"
    
    try:
      self.cursor.execute(sql)
      resultado = self.cursor.fetchall()

      pessoas = []
      for linha in resultado:
        pessoa = Pessoa(linha[0], linha[1])
        pessoas.append(pessoa)

      return pessoas
    except Exception as e:
      return e

  #Função/método para inserir no banco.
  def save(self, pessoa):
    sql = "INSERT INTO pessoa (nome) VALUES (%s)"

    try:
      self.cursor.execute(sql, pessoa.nome)
      self.conexao.commit()
      pessoa.id = self.cursor.lastrowid 
      return pessoa
    except Exception as e:
      return e

  

 
 













