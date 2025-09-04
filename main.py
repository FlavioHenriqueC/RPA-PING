import pandas as pd
import subprocess
import csv


# comando que lê o arquivo
df = pd.read_csv("maquinas.csv", sep=";")
resultados = []
# Supondo que exista uma coluna chamada "nome"
for nome in df["Nome"]:
    comando = f'ping {nome}'  # exemplo de comando
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)

    resultados.append([nome])

    df_resultados = pd.DataFrame(resultados, columns=["Maquina"])

    df_resultados.to_csv("resultado.csv", index=False, encoding="utf-8-sig")