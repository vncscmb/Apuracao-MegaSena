import random
import csv

def gerar_aposta():
    id_aposta = f"AP-{''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))}"
    numeros = random.sample(range(1, 61), 6)
    return [id_aposta] + numeros

with open("apostas.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    for _ in range(5):
        writer.writerow(gerar_aposta())