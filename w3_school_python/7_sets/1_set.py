# set são não ordenados
thisSet = {"apple", "banana", "cherry"}

print(thisSet)  # a ordem que os itens vão aparece é aleatória
print("\n################################")
# valores duplicados não são permitidos, vão ser ignorados
thisSet = {"apple", "banana", "cherry", "apple"}

print(thisSet)  # => só vai ter um "apple" no set
print("\n################################")
# True e 1 são tradados como o mesmo valor em set, e o duplicado vai ser ignorado
thisSet = {"apple", "banana", "cherry", True, 1, 2}

print(thisSet)  # => item "1" vai ser ignorado
print("\n################################")
# pode armazenar diferentes tipos
set1 = {"abc", 34, True, 40, "male"}  # todos os valores são aceitos
print("\n################################")
# Usando o construtor set
thisSet = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisSet)
