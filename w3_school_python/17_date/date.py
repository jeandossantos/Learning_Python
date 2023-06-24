import datetime

x = datetime.datetime.now()

print(x)
print(x.year)
print(x.strftime("%A")) # formata data => Dia da semana em texto completo
print("\n################################")

x = datetime.datetime(2020, 5, 23)

print(x)