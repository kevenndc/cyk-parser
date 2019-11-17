# Cria a matriz com a primeira fila já preenchida
def criarMatriz(palavra, gramatica):
  matriz = []
  for i in range(palavra.__len__()):
    arraySimbolo = []
    for j in range(palavra.__len__() - i):
      arraySimbolo.append([])
    matriz.append(arraySimbolo)

  for i in range(palavra.__len__()):
    simbolo = gramatica[palavra[i]]
    matriz[0][i] = simbolo
      
  return matriz

  
# Cria um diciionário com as producoes como chave e os simbolos geradores como valores
def criarGramatica(arquivo):
  producoes = arquivo.read().splitlines()
  gramatica = {}

  print('Gramatica:')
  for producao in producoes:
    print(producao)
    gerador = producao[:producao.index("=>")].strip()
    regras = []

    if('|' in producao):
      regras = producao[producao.index("=>") + 2:producao.__len__()].split(' | ')
    else:
      regras.append(producao[producao.index("=>") + 2:producao.__len__()])

    for i in range(0, regras.__len__()):
      regras[i] = regras[i].strip()

      if (regras[i] in gramatica.keys()):
        gramatica[regras[i]].append(gerador)
      else:
        gramatica.update({regras[i] : [gerador]})

  return gramatica

#Retorna o símbolo da combinação se encontrada
def testaCombinacao(a, b, gramatica):
  for g in a:
    for h in b:
      if((g+h) in list(gramatica.keys())):
        return gramatica.get(g+h)

  return []
  
#Mostra a tabela
def imprimeTabela(matriz, palavra):
  for i in range(matriz.__len__() - 1, -1, -1):
    print(matriz[i])
  print('--------------------------------------------------------------------------------------------------')
  print(list(palavra))
  print('--------------------------------------------------------------------------------------------------')

def cyk(palavra, gramatica, matriz):
  # print(matriz)
  n = matriz.__len__()
  resultado = []

  for l in range(2, n+1):
    for k in range(1, n-l+2):
      for j in range(1, l):
        resultado = testaCombinacao(matriz[j-1][k-1], matriz[l-j-1][k+j-1], gramatica)
        if (resultado):
          matriz[l-1][k-1] = resultado

  if(list(gramatica.values())[0][0] in matriz[n-1][0]):
    print('\nEssa palavra PERTENCE a gramatica.\n')
  else:
    print('\nEssa palavra NAO pertence à gramatica.\n')

  print('Tabela de derivacao:\n')
  imprimeTabela(matriz, palavra)
    

def init(arquivo):
  palavra = input("Digite a palavra que deverá ser testada na gramatica:")
  with open(arquivo) as arquivo:
    gramatica = criarGramatica(arquivo)
    # print(gramatica.keys())
    # print(gramatica.values())
    matriz = criarMatriz(palavra, gramatica)
    cyk(palavra, gramatica, matriz)