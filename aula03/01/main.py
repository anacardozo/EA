import random

alunos = ["Rogério", "Ricardo", "Shimada", "Caio", "Camila", "Vitor", "Geovanna", "Renan", "Carlos", "Miguel", "Ana", "Sthevens", "Guilherme", "Raissa", "Matheus", "Felipe", "Endrew", "Arthur", "Gabriela", "Pedro"]

random.seed(2)

# sample - escolhe de forma aleatoria elementos de um determinado conjunto
amostra = random.sample(alunos, 3)

print(amostra)