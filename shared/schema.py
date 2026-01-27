# shared/schema.py
# Ley universal de validación de señales
# Si una señal no cumple esto, muere legalmente.

from typing import Optional


REQUIRED_FIELDS = {
    "symbol": str,
    "price": float,
    "rsi": float,
    "timestamp": int,
    "source": str,
    "action": str,  # BUY o SELL
}

OPTIONAL_FIELDS = {
    "confidence": float,  # 0.0 a 1.0
}


ALLOWED_ACTIONS = {"BUY", "SELL"}


class SignalValidationError(Exception):
    pass


def validate_signal(signal: dict) -> bool:
    # Validar campos obligatorios
    for field, field_type in REQUIRED_FIELDS.items():
        if field not in signal:
            raise SignalValidationError(f"Falta campo obligatorio: {field}")

        if not isinstance(signal[field], field_type):
            raise SignalValidationError(
                f"Tipo incorrecto en '{field}': "
                f"esperado {field_type.__name__}, recibido {type(signal[field]).__name__}"
            )

    # Validar acción
    if signal["action"] not in ALLOWED_ACTIONS:
        raise SignalValidationError(
            f"Acción inválida: {signal['action']}"
        )

    # Validar campos opcionales
    for field, field_type in OPTIONAL_FIELDS.items():
        if field in signal:
            if not isinstance(signal[field], field_type):
                raise SignalValidationError(
                    f"Tipo incorrecto en '{field}': "
                    f"esperado {field_type.__name__}"
                )

            if field == "confidence":
                if not 0.0 <= signal[field] <= 1.0:
                    raise SignalValidationError(
                        "confidence debe estar entre 0.0 y 1.0"
                    )

    # Si llegó aquí, la señal vive
    return True
