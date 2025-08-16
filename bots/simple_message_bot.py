#!/usr/bin/env python3
"""
Simple Message Bot
Sends a basic "Hello World" message to demonstrate basic messaging functionality.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import TelegramBot

def main():
    """Send a simple hello message"""
    try:
        bot = TelegramBot()
        
        # Send hello message
        result = bot.send_message("Hello Code World! 🤖")
        
        if result.get("ok"):
            print(f"✅ Message sent successfully: {result['result']['text']}")
        else:
            print(f"❌ Failed to send message: {result.get('error', 'Unknown error')}")
            
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("Please check your .env file and ensure TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are set")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()