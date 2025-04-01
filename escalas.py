from datetime import date, timedelta
from enum import Enum
from math import lcm


class Primeiro_ou_ultimo(Enum):
    Primeiro = 1
    Ultimo = 2


class Dia_da_semana(Enum):
    Domingo = 6
    Segunda = 0
    Terca = 1
    Quarta = 2
    Quinta = 3
    Sexta = 4
    Sabado = 5


class Escala:
    def __init__(self, pessoas: list[str], tarefas: list[str]):
        self.pessoas = pessoas
        self.tarefas = tarefas
        self.data = date.today()
        self.ano = self.data.year
        self.data_inicial = self.get_data_inicial()
        self.data_final = self.get_data_final()
        self.quantidade_dias = (self.data_final - self.data_inicial).days + 1
        self.quantidade_semanas = self.quantidade_dias // 7
        self.combinacoes = self.get_combinacoes()

    def get_data_inicial(self):
        return self.get_dia_da_semana(Dia_da_semana.Domingo, Primeiro_ou_ultimo.Ultimo)

    def get_data_final(self):
        return self.get_dia_da_semana(
            Dia_da_semana.Domingo, Primeiro_ou_ultimo.Primeiro
        )

    def get_dia_da_semana(
        self, dia_da_semana: Dia_da_semana, primeiro_ou_ultimo: Primeiro_ou_ultimo
    ):
        if primeiro_ou_ultimo == Primeiro_ou_ultimo.Primeiro:
            ano = self.ano + 1
            dia_base = date(ano, 1, 1)
            delta = (dia_da_semana.value - dia_base.weekday()) % 7
            if delta == 0:
                return dia_base

            return dia_base + timedelta(days=delta)
        else:
            ano = self.ano - 1
            dia_base = date(ano, 12, 31)
            delta = (dia_da_semana.value - dia_base.weekday()) % 7
            if delta == 0:
                return dia_base

            return dia_base - timedelta(days=7 - delta)

    def get_combinacoes(self):
        combinacoes = {}
        semanas_validas = []

        historico_tarefas = {pessoa: set() for pessoa in self.pessoas}

        tarefas_permitidas = {}
        for pessoa in self.pessoas:
            if pessoa in ["Esther", "Mayara"]:
                tarefas_permitidas[pessoa] = [
                    t for t in self.tarefas if t != "Banheiro"
                ]
            else:
                tarefas_permitidas[pessoa] = self.tarefas.copy()

        semana_atual = 0

        while len(semanas_validas) < 54:
            combinacoes_semana = {}
            tarefas_disponiveis = self.tarefas.copy()

            ordem_pessoas = (
                self.pessoas[semana_atual % len(self.pessoas) :]
                + self.pessoas[: semana_atual % len(self.pessoas)]
            )

            for pessoa in ordem_pessoas:
                tarefas_candidatas = [
                    t for t in tarefas_disponiveis if t in tarefas_permitidas[pessoa]
                ]

                if not tarefas_candidatas:
                    break

                tarefas_nao_feitas = [
                    t for t in tarefas_candidatas if t not in historico_tarefas[pessoa]
                ]

                if tarefas_nao_feitas:
                    tarefa_escolhida = tarefas_nao_feitas[0]
                else:
                    tarefa_escolhida = tarefas_candidatas[0]

                combinacoes_semana[pessoa] = tarefa_escolhida
                tarefas_disponiveis.remove(tarefa_escolhida)

            if len(combinacoes_semana) == len(self.pessoas):
                for pessoa, tarefa in combinacoes_semana.items():
                    historico_tarefas[pessoa].add(tarefa)

                semanas_validas.append(combinacoes_semana)

            semana_atual += 1

        for i, semana in enumerate(semanas_validas):
            numero_semana = i + 1
            combinacoes[numero_semana] = semana

        return combinacoes
