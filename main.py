import time
from brain.data_engine import fetch_candles, preparar_datos_mercado, QUINTETO
from brain.telegram_engine import enviar_aviso

def ejecutar_ciclo():
    print("\n🚀 Z-Bot Padre: Iniciando ciclo de vigilancia...")
    # Aviso de arranque a Telegram
    enviar_aviso("⚡ Sistema de vigilancia activado. Analizando el Quinteto...")

    for symbol in QUINTETO:
        print(f"🔍 Analizando {symbol}...")
        velas = fetch_candles(symbol)
        
        if velas:
            df = preparar_datos_mercado(symbol, velas)
            if not df.empty:
                ultimo_precio = df['close'].iloc[-1]
                ultimo_rsi = round(df['rsi'].iloc[-1], 2)
                
                print(f"✅ {symbol} en memoria. Precio: ${ultimo_precio} | RSI: {ultimo_rsi}")
                
                # Reporte opcional a Telegram
                # enviar_aviso(f"📊 {symbol}\nPrecio: ${ultimo_precio}\nRSI: {ultimo_rsi}")
        
    print("⌛ Ciclo completado. Reposando 1 minuto...")

if __name__ == "__main__":
    while True:
        try:
            ejecutar_ciclo()
            time.sleep(60) 
        except Exception as e:
            print(f"❌ Error en el bucle principal: {e}")
            enviar_aviso(f"⚠️ Error crítico en el bot: {e}")
            time.sleep(30)
