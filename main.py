
from pyrogram import Client, filters
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("file2link_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & (filters.document | filters.video))
async def handle_file(client, message):
    file = message.document or message.video
    if not file:
        return await message.reply("❌ الملف غير مدعوم.")

    link = f"https://t.me/{(await client.get_me()).username}?start={file.file_id}"
    await message.reply_text(
        f"🔗 لقد تم إنشاء رابط المشاركة:\n\n"
        f"📁 الاسم: `{file.file_name}`\n"
        f"🔗 [اضغط هنا للتحميل]({link})",
        disable_web_page_preview=True
    )

app.run()
