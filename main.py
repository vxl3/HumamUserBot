from pyrogram import Client
import config
from plugins import basic  # نحمل الأوامر من ملف basic.py

app = Client(
    config.session_name,
    api_id=config.api_id,
    api_hash=config.api_hash
)

# تسجيل الأوامر من ملف basic
basic.init(app)

print("!Humam User Bot is Ready ✅")
app.run()
