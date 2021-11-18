nome = 'Tiago'
idade = 28
altura = 1.80
peso = 75
ano_atual = 2021
data_nasc = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e seu peso é {peso}')
print(f'o imc de Tiago é {imc:.2f}')
print(f'{nome} nasceu em {data_nasc}')
