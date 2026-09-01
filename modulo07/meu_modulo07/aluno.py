# ==============================================================================
# MÓDULO: aluno.py
# Descrição: Responsável por gerar dados do estudante usando Faker e Datetime.
# ==============================================================================

import random
from faker import Faker

fake = Faker('pt_BR')

def gerar_registro_aluno():
    nota1 = round(random.uniform(0, 10), 1)
    nota2 = round(random.uniform(0, 10), 1)
    nota3 = round(random.uniform(0, 10), 1)

    media = round((nota1 + nota2 + nota3) / 3, 1)
    status = "Aprovado" if media >= 7.0 else "Recuperação" if media >= 5 else "Reprovado"

    return {
        "nome": fake.name(),
        "materia": fake.random_element(elements=("Matemática", "Português", "Geografia", "História")),
        "nota_1": nota1,
        "nota_2": nota2,
        "nota_3": nota3,
        "media": media, 
        "status": status,
    }