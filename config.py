## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BADUDUsAQvGoOEdKolincE8tZ_HfM5K92jF_c53BBjq70DsK0S38Fgi1_g-BifHwmQLbELOl3nG5C3A-VrIUS3EUR6Oi4vnXY_-w_L0l1KNWplU5jS2D7VvXuUll4U_f1ggcVuSpN2d6yXCam6mg-ZHCDydNl2LmaQm_-dqfkDwFWL-SAq89iVoPlDoEP9Yt-_haxOPq6z_CNk_rBJFCENPbNEoCif3nciBx-a5Oh6oUATL6uYS3yrx4Wv2SyZyVabACIjbnIf8cWWU1wgWpJJ2dDvMWW1uF2Dw3CPp1b4kYo8RFjAqeTPkC9UipKikPpkkyrzqJUYjqkmtijG3-LIWTaJu5NQAAAAEyI6PEAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5169177807:AAERFI-Xv4xeuSdne-N_9u-0knES8bjq7SQ")
BOT_NAME = getenv("BOT_NAME", "ᯓ 𓆩 ˹ 𝕄𝕌𝕊𝕀ℂ 𝔾𝔼ℕ𝔼ℝ𝔸𝕃 ˼ 𓆪 𓆃")
API_ID = int(getenv("API_ID", "13897035"))
API_HASH = getenv("API_HASH", "6980ca34dc4d7295b4f52021f2b863d3")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ZzZzZ5")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "musicgeneral3_bot")
OWNER_ID = getenv("OWNER_ID", "5261857178")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "musicgeneral0")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
