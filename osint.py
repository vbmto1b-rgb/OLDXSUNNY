# bot.py
# Developer: @TEAMK0RN

import os
import re
from urllib.parse import quote_plus

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEVELOPER = "@TEAMK0RN"

if not BOT_TOKEN:
    raise RuntimeError("8722297226:AAGdjJpTp02xFwDpttop_a93gLIDjHVL-9g")


def normalize_number(text: str):
    # Remove spaces, + and other separators
    number = re.sub(r"\D", "", text)

    if len(number) != 12:
        return None

    return number


def result_message(number: str) -> str:
    encoded = quote_plus(number)

    google = f"https://www.google.com/search?q=%22{encoded}%22"
    bing = f"https://www.bing.com/search?q=%22{encoded}%22"
    duck = f"https://duckduckgo.com/?q=%22{encoded}%22"

    return (
        "⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡\n\n"
        "🔍 SEARCH RESULTS\n"
        f"📊 Query: {number}\n"
        "📊 Total Sources: 3\n"
        "📊 Total Records: 3\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"

        "[1]\n"
        "📁 🌐 Google\n"
        "📝 Public web-search results\n"
        f"   • Query: {number}\n"
        "   • Type: Public web search\n\n"

        "[2]\n"
        "📁 🌐 Bing\n"
        "📝 Public web-search results\n"
        f"   • Query: {number}\n"
        "   • Type: Public web search\n\n"

        "[3]\n"
        "📁 🌐 DuckDuckGo\n"
        "📝 Public web-search results\n"
        f"   • Query: {number}\n"
        "   • Type: Public web search\n\n"

        "◆ ◇ ◆ ◇ ◆ ◇ ◆ ◇\n"
        "📄 Page 1 | Records 1-3 of 3\n"
        f"👨‍💻 Developer: {DEVELOPER}\n"
        "⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡"
    ), [
        [
            InlineKeyboardButton("🔎 Google", url=google),
            InlineKeyboardButton("🔎 Bing", url=bing),
        ],
        [
            InlineKeyboardButton("🔎 DuckDuckGo", url=duck),
        ],
    ]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚡ Welcome!\n\n"
        "12-digit number bhejo.\n"
        "Example: +919997284829\n\n"
        "The + sign automatically remove ho jayega.\n\n"
        f"👨‍💻 Developer: {DEVELOPER}"
    )


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    number = normalize_number(text)

    if not number:
        await update.message.reply_text(
            "❌ Invalid input.\n\n"
            "Exactly 12 digits required.\n"
            "Example: 919997284829"
        )
        return

    message, keyboard = result_message(number)

    await update.message.reply_text(
        message,
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            search
        )
    )

    print("🤖 Bot started...")
    print(f"👨‍💻 Developer: {DEVELOPER}")

    app.run_polling()


if __name__ == "__main__":
    main()

requirements.txt

python-telegram-bot>=21.0

Run

pip install -r requirements.txt

Linux/VPS/Render/Railway par:

export BOT_TOKEN="8722297226:AAGdjJpTp02xFwDpttop_a93gLIDjHVL-9g"
python bot.py

Windows:

set BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
python bot.py

Bot ko Telegram mein "/start" bhejo, phir:

+919997284829

Bot ise internally:

919997284829

mein convert karega.