from brain.core import ZBotPadreV2
from brain.data_engine import preparar_datos_mercado

def ejecutar_cerebro(datos_brutos):
    """
    Punto de entrada principal para el Bot-Padre V2.
    """
    # 1. Inicializar el cerebro para BTC
    cerebro = ZBotPadreV2(symbol="BTCUSDT")
    
    # 2. Procesar los datos recibidos (EMA, RSI)
    df_listo = preparar_datos_mercado(datos_brutos)
    
    # 3. Obtener la decisión de la Estrategia V1.0
    decision = cerebro.analizar_estrategia_v1(df_listo)
    
    # 4. Mostrar reporte (Regla de la Matrix: Auditoría evaluada)
    print(f"🧠 REPORTE CEREBRO: {decision}")
    return decision

if __name__ == "__main__":
    print("🚀 Ecosistema Z-Bot: Cerebro encendido y esperando datos...")
