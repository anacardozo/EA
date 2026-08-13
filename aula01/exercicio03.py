import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Produto" : ["Pão", "Arroz", "Macarrão"],
    "Preco" : [10.0, 23.45, 2.5],
    "Quantidade" : [2,3,1]
}

df = pd.DataFrame(dados)

# print(df)

plt.bar(
    df["Produto"], df["Preco"],
    width=0.2,
    color="red"
)

plt.show()

plt.plot(
    df["Produto"], df["Quantidade"],
    color="#a5ba00"
)

plt.show()

# plt.bar(df["Preco"], df["Quantidade"])

# plt.show()