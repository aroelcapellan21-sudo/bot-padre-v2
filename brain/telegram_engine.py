import telebot

# --- CONFIGURACIÓN DE SEGURIDAD ---
# Pon tu token entre las comillas
TOKEN = "7991523120:AAGeQYuWAdkVcNUFWwa7h71dmx9S_s1qZFA" 

# IDs numéricos corregidos (IMPORTANTE: Sin comillas para que funcionen)
ADMIN_YAYO = 6391483842
ADMIN_SOCIA = 6953926084
# ----------------------------------

bot = telebot.TeleBot(TOKEN)

def enviar_aviso(mensaje):
    """Envía un reporte a los supervisores."""
    try:
        # Envío directo usando los números corregidos
        bot.send_message(ADMIN_YAYO, f"🤖 [Z-BOT PADRE]:\n{mensaje}")
        bot.send_message(ADMIN_SOCIA, f"🤖 [Z-BOT PADRE]:\n{mensaje}")
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}")

def iniciar_escucha():
    """Activa la respuesta a comandos."""
    @bot.message_handler(commands=['start', 'hola'])
    def saludar(message):
        bot.reply_to(message, "Saludos, Supervisor. Z-Bot está en línea 🇩🇴.")

    @bot.message_handler(commands=['status'])
    def enviar_status(message):
        bot.reply_to(message, "Estado: Operativo. Motor: Kraken. ✅")

    print("📢 Voz de Telegram activada...")
    bot.polling(non_stop=True, timeout=20)
