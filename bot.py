#!/usr/bin/env python3
"""
Telegram Bot - A feature-rich bot with multiple commands and functionality
"""

import logging
import os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    CallbackQueryHandler,
    filters, 
    ContextTypes
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self, token: str):
        self.token = token
        self.application = Application.builder().token(token).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Set up all command and message handlers"""
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("time", self.time_command))
        self.application.add_handler(CommandHandler("weather", self.weather_command))
        self.application.add_handler(CommandHandler("joke", self.joke_command))
        self.application.add_handler(CommandHandler("calc", self.calc_command))
        self.application.add_handler(CommandHandler("info", self.info_command))
        
        # Callback query handler for inline keyboards
        self.application.add_handler(CallbackQueryHandler(self.button_handler))
        
        # Message handlers
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.echo_message))
        self.application.add_handler(MessageHandler(filters.PHOTO, self.photo_handler))
        self.application.add_handler(MessageHandler(filters.DOCUMENT, self.document_handler))
        
        # Error handler
        self.application.add_error_handler(self.error_handler)

    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        
        keyboard = [
            [InlineKeyboardButton("📚 Help", callback_data="help")],
            [InlineKeyboardButton("⏰ Current Time", callback_data="time")],
            [InlineKeyboardButton("😄 Random Joke", callback_data="joke")],
            [InlineKeyboardButton("ℹ️ Bot Info", callback_data="info")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        welcome_message = f"""
🤖 **Welcome {user.first_name}!**

I'm a feature-rich Telegram bot ready to help you!

**Available Commands:**
• /start - Show this welcome message
• /help - Get detailed help
• /time - Get current time
• /weather [city] - Get weather info (placeholder)
• /joke - Get a random joke
• /calc [expression] - Simple calculator
• /info - Bot information

You can also:
📝 Send me any text and I'll echo it back
📷 Send photos and I'll analyze them
📄 Send documents and I'll provide info

Click the buttons below to get started! 👇
        """
        
        await update.message.reply_text(
            welcome_message, 
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a help message when the command /help is issued."""
        help_text = """
🆘 **Detailed Help**

**Commands:**
• `/start` - Show welcome message with quick actions
• `/help` - Show this detailed help
• `/time` - Get current date and time
• `/weather [city]` - Get weather for a city (e.g., `/weather London`)
• `/joke` - Get a random programming joke
• `/calc [expression]` - Calculate math expressions (e.g., `/calc 2+2*3`)
• `/info` - Get information about this bot

**Features:**
📝 **Text Echo**: Send any text message and I'll echo it back with some analysis
📷 **Photo Analysis**: Send photos and I'll provide basic information
📄 **Document Info**: Send documents and I'll show file details
⌨️ **Inline Keyboards**: Use buttons for quick actions

**Tips:**
• Commands are case-sensitive
• Use `/calc` for basic math: +, -, *, /, **, (), etc.
• The weather command is a placeholder - integrate with a real weather API
• All your messages are logged for debugging purposes

Need more help? Contact the bot developer!
        """
        
        await update.message.reply_text(help_text, parse_mode='Markdown')

    async def time_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send current time when the command /time is issued."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_message = f"🕒 Current time: `{current_time}`"
        await update.message.reply_text(time_message, parse_mode='Markdown')

    async def weather_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Weather command (placeholder implementation)."""
        if not context.args:
            await update.message.reply_text(
                "❗ Please specify a city!\nUsage: `/weather London`",
                parse_mode='Markdown'
            )
            return
        
        city = ' '.join(context.args)
        # This is a placeholder - in a real implementation, you'd call a weather API
        weather_message = f"""
🌤️ **Weather for {city}**

Temperature: 22°C
Condition: Partly Cloudy
Humidity: 65%
Wind: 10 km/h

*Note: This is placeholder data. Integrate with a real weather API like OpenWeatherMap for actual data.*
        """
        
        await update.message.reply_text(weather_message, parse_mode='Markdown')

    async def joke_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a random programming joke."""
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
            "Why don't programmers like nature? It has too many bugs! 🌿🐛",
            "What's a programmer's favorite hangout place? Foo Bar! 🍺",
            "Why did the programmer quit his job? He didn't get arrays! 📊",
            "How do you comfort a JavaScript bug? You console it! 🎮",
            "Why do Java developers wear glasses? Because they can't C#! 👓",
            "What do you call a programmer from Finland? Nerdic! 🇫🇮"
        ]
        
        import random
        joke = random.choice(jokes)
        await update.message.reply_text(f"😄 {joke}")

    async def calc_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Simple calculator command."""
        if not context.args:
            await update.message.reply_text(
                "🔢 Please provide a math expression!\nUsage: `/calc 2+2*3`\n\nSupported operations: +, -, *, /, **, ()",
                parse_mode='Markdown'
            )
            return
        
        expression = ' '.join(context.args)
        
        try:
            # Basic security: only allow certain characters
            allowed_chars = set('0123456789+-*/().** ')
            if not all(c in allowed_chars for c in expression):
                await update.message.reply_text("❗ Invalid characters in expression. Only numbers and basic operators allowed.")
                return
            
            result = eval(expression)
            calc_message = f"🔢 **Calculator**\n\n`{expression} = {result}`"
            await update.message.reply_text(calc_message, parse_mode='Markdown')
            
        except Exception as e:
            await update.message.reply_text(f"❗ Error calculating expression: {str(e)}")

    async def info_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send bot information."""
        info_message = """
🤖 **Bot Information**

**Name:** Feature-Rich Telegram Bot
**Version:** 1.0.0
**Language:** Python 3.8+
**Library:** python-telegram-bot

**Features:**
✅ Command handling
✅ Inline keyboards
✅ Text echo with analysis
✅ Photo handling
✅ Document processing
✅ Error handling
✅ Logging

**Developer:** Your Name
**Source:** Available on GitHub
**Last Updated:** 2024

This bot demonstrates various Telegram Bot API features and can be extended with more functionality!
        """
        
        await update.message.reply_text(info_message, parse_mode='Markdown')

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle inline keyboard button presses."""
        query = update.callback_query
        await query.answer()
        
        if query.data == "help":
            await self.help_command(update, context)
        elif query.data == "time":
            await self.time_command(update, context)
        elif query.data == "joke":
            await self.joke_command(update, context)
        elif query.data == "info":
            await self.info_command(update, context)

    async def echo_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Echo user message with some analysis."""
        user_message = update.message.text
        user_name = update.effective_user.first_name
        
        # Simple message analysis
        word_count = len(user_message.split())
        char_count = len(user_message)
        has_emoji = any(ord(char) > 127 for char in user_message)
        
        echo_response = f"""
💬 **Message Echo**

**From:** {user_name}
**Message:** "{user_message}"

**Analysis:**
📊 Words: {word_count}
📏 Characters: {char_count}
😊 Contains emoji: {"Yes" if has_emoji else "No"}

*Tip: Try sending me commands starting with '/' for more features!*
        """
        
        await update.message.reply_text(echo_response, parse_mode='Markdown')

    async def photo_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle photo messages."""
        photo = update.message.photo[-1]  # Get highest resolution
        file_info = await context.bot.get_file(photo.file_id)
        
        photo_response = f"""
📷 **Photo Received!**

**File Info:**
• File ID: `{photo.file_id}`
• Size: {photo.width}x{photo.height}
• File Size: {file_info.file_size} bytes

*Note: In a full implementation, you could download and analyze the image content using AI services or image processing libraries.*
        """
        
        await update.message.reply_text(photo_response, parse_mode='Markdown')

    async def document_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle document messages."""
        document = update.message.document
        
        document_response = f"""
📄 **Document Received!**

**File Info:**
• Name: `{document.file_name}`
• Size: {document.file_size} bytes
• MIME Type: `{document.mime_type}`
• File ID: `{document.file_id}`

*Note: In a full implementation, you could process different document types, extract text, or perform other analysis.*
        """
        
        await update.message.reply_text(document_response, parse_mode='Markdown')

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Log errors caused by Updates."""
        logger.warning(f'Update {update} caused error {context.error}')

    def run(self):
        """Start the bot."""
        logger.info("Starting bot...")
        self.application.run_polling(allowed_updates=Update.ALL_TYPES)

def main():
    """Main function to run the bot."""
    # Get bot token from environment variable
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    
    if not token:
        print("❗ Error: TELEGRAM_BOT_TOKEN environment variable not found!")
        print("5384719653:AAFQhoSt8G6d4SZoecKhOG3D5KrCtIr4JOk")
        print("export TELEGRAM_BOT_TOKEN='your_bot_token_here'")
        return
    
    # Create and run bot
    bot = TelegramBot(token)
    bot.run()

if __name__ == '__main__':
    main()