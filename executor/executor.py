"""
executor/executor.py
EL EJECUTOR

Este módulo:
- NO decide
- NO analiza
- NO interpreta

Solo ejecuta órdenes que ya son legales.
"""

from shared.schema import validate_signal, SignalValidationError


def execute(signal: dict, signal_path: str) -> None:
    """
    Ejecuta una señal solo si es legal.
    Si no lo es, muere legalmente.
    """
    try:
        validate_signal(signal)
    except SignalValidationError as e:
        print(f"[EJECUTOR] Señal rechazada (MUERTE LEGAL): {e}")
        return

    print("[EJECUTOR] Señal válida. Ejecutando orden:")
    print(signal)

    # Aquí irá la ejecución real o simulada (más adelante)
