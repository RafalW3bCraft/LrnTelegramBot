"""
Configuration module for Telegram Bot Collection
Handles environment variables and default settings
"""
import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class BotConfig:
    """Configuration class for Telegram bots"""
    
    def __init__(self):
        self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.getenv('TELEGRAM_CHAT_ID')
        self.message_delay = int(os.getenv('MESSAGE_DELAY', 3))
        self.update_limit = int(os.getenv('UPDATE_LIMIT', 10))
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}" if self.bot_token else None
    
    def validate(self) -> bool:
        """Validate required configuration"""
        if not self.bot_token:
            print("ERROR: TELEGRAM_BOT_TOKEN is required")
            return False
        if not self.chat_id:
            print("ERROR: TELEGRAM_CHAT_ID is required")
            return False
        return True
    
    def get_api_url(self, method: str) -> Optional[str]:
        """Get API URL for specific method"""
        if not self.base_url:
            return None
        return f"{self.base_url}/{method}"