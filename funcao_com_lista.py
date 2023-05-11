def funcao():
        a = 1
        b = 15
        soma = a + b
        return [a, b, soma]
lista = funcao()
print(f"O valor de a = {lista[0]}, o valor de b = {lista[1]} e a soma de a + b é igual a {lista[2]}")