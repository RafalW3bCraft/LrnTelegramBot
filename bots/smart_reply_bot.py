#!/usr/bin/env python3
"""
Smart Reply Bot
Monitors incoming messages and provides intelligent responses using a Q&A dataset.
Includes conversation logging and graceful error handling.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from utils import TelegramBot

# Dataset URL for Q&A responses
QNA_DATASET_URL = 'https://raw.githubusercontent.com/vikasjha001/telegram/main/qna_chitchat_professional.tsv'

class SmartReplyBot(TelegramBot):
    """Enhanced bot with smart reply capabilities"""
    
    def __init__(self):
        super().__init__()
        self.df = None
        self.load_dataset()
    
    def load_dataset(self):
        """Load Q&A dataset from URL"""
        try:
            print("📚 Loading Q&A dataset...")
            self.df = pd.read_csv(QNA_DATASET_URL, sep="\t")
            print(f"✅ Dataset loaded successfully: {len(self.df)} Q&A pairs")
        except Exception as e:
            print(f"❌ Failed to load dataset: {e}")
            print("Bot will use default responses only")
    
    def find_answer(self, question: str) -> str:
        """Find answer for a given question"""
        if self.df is None:
            return "Sorry, I'm having trouble accessing my knowledge base right now."
        
        try:
            # Clean and normalize the question
            question_clean = question.lower().strip()
            
            # Look for exact match first
            exact_match = self.df.loc[self.df['Question'].str.lower() == question_clean]
            
            if not exact_match.empty:
                return exact_match.iloc[0]['Answer']
            
            # Look for partial matches
            partial_matches = self.df.loc[self.df['Question'].str.lower().str.contains(
                question_clean, case=False, na=False
            )]
            
            if not partial_matches.empty:
                return partial_matches.iloc[0]['Answer']
            
            # Default response for unknown questions
            return "Sorry, I couldn't understand your question. I'm still learning and trying to get better at answering! 🤖"
            
        except Exception as e:
            print(f"❌ Error finding answer: {e}")
            return "I'm having some technical difficulties. Please try again later."
    
    def process_message(self, message_data: dict):
        """Process incoming message and send reply"""
        try:
            if 'message' not in message_data or 'text' not in message_data['message']:
                return
            
            user_message = message_data['message']['text']
            message_id = message_data['message']['message_id']
            user_name = message_data['message'].get('from', {}).get('first_name', 'User')
            
            print(f"💬 Received from {user_name}: {user_message}")
            
            # Generate response
            answer = self.find_answer(user_message)
            
            # Send reply
            result = self.send_message(answer, reply_to_message_id=message_id)
            
            if result.get("ok"):
                print(f"✅ Reply sent: {answer}")
            else:
                error_msg = result.get("error", "Unknown error")
                print(f"❌ Failed to send reply: {error_msg}")
                
        except Exception as e:
            print(f"❌ Error processing message: {e}")
    
    def run(self):
        """Main bot loop"""
        print("🤖 Starting Smart Reply Bot...")
        print(f"👂 Listening for messages in chat {self.config.chat_id}")
        
        offset = 0
        message_count = 0
        
        try:
            while True:
                # Get updates
                updates = self.get_updates(offset)
                
                if not updates.get("ok"):
                    print(f"❌ Error getting updates: {updates.get('error', 'Unknown error')}")
                    self.wait(5)  # Wait longer on error
                    continue
                
                # Process each message
                for update in updates.get("result", []):
                    message_count += 1
                    print(f"\n📨 Processing message #{message_count}")
                    self.process_message(update)
                    
                    # Update offset to mark message as processed
                    offset = update["update_id"] + 1
                
                # Wait before next check
                self.wait(1)  # Check for new messages every second
                
        except KeyboardInterrupt:
            print(f"\n🛑 Bot stopped by user. Processed {message_count} messages")

def main():
    """Run the smart reply bot"""
    try:
        bot = SmartReplyBot()
        bot.run()
        
    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        print("Please check your .env file and ensure TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID are set")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()