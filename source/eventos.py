import pandas as pd
import os
from datetime import datetime, timedelta

# Caminho do arquivo CSV
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, '../data/eventos.csv')

def carregar_eventos ():
    """Carrega os eventos do CSV e valida os dados"""

    try:
        eventos = pd.read_csv(CSV_PATH)
        eventos.columns = [col.strip() for col in eventos.columns] #Remove espaços extras

        #Verificação de colunas
        colunas_necessarias = {'id', 'nome_evento', 'data', 'hora', 'notificado'}
        if not colunas_necessarias.issubset(eventos.columns):
            print("Erro: O arquivo 'eventos.csv' não contém todas as colunas necessárias.")
            return pd.DataFrame()
        
        #Conversão de colunas de data e hora
        eventos['data'] = pd.to_datetime(eventos['data'], format='%Y-%m-%d', errors='coerce')
        eventos['hora'] = pd.to_datetime(eventos['hora'], format='%H:%M', errors='coerce').dt.time

        return eventos.dropna() #Remove linhas com valores inválidos
    
    except FileNotFoundError:
        print("Erro:Arquivo 'eventos.csv' não encontrado!")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo 'eventos.csv' está vazio!")
    except Exception as e:
        print(f"Erro inesperado ao carregar eventos: {e}")

    return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro

def verificar_eventos_proximos(eventos):
    """Filtra eventos que ocorrerão nas próximas 24 horas"""

    agora = datetime.now()
    limite = agora + timedelta(hours=24)

    eventos['data_hora'] = pd.to_datetime(eventos['data'].dt.strftime('%Y-%m-%d') + ' ' + eventos['hora'].astype(str))

    return eventos[(eventos['data_hora'] >= agora) & (eventos['data_hora'] <= limite)]  
