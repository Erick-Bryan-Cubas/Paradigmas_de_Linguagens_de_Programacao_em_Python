def funcao(a, b):
        soma = a + b
        return [a, b, soma]

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
lista = funcao(a, b)
print(f"O valor de a = {lista[0]}, o valor de b = {lista[1]} e a soma de a + b é igual a {lista[2]}")