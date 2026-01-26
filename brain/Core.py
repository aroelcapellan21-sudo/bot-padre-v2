import pandas as pd
import pandas_ta as ta

class ZBotPadreV2:
    def __init__(self, symbol="BTCUSDT"):
        self.symbol = symbol
        # Configuración de Riesgo según Estrategia V1.0
        self.config = {
            "sl_percent": 0.015,  # 1.5% de Stop Loss
            "tp_ratio": 2.0       # Take Profit 2 veces el riesgo (3%)
        }

    def analizar_estrategia_v1(self, df):
        """
        Aplica la lógica: Tendencia (EMA 200) -> Pullback (EMA 50) -> Confirmación (RSI)
        """
        if df.empty or len(df) < 200:
            return {"accion": "WAIT", "motivo": "Esperando datos (mínimo 200 velas)"}

        # Obtener datos de la última vela cerrada
        actual = df.iloc[-1]
        precio = actual['close']
        ema_200 = actual['ema_200']
        ema_50 = actual['ema_50']
        rsi = actual['rsi']

        # LÓGICA DE COMPRA (LONG)
        if precio > ema_200 and precio < ema_50 and rsi < 40:
            return {"accion": "BUY", "precio": precio, "motivo": "Pullback en tendencia alcista"}

        return {"accion": "WAIT", "motivo": "Mercado sin señal clara"}

    def simular_trade(self, precio_entrada, precio_salida, tipo="LONG"):
        """
        Simulador de ganancias/pérdidas para la Fase A.
        """
        if tipo == "LONG":
            resultado = (precio_salida - precio_entrada) / precio_entrada
        
        print(f"📊 SIMULACIÓN: Entrada: {precio_entrada} | Salida: {precio_salida} | Rendimiento: {resultado:.2%}")
        return resultado
