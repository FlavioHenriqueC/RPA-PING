import pandas as pd
import subprocess
import csv


# Lendo o CSV
df = pd.read_csv("maquinas.csv", sep=";")

# Supondo que exista uma coluna chamada "nome"
for nome in df["Nome"]:
    comando = f'ping {nome}'  # exemplo de comando
    subprocess.run(comando, shell=True)
