from faker import Faker
import random

fake = Faker ('pt_BR')

def gerar_registro_aluno():
    nota1 = round (random.uniform(0,10), 1)
    nota2 = round (random.uniform(0,10), 1)
    nota3 = round (random.uniform(0,10), 1)

    media = round((nota1 + nota2 + nota3) / 3, 1)

    status = "Aprovado" if media >= 7.0 else "Recuperação" if media >= 5 else "Reprovado"

    return{
        "nome": fake.name(),
        "materia": fake.random_element(elements=("Matemática", "Português", "Geografia", "História")),
        "nota_1": nota1,
        "nota_2": nota2,
        "nota_3": nota3,
        "media": media, 
        "status": status,

    }

if __name__ == "__main__":
    print(f"{'Nome': <25}| {'Nota 1':<6} | {'Nota 2':<6} | {'Nota 3':<6} | {'Média': <6} | {'Status'}") 
    print("-" * 70)
    for _ in range (5):
        aluno = gerar_registro_aluno()
        print(f"{aluno['nome']:<25} | {aluno['nota_1']:<6} | {aluno['nota_2']:<6} | {aluno['nota_3']:<6} | {aluno['media']:<6} | {aluno['status']}")

