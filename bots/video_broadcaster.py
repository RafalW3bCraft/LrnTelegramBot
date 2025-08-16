#!/usr/bin/env python3
"""
Video Broadcasting Bot
Sends video files from the assets directory with proper error handling.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import TelegramBot
from asset_manager import AssetManager

def main():
    """Broadcast video files"""
    try:
        bot = TelegramBot()
        asset_manager = AssetManager()
        
        print("🎬 Starting Video Broadcasting Bot...")
        
        # Load video files from assets
        video_files = asset_manager.get_video_files()
        
        if not video_files:
            print("❌ No video files found in assets/video directory")
            print("Please add video files (.mp4, .avi, .mkv, .mov, .webm) to assets/video/")
            return
        
        print(f"📁 Found {len(video_files)} video files in assets")
        print(f"📨 Will send video files to chat {bot.config.chat_id}")
        
        sent_count = 0
        
        for i, video in enumerate(video_files, 1):
            print(f"📤 Sending video {i}/{len(video_files)}: {video['filename']}")
            
            result = bot.send_video(video["file"], video["caption"])
            
            if result.get("ok"):
                sent_count += 1
                print(f"✅ Video sent successfully: {video['filename']}")
            else:
                error_msg = result.get("error", "Unknown error")
                print(f"❌ Failed to send video {video['filename']}: {error_msg}")
            
            # Wait between video files
            if i < len(video_files):
                print(f"⏳ Waiting {bot.config.message_delay} seconds...")
                bot.wait()
        
        print(f"\n🎉 Video broadcasting completed! Sent {sent_count}/{len(video_files)} files")
        
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("Please check your .env file and ensure TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are set")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()