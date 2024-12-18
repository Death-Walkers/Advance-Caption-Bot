from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "7427294551"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://ar-hosting.pages.dev/1732525428303.jpg")
API_ID = int(getenv("API_ID", "29196607"))
API_HASH = str(getenv("API_HASH", ""))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
FORCE_SUB = os.environ.get("FORCE_SUB", "Ashlynn_Repository") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://caption:caption32@caption.27mvj.mongodb.net/?retryWrites=true&w=majority&appName=Caption",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
