thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort(reverse=True)

print(thisList)  # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

print("================================")

thisList = [100, 50, 65, 82, 23]
thisList.sort(reverse=True)

print(thisList)  # => [100, 82, 65, 50, 23]

print("================================")
# sort method is case-sensitive
thisList = ["banana", "Orange", "Kiwi", "cherry"]
thisList.sort()

print(thisList)  # =>  ['Kiwi', 'Orange', 'banana', 'cherry']

print("================================")

thisList = ["banana", "Orange", "Kiwi", "cherry"]
# turning it case-insensitive
thisList.sort(key=str.lower)

print(thisList)  # => ['banana', 'cherry', 'Kiwi', 'Orange']
