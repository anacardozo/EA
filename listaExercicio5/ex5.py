import pandas as pd
import matplotlib.pyplot as plt

Linguagens = ['Python', 'Java', 'Python', 'JavaScript', 'Python', 'C#', 
'Java', 'Python', 'C#', 'Python']

# 1
serie = pd.Series(Linguagens)

# 2.
freq = serie.value_counts()
print("Frequência absoluta")
print(freq)
print("Moda")
moda = serie.mode()
print(moda)

# 3. 
freq.r = serie.value_counts(normalize=True)
print("Frequência relativa")
print(freq.r)

# 4.
freq.plot(kind="bar")
plt.title("preferencia de linguagem")
plt.show()