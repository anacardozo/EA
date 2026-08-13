import pandas as pd

Produtos = {
    "Produto" : ["Mouse", "Teclado", "Monitor", "Webcam", "Headset"],
    "Preco" : [85, 150, 980, 220, 320],
    "Quantidade" : [12,8,4,10,6]
}

df = pd.DataFrame(Produtos)

# quantos produtos existem
# print(len(df))

# qual possui o maior preço
# print(max(df['Preco']))

# qual possui o menor preço
# print(min(df['Preco']))

# qual a soma das quantidades
print(sum(df['Quantidade']))