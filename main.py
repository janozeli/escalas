from datetime import date, timedelta
import sys

PESSOAS = ["Lucas", "Pedro", "Kaue", "Myara", "Esther"]
TAREFAS = ["Banheiro","SG", "Lavanderia", "TG", "Cozinha"]


def main():
    # Verifica se foram fornecidos argumentos de linha de comando
    if len(sys.argv) >= 3:
        try:
            # Tenta interpretar a data inicial (formato: DD/MM/AAAA)
            data_partes = sys.argv[1].split('/')
            data_inicial = date(int(data_partes[2]), int(data_partes[1]), int(data_partes[0]))
            numero_semanas_exibir = int(sys.argv[2])
            
            # Calcula a semana da data inicial
            semana_inicial = get_semana_da_data(data_inicial)
        except (ValueError, IndexError):
            print("Formato de data inválido. Use: DD/MM/AAAA")
            return
    else:
        # Sem argumentos, usa a semana atual e exibe até o final do ano
        semana_inicial = get_semana_atual()
        numero_semanas_exibir = get_total_semanas_no_ano() - semana_inicial + 1
    
    numero_de_semanas = get_total_semanas_no_ano()
    
    # Garante que não ultrapasse o total de semanas do ano
    semana_final = min(semana_inicial + numero_semanas_exibir, numero_de_semanas + 1)
    
    print(f"Escalas da semana {semana_inicial:02d} até a semana {semana_final - 1:02d}")
    print("-" * 40)
    
    for semana in range(semana_inicial, semana_final):
        domingo, sabado = get_domingo_e_sabado_da_semana(semana)
        
        # Formata as datas com o mês em português
        domingo_formatado = formatar_data(domingo)
        sabado_formatado = formatar_data(sabado)
        
        print(f"Semana {semana:02d} | {domingo_formatado} - {sabado_formatado}")
        distribuir_tarefas(semana)
        print("-" * 40)


def distribuir_tarefas(numero_semana):
    # Número de pessoas e tarefas
    num_pessoas = len(PESSOAS)
    
    # O banheiro precisa seguir uma rotação específica entre os homens
    homens = ["Lucas", "Pedro", "Kaue"]
    
    # Determina quem fica com o banheiro nesta semana (um dos homens)
    homem_com_banheiro = homens[(numero_semana - 1) % len(homens)]
    idx_homem_com_banheiro = PESSOAS.index(homem_com_banheiro)
    
    # Distribui as outras tarefas baseado na rotação normal
    rotacao = (numero_semana - 1) % num_pessoas
    
    # Cria a distribuição inicial (sem o banheiro)
    tarefas_sem_banheiro = [t for t in TAREFAS if t != "Banheiro"]
    distribuicao = [None] * num_pessoas
    
    # Primeiro, atribui o banheiro para o homem escolhido
    distribuicao[idx_homem_com_banheiro] = (homem_com_banheiro, "Banheiro")
    
    # Depois, atribui as outras tarefas para as outras pessoas
    idx_tarefa = rotacao % len(tarefas_sem_banheiro)
    
    for i in range(num_pessoas):
        if distribuicao[i] is None:  # se ainda não tem tarefa atribuída
            tarefa = tarefas_sem_banheiro[idx_tarefa]
            distribuicao[i] = (PESSOAS[i], tarefa)
            idx_tarefa = (idx_tarefa + 1) % len(tarefas_sem_banheiro)
    
    # Imprime a distribuição
    for pessoa, tarefa in distribuicao:
        print(f"  {pessoa}: {tarefa}")


def get_total_semanas_no_ano():
    ultimo_dia_ano_anterior = date(date.today().year - 1, 12, 31)
    dias_ate_ultimo_domingo = ultimo_dia_ano_anterior.weekday() + 1
    ultimo_domingo_ano_anterior = ultimo_dia_ano_anterior - timedelta(days=dias_ate_ultimo_domingo)
    
    primeiro_dia_ano_seguinte = date(date.today().year + 1, 1, 1)
    dias_ate_domingo = (6 - primeiro_dia_ano_seguinte.weekday()) % 7
    primeiro_domingo_ano_seguinte = primeiro_dia_ano_seguinte + timedelta(days=dias_ate_domingo)
    
    return int(((primeiro_domingo_ano_seguinte - ultimo_domingo_ano_anterior).days / 7))


def get_domingo_e_sabado_da_semana(numero_semana):
    ultimo_dia_ano_anterior = date(date.today().year - 1, 12, 31)
    dias_ate_ultimo_domingo = ultimo_dia_ano_anterior.weekday() + 1
    ultimo_domingo_ano_anterior = ultimo_dia_ano_anterior - timedelta(days=dias_ate_ultimo_domingo)
    
    primeiro_domingo = ultimo_domingo_ano_anterior
    
    domingo_da_semana = primeiro_domingo + timedelta(weeks=(numero_semana - 1))
    sabado_da_semana = domingo_da_semana + timedelta(days=6)
    
    return domingo_da_semana, sabado_da_semana


def daterange(start_date: date, end_date: date):
    days = int((end_date - start_date).days)
    for n in range(days):
        yield start_date + timedelta(n)


def formatar_data(data):
    dia = data.day
    
    # Mapeia os nomes dos meses em português
    meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril",
        5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
        9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }
    
    mes = meses[data.month]
    return f"{dia} de {mes}"


def get_semana_atual():
    # Obtém a data atual
    hoje = date.today()
    
    # Obtém o último domingo do ano anterior (referência para a primeira semana)
    ultimo_dia_ano_anterior = date(date.today().year - 1, 12, 31)
    dias_ate_ultimo_domingo = ultimo_dia_ano_anterior.weekday() + 1
    ultimo_domingo_ano_anterior = ultimo_dia_ano_anterior - timedelta(days=dias_ate_ultimo_domingo)
    
    # Calcula quantas semanas se passaram desde o último domingo do ano anterior
    dias_passados = (hoje - ultimo_domingo_ano_anterior).days
    semana_atual = (dias_passados // 7) + 1
    
    return semana_atual


def get_semana_da_data(data):
    # Obtém o último domingo do ano anterior (referência para a primeira semana)
    ultimo_dia_ano_anterior = date(date.today().year - 1, 12, 31)
    dias_ate_ultimo_domingo = ultimo_dia_ano_anterior.weekday() + 1
    ultimo_domingo_ano_anterior = ultimo_dia_ano_anterior - timedelta(days=dias_ate_ultimo_domingo)
    
    # Calcula quantas semanas se passaram desde o último domingo do ano anterior
    dias_passados = (data - ultimo_domingo_ano_anterior).days
    semana = (dias_passados // 7) + 1
    
    return max(1, semana)  # garante que a semana seja pelo menos 1


main()
