# analisando conjunto de dados com pandas
# nosso primeiro DataFrame

import pandas as pd

import matplotlib.pyplot as plt

dados = {
    "Aluno": ["Rogério", "Matheus", "Camila", "Geovana"],
    "Nota": [8,5,9,6]
}

df = pd.DataFrame(dados)

# exibe algumas informações do DataFrame, exibe os dados, não retorna nada
# df.info()
# retorna uma descrição, precisa de um print
# print(df.describe())

# serve para saber se o dataframe conseguiu carregar os dados
# print(df.head())

# define as barras de um gráfico
# o primeiro é o eixo x e o segundo o eixo y
plt.bar(df["Aluno"],df["Nota"])

plt.show()