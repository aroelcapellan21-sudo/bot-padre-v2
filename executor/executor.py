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

    try:
        import os
        import shutil

        filename = os.path.basename(signal_path)
        rejected_path = os.path.join("rejected", filename)

        shutil.move(signal_path, rejected_path)
        print(f"[EJECUTOR] Señal movida a rejected/: {filename}")

    except Exception as move_error:
        print(f"[EJECUTOR] ERROR moviendo señal a rejected/: {move_error}")

    return

    print("[EJECUTOR] Señal válida. Ejecutando orden:")
    print(signal)

    # Aquí irá la ejecución real o simulada (más adelante)
