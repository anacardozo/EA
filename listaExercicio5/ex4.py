import pandas as pd
import numpy as np

tempos = [100,200,500]
qts = [500,300,200]


m_ponderada = np.average(
    tempos,
    weights=qts
)

print("Média ponderada dos tempos de requisição:")
print(m_ponderada)

# desenvolvendo em zip

numerador = sum(
    tempos * qts
    for tempos, qts in zip(tempos,qts)
)