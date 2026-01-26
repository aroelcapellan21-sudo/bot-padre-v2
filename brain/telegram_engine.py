import telebot
from brain.data_engine import fetch_candles, preparar_datos_mercado, QUINTETO

# --- CONFIGURACIÓN ---
TOKEN = "7991523120:AAGeQYuWAdkVcNUFWwa7h71dmx9S_s1qZFA" 
ADMIN_YAYO = 6578945006
ADMIN_SOCIA = 6533031969
# ---------------------

bot = telebot.TeleBot(TOKEN)

def enviar_aviso(mensaje):
    """Solo para errores críticos del sistema."""
    try:
        bot.send_message(ADMIN_YAYO, f"🤖 [Z-BOT]: {mensaje}")
    except Exception as e:
        print(f"❌ Error Telegram: {e}")

@bot.message_handler(commands=['reporte', 'status'])
def enviar_reporte_manual(message):
    """Esta función solo se activa si tú escribes /reporte en Telegram."""
    if message.chat.id not in [ADMIN_YAYO, ADMIN_SOCIA]:
        return

    bot.reply_to(message, "📊 Generando reporte del Quinteto para el Supervisor...")
    
    informe = "📈 **ESTADO ACTUAL DEL MERCADO**\n\n"
    for symbol in QUINTETO:
        velas = fetch_candles(symbol)
        if velas:
            df = preparar_datos_mercado(symbol, velas)
            if not df.empty:
                precio = df['close'].iloc[-1]
                rsi = round(df['rsi'].iloc[-1], 2)
                informe += f"🔹 {symbol}: ${precio} | RSI: {rsi}\n"
    
    bot.send_message(message.chat.id, informe)

def iniciar_escucha():
    print("📢 Z-Bot esperando tus órdenes en Telegram...")
    bot.polling(non_stop=True)
