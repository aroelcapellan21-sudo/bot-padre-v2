import pandas as pd
import pandas_ta as ta
import ccxt

# 1. PARAMETRIZACIÓN DINÁMICA
EMA_LONG = 200
EMA_SHORT = 50
RSI_PERIOD = 14
QUINTETO = ["BTC", "ETH", "SOL", "BNB", "AVAX"]

# 2. CONEXIÓN Y CARGA RÁPIDA DE MERCADOS
exchange = ccxt.binance()
MARKETS = exchange.load_markets() # Esto es lo que optimiza la velocidad

def fetch_candles(symbol, timeframe='1h', limit=500):
    """Obtiene velas usando la caché de mercados para evitar sobrecarga."""
    try:
        par = f"{symbol}/USDT"
        if par not in MARKETS:
            print(f"⚠️ {par} no disponible.")
            return []
            
        return exchange.fetch_ohlcv(par, timeframe=timeframe, limit=limit)
    except Exception as e:
        print(f"⚠️ Error de conexión {symbol}: {e}")
        return []

def preparar_datos_mercado(symbol, velas_raw):
    """Procesa indicadores y genera memoria legible con datetime."""
    try:
        if not velas_raw: return pd.DataFrame()
            
        df = pd.DataFrame(velas_raw, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        # Conversión a fecha legible para humanos
        df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
        
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = df[col].astype(float)
        
        # Cálculo de Indicadores (Usando los parámetros definidos arriba)
        df[f'ema_{EMA_LONG}'] = ta.ema(df['close'], length=EMA_LONG)
        df[f'ema_{EMA_SHORT}'] = ta.ema(df['close'], length=EMA_SHORT)
        df['rsi'] = ta.rsi(df['close'], length=RSI_PERIOD)
        
        # Persistencia: Guardar en CSV para crear la memoria del organismo
        df.to_csv(f"memory_{symbol}.csv", index=False)
        
        return df.dropna()
    except Exception as e:
        print(f"⚠️ Error procesando {symbol}: {e}")
        return pd.DataFrame()
