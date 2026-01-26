import telebot

# --- CONFIGURACIÓN AUTOMATIZADA ---
# Pega tu token de Telegram entre las comillas abajo
TOKEN = "7991523120:AAGeQYuWAdkVcNUFWwa7h71dmx9S_s1qZFA" 

# IDs de los supervisores cargados desde el registro
ADMIN_YAYO = "6391483842"
ADMIN_SOCIA = "6953926084"
# ----------------------------------

bot = telebot.TeleBot(TOKEN)

def enviar_aviso(mensaje):
    """Envía un reporte rápido a los supervisores."""
    try:
        # Envío a Yayo
        bot.send_message(ADMIN_YAYO, f"🤖 [Z-BOT PADRE]:\n{mensaje}")
        # Envío a la Socia
        bot.send_message(ADMIN_SOCIA, f"🤖 [Z-BOT PADRE]:\n{mensaje}")
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}")

def iniciar_escucha():
    """Activa la capacidad del bot para responderte."""
    @bot.message_handler(commands=['start', 'hola'])
    def saludar(message):
        bot.reply_to(message, "Saludos, Supervisor. El Ecosistema Z-Bot está en línea y vigilando el mercado. 🇩🇴")

    @bot.message_handler(commands=['status'])
    def enviar_status(message):
        bot.reply_to(message, "Estado: Estable. Motor: Kraken. Memoria: Activa. ✅")

    print("📢 Voz de Telegram activada...")
    bot.polling(non_stop=True, timeout=20)
