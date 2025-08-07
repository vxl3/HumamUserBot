from pyrogram import filters
from pyrogram.types import Message

def init(app):
    # أمر /hello
    @app.on_message(filters.command("hello") & filters.me)
    def hello_handler(_, message: Message):
        message.reply("هلا حمودي! 👋 هذا أول أمر من بوتك ✨")

    # أمر /ping
    @app.on_message(filters.command("ping") & filters.me)
    def ping_handler(_, message: Message):
        message.reply("🏓 Pong!")

    # أمر /id
    @app.on_message(filters.command("id") & filters.me)
    def id_handler(_, message: Message):
        message.reply(f"آي دي الرسالة: `{message.message_id}`\nآي ديك: `{message.from_user.id}`", quote=True)
