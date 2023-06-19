import random
import sys


class SimuladorDeDado:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6

    def chutar_valor(self):
        run = True
        valores_do_dado = range(self.min_value, self.max_value)

        while run:
            chute = int(input("Qual o valor o dado vai cair? "))

            if chute not in valores_do_dado:
                print(
                    f"Valor deve ser entre {self.min_value} e {self.max_value}. Tente novamente.")
                continue

            valor_do_dado = self.girar_dado()

            if (valor_do_dado == chute):
                print(f"Você acertou! O dado caiu no número {valor_do_dado}")
            else:
                print(f"Você Errou! O dado caiu no número {valor_do_dado}")

            self.tentar_chutar_valor_novamente()

    def girar_dado(self):
        return random.randint(self.min_value, self.max_value)

    def tentar_chutar_valor_novamente(self):
        run = True

        operacoes_possiveis = ["sim", "nao", "s", "n"]

        while run:
            tentar_novamente = input("""
Você gostaria de tentar novamente?
sim | s - para tentar novamente.
nao | n - para encerrar o programa.""").lower()

            if tentar_novamente not in operacoes_possiveis:
                print("Opção Inválida!")
                continue
            else:
                if tentar_novamente == "sim" or tentar_novamente == "s":
                    self.chutar_valor()
                else:
                    sys.exit(0)


SimuladorDeDado().chutar_valor()
