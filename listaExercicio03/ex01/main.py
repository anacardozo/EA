import pandas as pd

alunos = pd.DataFrame({
    "Nome":[ "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena","Igor", "Julia", "Lucas", "Marina"],
    "Nota": [8, 7, 9, 6, 10, 8, 7, 9, 5, 8, 6, 10]
})

df = pd.DataFrame(alunos)

# verificando o tamanho da população
# print(df.shape)

# calculando a media da população

media_populacao = df["Nota"].mean()

print(f"A média da população é: {media_populacao}")

# retirando uma amostra
amostra = df.sample(n=5, random_state=15)

# media da amostra
media_amostra = amostra["Nota"].mean()

print(f"A média da amostra é: {media_amostra}")

# comparação das medias
print(f"A comparação das médias é: {media_populacao - media_amostra}")

# amostra com 8 e repetindo as outras coisas
amostra2 = df.sample(n=8, random_state=15)

media_amostra2 = amostra2["Nota"].mean()

print(f"A média da amostra é: {media_amostra}")

print(f"A comparação das médias é: {media_populacao - media_amostra2}")