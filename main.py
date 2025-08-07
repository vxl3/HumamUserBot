import os
from pyrogram import Client
from pyrogram.enums import ParseMode
from plugins import basic  # تحميل الأوامر

app = Client(
    name="humambot",
    session_string=os.getenv("SESSION_STRING"),
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    parse_mode=ParseMode.HTML
)

# تسجيل الأوامر من ملف basic
basic.init(app)

print("✅ Humam User Bot is Ready and Running!")
app.run()
