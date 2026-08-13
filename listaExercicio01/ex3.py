import pandas as pd

dados = {
    "num" : [12,15,18,40,32,11,9,28,37,15]
}

df = pd.DataFrame(dados)

# quantidade de elementos
# print(len(df))

# soma
# print(sum(df['num']))

# media
# print(df['num'].mean())

# maior
# print(df['num'].max())

# menor
# print(df['num'].min())

# ordem decrescente
df_ordenado = df.sort_values(by='num', ascending=False)

print(df_ordenado)
