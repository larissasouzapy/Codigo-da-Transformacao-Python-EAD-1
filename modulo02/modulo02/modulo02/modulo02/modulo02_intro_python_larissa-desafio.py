from datetime import datetime

nome = input("Por favor, digite o seu nome: ")

hora_atual = datetime.now().strftime("%H:%M:%S")

print(f"Olá, {nome}! Agora são exatamente {hora_atual}.")
