import random
import csv
import sys

def gerar_aposta():
    id_aposta = f"AP-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))}"
    qtd_numeros = random.randint(6, 15)
    numeros = random.sample(range(1, 61), qtd_numeros)
    return [id_aposta] + numeros

quantidade = int(sys.argv[1]) if len(sys.argv) > 1 else 5

with open("apostas.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    for _ in range(quantidade):
        writer.writerow(gerar_aposta())