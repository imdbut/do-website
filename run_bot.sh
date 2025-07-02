#!/bin/bash

# Telegram Bot Runner Script
# This script helps set up and run the Telegram bot

echo "🤖 Starting Telegram Bot..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip3."
    exit 1
fi

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ requirements.txt not found. Please ensure you're in the correct directory."
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found."
    echo "📝 Please create a .env file with your bot token:"
    echo "   1. Copy .env.example to .env"
    echo "   2. Edit .env and add your TELEGRAM_BOT_TOKEN"
    echo ""
    echo "💡 Example:"
    echo "   cp .env.example .env"
    echo "   # Then edit .env with your token"
    exit 1
fi

# Source environment variables
echo "🔧 Loading environment variables..."
set -a
source .env
set +a

# Check if token is set
if [ -z "$TELEGRAM_BOT_TOKEN" ]; then
    echo "❌ TELEGRAM_BOT_TOKEN is not set in .env file."
    echo "💡 Please edit .env and add your bot token from @BotFather"
    exit 1
fi

# Run the bot
echo "🚀 Starting bot..."
echo "📱 Your bot should now be responsive on Telegram!"
echo "🛑 Press Ctrl+C to stop the bot"
echo ""

python3 bot.py