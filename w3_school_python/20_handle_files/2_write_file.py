import os

path = os.path.join(os.getcwd(), "w3_school_python", "20_handle_files", "demofile2.txt")
# acrescenta texto ao arquivo
f = open(path, 'a') # append to the file
f.write("\nNow the file has more content!")
f.close()

# ler o arquivo
f = open(path, 'r')
print(f.read())
print("\n################################")

f = open(path, 'w') # re-white the file
f.write("Ops! I have deleted the whole content!")
f.close()

f  = open(path, 'r') # read
print(f.read())
f.close()
