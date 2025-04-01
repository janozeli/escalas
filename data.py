from datetime import date, timedelta
from enum import Enum


class __Dia_da_semana(Enum):
    Domingo = 7
    Segunda = 1
    Terca = 2
    Quarta = 3
    Quinta = 4
    Sexta = 5
    Sabado = 6


class Datas:
    def __init__(self):
        self.__data = date.today()
        self.__ano = self.__data.year
        self.data_inicial = self.__get_data_inicial()
        self.data_final = self.__get_data_final()

    def __get_data_inicial():
        pass

    def __get_data_final():
        pass

    def __get_primeiro_domingo_ano(self):
        ano = self.__ano - 1
        primeiro_dia = date(ano, 1, 1)
        delta = (6 - primeiro_dia.weekday()) % 7
        primeiro_domingo = primeiro_dia + timedelta(days=delta)
        return primeiro_domingo

    def __get_ultimo_domingo_ano(self):
        ano = self.__ano + 1
        ultimo_dia = date(ano, 12, 31)
        delta = (ultimo_dia.weekday() - 6) % 7
        ultimo_domingo = ultimo_dia - timedelta(days=delta)
        return ultimo_domingo
