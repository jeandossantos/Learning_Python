set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)  # retorna a união dos sets set1 e set2
print(set3)
print("\n###############################")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)  # une set2 ao set1
print(set1)

print("\n###############################")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)  # matem os itens que existem em ambos set

print(x)  # => {"apple"}
print("\n###############################")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)  # retorna os itens que existem em ambos set

print(z)  # => {"apple"}
print("\n###############################")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)  # matem os itens que NÂO existem em ambos set

print(x)  # => {"apple"} não vai estar no set
print("\n###############################")

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)  # matem os itens que NÂO existem em ambos set

print(z)  # => {"apple"} não vai estar no set z
print("\n###############################")
# lembrando que True e 1 são tratados como iguais em set
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

# => {"apple" TRUE, and 1} não vão estar no set z
z = x.symmetric_difference(y)
