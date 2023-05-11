# criando a lista vazia para armazenar os dados
pessoas = []

# criando variáveis para guardar os dados das pessoas mais pesadas e mais leves
mais_pesado = ['', 0]
mais_leve = ['', float('inf')]

# loop para a entrada dos dados das pessoas
while True:
    # lendo nome e peso da pessoa
    nome = input('Digite o nome da pessoa (ou "fim" para encerrar): ')
    if nome == 'fim':
        break
    peso = float(input('Digite o peso da pessoa em kg: '))

    # adicionando os dados da pessoa na lista
    pessoas.append([nome, peso])

    # atualizando as variáveis para a pessoa mais pesada e mais leve
    if peso > mais_pesado[1]:
        mais_pesado = [nome, peso]
    if peso < mais_leve[1]:
        mais_leve = [nome, peso]

# calculando a quantidade de pessoas cadastradas
quantidade = len(pessoas)

# calculando a média de peso das pessoas
soma_pesos = sum(p[1] for p in pessoas)
media = soma_pesos / quantidade

# apresentando as informações
print(f'Foram cadastradas {quantidade} pessoas.')
print(f'A pessoa mais pesada é {mais_pesado[0]} com {mais_pesado[1]} kg.')
print(f'A pessoa mais leve é {mais_leve[0]} com {mais_leve[1]} kg.')
print(f'A média de peso das pessoas é {media:.2f} kg.')
