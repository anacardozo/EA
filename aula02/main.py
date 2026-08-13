# import pandas as pd

# dados = {
#     "Nome": ["Ana", "Carlos", "João", "Felipe", "Marcos", "José"],
#     "Idade": [20, 25, 63, 10, 58, 25],
#     "Nota": [10,9,9,8,7,3]
# }

# df = pd.DataFrame(dados)

# shape e columns são atributos, armazena os dados que representa o tamanho do dataframe ,as linhas e colunas. LxC
# columns -> retorna as colunas e os tipos
# métodos são aqueles que possuem um nome e parenteses na frente = nome()
# atributo -> nomeatributo
# objeto - instancia de uma classe para que voce possa usar ela

# print(df.columns)

# print(df["Nome"])

# print(df[["Nome", "Nota"]])

# seleciona a primeira linha
# o numero entre os colchetes, fala qual linha ele vai puxar
# print(df.iloc[0])

# selecionando varias linhas
# print(df.iloc[0:2])

# selecionando uma celula
# print(df.iloc[4,2])

# METODOS DO PANDAS

# puxando a maior idade
# print(df["Idade"].max())

# criando uma nova coluna
# df["Nota_Final"] = df["Nota"] + 1.3

# print(df)

# import pandas as pd

# dados = {
#     "Produto": ["Mouse", "Teclado", "Monitor", "Gabinete"],
#     "Preço": [80, 50, 800, 250],
#     "Quantidade": [10, 50, 15, 25]
# }

# df = pd.DataFrame(dados)

# df["Valor_total"] = df["Preço"] * df["Quantidade"]

# ordenando dados
# ascending = True -> crescente
# ascending = False -> decrescente

# print(df.sort_values("Preço"))

# representa com true os que estão nessa condição
# print(df["Quantidade"] < 20)

# retorna as informações que estão dentro dessa condição
# print(df[df["Quantidade"] < 20])

# print(df[(df["Quantidade"] > 7) & (df["Preço"] < 100)])


# ARQUIVO CSV

import pandas as pd

df = pd.read_csv("dados.csv")

print(df)

print(df.describe())