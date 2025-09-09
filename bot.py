import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Command function
async def bochinche(update: Update, context: ContextTypes.DEFAULT_TYPE):
    respuestas = [
        "👀 Te tengo un bochinche fresquito...",
        "Ay nooo, ¿están listos para el drama? 😏",
        "🔥 Esto está mejor que una novela...",
        "🙊 No deberían saberlo, pero igual les cuento..."
    ]
    respuesta = random.choice(respuestas)
    await update.message.reply_text(respuesta)

# Main function
def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("⚠️ No BOT_TOKEN found. Did you set it in Render environment variables?")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("bochinche", bochinche))
    app.run_polling()

# Correct way to start the bot
if __name__ == "__main__":
    main()
