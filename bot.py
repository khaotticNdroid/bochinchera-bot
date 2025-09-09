from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # safer: read token from environment variable

BOCHINCHE_RESPONSES = [
    "👀 Ay nooo, ¿supiste lo de Samuel? Candela 🔥",
    "🍿 César tiene cuento nuevo, prepárate...",
    "💅 Abi anda dejando bochinche por todos lados.",
    "🙊 Mija, si yo hablara… ¡ah no espera, sí hablo!",
]

async def bochinche(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)
    response = random.choice(BOCHINCHE_RESPONSES)
    if question:
        await update.message.reply_text(f"🤔 Sobre *{question}*: {response}", parse_mode="Markdown")
    else:
        await update.message.reply_text("Dime el bochinche con /bochinche seguido de tu pregunta 💬")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("bochinche", bochinche))
    app.run_polling()

if name == "main":
    main()