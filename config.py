from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/6a7652891cf711479e8fc.png")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/5d9d0c0b7d9cb483f9867.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/T7_Au")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/T7_AU")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6878497585").split()))


FAILED = "https://telegra.ph/file/5d9d0c0b7d9cb483f9867.jpg"
