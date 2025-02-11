import pandas as pd
import os

from eventos import CSV_PATH

def notificar_eventos(eventos_proximos, eventos):
    """Exibir notificações e atualizar status no CSV"""
    if eventos_proximos.empty:
        print("Nenhum evento para notificar.")
        return 
    
    print ("\n🔔 Notificações de eventos próximos:")
    for index, evento in eventos_proximos.iterrows():
        print(f"🔔 O evento '{evento['nome_evento']}' ocorrerá em {evento['data']} às {evento['hora']}.")

        #Marcar evento como notificado
        eventos.at[index, 'notificado'] = "Sim"

    #Atualizar arquivo CSV sem modificar o formato da hora
    eventos['hora'] = eventos['hora'].apply(lambda x: x.strftime('%H:%M'))
    eventos[['id', 'nome_evento', 'data', 'hora', 'notificado']].to_csv(CSV_PATH, index=False)

    print("\n✅ Eventos atualizados no arquivo 'eventos.csv'.")