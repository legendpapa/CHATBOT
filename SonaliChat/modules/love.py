from pyrogram import Client, filters
import random
from SonaliChat import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests 

SUPPORT_CHAT = "PURVI_UPDATES"

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "❍ ʟᴏᴠᴇ ɪs ɪɴ ᴛʜᴇ ᴀɪʀ ʙᴜᴛ ɴᴇᴇᴅs ᴀ ʟɪᴛᴛʟᴇ sᴘᴀʀᴋ.",
            "❍ ᴀ ɢᴏᴏᴅ sᴛᴀʀᴛ ʙᴜᴛ ᴛʜᴇʀᴇ's ʀᴏᴏᴍ ᴛᴏ ɢʀᴏᴡ.",
            "❍ ɪᴛ's ᴊᴜsᴛ ᴛʜᴇ ʙᴇɢɪɴɴɪɴɢ ᴏғ sᴏᴍᴇᴛʜɪɴɢ ʙᴇᴀᴜᴛɪғᴜʟ."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "❍ ᴀ sᴛʀᴏɴɢ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ɪs ᴛʜᴇʀᴇ. ᴋᴇᴇᴘ ɴᴜʀᴛᴜʀɪɴɢ ɪᴛ.",
            "❍ ʏᴏᴜ'ʜᴠ ɢᴏᴛ ᴀ ɢᴏᴏᴅ ᴄʜᴀɴᴄᴇ. ᴡᴏʀᴋ ᴏɴ ɪᴛ.",
            "❍ ʟᴏᴠᴇ ɪs ʙʟᴏssᴏᴍɪɴɢ, ᴋᴇᴇᴘ ɢᴏɪɴɢ."
        ])
    else:
        return random.choice([
            "❍ ᴡᴏᴡ ! ɪᴛ's ᴀ ᴍᴀᴛᴄʜ ᴍᴀᴅᴇ ɪɴ ʜᴇᴀᴠᴇɴ!",
            "❍ ᴘᴇʀғᴇᴄᴛ ᴍᴀᴛᴄʜ ! ᴄʜᴇʀɪsʜ ᴛʜɪs ʙᴏɴᴅ.",
            "❍ ᴅᴇsᴛɪɴᴇᴅ ᴛᴏ ʙᴇ ᴛᴏɢᴇᴛʜᴇʀ. ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs!"
        ])


EVAA = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url="https://t.me/SonaliSonaliChat?startgroup=true"),
    ],
]


@app.on_message(filters.command("love"))
async def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = (
            f"❖ ʜᴇʀᴇ ɪs ʏᴏᴜʀ ʟᴏᴠᴇ ᴘᴇʀᴄᴇɴᴛᴀɢᴇ ⏤͟͟͞͞★ \n\n"
            f"❅ {name1} ♥️ + {name2} ♥️ = {love_percentage}%\n\n{love_message}"
        )
        await client.send_message(
            message.chat.id,
            response,
            reply_markup=InlineKeyboardMarkup(EVAA),
        )
    else:
        await client.send_message(
            message.chat.id,
            "❍ ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ᴛᴡᴏ ɴᴀᴍᴇs ᴀғᴛᴇʀ /love ᴄᴏᴍᴍᴀɴᴅ.",
            reply_markup=InlineKeyboardMarkup(EVAA),
        )


@app.on_message(filters.command("wish"))
async def wish(_, m):
    if len(m.command) < 2:
        await m.reply("ᴀᴅᴅ ᴡɪꜱʜ ʙᴀʙʏ🥀!")
        return 

    api = requests.get("https://nekos.best/api/v2/happy").json()
    url = api["results"][0]['url']
    text = m.text.split(None, 1)[1]
    wish_count = random.randint(1, 100)
    wish = f"✨ ʜᴇʏ! {m.from_user.first_name}! "
    wish += f"✨ ʏᴏᴜʀ ᴡɪꜱʜ: {text} "
    wish += f"✨ ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏ: {wish_count}%"
    
    await app.send_animation(
        chat_id=m.chat.id,
        animation=url,
        caption=wish,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}")]])
    )
            
    
BUTTON = [[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}")]]
CUTIE = "https://64.media.tumblr.com/d701f53eb5681e87a957a547980371d2/tumblr_nbjmdrQyje1qa94xto1_500.gif"

@app.on_message(filters.command("cute"))
async def cute(_, message):
    if not message.reply_to_message:
        user_id = message.from_user.id
        user_name = message.from_user.first_name
    else:
        user_id = message.reply_to_message.from_user.id
        user_name = message.reply_to_message.from_user.first_name

    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"🍑 {mention} {mm}% ᴄᴜᴛᴇ ʙᴀʙʏ🥀"

    await app.send_document(
        chat_id=message.chat.id,
        document=CUTIE,
        caption=CUTE,
        reply_markup=InlineKeyboardMarkup(BUTTON),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )
