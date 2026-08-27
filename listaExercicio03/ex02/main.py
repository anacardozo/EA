import pandas as pd

alunos = {
    "Nome": [
        "Ana", "Bruno", "Carlos", "Daniela", "Eduardo",
        "Fernanda", "Gabriel", "Helena", "Igor", "Julia",
        "Lucas", "Marina", "Nicolas", "Olivia", "Pedro",
        "Rafaela", "Samuel", "Tatiane", "Victor", "Yasmin",
        "Arthur", "Beatriz", "Caio", "Larissa", "Matheus",
        "Nicole", "Rafael", "Sofia", "Thiago", "Valentina"
    ],
    "Notas": [
        8.5, 7.0, 9.0, 6.5, 10.0,
        8.0, 7.5, 9.0, 5.5, 8.5,
        6.0, 10.0, 7.0, 8.0, 9.5,
        7.5, 6.5, 8.5, 5.0, 9.0,
        8.0, 7.5, 9.5, 6.0, 8.5,
        7.0, 9.0, 8.0, 6.5, 10.0
    ],
    "Idade": [
        18, 19, 20, 18, 21,
        19, 20, 18, 22, 19,
        21, 20, 18, 19, 22,
        20, 21, 18, 23, 19,
        20, 18, 21, 19, 22,
        20, 18, 21, 19, 20
    ]
}

df = pd.DataFrame(alunos)

# calcule a media da população
media_populacao = df["Idade"].mean()

print(f"A media da população é: {media_populacao}")

# selecione aleatoriamente 5 alunos
amostra1 = df.sample(n=5, random_state=15)

# calcule a media da amostra
media_amostra1 = amostra1["Idade"].mean()

print(f"A media da primeira amostra é: {media_amostra1}")

# selecione aleatoriamente 10 alunos
amostra2 = df.sample(n=10, random_state=15)

# calcule a media da amostra
media_amostra2 = amostra2["Idade"].mean()

print(f"A media da segunda amostra é: {media_amostra2}")

# compare os resultados

# comparando media população com a primeira amostra
print(f"A comparação da primeira amostra é: {media_populacao - media_amostra1}")

# comparando media população com a segunda amostra
print(f"A comparação da segunda amostra é: {media_populacao - media_amostra2}")