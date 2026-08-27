import pandas as pd
import matplotlib.pyplot as plt

idades = [18, 19, 20, 21, 22, 25, 27, 30, 31, 35]
plt.hist(idades)
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.title("Distribuição das Idades")
plt.show()