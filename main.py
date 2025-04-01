from datetime import date, timedelta
from data import Datas

PESSOAS = ["Lucas", "Pedro", "Kaue", "Myara", "Esther"]
TAREFAS = ["Banheiro", "SG", "Lavanderia", "TG", "Cozinha"]


def main():
    d = Datas()
    print(d.data_inicial)
    print(d.data_final)


main()
