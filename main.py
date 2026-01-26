import time
# Importamos las funciones optimizadas
from brain.data_engine import fetch_candles, preparar_datos_mercado, QUINTETO

print("🚀 Ecosistema Z-Bot: Iniciando Bots Observadores (V1.1)...")

while True:
    for moneda in QUINTETO:
        print(f"\n🔍 Analizando {moneda}...")
        
        # 1. Succión rápida de velas reales
        datos_raw = fetch_candles(moneda)
        
        # 2. Procesamiento de indicadores y guardado en memoria CSV
        df = preparar_datos_mercado(moneda, datos_raw)
        
        if not df.empty:
            precio = df['close'].iloc[-1]
            rsi = df['rsi'].iloc[-1]
            print(f"✅ {moneda} en memoria. Precio: ${precio} | RSI: {rsi:.2f}")
        else:
            print(f"❌ {moneda}: Fallo al obtener o procesar datos.")

    print("\n⏳ Ciclo completado. Reposando 1 minuto...")
    time.sleep(60)
