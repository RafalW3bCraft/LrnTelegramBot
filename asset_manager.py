#!/usr/bin/env python3
"""
Asset Manager for Telegram Bot Collection
Handles loading and managing media assets from the assets folder
"""
import os
import glob
from typing import List, Dict, Optional

class AssetManager:
    """Manages media assets for bot operations"""
    
    def __init__(self, assets_dir: str = "assets"):
        self.assets_dir = assets_dir
        self.images_dir = os.path.join(assets_dir, "images")
        self.audio_dir = os.path.join(assets_dir, "audio")
        self.video_dir = os.path.join(assets_dir, "video")
    
    def get_image_urls(self) -> List[Dict[str, str]]:
        """Get list of image URLs with captions"""
        image_list_file = os.path.join(self.images_dir, "sample_images.txt")
        images = []
        
        if os.path.exists(image_list_file):
            with open(image_list_file, 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    line = line.strip()
                    if line and not line.startswith('#'):
                        images.append({
                            "url": line,
                            "caption": f"📸 Nature Scene #{i+1} - Curated Collection",
                            "source": "Unsplash Collection"
                        })
        
        # Fallback images if file doesn't exist
        if not images:
            images = [
                {
                    "url": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
                    "caption": "🌄 Mountain Landscape - Default Collection",
                    "source": "Default"
                },
                {
                    "url": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=800",
                    "caption": "🌊 Ocean View - Default Collection", 
                    "source": "Default"
                },
                {
                    "url": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800",
                    "caption": "🌲 Forest Path - Default Collection",
                    "source": "Default"
                }
            ]
        
        return images
    
    def get_audio_files(self) -> List[Dict[str, str]]:
        """Get list of local audio files with captions"""
        audio_files = []
        
        # Scan for audio files in assets/audio
        audio_patterns = ['*.wav', '*.mp3', '*.ogg', '*.m4a']
        for pattern in audio_patterns:
            files = glob.glob(os.path.join(self.audio_dir, pattern))
            for file_path in files:
                filename = os.path.basename(file_path)
                name_without_ext = os.path.splitext(filename)[0]
                
                # Generate friendly caption from filename
                caption = self._generate_audio_caption(name_without_ext)
                
                audio_files.append({
                    "file": file_path,
                    "caption": caption,
                    "filename": filename
                })
        
        return audio_files
    
    def get_video_files(self) -> List[Dict[str, str]]:
        """Get list of local video files with captions"""
        video_files = []
        
        # Scan for video files in assets/video
        video_patterns = ['*.mp4', '*.avi', '*.mkv', '*.mov', '*.webm']
        for pattern in video_patterns:
            files = glob.glob(os.path.join(self.video_dir, pattern))
            for file_path in files:
                filename = os.path.basename(file_path)
                name_without_ext = os.path.splitext(filename)[0]
                
                # Generate friendly caption from filename
                caption = self._generate_video_caption(name_without_ext)
                
                video_files.append({
                    "file": file_path,
                    "caption": caption,
                    "filename": filename
                })
        
        return video_files
    
    def _generate_audio_caption(self, filename: str) -> str:
        """Generate friendly caption from audio filename"""
        # Clean up filename and make it readable
        clean_name = filename.replace('_', ' ').replace('-', ' ').title()
        return f"🎵 {clean_name} - Audio Collection"
    
    def _generate_video_caption(self, filename: str) -> str:
        """Generate friendly caption from video filename"""
        # Clean up filename and make it readable
        clean_name = filename.replace('_', ' ').replace('-', ' ').title()
        return f"🎬 {clean_name} - Video Collection"
    
    def check_assets(self) -> Dict[str, int]:
        """Check available assets and return counts"""
        return {
            "images": len(self.get_image_urls()),
            "audio": len(self.get_audio_files()), 
            "video": len(self.get_video_files())
        }
    
    def ensure_directories(self):
        """Ensure all asset directories exist"""
        os.makedirs(self.images_dir, exist_ok=True)
        os.makedirs(self.audio_dir, exist_ok=True)
        os.makedirs(self.video_dir, exist_ok=True)