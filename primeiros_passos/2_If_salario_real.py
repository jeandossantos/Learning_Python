salario = int(input("Salário? "))
imposto = input("Imposto em % (ex: 27.5)? ")

if imposto == '':
    imposto = 27.5
else:
    imposto = float(imposto)

print("🚀 ~ file: salario_real.py:8 ~ imposto:", imposto)

print("Valor real: {0}".format(salario - (salario * imposto  * 0.1)))

