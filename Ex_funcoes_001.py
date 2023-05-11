def multiplicacao():
    primeira_variavel = int(input('Digite o valor da primeira variável: '))
    segunda_variavel = int(input('Digite o valor da segunda variável: '))
    multiplica = primeira_variavel * segunda_variavel
    return [primeira_variavel, segunda_variavel, multiplica]

lista = multiplicacao()
print(f"O valor da primeira variável é igual a {lista[0]}, o valor da segunda é {lista[1]} e a multiplicação entre a primeira e a segunda variável é igual a {lista[2]}")