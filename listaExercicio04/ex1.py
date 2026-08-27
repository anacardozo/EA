import pandas as pd
import matplotlib.pyplot as plt

notas = [
 7, 8, 6, 9, 7, 5, 8, 7, 10, 6, 8, 9, 7, 5, 6, 8, 7, 9, 8, 10
]

serie = pd.Series(notas)

fab = serie.value_counts()

fr = serie.value_counts(normalize=True)

fac = fab.cumsum()

tabela = pd.DataFrame({
    "F_absoluta": fab,
    "F_relativa": fr,
    "F_acumulada": fac
})

print(tabela)

# grafico de barras
# fab.plot(kind="bar")


# plt.title("Frequencia das Notas")
# plt.xlabel("Notas")
# plt.ylabel("Frequencia")
# plt.show()

# gráfico de pizza
# fab.plot(
#  kind="pie",
#  autopct="%1.1f%%"
# )
# plt.title("Distribuição das Notas")
# plt.ylabel("")
# plt.show()