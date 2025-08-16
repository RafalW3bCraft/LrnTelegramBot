"""
Utility functions for Telegram Bot Collection
Common functions used across multiple bot scripts
"""
import requests
import json
import time
from typing import Dict, List, Optional, Any
from config import BotConfig

class TelegramBot:
    """Base class for Telegram bots with common functionality"""
    
    def __init__(self):
        self.config = BotConfig()
        if not self.config.validate():
            raise ValueError("Invalid bot configuration")
    
    def send_message(self, text: str, reply_to_message_id: Optional[int] = None) -> Dict[str, Any]:
        """Send a text message to the configured chat"""
        url = self.config.get_api_url("sendMessage")
        if not url:
            return {"ok": False, "error": "Invalid configuration"}
        
        params = {
            "chat_id": self.config.chat_id,
            "text": text
        }
        if reply_to_message_id:
            params["reply_to_message_id"] = reply_to_message_id
        
        try:
            response = requests.get(url, data=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error sending message: {e}")
            return {"ok": False, "error": str(e)}
    
    def send_photo(self, photo_url: str, caption: str = "") -> Dict[str, Any]:
        """Send a photo from URL to the configured chat"""
        url = self.config.get_api_url("sendPhoto")
        if not url:
            return {"ok": False, "error": "Invalid configuration"}
        
        params = {
            "chat_id": self.config.chat_id,
            "photo": photo_url,
            "caption": caption
        }
        
        try:
            response = requests.get(url, data=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error sending photo: {e}")
            return {"ok": False, "error": str(e)}
    
    def send_audio(self, audio_file_path: str, caption: str = "") -> Dict[str, Any]:
        """Send an audio file to the configured chat"""
        url = self.config.get_api_url("sendAudio")
        if not url:
            return {"ok": False, "error": "Invalid configuration"}
        
        params = {
            "chat_id": self.config.chat_id,
            "caption": caption
        }
        
        try:
            with open(audio_file_path, 'rb') as audio_file:
                files = {"audio": audio_file}
                response = requests.post(url, data=params, files=files)
                response.raise_for_status()
                return response.json()
        except (requests.RequestException, IOError) as e:
            print(f"Error sending audio: {e}")
            return {"ok": False, "error": str(e)}
    
    def send_video(self, video_file_path: str, caption: str = "") -> Dict[str, Any]:
        """Send a video file to the configured chat"""
        url = self.config.get_api_url("sendVideo")
        if not url:
            return {"ok": False, "error": "Invalid configuration"}
        
        params = {
            "chat_id": self.config.chat_id,
            "caption": caption
        }
        
        try:
            with open(video_file_path, 'rb') as video_file:
                files = {"video": video_file}
                response = requests.post(url, data=params, files=files)
                response.raise_for_status()
                return response.json()
        except (requests.RequestException, IOError) as e:
            print(f"Error sending video: {e}")
            return {"ok": False, "error": str(e)}
    
    def get_updates(self, offset: Optional[int] = None) -> Dict[str, Any]:
        """Get updates from Telegram"""
        url = self.config.get_api_url("getUpdates")
        if not url:
            return {"ok": False, "error": "Invalid configuration"}
        
        params = {
            "limit": self.config.update_limit
        }
        if offset:
            params["offset"] = offset
        
        try:
            response = requests.get(url, data=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error getting updates: {e}")
            return {"ok": False, "error": str(e)}
    
    def wait(self, seconds: Optional[int] = None):
        """Wait for specified time or default delay"""
        delay = seconds if seconds is not None else self.config.message_delay
        time.sleep(delay)