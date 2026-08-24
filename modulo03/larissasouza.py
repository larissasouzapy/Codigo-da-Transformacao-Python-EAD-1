'''
Como lavar o cabelo.

Antes de tudo você precisa dos produtos para fazer a lavagem;
Produtos: shampoo e condicionador (essa é a forma mais simples de como lavar);
1º Molhe o seu cabelo com água corrente(se preferir);
2º Aplique uma quatidade razoável de shampoo sobre a cabeça;
3º Espalhe o produto aplicado e comece a  esfregar a ponta dos dedos em movimentos circulares
(não se esqueca:shampoo é usado somente na raiz do cabelo);
4º Enxágue o cabelo ambundantemente até sair todo o resíduo de shampoo;
5º Repita o processo do shampoo pela segunda vez;
6º Após isso tire o máximo que conseguir de água do cabelo;
7º Com o cabelo úmido pegue uma quantidade razoável de condicionador;
8º Aplique o produto somente no comprimento do cabelo massageie  o comprimento do cabelo deixando o produto agir o tempo que é pedido (normalmnete entre 3 a 5 minutos);
9º Enxágue o cabelo até tirar todo o resíduo do produto;
10º Por fim  finalize da forma que preferir.
'''


def lavar_cabelo(cabelo_sedoso):
    print('💆‍♀️👌✨ Lavado cabelo - sistema simples ')
    print('Passo a passo para deixar o seu cabelo sedoso')
    print('1º Molhe o seu cabelo com água corrente(se preferir)')
    print('2º Aplique uma quatidade razoável de shampoo sobre a cabeça')
    print('3º Espalhe o produto aplicado e comece a  esfregar a ponta dos dedos em movimentos circulares (não se esqueca:shampoo é usado somente na raiz do cabelo)')
    print ('4º Enxágue o cabelo ambundantemente até sair todo o resíduo de shampoo ')
    print('5º Repita o processo do shampoo pela segunda vezo')
    print('6º Após isso tire o máximo que conseguir de água do cabelo')
    print('7º Com o cabelo úmido pegue uma quantidade razoável de condicionador')
    print('8º Aplique o produto somente no comprimento do cabelo, massageie os fios deixando o produto agir o tempo que é pedido (normalmnete entre 3 a 5 minutos)')
    print('9º Enxágue o cabelo até tirar todo o resíduo do produto')
    print('10º Por fim  finalize da forma que preferir.')


    if cabelo_sedoso.lower() == "cabelo sujo": 
        resultado = 'Cabelo oleoso sem brilho.'
    elif cabelo_sedoso.lower() == "cabelo limpo":
        resultado = 'Cabelo cheiroso e belo.'
    else:
        resultado = 'Dá pra disfarçar a sujeira.'

    return resultado 
meu_cabelo = lavar_cabelo('cabelo limpo')
print(f'Meu cabelo está:{meu_cabelo}')
