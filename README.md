# Telegram Bot Collection

A comprehensive collection of Telegram bots demonstrating various bot functionalities including messaging, media sharing, and intelligent conversation capabilities.

## 📋 Features

- **Simple Messaging**: Basic text message sending
- **Image Broadcasting**: Automated image sharing from various sources
- **Audio Broadcasting**: Local audio file distribution
- **Smart Replies**: AI-powered conversational responses using Q&A datasets
- **Message Monitoring**: Real-time message reading and processing
- **Motivational Messages**: Automated inspirational quote broadcasting

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- A Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- A Telegram Chat ID where messages will be sent

### Installation

1. **Clone or download this project**

2. **Install dependencies**:
   The required packages are already installed in this Replit environment:
   - `requests` - For HTTP API calls
   - `pandas` - For data processing
   - `python-dotenv` - For environment variable management

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file with your actual values:
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   TELEGRAM_CHAT_ID=your_chat_id_here
   MESSAGE_DELAY=3
   UPDATE_LIMIT=10
   ```

### Getting Your Bot Token and Chat ID

1. **Create a Bot**:
   - Message [@BotFather](https://t.me/botfather) on Telegram
   - Send `/newbot` and follow the instructions
   - Save the bot token provided

2. **Get Chat ID**:
   - Add your bot to a group or start a private chat
   - Send a message to the bot
   - Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Find the `chat.id` in the response

## 🤖 Available Bots

### 1. Simple Message Bot
**File**: `bots/simple_message_bot.py`

Sends a basic "Hello World" message to demonstrate fundamental messaging.

```bash
python bots/simple_message_bot.py
```

### 2. Image Broadcasting Bot
**File**: `bots/image_broadcaster.py`

Automatically broadcasts images from various sources with captions in a continuous loop.

**Features**:
- Multiple image sources (Unsplash, Cloudinary)
- Custom captions for each image
- Configurable delay between images
- Error handling and retry logic
- Cycle counting and statistics

```bash
python bots/image_broadcaster.py
```

### 3. Audio Broadcasting Bot
**File**: `bots/audio_broadcaster.py`

Sends audio files from the `assets/audio/` directory with captions.

**Supported formats**: .wav, .mp3, .ogg, .m4a

**Features**:
- Auto-discovers audio files from assets directory
- Generates friendly captions from filenames
- Validates file existence before sending
- Progress tracking and comprehensive error handling

```bash
python bots/audio_broadcaster.py
```

### 4. Video Broadcasting Bot
**File**: `bots/video_broadcaster.py`

Sends video files from the `assets/video/` directory with captions.

**Supported formats**: .mp4, .avi, .mkv, .mov, .webm

**Features**:
- Auto-discovers video files from assets directory
- Generates friendly captions from filenames
- Progress tracking and error handling

```bash
python bots/video_broadcaster.py
```

### 5. Media Showcase Bot
**File**: `bots/media_showcase.py`

Demonstrates all media types by sending a sample from each category.

**Features**:
- Sends 3 images, 2 audio files, and 1 video
- Shows comprehensive media capabilities
- Perfect for testing all media types quickly

```bash
python bots/media_showcase.py
```

### 6. Smart Reply Bot
**File**: `bots/smart_reply_bot.py`

Monitors incoming messages and provides intelligent responses using a Q&A dataset.

**Features**:
- Real-time message monitoring
- AI-powered responses using external dataset
- Exact and partial question matching
- Conversation logging
- Graceful fallback for unknown questions
- Reply-to-message functionality

```bash
python bots/smart_reply_bot.py
```

## 📁 Project Structure

```
.
├── assets/                     # Media assets directory
│   ├── images/                 # Image URLs and local image files
│   │   └── sample_images.txt   # Curated image URL collection
│   ├── audio/                  # Audio files (.wav, .mp3, .ogg, .m4a)
│   │   ├── ChillVibes.wav      # Sample audio files
│   │   ├── HourTriumph.wav
│   │   └── FantasyHeart.wav
│   └── video/                  # Video files (.mp4, .avi, .mkv, .mov, .webm)
├── bots/                       # Modern bot implementations
│   ├── simple_message_bot.py   # Basic messaging
│   ├── image_broadcaster.py    # Image broadcasting from assets
│   ├── audio_broadcaster.py    # Audio broadcasting from assets
│   ├── video_broadcaster.py    # Video broadcasting from assets
│   ├── media_showcase.py       # All media types demo
│   └── smart_reply_bot.py      # Intelligent conversations
├── asset_manager.py            # Media asset management
├── config.py                   # Configuration management
├── utils.py                    # Common utilities and base bot class
├── .env.example               # Environment variables template
├── README.md                  # This file
├── SECURITY.md               # Security guidelines
└── legacy_bots/              # Original bot implementations
    ├── bot-1.py              # Basic update fetching
    ├── bot-2.py              # Simple getUpdates
    ├── bot-3.py              # Enhanced update fetching
    ├── bot-send-msg.py       # Basic message sending
    ├── bot-img-send.py       # Image broadcasting (legacy)
    ├── bot-music-send.py     # Audio broadcasting (legacy)
    ├── bot-engage.py         # Smart replies (legacy)
    ├── bot-read-reply.py     # Message monitoring (legacy)
    └── bot-auto-msg.py       # Auto messaging (legacy)
```

## 🛠️ Configuration Options

All bots use the same configuration system via environment variables:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `TELEGRAM_BOT_TOKEN` | Your bot token from @BotFather | - | ✅ |
| `TELEGRAM_CHAT_ID` | Target chat ID for messages | - | ✅ |
| `MESSAGE_DELAY` | Delay between messages (seconds) | 3 | ❌ |
| `UPDATE_LIMIT` | Max updates to fetch at once | 10 | ❌ |

## 🔧 Advanced Usage

### Custom Bot Development

Use the `TelegramBot` base class from `utils.py` to create custom bots:

```python
from utils import TelegramBot

class MyCustomBot(TelegramBot):
    def __init__(self):
        super().__init__()
    
    def custom_functionality(self):
        # Your custom bot logic here
        result = self.send_message("Custom message")
        return result

# Usage
bot = MyCustomBot()
bot.custom_functionality()
```

### Error Handling

All bots include comprehensive error handling:
- Network connectivity issues
- Invalid API responses
- Missing files (for audio bot)
- Configuration errors
- Rate limiting

### Logging

Bots provide detailed console output including:
- Success/failure status with emojis
- Message counts and statistics
- Error descriptions
- Progress tracking

## 🔒 Security Considerations

- **Never commit your `.env` file** - Contains sensitive tokens
- **Use environment variables** - Keep credentials secure
- **Validate input** - All bots include input validation
- **Rate limiting** - Built-in delays prevent API abuse
- **Error handling** - Prevents token exposure in error messages

## 🧪 Testing

Test your configuration with the simple message bot:

```bash
python bots/simple_message_bot.py
```

If successful, you'll see:
```
✅ Message sent successfully: Hello Code World! 🤖
```

## 🐛 Troubleshooting

### Common Issues

1. **Configuration Error**:
   ```
   ❌ Configuration error: Invalid bot configuration
   ```
   **Solution**: Check your `.env` file and ensure `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are set correctly.

2. **Bot Token Invalid**:
   ```
   ❌ Failed to send message: Unauthorized
   ```
   **Solution**: Verify your bot token is correct and hasn't been revoked.

3. **Chat ID Invalid**:
   ```
   ❌ Failed to send message: Bad Request: chat not found
   ```
   **Solution**: Ensure the chat ID is correct and the bot has been added to the chat/group.

4. **Audio Files Missing**:
   ```
   ❌ Missing audio files: ChillVibes.wav, HourTriumph.wav, FantasyHeart.wav
   ```
   **Solution**: Ensure all required audio files are in the project root directory.

### Getting Help

1. Check the console output for detailed error messages
2. Verify your `.env` configuration
3. Test with the simple message bot first
4. Ensure your bot has proper permissions in the target chat

## 📚 API Reference

### TelegramBot Class Methods

- `send_message(text, reply_to_message_id=None)` - Send text message
- `send_photo(photo_url, caption="")` - Send image from URL
- `send_audio(audio_file_path, caption="")` - Send local audio file
- `get_updates(offset=None)` - Fetch new messages
- `wait(seconds=None)` - Wait with configurable delay

### Configuration Class

- `BotConfig.validate()` - Validate configuration
- `BotConfig.get_api_url(method)` - Get API endpoint URL

## 🤝 Contributing

1. Follow the existing code structure
2. Add proper error handling
3. Include docstrings and comments
4. Test your changes
5. Update documentation

## 📄 License

This project is provided as-is for educational and demonstration purposes.

## 🔗 Useful Links

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [BotFather - Create New Bots](https://t.me/botfather)
- [Telegram Bot API - Getting Updates](https://core.telegram.org/bots/api#getting-updates)
- [Python Requests Documentation](https://docs.python-requests.org/)

---

**Made with ❤️ for the Telegram Bot Community**