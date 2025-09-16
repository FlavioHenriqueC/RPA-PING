import pandas as pd
import subprocess
import csv

# Lê o arquivo com os nomes das máquinas
df = pd.read_csv("maquinas.csv", sep=";")



# Abre o arquivo CSV uma vez e escreve o cabeçalho
with open("resultado.csv", "w", newline='', encoding="utf-8-sig") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Maquina", "Status"])



# Processa cada máquina
for nome in df["Nome"]:
    comando = f'ping -n 4 {nome}'  # 4 tentativas no Windows
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)


    
    # Verifica status
    status = "Online" if resultado.returncode == 0 else "Offline"
    
    saida_ping = resultado.stdout
    print(saida_ping)
    print(f"Status: {status}")


    # Adiciona linha ao arquivo CSV

    with open("resultado.csv", "a", newline='', encoding="utf-8-sig") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, status])

print("Arquivo resultado.csv criado/atualizado com sucesso!")