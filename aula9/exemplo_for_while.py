# Explicando for while
list_valores = []

for i in range(5):
    num = float(input('\nInforme o número: '))
    list_valores.append(num)

print(f'\nOs úmeros são {list_valores}')

# While
list_nome = []
resposta = ''

while resposta != 'n':
    nome = input('\nInforme o nome: ')
    list_nome.append(nome)

    resposta = input('\nQuer continuar? [s/n]: ')[0].lower()
    print(resposta)
print(f'\nOs nomes foram {list_nome}')

list_nome2 = []
while True:
    nome = input('\nInforme o nome: ')
    list_nome2.append(nome)

    resposta = input('\nQuer continuar? [s/n]: ')
    if resposta == 'n':
        break

# loop infinito while ou for


# While
list_nome = []
# resposta = ''
contador = 0 
while contador < 5:
    nome = input('\nInforme o nome: ')
    list_nome.append(nome)
    contador += 1

print(f'\nOs nomes foram {list_nome}')