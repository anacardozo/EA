import pandas as pd

notas = [
    7, 8, 6, 9, 7,
    5, 8, 7, 10, 6,
    8, 9, 7, 5, 6,
    8, 7, 9, 8, 10
]

# transforma em um vetor do tipo series
serie = pd.Series(notas)

# print(serie)

# calcula a frequência absoluta e ta ordenando pelo index (as notas nesse caso)
# print(serie.value_counts().sort_index())

# o sort_values ordena pela frequência
# print(serie.value_counts().sort_values())

# frequência relativa, para deixar em porcentagem tem que multiplicar por 100
# print(serie.value_counts(normalize=True) * 100)

# frequência acumulada
frequencia = serie.value_counts().sort_index()
frequencia_acumulada = frequencia.cumsum()

# tabela de frequencias
tabela = pd.DataFrame({
    "Frequencia": frequencia,
    "Frequencia_Relativa": frequencia / len(serie),
    "Frequencia_Acumulada": frequencia_acumulada
})

print(tabela)

