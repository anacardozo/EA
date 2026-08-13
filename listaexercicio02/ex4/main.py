import pandas as pd

dados = {
    "Produto": ["Mouse", "Teclado", "Monitor", "Gabinete", "Mesa", "Cadeira", "HeadSet", "Microfone"],
    "Categoria": ["Periférico", "Periférico", "Vídeo", "Periférico", "Movel", "Movel", "Periférico", "Periférico"],
    "Preço": [80, 50, 800, 250, 150, 435, 100, 950],
    "Quantidade": [10, 50, 15, 25, 2, 4, 8, 1]
}

df = pd.DataFrame(dados)

df["Valor_Total"] = df["Preço"] * df["Quantidade"]

# print(df.sort_values("Preço"))

# print(df[df["Preço"] > 100])

print(df[df["Quantidade"] < 10])