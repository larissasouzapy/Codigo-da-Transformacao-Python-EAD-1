from faker import Faker
import random

fake = Faker ('pt_BR')
#gera as notas maximas, medias e ruins. tendo tambem o calculo da media 
# onde é somado  e com o total dividido por 3
def gerar_registro_aluno():
    nota1 = round (random.uniform(0,10), 1)
    nota2 = round (random.uniform(0,10), 1)
    nota3 = round (random.uniform(0,10), 1)

    media = round((nota1 + nota2 + nota3) / 3, 1)

    status = "Aprovado" if media >= 7.0 else "Recuperação" if media >= 5 else "Reprovado"
# Retorno de dados, é devolvido um dicionários estruturado com as chaves de informação
    return{
        "nome": fake.name(),
        "materia": fake.random_element(elements=("Matemática", "Português", "Geografia", "História")),
        "nota_1": nota1,
        "nota_2": nota2,
        "nota_3": nota3,
        "media": media, 
        "status": status,

    }

if __name__ == "__main__":#garente qe o codigo só funcionará quando executar diretamente
    print(f"{'Nome': <25}| {'Nota 1':<6} | {'Nota 2':<6} | {'Nota 3':<6} | {'Média': <6} | {'Status'}") #cria o topo da tabela
    print("-" * 70)#criando uma linha horizontal separadora

    for _ in range (5):
        aluno = gerar_registro_aluno()
        print(f"{aluno['nome']:<25} | {aluno['nota_1']:<6} | {aluno['nota_2']:<6} | {aluno['nota_3']:<6} | {aluno['media']:<6} | {aluno['status']}")

