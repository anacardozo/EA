import pandas as pd

dados = {
    "Produto": ["Mouse", "Teclado", "Monitor", "WebCam", "Headset"],
    "Categoria": ["Periférico", "Periférico", "Vídeo", "Vídeo", "Áudio"],
    "Preço": [80, 120, 900, 250, 300],
    "Quantidade": [10, 8, 4, 6, 5]
}

df = pd.DataFrame(dados)

# print(df)

# print(df.shape)

# df.info()

# print(df.describe())

# print(df[["Produto", "Preço"]])

# comece no indice 0 e termine antes do indice 2
# print(df.iloc[0:2])

# idxmax - pega o maior valor
print(df.iloc[df["Preço"].idxmax()])

# print(df["preço"].idxmax()) #-> mostra a linha do indice que o preço é o maior (o valor da linha)