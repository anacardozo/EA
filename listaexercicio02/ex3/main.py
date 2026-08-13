import pandas as pd

dados = {
    "Nome": ["Ana", "Nayara", "Carla", "Luan", "Pedro", "Julia", "João", "Mariele", "Geovanna", "Vitor"],
    "Idade": [19,15,20,14,18,23,20,18,21,20],
    "Nota": [9,8,9,10,7,6,3,7,10,10]
}

df = pd.DataFrame(dados)

# print(df["Nota"].mean())

# print(df.iloc[df["Nota"].idxmax()])

# print(df.iloc[df["Nota"].idxmin()])

# print(df.sort_values("Nota"))

print(df[df["Nota"] >= 7])