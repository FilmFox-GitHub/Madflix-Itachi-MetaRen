import os
import time
import re

# Regular expression to validate ID format
id_pattern = re.compile(r'^\d+$')

class Config(object):
    # Pyrogram client config
    API_ID = os.environ.get("API_ID", "20581507")
    API_HASH = os.environ.get("API_HASH", "60ee9616e45c8a8a429fd8390b53fe74")
    
    # Fixing BOT_TOKENS extraction from environment
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7035835268:AAHZfWaCKiAR81QjN1U-hKtBpP11Pk3midE")

    # Database config
    DB_NAME = os.environ.get("DB_NAME", "test")
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://mavi:mavi@cluster0.g5gbgkz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # Other configs
    BOT_UPTIME = time.time()
    GLOBAL_THUMBNAIL_URL = os.environ.get("GLOBAL_THUMBNAIL_URL", "https://i.postimg.cc/ZRRrhLkj/IMG-20241209-204819-543.jpg")
    START_PIC = os.environ.get("START_PIC", "")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2126131508').split()]

    # Channels logs
    FORCE_SUB = os.environ.get("FORCE_SUB", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002130121487"))

    # Webhook response configuration     
    WEBHOOK = bool(int(os.environ.get("WEBHOOK", True)))
    PORT = os.environ.get("PORT", "8080") # Use 1 for True (instead of True/False)
class Txt(object):
    # Part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.

<b>Bot Is Made By :</b> @Madflix_Bots"""

    ABOUT_TXT = """
╭───────────────⍟
├<b>🤖 My Name</b> : {}
├<b>🖥️ Developer</b> : <a href=https://t.me/Madflix_Bots>Madflix Botz</a> 
├<b>👨‍💻 Programer</b> : <a href=https://t.me/MadflixOfficials>Jishu Developer</a>
├<b>📕 Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>✏️ Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>💾 Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>📊 Build Version</b> : <a href=https://instagram.com/jishu.editz>Rename v4.5.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/MadflixOfficials>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `madflixofficial@axl`
"""

# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
