import pandas as pd

dados = {
    "Nome" : ["João", "Maria", "Pedro", "Ana", "Lucas", "Julia", "Carlos", "Fernanda"],
    "Idade" : [18,20,19,22,21,18,23,20]
}

df = pd.DataFrame(dados)

# exiba o dataframe
# print(df)

# mostre a cinco primeiras linhas
# print(df.head(5))

# exiba as informações do dataframe
# print(df.info())

# exiba o resumo estatistico
print(df.describe())