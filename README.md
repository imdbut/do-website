# 🤖 Telegram Bot

A feature-rich Telegram bot built with Python that demonstrates various Bot API capabilities including command handling, inline keyboards, message processing, and file handling.

## ✨ Features

- **Command Handlers**: Multiple commands with different functionalities
- **Inline Keyboards**: Interactive buttons for quick actions
- **Message Processing**: Echo messages with analysis
- **File Handling**: Process photos and documents
- **Calculator**: Simple math expression evaluation
- **Weather**: Placeholder weather command (ready for API integration)
- **Jokes**: Random programming jokes
- **Error Handling**: Comprehensive error logging and handling

## 🚀 Quick Start

### 1. Create a Telegram Bot

1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` command
3. Choose a name for your bot (e.g., "My Awesome Bot")
4. Choose a username for your bot (must end with "bot", e.g., "myawesomebot")
5. Copy the HTTP API token you receive

### 2. Setup Environment

```bash
# Clone or download this repository
git clone <your-repo-url>
cd telegram-bot

# Install Python dependencies
pip install -r requirements.txt

# Set your bot token as an environment variable
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
```

### 3. Run the Bot

```bash
python bot.py
```

## 📋 Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `/start` | Show welcome message with quick action buttons | `/start` |
| `/help` | Display detailed help information | `/help` |
| `/time` | Get current date and time | `/time` |
| `/weather [city]` | Get weather info (placeholder) | `/weather London` |
| `/joke` | Get a random programming joke | `/joke` |
| `/calc [expression]` | Calculate math expressions | `/calc 2+2*3` |
| `/info` | Show bot information | `/info` |

## 🔧 Features Overview

### Command Handling
- Comprehensive command system with proper argument handling
- Input validation and error messages
- Case-sensitive commands with helpful usage examples

### Interactive Elements
- Inline keyboard buttons for quick actions
- Callback query handling for button interactions
- User-friendly navigation system

### Message Processing
- Text message echo with analysis (word count, character count, emoji detection)
- Photo handling with file information display
- Document processing with metadata extraction

### Calculator
- Safe math expression evaluation
- Support for basic operations: `+`, `-`, `*`, `/`, `**`, `()`
- Input validation to prevent code injection

### Error Handling
- Comprehensive error logging
- Graceful error recovery
- User-friendly error messages

## 🛠️ Configuration

### Environment Variables

- `TELEGRAM_BOT_TOKEN`: Your bot token from BotFather (required)

### Customization

You can easily extend the bot by:

1. **Adding new commands**: Create new methods and register them in `setup_handlers()`
2. **Integrating APIs**: Replace placeholder implementations (like weather) with real API calls
3. **Adding databases**: Store user data, preferences, or conversation history
4. **Extending file handling**: Add support for more file types or AI-powered analysis

## 📁 Project Structure

```
telegram-bot/
├── bot.py              # Main bot implementation
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .env              # Environment variables (create this file)
```

## 🔒 Security Features

- Input validation for calculator expressions
- Safe character filtering to prevent code injection
- Error handling to prevent crashes
- Logging for monitoring and debugging

## 🌟 Extension Ideas

Here are some ideas to extend the bot:

1. **Weather Integration**: 
   - Integrate with OpenWeatherMap API
   - Add location-based weather forecasts

2. **Database Integration**:
   - Store user preferences
   - Save conversation history
   - User statistics

3. **AI Features**:
   - Image recognition using OpenAI Vision
   - Chatbot responses using GPT
   - Text summarization

4. **Advanced Features**:
   - Scheduled messages
   - User authentication
   - Group management
   - Payment processing

## 🐛 Troubleshooting

### Common Issues

1. **Bot doesn't respond**:
   - Check if the token is correctly set
   - Verify the bot is running without errors
   - Check network connectivity

2. **Import errors**:
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version (3.8+ recommended)

3. **Permission errors**:
   - Ensure the bot has necessary permissions in group chats
   - Check if the bot is blocked by the user

### Logs

The bot logs important information to help with debugging:
- All updates and errors are logged with timestamps
- Check console output for error messages
- Enable debug logging by changing the logging level in `bot.py`

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the Telegram Bot API documentation
3. Create an issue in this repository

---

**Happy coding! 🚀**