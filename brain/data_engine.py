import pandas as pd
import pandas_ta as ta
import os

# Lista de seguimiento definida por el usuario (Quinteto de Poder)
QUINTETO = ["BTC", "ETH", "SOL", "BNB", "AVAX"]

def preparar_datos_mercado(symbol, velas_raw):
    """
    Transforma velas crudas en datos con indicadores y guarda memoria histórica.
    """
    try:
        # 1. Crear DataFrame y asegurar tipos numéricos
        df = pd.DataFrame(velas_raw, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = df[col].astype(float)
        
        # 2. Calcular Indicadores (Estrategia V1.0)
        df['ema_200'] = ta.ema(df['close'], length=200)
        df['ema_50'] = ta.ema(df['close'], length=50)
        df['rsi'] = ta.rsi(df['close'], length=14)
        
        # 3. ENRIQUECER MEMORIA: Guardar datos en archivo local
        nombre_archivo = f"memory_{symbol}.csv"
        df.to_csv(nombre_archivo, index=False)
        
        # 4. Limpiar valores nulos y retornar
        return df.dropna()
        
    except Exception as e:
        print(f"⚠️ AVISO ECOSISTEMA: Error en Motor de Datos ({symbol}): {e}")
        return pd.DataFrame()
