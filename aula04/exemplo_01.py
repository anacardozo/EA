import pandas as pd

# transformando um arquivo csv em dataframe
tabela = pd.read_csv('dados.csv')

serie = tabela["estado"]

# print(serie.value_counts(normalize=True))

frequencia = serie.value_counts()
frequencia_acumulada = frequencia.cumsum()

tabela = pd.DataFrame({
    "Frequenica": frequencia,
    "Frequencia_Relativa": frequencia / len(serie),
    "Frequencia_Acumulada": frequencia_acumulada
})
 
print((tabela))
 