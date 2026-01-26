import telebot

# --- CONFIGURACIÓN DEFINITIVA ---
# Pon tu Token real aquí (mantén las comillas)
TOKEN = "7991523120:AAGeQYuWAdkVcNUFWwa7h71dmx9S_s1qZFA" 

# IDs correctos (SIN COMILLAS para evitar Error 400)
ADMIN_YAYO = 6578945006
ADMIN_SOCIA = 6533031969
# ----------------------------------

bot = telebot.TeleBot(TOKEN)

def enviar_aviso(mensaje):
    """Envía un reporte directo a Luis y Estefania."""
    try:
        # Envío a Luis
        bot.send_message(ADMIN_YAYO, f"🤖 [Z-BOT PADRE]:\n{mensaje}")
        # Envío a Estefania
        bot.send_message(ADMIN_SOCIA, f"🤖 [Z-BOT PADRE]:\n{mensaje}")
    except Exception as e:
        print(f"❌ Error de conexión con Telegram: {e}")

def iniciar_escucha():
    """Activa los comandos para interactuar con el bot."""
    @bot.message_handler(commands=['start', 'hola'])
    def saludar(message):
        bot.reply_to(message, "Saludos, Supervisor. Z-Bot está en línea 🇩🇴.")

    @bot.message_handler(commands=['status'])
    def enviar_status(message):
        bot.reply_to(message, "Estado: Operativo. Motor: Kraken. ✅")

    print("📢 Voz de Telegram activada...")
    bot.polling(non_stop=True, timeout=20)
