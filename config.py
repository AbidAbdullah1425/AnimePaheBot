#..........This Bot Made By [RAHAT](https://t.me/r4h4t_69)..........#
#..........Anyone Can Modify This As He Likes..........#
#..........Just one requests do not remove my credit..........#

import os
import logging
from logging.handlers import RotatingFileHandler

API_ID = int(os.environ.get("API_ID", "26254064"))
API_HASH = os.environ.get("API_HASH", "72541d6610ae7730e6135af9423b319c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
#Logs
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002197279542"))
# MongoDB setup
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://abidabdullahown7:abidabdullah1425@cluster0.7lgug.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "AnimeDB")

DOWNLOAD_DIR = "./downloads"
#ADMIN INFO
ADMIN = int(os.environ.get("ADMIN", "5296584067"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/dfd1842d8a2dcc536a2b7.jpg https://graph.org/file/b55f0baaa7a6fde7c5682.jpg https://graph.org/file/3298ca8910c82f33418a8.jpg https://graph.org/file/4e4935469a7214c734721.jpg https://graph.org/file/fa5f2b241fe77beff8ba0.jpg https://graph.org/file/bcb9969f78ab4a47a483c.jpg https://graph.org/file/a9af161696d82f17b8888.jpg https://graph.org/file/d23b00650c00ce4d9a467.jpg https://graph.org/file/4dc0b3dfaad61fbcf0a49.jpg https://graph.org/file/7088315e9b0b6a2fa7118.jpg https://graph.org/file/9c9911d06e5f2316febb9.jpg https://graph.org/file/d2ee185180469cfd28071.jpg https://graph.org/file/dea04b2d615406aeb0181.jpg https://graph.org/file/98b63d3bb84984a68cc76.jpg").split()

PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "1"))
LOG_FILE_NAME = "filesharingbot.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
