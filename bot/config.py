from os import getenv
from dotenv import load_dotenv
from pathlib import Path

if Path("config.env").exists():
    load_dotenv("config.env")

class Telegram:
    API_ID = int(getenv("API_ID", "9301087"))
    API_HASH = getenv("API_HASH", "cbabdb3f23de6326352ef3ac26338d9c")
    BOT_TOKEN = getenv("BOT_TOKEN", "7105712052:AAGBSbUiLzffkGu5acMxHj7zgXHdeXH45EQ")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "")
    BASE_URL = getenv("BASE_URL", "https://vercel.com/bob-files-projects/surftg-org/C9mh3ngN46L7iZJ5i3yH4QzhNt6z").rstrip('/')
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://Shivji:BoBfiles@cluster0.t1mka5v.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", " -1001844691460").split(",") if channel.strip()]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "")
    PASSWORD = getenv("PASSWORD", "")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "Asssaulter_shiv")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "Mishraji99@")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = getenv('MULTI_CLIENT', 'False')
    HIDE_CHANNEL = getenv('HIDE_CHANNEL', 'False')
