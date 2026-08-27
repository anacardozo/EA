import pandas as pd
import matplotlib.pyplot as plt

linguagens = [
        "Python",
        "JavaScript",
        "Python",
        "Java",
        "C#",
        "JavaScript",
        "Python",
        "TypeScript",
        "Java",
        "Python",
        "JavaScript",
        "C++",
        "Python",
        "JavaScript",
        "Java",
        "TypeScript",
        "Python",
        "C#",
        "JavaScript",
        "Python",
        "Java",
        "TypeScript",
        "C++",
        "JavaScript",
        "Python",
        "C#",
        "Java",
        "TypeScript",
        "C++",
        "JavaScript",
    ]


frequencia = pd.Series(linguagens)

# frequencia absoluta
fab = frequencia.value_counts()
# print("Frequência absoluta: ")
# print(fab)

# frequencia relativa
fr = (frequencia.value_counts(normalize=True) * 100) 
# print("Frequência relativa: ")
# print(fr)

# mais frequente
print("Linguagem mais frequente: ")
print(fab.idxmax(), )

tabela = pd.DataFrame({
    "F_absoluta": fab,
    "F_relativa": fr
})

# print(tabela)

# fab.plot(kind="bar")
# plt.title("Frequência de Linguagens")
# plt.xlabel(frequencia)
# plt.ylabel(linguagens)
# plt.show()