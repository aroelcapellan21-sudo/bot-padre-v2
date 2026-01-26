import pandas as pd
import pandas_ta as ta
import ccxt

# 1. PARAMETRIZACIÓN (Ajustada para compatibilidad con Kraken)
EMA_LONG = 200
EMA_SHORT = 50
RSI_PERIOD = 14
QUINTETO = ["BTC", "ETH", "SOL", "ADA", "DOT"] # ADA y DOT en lugar de BNB/AVAX

# 2. CONEXIÓN RÁPIDA (Cambiado a Kraken para evitar bloqueo de Google)
exchange = ccxt.kraken()
MARKETS = exchange.load_markets() 

def fetch_candles(symbol, timeframe='1h', limit=500):
    """Obtiene velas usando la caché de mercados de Kraken."""
    try:
        par = f"{symbol}/USDT"
        if par not in MARKETS:
            # Kraken a veces usa nombres como XBT en lugar de BTC internamente
            # pero ccxt suele normalizarlo. Si falla, avisará aquí.
            print(f"⚠️ {par} no disponible en Kraken.")
            return []
            
        return exchange.fetch_ohlcv(par, timeframe=timeframe, limit=limit)
    except Exception as e:
        print(f"⚠️ Error de conexión {symbol}: {e}")
        return []

def preparar_datos_mercado(symbol, velas_raw):
    """Procesa indicadores y genera memoria legible."""
    try:
        if not velas_raw: return pd.DataFrame()
            
        df = pd.DataFrame(velas_raw, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
        
        for col in ['open', 'high', 'low', 'close', 'volume']:
            df[col] = df[col].astype(float)
        
        # Cálculo de Indicadores
        df[f'ema_{EMA_LONG}'] = ta.ema(df['close'], length=EMA_LONG)
        df[f'ema_{EMA_SHORT}'] = ta.ema(df['close'], length=EMA_SHORT)
        df['rsi'] = ta.rsi(df['close'], length=RSI_PERIOD)
        
        # Persistencia: Crear memoria física en la nube
        df.to_csv(f"memory_{symbol}.csv", index=False)
        
        return df.dropna()
    except Exception as e:
        print(f"⚠️ Error procesando {symbol}: {e}")
        return pd.DataFrame()
