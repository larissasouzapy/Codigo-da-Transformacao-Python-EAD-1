import random 
import math


def jogo_adivinhacao():
    limite_maximo = 24

    tentativas_maximas = math.ceil(math.log2(limite_maximo)) + 1
    numero_secreto = random.randint(1, limite_maximo)

    print("Bem-vindo ao jogo  da adivinhação!")
    print("--🍀JOGO DA ADIVINHAÇÃO🍀--")
    print(f"Pensei em um numero entre 1 e {limite_maximo}")
    print(f"Você tem {tentativas_maximas} para acertar!\n")

    for rodada in range(1, tentativas_maximas + 1):
        try:
             palpite = int(input(f"Tentativa{rodada} de {tentativas_maximas} - Digite seu palpite:"))
        except ValueError:
             print("Por favor digite apenas numeros inteiro válidos!|n")

        if palpite < 1 or palpite > limite_maximo:
             print(f"Atenção: O número deve estar entre 1 e {limite_maximo}!\n")
             continue

        if palpite == numero_secreto:
            print(f"\nParabéns! Você acertou o número {numero_secreto} em {rodada} tentativa(s)!")
            return

        elif palpite < numero_secreto:
            print("Dica: O número secreto é MAIOR.\n")
        else:
         print("Dica: O número secreto é MENOR.\n")

         print(f"\nGame Over! Suas tentativas acabaram. O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogo_adivinhacao()