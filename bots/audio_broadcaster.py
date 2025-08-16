#!/usr/bin/env python3
"""
Audio Broadcasting Bot
Sends audio files from the local directory with proper error handling.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import TelegramBot
from asset_manager import AssetManager

def main():
    """Broadcast audio files"""
    try:
        bot = TelegramBot()
        asset_manager = AssetManager()
        
        print("🎵 Starting Audio Broadcasting Bot...")
        
        # Load audio files from assets
        audio_files = asset_manager.get_audio_files()
        
        if not audio_files:
            print("❌ No audio files found in assets/audio directory")
            print("Please add audio files (.wav, .mp3, .ogg, .m4a) to assets/audio/")
            return
        
        print(f"📁 Found {len(audio_files)} audio files in assets")
        print(f"📨 Will send audio files to chat {bot.config.chat_id}")
        
        sent_count = 0
        
        for i, audio in enumerate(audio_files, 1):
            print(f"📤 Sending audio {i}/{len(audio_files)}: {audio['filename']}")
            
            result = bot.send_audio(audio["file"], audio["caption"])
            
            if result.get("ok"):
                sent_count += 1
                print(f"✅ Audio sent successfully: {audio['filename']}")
            else:
                error_msg = result.get("error", "Unknown error")
                print(f"❌ Failed to send audio {audio['filename']}: {error_msg}")
            
            # Wait between audio files
            if i < len(audio_files):
                print(f"⏳ Waiting {bot.config.message_delay} seconds...")
                bot.wait()
        
        print(f"\n🎉 Audio broadcasting completed! Sent {sent_count}/{len(audio_files)} files")
        
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("Please check your .env file and ensure TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are set")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()