# cadatra
def cadastra_pessoa(num):
    for i in range(num):
        nome = input('\nInforme o nome do vendedor: ')
        valor = float(input('\nInforme valor da venda: '))

        pessoas = {
            'Nome': nome,
            'Valor': valor,
        }

        list_cadastro.append(pessoas)


# Média e Total
def caucula_total_media():
    tot = 0
    for pessoas in list_cadastro:
        tot += pessoas['Valor']

    med = tot / len(list_cadastro)  # len da a quantidade de elementos
    return tot, med


# BUSCAR O MAIOR E O NOME DO VENDEDOR
def buscar_maior():
    maior = 0
    vendedor = ''

    for v in list_cadastro:
        if v['Valor'] > maior:
            maior = v['Valor']
            vendedor = v['Nome']

    return maior, vendedor


# BUSCAR NOME DO VENDEDOR
def buscar_vendedor(nome):
    resposta = ''
    vl = 0

    for cadastro in list_cadastro:
        if cadastro['Nome'] == nome:
            resposta = cadastro['Nome']
            vl = cadastro['Valor']

            return resposta, vl
    return resposta, vl


# EXEMPLO 01 - CADASTRO FUNCIONARIO
list_cadastro = []

qnt = int(input('\nQuantas pessoas: '))
cadastra_pessoa(qnt)
print(f'\n', list_cadastro)

# ---------------------//----------------------
# EXEMPLO 02 - TOTAL E MÉDIA
total, media = caucula_total_media()
print('\n', 30*'=')
print(f'Total: {total:.2f}')
print(f'Média: {media:.2f}')

# EXEMPLO 03 - MAIOR VALOR e VENDEDOR
maior_venda, maior_vendedor = buscar_maior()
print(30*'=')
print(f'Maior venda {total:.2f}')
print(f'Maior vendedor {maior_vendedor}')

# EXEMPLO 04 - BUSCAR VENDEDOR 
vendedor = input('\nDigite o nome do vendedor: ')
nome_vendedor, valor = buscar_vendedor(vendedor)

if nome_vendedor:
    print(f'\nO vendedor {nome_vendedor} está listado')
    print(f'\nO valor {valor}')
else:
    print(f'\n{nome_vendedor} Vendedor não encontrado')