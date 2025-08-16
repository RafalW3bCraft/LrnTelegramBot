#!/usr/bin/env python3
"""
Image Broadcasting Bot
Automatically sends a collection of images from various sources with captions.
Includes proper error handling and logging.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import TelegramBot
from asset_manager import AssetManager

def main():
    """Broadcast images continuously"""
    sent_count = 0
    cycle_count = 0
    
    try:
        bot = TelegramBot()
        asset_manager = AssetManager()
        
        # Load images from assets
        images = asset_manager.get_image_urls()
        
        print("🚀 Starting Image Broadcasting Bot...")
        print(f"📁 Loaded {len(images)} images from assets")
        print(f"📨 Will send images to chat {bot.config.chat_id}")
        
        while True:
            cycle_count += 1
            print(f"\n🔄 Cycle {cycle_count} - Broadcasting images...")
            
            for i, image in enumerate(images, 1):
                print(f"📤 Sending image {i}/{len(images)}: {image['source']}")
                
                result = bot.send_photo(image["url"], image["caption"])
                
                if result.get("ok"):
                    sent_count += 1
                    print(f"✅ Image sent successfully (Total: {sent_count})")
                else:
                    error_msg = result.get("error", "Unknown error")
                    print(f"❌ Failed to send image: {error_msg}")
                
                # Wait between images
                print(f"⏳ Waiting {bot.config.message_delay} seconds...")
                bot.wait()
                
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("Please check your .env file and ensure TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are set")
    except KeyboardInterrupt:
        print(f"\n🛑 Bot stopped by user. Total images sent: {sent_count}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print(f"Total images sent before error: {sent_count if 'sent_count' in locals() else 0}")

if __name__ == "__main__":
    main()