class Exercicio:
    def __init__(self, nome, repeticoes, series):
        self.nome = nome
        self.repeticoes = repeticoes
        self.series = series

exercicios = []

while True:
    nome = input("Digite o nome do exercício (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    repeticoes = int(input("Digite o número de repetições: "))
    series = int(input("Digite o número de séries: "))
    exercicios.append(Exercicio(nome, repeticoes, series))

for exercicio in exercicios:
    print(f"{exercicio.nome}: {exercicio.repeticoes} repetições, {exercicio.series} séries")
