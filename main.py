from datetime import date, timedelta
from escalas import Escala

PESSOAS = ["Lucas", "Pedro", "Kaue", "Mayara", "Esther"]
TAREFAS = ["TG", "Cozinha", "Banheiro", "SG", "Lavanderia"]


def main():
    d = Escala(PESSOAS, TAREFAS)


main()
