import telebot

# --- CONFIGURACIÓN DE SEGURIDAD ---
# Pega aquí el token que te dio BotFather (este sí lleva comillas)
TOKEN = "7991523120:AAGeQYuWAdkVcNUFWwa7h71dmx9S_s1qZFA" 

# IDs numéricos corregidos (SIN COMILLAS para evitar el Error 400)
ADMIN_YAYO = 6391483842
ADMIN_SOCIA = 6953926084
# ----------------------------------

bot = telebot.TeleBot(TOKEN)

def enviar_aviso(mensaje):
    """Función para que el bot les escriba proactivamente."""
    try:
        # Reporte a Yayo
        bot.send_message(ADMIN_YAYO, f"🤖 [Z-BOT PADRE]:\n{mensaje}")
        # Reporte a la Socia
        bot.send_message(ADMIN_SOCIA, f"🤖 [Z-BOT PADRE]:\n{mensaje}")
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}")

def iniciar_escucha():
    """Para que el bot responda cuando ustedes le escriban."""
    @bot.message_handler(commands=['start', 'hola'])
    def saludar(message):
        bot.reply_to(message, "Saludos, Supervisor. Z-Bot está en línea desde RD 🇩🇴. Estoy vigilando el Quinteto en Kraken.")

    @bot.message_handler(commands=['status'])
    def enviar_status(message):
        bot.reply_to(message, "Estado: Operativo. Motor: Kraken. Memoria: Activa. ✅")

    print("📢 Voz de Telegram activada y esperando órdenes...")
    bot.polling(non_stop=True, timeout=20)
