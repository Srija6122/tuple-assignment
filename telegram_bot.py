from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8735278291:AAF_qUbB2-JPGD_npfymOEwgVVahcyY7lfc"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Use /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Welcome message\n/help - Show commands\n/echo <message> - Echo your message"
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        message = " ".join(context.args)
        await update.message.reply_text(message)
    else:
        await update.message.reply_text("Please provide a message.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("echo", echo))

print("Bot is running...")
app.run_polling()