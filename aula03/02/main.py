import pandas as pd

df = pd.read_csv("dados.csv")

# print(df.shape) -. linhas e colunas

# print(df.head()) -> prévia do dataframe

# criando uma amostra com 50 elementos
# seleciona aleatoriamente 50 elementos
# amostra = df.sample(n=50)
# print(amostra)

# selecionando a mesma amostra
# amostra = df.sample(n=10, random_state=15)
# print(amostra.shape)


# CALCULANDO MÉDIA
amostra = df.sample(n=100, random_state=15)
mediaPop = df["idade"].mean()
print(f"Média população: {mediaPop}")

mediaAmo = amostra["idade"].mean()
print(f"Média da amostra: {mediaAmo}")

print(f"Erro amostral: {mediaPop - mediaAmo}")