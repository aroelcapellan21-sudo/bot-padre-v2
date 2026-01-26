import time
from brain.data_engine import fetch_candles, preparar_datos_mercado, QUINTETO
from brain.telegram_engine import enviar_aviso

def ejecutar_ciclo_silencioso():
    # El mensaje de inicio en Telegram ha sido ELIMINADO para evitar ruido
    print("\n🔍 Z-Bot Padre: Vigilancia silenciosa en curso...")

    for symbol in QUINTETO:
        velas = fetch_candles(symbol)
        if velas:
            df = preparar_datos_mercado(symbol, velas)
            if not df.empty:
                ultimo_precio = df['close'].iloc[-1]
                ultimo_rsi = round(df['rsi'].iloc[-1], 2)
                
                # Esto SOLO se ve en la pantalla negra (Consola), NO en Telegram
                print(f"✅ {symbol}: ${ultimo_precio} | RSI: {ultimo_rsi}")
                
    print("⌛ Ciclo completado. Consola actualizada. Reposando...")

if __name__ == "__main__":
    # Al encenderse, solo avisa una vez que está listo y se calla
    enviar_aviso("🤫 Z-Bot en modo Silencio Inteligente. Solo responderé si me escribes /status.")
    
    while True:
        try:
            ejecutar_ciclo_silencioso()
            time.sleep(60) 
        except Exception as e:
            # Solo avisa si hay un error real
            enviar_aviso(f"⚠️ Error: {e}")
            time.sleep(30)
