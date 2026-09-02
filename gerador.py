import random
import csv

def gerar_aposta():
    id_aposta = f"AP-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))}"
    qtd_numeros = random.randint(4, 17) # Gera intencionalmente números inválidos
    numeros = random.sample(range(1, 61), qtd_numeros)
    return [id_aposta] + numeros

with open("apostas.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    geradas = 0
    while geradas < 5:
        aposta = gerar_aposta()
        # Valida se possui no mínimo 6 e máximo 15 números (descontando o ID)
        if 6 <= len(aposta) - 1 <= 15:
            writer.writerow(aposta)
            geradas += 1