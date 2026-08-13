import pandas as pd

dados = {
    "Produto": ["Mouse", "Teclado", "Monitor", "WebCam", "Headset"],
    "Categoria": ["Periférico", "Periférico", "Vídeo", "Vídeo", "Áudio"],
    "Preço": [80, 120, 900, 250, 300],
    "Quantidade": [10, 8, 4, 6, 5]
}

df = pd.DataFrame(dados)

df["Valor_Estoque"] = df["Preço"] * df["Quantidade"]

# print(df)

# print(df.iloc[df["Valor_Estoque"].idxmax()])

# print(df.iloc[df["Preço"].idxmin()])

print(df["Valor_Estoque"].sum())