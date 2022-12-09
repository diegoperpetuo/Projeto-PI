import matplotlib.pyplot as plt
import json
import seaborn as sns
import pandas as pd

def age_graph(file='data.json'):
  ages = []
  with open(file, 'r') as f:
      data = json.load(f)
      for i in range(len(data['data'])):
        ages.append(data['data'][i]['idade'])

      plt.hist(ages, color = 'green',
            histtype = 'bar', rwidth = 0.8) 
      plt.xlabel('age')
      plt.ylabel('No. of people')
      plt.show()
     
def gender_graph(title = 'Gráfico de genêro', file='data.json'):
  with open(file, 'r') as f:
      data = json.load(f)
      count_m = 0
      count_f = 0
      count_outros = 0
      for i in range(len(data['data'])):
        if 'm' == data['data'][i]['genero']:
          count_m+= 1
        elif 'f' == data['data'][i]['genero']:
          count_f += 1
        elif 'outros' == data['data'][i]['genero']:
          count_outros += 1

      labels='Masculino','feminino', 'Outros'
      size =[count_m, count_f, count_outros]
      color_list = ['pink','lightblue', 'red']
      figl, axl = plt.subplots()
      axl.pie(size,labels=labels,shadow = True,autopct='%1.1f%%', startangle = 90,colors=color_list)
      axl.axis('equal')
      axl.set_title(title,fontsize = 14)
      sns.set(style="whitegrid")
      sns.set_color_codes("pastel")
      plt.show()


def pizza_graph(title, data1, data2):

  labels='sim','não'
  size =[data1, data2]
  color_list = ['pink','lightblue']
  figl, axl = plt.subplots()
  axl.pie(size,labels=labels,shadow = True,autopct='%1.1f%%', startangle = 90,colors=color_list)
  axl.axis('equal')
  axl.set_title(title,fontsize = 14)
  sns.set(style="whitegrid")
  sns.set_color_codes("pastel")
  plt.show()

def yes_no_data(title, dta, file='data.json'):
  with open(file, 'r') as f:
      data = json.load(f)
      count_yes = 0
      count_no = 0
      for i in range(len(data['data'])):
        if 's' == data['data'][i][dta]:
          count_yes+= 1
        else:
          count_no += 1
      pizza_graph(title, count_yes, count_no)

def write_data_json(data, file='data.json'):
    with open(file, "w+") as f:
        json.dump(data, f, indent=4)
         
def update_data_json(dados, file='data.json'):
    with open(file, 'r+') as f:
        data = json.load(f)
        temp = data['data']
        temp.append(dados)
        write_data_json(data)
        
def read_data_json(file='data.json'):
    df = pd.read_json(file)
    if len(df) != 0:
      print(df)
    else:
      print("adicione dados!")

def individual_data(file='data.json'):
    nome = str(input("informe o nome que gostaria de procurar: "))
    sobrenome = str(input("informe o sobrenome que gostaria de procurar: "))
    with open(file, 'r') as f:
        data = json.load(f)
        for i in range(len(data['data'])):
            if nome == data['data'][i]['nome']:
              if sobrenome == data['data'][i]['sobrenome']:
                print(data['data'][i])
            else:
              print('Digite o nome corretamente!')

def graphics(resp):
   
    if resp == 1:
      yes_no_data('Discriminação por raça', 'pergunta_1')
    elif resp == 2:
      yes_no_data('Discriminação por religião', 'pergunta_2')
    elif resp == 3:
      yes_no_data('Discriminação por gênero', 'pergunta_3')
    elif resp == 4:
      yes_no_data('Discriminação por sexualidade', 'pergunta_4')
    elif resp == 5:
      yes_no_data('Discriminação no ambiente de trabalho/acadêmico', 'pergunta_5')
    elif resp == 6:
      yes_no_data('Acesso a diversos locais', 'pergunta_6')
    elif resp == 7:
      yes_no_data('Dedicação de tempo', 'pergunta_7')
    elif resp == 8:
      gender_graph('Gráfico de genêro')
    elif resp == 9:
      age_graph()
    

def statistics_menu():
  num = 0
  while (num != 10):
    print('Informe a porcentagem que gostaria de visualizar: \n')
    print('(1) Discriminação por raça \n')
    print('(2) Discriminação por religião \n')
    print('(3) Discriminação por gênero \n')
    print('(4) Discriminação por sexualidade \n')
    print('(5) Discriminação no ambiente de trabalho/acadêmico \n')
    print('(6) Acesso a diversos locais \n')
    print('(7) Dedicação de tempo \n')
    print('(8) Gênero \n')
    print('(9) Idade \n')
    print("(10) Sair \n")

    num = int(input())
    if num == 10:
      break

    graphics(num)

def dados_de_pesquisa():
  
  nome = str(input("Digite seu nome:" )).lower()
  sobrenome = str(input("Digite seu sobrenome:" )).lower()
  idade = int(input("Digite sua idade:" ))
  gen = str(input("Informe seu gênero(M/F/Outros):" )).lower()
  pergunta_1 = str(input("Voce já se sentiu discriminado pela sua raça?(S/N)")).lower()
  pergunta_2 = str(input("Voce já se sentiu discriminado pela sua religião?(S/N)")).lower()
  pergunta_3 = str(input("Voce já se sentiu discriminado pelo seu gênero?(S/N)")).lower()
  pergunta_4 = str(input("Voce já se sentiu discriminado pela sua sexualidade?(S/N)")).lower()
  pergunta_5 = str(input("Voce já se sentiu oprimido no ambiente de trabalho ou acadêmico?(S/N)")).lower()
  pergunta_6 = str(input("Voce consegue acessar diversos locais quando precisa?(S/N)")).lower()
  pergunta_7 = str(input("Voce consegue dedicar tempo ao lazer e descanso?(S/N)")).lower()
  print()

  dict = {
    "nome": nome,
    "sobrenome": sobrenome, 
    "idade": idade,
    "genero":gen, 
    "pergunta_1": pergunta_1,
    "pergunta_2": pergunta_2,
    "pergunta_3": pergunta_3,
    "pergunta_4": pergunta_4,
    "pergunta_5": pergunta_5,
    "pergunta_6": pergunta_6,
    "pergunta_7": pergunta_7
  } 

  update_data_json(dict) 

def create_json():
  list = {'data': []}
  with open('data.json', "w+") as file:
    json.dump(list, file, indent=4)

create_json()

var = ''

while ((var != 'e') and (var != 'n')):
  print("(a) Responder a pesquisa \n")
  print("(b) Listar dados dos repondentes\n")
  print("(c) Listar dados individuais\n")
  print("(d) Listar estatística\n")
  print("(e) Fim \n")

  var = str(input()).lower()

  if var == 'a':

    dados_de_pesquisa()

  elif var == 'b':

      read_data_json()

  elif var == 'c':

    individual_data()

  elif var == 'd':
      statistics_menu()

  elif var == 'e':
    print('Fim do programa :)')
    break

  else:
    print("Escolha uma letra válida!")
  
  print("Gostaria de realizar mais alguma operação? (s/n)")

  var = str(input()).lower()

  if var == 'n':

    print('Fim do programa :)')
