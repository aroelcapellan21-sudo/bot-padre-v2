import time
# Importamos el motor y la lista de monedas
from brain.data_engine import preparar_datos_mercado, QUINTETO

print("🚀 Ecosistema Z-Bot: Iniciando Quinteto de Poder...")

while True:
    for moneda in QUINTETO:
        print(f"\n🔍 Analizando {moneda}...")
        
        # Por ahora enviamos una lista vacía para probar la conexión del motor
        # En la siguiente fase conectaremos la API real aquí
        datos_simulados = [] 
        
        df = preparar_datos_mercado(moneda, datos_simulados)
        
        if df.empty:
            print(f"⚠️ {moneda}: Esperando flujo de datos reales...")
        else:
            print(f"✅ Memoria enriquecida para {moneda}")

    print("\n⏳ Ciclo completado. Reintentando en 10 segundos...")
    time.sleep(10)
