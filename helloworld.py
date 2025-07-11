from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# === CONFIGURATION ===
# IMPORTANT: You should create a *new* bot via BotFather on Telegram
# and use its unique token here. Reusing a token from another active bot
# can cause conflicts.
TELEGRAM_TOKEN = '<token>' # Replace with your bot's token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()}! Send me /hello to see a response."
    )

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responds with 'world' when the command /hello is issued."""
    await update.message.reply_text("world")

def main() -> None:
    """Starts the bot."""
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("hello", hello_command))

    # Run the bot until the user presses Ctrl-C
    print("Bot started. Send /start or /hello to your bot.")
    application.run_polling()

if __name__ == "__main__":
    main()
