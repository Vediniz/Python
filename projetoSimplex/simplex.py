# -*- coding: utf-8 -*-

import math
import pandas as pd

dic_global = None
columns_global = None
resp_global = None
linhas_global = None
sinalgeral_global = None

def receber_restricoes():
  numeroRestricoes = int(input("Digite o numero de Restriçoes: "))
  numeroVariaveis = int(input("Digite o numero de variaveis por restrição: "))
  resp = str(input("Deseja Maximizar ou Minimizar[max/min]: "))
  sinalgeral = str(input("Digite o sinal geral: "))
  print("-="*40)

  #Criando dic com lines
  columns = "['z',"
  lines = "['z',"

  for i in range(numeroVariaveis):
        columns += (f"'x{i+1}',")

  for i in range(numeroRestricoes):
        columns += (f"'f{i+1}',")
        lines += (f"'l{i+1}',")

  columns += "'b']"
  lines += "]"

  columns = eval(columns)
  lines = eval(lines)

  dic = {}.fromkeys(lines, None)


  #Alimentando dic
  for j in range(numeroRestricoes+1):
        sinal = None 
      
        if j == 0:
          variavel = "[1,"
          for i in range(numeroVariaveis): 
            variavel += str(input(f"Digite x{i+1} de z: ")) + ","
          for k in dic.keys():
            if k != "z":
              variavel += "0," 
          variavel += "0,"
          print("-="*40)
        
      
        if j != 0:
          variavel = "[0,"
          
          for i in range(numeroVariaveis):            
            variavel += str(input(f"Digite x{i+1} da {j}º restrição: ")) + ","
            
          for k in dic.keys():
            if k != "z":
              if (f"l{j}") == k:
                variavel += "1,"
              else:
                variavel += "0,"

          variavel += str(input(f"Digite o valor de b de l{j}: ")) + ","
          print("-="*40)
        
        #final base
        variavel += "]"
        variavel = eval(variavel)
        
        for v in range(len(variavel)):
                float(variavel[v])
        
        if j == 0:
                dic["z"] = variavel
        else:
                dic[f"l{j}"] = variavel 
  
  if sinalgeral == ">=":
    if resp == "max":
      resp = "min"
    else:
      resp = "max"
    
    columnsT = "['z',"
    linesT = "['z',"

    for i in range(numeroRestricoes):
        columnsT += (f"'x{i+1}',")

    for i in range(numeroVariaveis):
        columnsT += (f"'f{i+1}',")
        linesT += (f"'l{i+1}',")

    columnsT += "'b']"
    linesT += "]"

    columnsT = eval(columnsT)
    linesT = eval(linesT)

    dicT = {}.fromkeys(linesT, None)

    cont = 0
    for j in range(numeroVariaveis+1):
        if j == 0:
            if resp == "min":
              linha_temp = "[1,"
              for k in range(numeroRestricoes+1):
                  if k != 0:
                    linha_temp += str(float(dic[f"l{k}"][-1])*(1))  + ","
              for k in dicT.keys():
                  if k != "z":
                      linha_temp += "0," 
              linha_temp += "0"
              linha_temp += "]"
            else:
              linha_temp = "[1,"
              for k in range(numeroRestricoes+1):
                  if k != 0:
                    linha_temp += str(dic[f"l{k}"][-1])  + ","
              for k in dicT.keys():
                  if k != "z":
                      linha_temp += "0," 
              linha_temp += "0"
              linha_temp += "]"
        else:
            cont+=1
            linha_temp = "[0,"
            for k in range(numeroRestricoes+1):
                if k != 0:
                  linha_temp += str(dic[f"l{k}"][cont])  + ","
            for k in dicT.keys():
                if k != "z":
                  if (f"l{j}") == k:
                    linha_temp += "1,"
                  else:
                    linha_temp += "0,"
            if resp == "min":
              linha_temp += str(float(dic["z"][(cont)])*(-1))
              linha_temp += "]"
            else:
              linha_temp += str(dic["z"][(cont)])
              linha_temp += "]"
        
        
        linha_temp = eval(linha_temp)

        for v in range(len(linha_temp)):
            float(linha_temp[v])
            
        if j == 0:
            dicT["z"] = linha_temp
        else:
            dicT[f"l{j}"] = linha_temp
    columns = columnsT
    dic = dicT
    lines = linesT

  return dic, columns, resp, lines, sinalgeral

def criar_df(dic, columns): 
  df = pd.DataFrame(dic, columns).transpose()
  df = df.astype(float)

  return df

def max_or_min(resp): 
    
  if resp == 'min': 
    pass
  elif resp == 'max': 
    dic_global['z'] = list(map(lambda x: x * (-1), dic_global['z']))
    dic_global['z'][0] = (dic_global['z'][0] * (-1))
  return resp

def encontrar_menor_valor(z, df): 
 
    return min(z)

def descobrir_linha_pivo(df):
  keys = list(df.keys())
  posic = None
  menor = 2147483647

  for i in range(1, len(df)):
    valor = df['b'][f'l{i}'] / df[keys[pos]][f'l{i}']
    

    if valor < menor and valor > 0: 
      menor = valor
      posic = f'l{i}'

  return posic, keys[pos]

def selecionar_pivo(df, linha, pos): 
  pivo = df[linha][pos]

  return pivo

def criar_linha_pivo(df, linha, pivo, columns):
  nlp = []
  for i in columns:
    nlp.append( df[i][linha_pivo]/selecionar_pivo(df,coluna_pivo, linha_pivo))

  cont = 0
  for k in columns:    
    df[k][linha_pivo] = nlp[cont]
    cont += 1

  return nlp

def modificar_linhas():
  indice = list(df.index)
  indice.pop(indice.index(linha_pivo))
  
  nova_linha = []
  for i in indice:
    for j in range(len(nlp)):
        nova_linha.append( (nlp[j] * ((df[coluna_pivo][i])*(-1))))
    cont = 0
    for k in columns_global:  
      df[k][i] = nova_linha[cont] + df[k][i]
      cont += 1

    nova_linha = []



dic_global,columns_global,resp_global,linhas_global, sinalgeral_global = receber_restricoes()
max_or_min(resp_global)

df = criar_df(dic_global, columns_global)


while True:
  print("-="*40)
  print(df)
  z = []
  for i in columns_global:
    z.append(df[i]['z'])
  df_temp = pd.DataFrame(z)
  df_temp = df_temp.astype(float)
  df_temp = df_temp[0].tolist()
  df_temp_b = encontrar_menor_valor(df_temp, df)

  if df_temp_b < 0:
    pos = df_temp.index(df_temp_b) 
    linha_pivo = descobrir_linha_pivo(df)[0]
    coluna_pivo = descobrir_linha_pivo(df)[1]
    pivo = selecionar_pivo(df, coluna_pivo, linha_pivo)
    nlp = criar_linha_pivo(df, linha_pivo, pivo, columns_global)
    modificar_linhas()
  else:
    break

print("-="*40)
print("Solução Ótima: ")
print(df)
print("-="*40)

if sinalgeral_global == "<=":
  ii = ""
  jj = ""
  for i in df.keys():
    ii = "z"
    jj = "l1"
    if i == "z":
      print("Valor de z:")
      print("  z: " + str(df["b"]["z"]))
      print("Variáveis Básicas:")
    else:
      bool = True
      for j in linhas_global:
        if j != "z":
          if df[i][j] != 0 and df[i][j] != 1:
              bool = False
          if df[i][j] == 1: 
              ii = i
              jj = j
      if df[ii][jj] == 1 and bool:
        print(f"  {i}: " + str(df["b"][jj]))
else: 
  for i in df.keys():
      if i[0] == "f":
        print(f"y{(i.split('f')[1])}: " + str(df[i]["z"]))
        
