from pyrogram import filters
from pyrogram.types import Message
import random
import asyncio

def init(app):

    # أمر /hello
    @app.on_message(filters.command("مرحبا") & filters.me)
    async def hello_handler(_, message: Message):
        await message.reply("تفضل، شنو تحتاج؟")

    # أمر /ping
    @app.on_message(filters.command("بنج") & filters.me)
    async def ping_handler(_, message: Message):
        await message.reply("🏓 بنج!")

    # أمر /id
    @app.on_message(filters.command("ايدي"))
    async def id_handler(_, message: Message):
        user = message.from_user
        await message.reply(f"آي دي الرسالة: `{message.message_id}`\nآي ديك: `{user.id}`", quote=True)

    # أمر .منو
    @app.on_message(filters.command("منو", prefixes=".") & filters.me)
    async def who_handler(_, message: Message):
        names = ["سجاد", "نور", "حسين", "رهف", "زينب", "علي", "محمد", "آمنة"]
        await message.reply(f"🤔 أكيد هو: **{random.choice(names)}**")

    # أمر .شكد تحبني
    @app.on_message(filters.command("شكد", prefixes=".") & filters.me)
    async def love_percent(_, message: Message):
        if "تحبني" in message.text:
            percent = random.randint(0, 100)
            await message.reply(f"❤️ أحبك بنسبة: {percent}%")

    # أمر .غزل
    @app.on_message(filters.command("غزل", prefixes=".") & filters.me)
    async def love_lines(_, message: Message):
        lines = [
            "كلبي ينطگ بس من اسمع اسمك ❤️",
            "تعال خل نضيع وننسى العالم 🌍",
            "أنت أول وآخر نبضة كلبي ❤️‍🔥",
            "جمالك آية نزلت بالغلط 😳",
            "عيونك مسويه إنقلاب بنظامي 😵‍💫",
            "إذا العيون تحچي، عيونك سوتلي رواية كاملة!"
        ]
        await message.reply(random.choice(lines))

    # أمر .قرار
    @app.on_message(filters.command("قرار", prefixes=".") & filters.me)
    async def decide_handler(_, message: Message):
        text = message.text.split(maxsplit=1)
        if len(text) < 2 or "او" not in text[1]:
            await message.reply("❓ لازم تكتب خيارين مفصولين بـ (او)\nمثال: `.قرار أطلع او أنام؟`")
        else:
            options = text[1].split("او")
            chosen = random.choice(options).strip()
            await message.reply(f"🤖 القرار هو: **{chosen}**")

    # أمر .زواج
    @app.on_message(filters.command("زواج", prefixes=".") & filters.me)
    async def marriage_handler(_, message: Message):
        if message.reply_to_message and message.reply_to_message.from_user:
            target = message.reply_to_message.from_user.first_name
            await message.reply(f"💍 تم قبول طلب الزواج من {target} ❤️ مبارك عليكم!")
        else:
            await message.reply("❗️ رد على رسالة الشخص اللي تريد تتزوج منه.")

    # أمر .سبني
    @app.on_message(filters.command("سبني", prefixes=".") & filters.me)
    async def insult_handler(_, message: Message):
        insults = [
            "يا عديم النكتة 😂",
            "وجهك مثل السماعة، ما يسمع ولا يرد!",
            "إنتي مثل الشاي، بدون سكر ما تسوى!",
            "عشاك سريع وراك ضايع!",
            "شوفلك هواية قبل لا تزهق حياتك!"
        ]
        await message.reply(random.choice(insults))

    # أمر .تفليش
    @app.on_message(filters.command("تفليش", prefixes=".") & filters.me)
    async def flash_handler(_, message: Message):
        if message.reply_to_message and message.reply_to_message.from_user:
            target = message.reply_to_message.from_user.first_name
            msg = await message.reply(f"💣 جاري تفليش {target} ...")
            await asyncio.sleep(2)
            await msg.edit("🔥 التفليش صار بنجاح!\n🚀 طير!")
        else:
            await message.reply("❗️ رد على رسالة الشخص اللي تريد تفلّشه.")

    # أمر .تحشيش
    @app.on_message(filters.command("تحشيش", prefixes=".") & filters.me)
    async def joke_handler(_, message: Message):
        jokes = [
            "ليش القطة قاعدة على الكمبيوتر؟ تنتظر الماوس! 🐱💻",
            "مرة واحد بخيل مات.. ضحكوا عليه حتى البخلاء!",
            "ليش السمكة ما تشتغل؟ لأنها دايمًا عائمة!",
            "البرمائي يحب البرمجة لأنه يحب يغوص بالأكواد!"
        ]
        await message.reply(random.choice(jokes))

    # أمر .نكتة
    @app.on_message(filters.command("نكتة", prefixes=".") & filters.me)
    async def joke2_handler(_, message: Message):
        jokes = [
            "مرة واحد نزل البحر، طلع مبلول!",
            "واحد سأل صاحبه: كيف تعرف البطة؟ قال له: من طقطقة أرجلها!",
            "مرة واحد بخيل أخذ تذكرة سفر ونسيها في البيت!",
            "ليش الكمبيوتر حزين؟ لأنه فيه فايروس!"
        ]
        await message.reply(random.choice(jokes))

    # أمر .سلام
    @app.on_message(filters.command("سلام", prefixes=".") & filters.me)
    async def sayhi_handler(_, message: Message):
        greetings = ["هلا والله!", "شلونك؟", "أهلاً وسهلاً!", "مرحبا!", "شلون الدنيا وياك؟"]
        await message.reply(random.choice(greetings))

    # أمر .عكس
    @app.on_message(filters.command("عكس", prefixes=".") & filters.me)
    async def reverse_handler(_, message: Message):
        text = message.text.split(maxsplit=1)
        if len(text) < 2:
            await message.reply("↩️ اكتبلي نص حتى أعكسه لك!\nمثال: `.عكس نص`")
        else:
            reversed_text = text[1][::-1]
            await message.reply(f"🔁 {reversed_text}")

    # أمر .نسبة
    @app.on_message(filters.command("نسبة", prefixes=".") & filters.me)
    async def gayrate_handler(_, message: Message):
        percentage = random.randint(0, 100)
        await message.reply(f"🌈 نسبتك هي: {percentage}% 😂")

    # أمر .اختراق
    @app.on_message(filters.command("اختراق", prefixes=".") & filters.me)
    async def hack_handler(_, message: Message):
        msg = await message.reply("🔍 جاري الاختراق...")
        await asyncio.sleep(1.5)
        await msg.edit("📡 اختراق السيرفرات...")
        await asyncio.sleep(1.5)
        await msg.edit("💀 تم الاختراق بنجاح!\n🤣 لا تزعل، مزحة بس!")
