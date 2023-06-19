lista = []

print("********************LIST vazio é falsy em IF*********************")
if lista: # array vazio é falsy em if 
    print("Nunca sou executado")
else:
    print("Sempre sou executado")

print("****************************************************************")

lista = [1, 2, 3, 4, 5]
print(lista)

lista.append(6) # adiciona item na lista 
print(lista)

lista.insert(0, -1) # adiciona item antes do index informado
print(lista)

lista.remove(6) # remove primeira ocorrência do item informado
print(lista)

lista.pop(0) # remove o item no index informado, se não informado remove o último
print(lista)

lista.reverse() # reverse a ordem da lista
print(lista)

lista.sort() # ordena a lista
print(lista)

print(lista.index(5)) # retorna index valor

lista_b = [6, 7, 8]
lista.extend(lista_b) # concatena listas
print(lista)

lista.clear()
print(lista)

print("****************************************************************")
