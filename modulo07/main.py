from meu_modulo07 import (
    gerar_registro_aluno,
    jogo_adivinhacao,
    potencia,
    somar,
    subtrair,
)

print("=== TESTANDO PACOTE MEU_MODULO07 ===")
print("Soma (10 + 5):", somar(10, 5))
print("Potência (2^3):", potencia(2, 3))

print("\n--- Dados do Aluno Gerado ---")
aluno = gerar_registro_aluno()
print(
    f"Nome: {aluno['nome']} | Média: {aluno['media']} | Status: {aluno['status']}\n"
)

print("--- Iniciando Jogo ---")
jogo_adivinhacao()