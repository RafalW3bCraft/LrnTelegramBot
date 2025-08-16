#!/usr/bin/env python3
"""
Media Showcase Bot
Demonstrates all media types: images, audio, and video from assets.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import TelegramBot
from asset_manager import AssetManager

def main():
    """Showcase all media types"""
    try:
        bot = TelegramBot()
        asset_manager = AssetManager()
        
        print("🎭 Starting Media Showcase Bot...")
        
        # Check available assets
        asset_counts = asset_manager.check_assets()
        print(f"📊 Available assets: {asset_counts['images']} images, {asset_counts['audio']} audio, {asset_counts['video']} video")
        
        if not any(asset_counts.values()):
            print("❌ No media assets found in assets directory")
            return
        
        total_sent = 0
        
        # Send images
        if asset_counts['images'] > 0:
            print("\n📸 Broadcasting Images...")
            images = asset_manager.get_image_urls()
            for i, image in enumerate(images[:3], 1):  # Send first 3 images
                print(f"📤 Sending image {i}: {image['source']}")
                result = bot.send_photo(image["url"], image["caption"])
                if result.get("ok"):
                    total_sent += 1
                    print(f"✅ Image sent successfully")
                else:
                    print(f"❌ Failed to send image: {result.get('error', 'Unknown error')}")
                bot.wait()
        
        # Send audio files
        if asset_counts['audio'] > 0:
            print("\n🎵 Broadcasting Audio...")
            audio_files = asset_manager.get_audio_files()
            for i, audio in enumerate(audio_files[:2], 1):  # Send first 2 audio files
                print(f"📤 Sending audio {i}: {audio['filename']}")
                result = bot.send_audio(audio["file"], audio["caption"])
                if result.get("ok"):
                    total_sent += 1
                    print(f"✅ Audio sent successfully")
                else:
                    print(f"❌ Failed to send audio: {result.get('error', 'Unknown error')}")
                bot.wait()
        
        # Send video files
        if asset_counts['video'] > 0:
            print("\n🎬 Broadcasting Video...")
            video_files = asset_manager.get_video_files()
            for i, video in enumerate(video_files[:1], 1):  # Send first video
                print(f"📤 Sending video {i}: {video['filename']}")
                result = bot.send_video(video["file"], video["caption"])
                if result.get("ok"):
                    total_sent += 1
                    print(f"✅ Video sent successfully")
                else:
                    print(f"❌ Failed to send video: {result.get('error', 'Unknown error')}")
                bot.wait()
        
        print(f"\n🎉 Media showcase completed! Sent {total_sent} items total")
        
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("Please check your .env file and ensure TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are set")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()