import pandas as pd

tempos =  pd.Series([120, 130, 125, 140, 120, 150, 125, 120, 135, 125])

media = tempos.mean()

print("Média:")
print(media)

mediana = tempos.median()

print("Mediana:")
print(mediana)

moda = tempos.mode()

print("Moda:")
print(moda)