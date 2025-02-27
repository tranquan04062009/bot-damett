import asyncio
import logging
import random
import os
import httpx
import pytz
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

# Thay thế bằng token bot của bạn
TELEGRAM_BOT_TOKEN = "7550168223:AAHswDYG8ozk1QnpKSnxFo9UuNhYgCh6mco"
CHAT_ID = "-1002370805497"  # Thay bằng ID nhóm hoặc người nhận video

# Khởi tạo bot và dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
scheduler = AsyncIOScheduler()

# API TikWM
API_URL = "https://www.tikwm.com/api/feed/search"
SEARCH_KEYWORDS = ["funny", "meme", "dance", "trend", "animal", "game", "food"]

async def get_random_tiktok():
    """ Lấy video TikTok ngẫu nhiên từ API """
    keyword = random.choice(SEARCH_KEYWORDS)
    params = {"keywords": keyword, "count": 5}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("data"):
            videos = data["data"]
            video = random.choice(videos)  # Chọn ngẫu nhiên 1 video
            
            video_url = video["play"]
            title = video["title"]
            author = video["author"]
            music = video["music"]
            return video_url, title, author, music
    
    return None, None, None, None

async def download_video(video_url, filename):
    """ Tải video về máy """
    async with httpx.AsyncClient() as client:
        response = await client.get(video_url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            return True
    return False

async def send_tiktok_video():
    """ Tải video, gửi lên Telegram và xóa file """
    video_url, title, author, music = await get_random_tiktok()
    if not video_url:
        return await bot.send_message(CHAT_ID, "Không tìm thấy video TikTok nào!")

    filename = "tiktok.mp4"
    if await download_video(video_url, filename):
        caption = f"🎥 *Video TikTok*\n📌 *Tiêu đề:* {title}\n👤 *Người đăng:* {author}\n🎵 *Nhạc:* {music}"
        await bot.send_video(CHAT_ID, open(filename, "rb"), caption=caption, parse_mode="Markdown")
        os.remove(filename)  # Xóa video sau khi gửi
    else:
        await bot.send_message(CHAT_ID, "Tải video thất bại!")

@dp.message_handler(commands=["randomtiktok"])
async def random_tiktok_command(message: Message):
    """ Xử lý lệnh /randomtiktok """
    await send_tiktok_video()

# Lên lịch gửi video theo giờ Việt Nam
vn_tz = pytz.timezone("Asia/Ho_Chi_Minh")
scheduler.add_job(send_tiktok_video, "cron", hour=7, minute=0, timezone=vn_tz)  # 7h sáng
scheduler.add_job(send_tiktok_video, "cron", hour=12, minute=0, timezone=vn_tz) # 12h trưa
scheduler.add_job(send_tiktok_video, "cron", hour=21, minute=0, timezone=vn_tz) # 9h tối
scheduler.start()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)