import pandas as pd
import pandas_ta as ta

def preparar_datos_mercado(velas_raw):
    """
    Transforma velas crudas en datos con indicadores para el Cerebro.
    """
    try:
        # 1. Crear DataFrame
        df = pd.DataFrame(velas_raw, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['close'] = df['close'].astype(float)
        df['high'] = df['high'].astype(float)
        df['low'] = df['low'].astype(float)
        
        # 2. Calcular Indicadores (Estrategia V1.0)
        df['ema_200'] = ta.ema(df['close'], length=200)
        df['ema_50'] = ta.ema(df['close'], length=50)
        df['rsi'] = ta.rsi(df['close'], length=14)
        
        # 3. Limpiar valores nulos iniciales (donde no hay suficientes velas para la EMA)
        return df.dropna()
        
    except Exception as e:
        # Reporte automático si algo falla (Regla del Ecosistema)
        print(f"⚠️ AVISO ECOSISTEMA: Error en Motor de Datos: {e}")
        return pd.DataFrame()
