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

        # 1. FILTRO DE TENDENCIA (EMA 200)
        alcista = precio > ema_200 and ema_50 > ema_200
        bajista = precio < ema_200 and ema_50 < ema_200

        # 2. EVALUACIÓN DE ENTRADAS
        # --- ESCENARIO COMPRA (LONG) ---
        if alcista:
            # Pullback a EMA 50 y RSI entre 40 y 50
            if precio <= (ema_50 * 1.002) and (40 <= rsi <= 50):
                return self._crear_orden("LONG", precio, "Pullback + RSI Alcista")

        # --- ESCENARIO VENTA (SHORT) ---
        elif bajista:
            # Pullback a EMA 50 y RSI entre 50 y 60
            if precio >= (ema_50 * 0.998) and (50 <= rsi <= 60):
                return self._crear_orden("SHORT", precio, "Pullback + RSI Bajista")

        # 3. FILTRO DE RANGO (Si el precio cruza la EMA 200 frecuentemente)
        return {"accion": "WAIT", "motivo": "Buscando oportunidad clara"}

    def _crear_orden(self, tipo, precio, motivo):
        """Calcula SL/TP y formatea la salida"""
        if tipo == "LONG":
            sl = precio * (1 - self.config["sl_percent"])
            tp = precio + ((precio - sl) * self.config["tp_ratio"])
        else: # SHORT
            sl = precio * (1 + self.config["sl_percent"])
            tp = precio - ((sl - precio) * self.config["tp_ratio"])

        return {
            "symbol": self.symbol,
            "accion": tipo,
            "entrada": round(precio, 5),
            "sl": round(sl, 5),
            "tp": round(tp, 5),
            "motivo": motivo,
            "estado": "PENDIENTE_AUDITORIA" # Regla de la Matrix
        }
