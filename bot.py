"""
Lordvincidev Telegram Bot
A Telegram bot for sharing coding tips, projects, and Termux tutorials.
"""

import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable (for security)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8412802601:AAGdZ1luF5f3CxvVMohc94iXlhGM-Z_Veo8")

# ---------- Command Handlers ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a welcome message with the command list."""
    logger.info(f"Start command received from: {update.effective_user.username}")
    
    welcome_text = (
        "👋 Welcome to Lordvincidev's bot!\n\n"
        "🐦 I'm your pocket guide to mobile coding!\n\n"
        "I build full-stack web apps, automation scripts, and UI experiments "
        "entirely on my phone using Termux.\n\n"
        "🔵 Get daily HTML/CSS/JS snippets\n"
        "🔵 See my live projects\n"
        "🔵 Learn Termux tricks\n"
        "🔵 Python automation demos\n\n"
        "Type /help to see all commands and start exploring! 🚀"
    )
    
    keyboard = [
        [InlineKeyboardButton("📢 Latest Post", callback_data="latest")],
        [InlineKeyboardButton("💻 Current Project", callback_data="project")],
        [InlineKeyboardButton("📘 Termux Setup", callback_data="termux")],
        [InlineKeyboardButton("🔧 Setup Guide", callback_data="setup")],
        [InlineKeyboardButton("✉️ Feedback", callback_data="feedback")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show all available commands."""
    help_text = (
        "📋 *Available Commands:*\n\n"
        "/start - Welcome & about me\n"
        "/help - Show all commands\n"
        "/latest - My newest social media post\n"
        "/project - What I'm building now\n"
        "/termux - My Termux setup guide\n"
        "/html - HTML snippet of the day\n"
        "/css - CSS tip of the day\n"
        "/js - JavaScript challenge\n"
        "/python - Python script demo\n"
        "/github - My GitHub repositories\n"
        "/setup - How to code like me on your phone\n"
        "/feedback - Send me a message"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

async def latest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show latest social media post."""
    await update.message.reply_text(
        "📱 *My latest post:*\n"
        "[Check out my latest update on Twitter/X](https://twitter.com/yourusername)",
        parse_mode="Markdown"
    )

async def project(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show current project."""
    await update.message.reply_text(
        "🚧 *Current Project:*\n"
        "I'm building a Telegram bot for developers! 🚀\n\n"
        "Follow my progress on GitHub: [github.com/yourusername](https://github.com/yourusername)",
        parse_mode="Markdown"
    )

async def termux(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show Termux setup guide."""
    termux_guide = (
        "📲 *Termux Setup Guide*\n\n"
        "1️⃣ Install Termux from F-Droid (not Play Store!)\n"
        "2️⃣ Update packages:\n"
        "   `pkg update && pkg upgrade`\n"
        "3️⃣ Install Python:\n"
        "   `pkg install python`\n"
        "4️⃣ Install pip:\n"
        "   `pkg install python-pip`\n"
        "5️⃣ Install required libraries:\n"
        "   `pip install python-telegram-bot`\n"
        "6️⃣ You're ready to code! 🎉"
    )
    await update.message.reply_text(termux_guide, parse_mode="Markdown")

async def html(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Share HTML snippet of the day."""
    await update.message.reply_text(
        "🌐 *HTML Snippet of the Day:*\n\n"
        "```html\n"
        "<!DOCTYPE html>\n"
        "<html>\n"
        "<head>\n"
        "    <title>My Page</title>\n"
        "</head>\n"
        "<body>\n"
        "    <button onclick=\"alert('Hello!')\">Click Me</button>\n"
        "</body>\n"
        "</html>\n"
        "```",
        parse_mode="Markdown"
    )

async def css(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Share CSS tip of the day."""
    await update.message.reply_text(
        "🎨 *CSS Tip of the Day:*\n\n"
        "Use Flexbox for responsive layouts:\n"
        "```css\n"
        ".container {\n"
        "    display: flex;\n"
        "    justify-content: center;\n"
        "    align-items: center;\n"
        "    gap: 20px;\n"
        "    flex-wrap: wrap;\n"
        "}\n"
        "```",
        parse_mode="Markdown"
    )

async def js(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Share JavaScript challenge."""
    await update.message.reply_text(
        "🧩 *JavaScript Challenge:*\n\n"
        "Write a function that reverses a string without using `.reverse()`.\n\n"
        "```javascript\n"
        "// Example:\n"
        "function reverseString(str) {\n"
        "    // Your code here\n"
        "}\n"
        "\n"
        "// Expected output: 'olleh'\n"
        "console.log(reverseString('hello'));\n"
        "```\n\n"
        "Share your solution with me! 💡",
        parse_mode="Markdown"
    )

async def python(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Share Python script demo."""
    await update.message.reply_text(
        "🐍 *Python Script Demo:*\n\n"
        "A simple web scraper:\n"
        "```python\n"
        "import requests\n"
        "from bs4 import BeautifulSoup\n"
        "\n"
        "def scrape_website(url):\n"
        "    response = requests.get(url)\n"
        "    soup = BeautifulSoup(response.text, 'html.parser')\n"
        "    return soup.title.string\n"
        "\n"
        "print(scrape_website('https://example.com'))\n"
        "```",
        parse_mode="Markdown"
    )

async def github(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show GitHub repositories."""
    await update.message.reply_text(
        "🐙 *My GitHub Repositories:*\n\n"
        "Check out my projects:\n"
        "🔹 [telegram-bot](https://github.com/yourusername/telegram-bot)\n"
        "🔹 [termux-setup](https://github.com/yourusername/termux-setup)\n"
        "🔹 [python-scripts](https://github.com/yourusername/python-scripts)\n"
        "🔹 [web-projects](https://github.com/yourusername/web-projects)\n\n"
        "⭐ Star my repos if you find them useful!",
        parse_mode="Markdown"
    )

async def setup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show mobile coding setup guide."""
    setup_guide = (
        "📱 *How to Code Like Me on Your Phone*\n\n"
        "1️⃣ Install Termux from F-Droid\n"
        "2️⃣ Install Python:\n"
        "   `pkg install python`\n"
        "3️⃣ Install a code editor:\n"
        "   `pkg install vim` or use Acode app\n"
        "4️⃣ Clone my setup scripts:\n"
        "   `git clone https://github.com/yourusername/setup-scripts`\n"
        "5️⃣ Start building! 🚀"
    )
    await update.message.reply_text(setup_guide, parse_mode="Markdown")

async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle feedback."""
    await update.message.reply_text(
        "✉️ *Send me a message:*\n\n"
        "You can reach me at:\n"
        "📧 email@example.com\n"
        "🐦 [Twitter](https://twitter.com/yourusername)\n"
        "💬 [Telegram](https://t.me/yourusername)\n\n"
        "I'd love to hear from you! 💬",
        parse_mode="Markdown"
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle inline button clicks."""
    query = update.callback_query
    await query.answer()
    
    data = query.data
    logger.info(f"Button clicked: {data}")
    
    responses = {
        "latest": "📱 My latest post: [Check my Twitter/X](https://twitter.com/yourusername)",
        "project": "🚧 Current project: Building this bot! Check my GitHub.",
        "termux": "📲 Termux Guide: `pkg update && pkg upgrade` then `pkg install python`",
        "setup": "📱 Mobile Coding Setup: Termux + Python + Vim",
        "feedback": "✉️ Reach me at email@example.com or @yourusername"
    }
    
    await query.edit_message_text(
        f"🔹 {responses.get(data, 'Coming soon!')}",
        parse_mode="Markdown"
    )

def main():
    """Main function to run the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("latest", latest))
    application.add_handler(CommandHandler("project", project))
    application.add_handler(CommandHandler("termux", termux))
    application.add_handler(CommandHandler("html", html))
    application.add_handler(CommandHandler("css", css))
    application.add_handler(CommandHandler("js", js))
    application.add_handler(CommandHandler("python", python))
    application.add_handler(CommandHandler("github", github))
    application.add_handler(CommandHandler("setup", setup))
    application.add_handler(CommandHandler("feedback", feedback))

    # Register callback for inline keyboard buttons
    application.add_handler(CallbackQueryHandler(button_callback))

    # Start the bot
    logger.info("🤖 Bot is starting...")
    print("🤖 Bot is running... Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()