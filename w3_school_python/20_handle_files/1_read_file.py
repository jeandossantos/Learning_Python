import os

path = os.path.join(os.getcwd(), "w3_school_python", "20_handle_files", "demofile.txt")

f = open(path, "r")

print(f.read()) # retorna o texto inteiro
f.close()    
print("\n################################")

f = open(path, "r")

print(f.read(5)) # ler 5 caracteres por vez
f.close()
print("\n################################")

f = open(path, "r")

print(f.readline()) # ler a primeira linha
print(f.readline()) # ler a segunda linha
f.close()
print("\n################################")

f = open(path, "r")

for x in f: # percorrendo linha por linha
  print(x.replace("\n", ""))
  
f.close()