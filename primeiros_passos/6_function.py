def sum(a, b):
    return a + b

rs = sum(2, 2)

print("The result is of the calc of 2 + 2 is: " + str(rs))

print("****************************************************************")

def salario_descontado_imposto(salario, imposto = 27.): 
    return salario - (salario * imposto * 0.01)

rs = salario_descontado_imposto(5000)

print(rs)

print("****************************************************************")

rs = salario_descontado_imposto(imposto=0.10, salario=5000)

print(rs)