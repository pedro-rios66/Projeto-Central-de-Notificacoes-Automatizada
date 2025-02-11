import schedule
import time

from eventos import carregar_eventos, verificar_eventos_proximos
from notificacoes import notificar_eventos

def processo_automatico():
    """Executa o fluxo completo da notificação de eventos"""
    print("\n🔍 Iniciando verificação de eventos...")
    eventos = carregar_eventos()
    if not eventos.empty:
        eventos_proximos = verificar_eventos_proximos(eventos)
        if not eventos_proximos.empty:
            print("📅 Eventos próximos encontrados:")
            print(eventos_proximos[['id', 'nome_evento', 'data', 'hora']])
            notificar_eventos(eventos_proximos, eventos)
        else:
            print ("ℹ️ Nenhum evento próximo encontrado.")

    else:
        print("⚠️ Nenhum evento disponível para verificação.")


#Agendar execução a cada 30 minutos
schedule.every(30).minutes.do(processo_automatico)

if __name__ == "__main__":
    print("Central de Notificações de Governança iniciada!")
    print("🔄 A verificação automática está ativa.")

    while True:
        schedule.run_pending()
        time.sleep(60)