import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatType

from config import STICKER, FSUB, IMG, BOT_USERNAME
from config import LOGGER_ID as LOGGER_GROUP_ID
from SonaliChat import app
from SonaliChat.database import add_user, add_chat, get_fsub, chatsdb
from SonaliChat.modules.helpers import (
    STBUTTON,
    HELP_BACK,
    ABOUT_BUTTON,
    START,
    HELP_READ,
    HELP_ABOUT,
    GROUP,
    STICKER,
    GAMES,
    FUN,
    SEARCH,
    TOOLS,
    SonaliChat,
    COUPLE,
    BASIC,
    HELP_BUTTON,
    HELP_M,
    ALPHA,
    SONALI
)


@app.on_message(filters.command(["start", "aistart"]) & ~filters.bot)
async def start(client, m: Message):
    if FSUB and not await get_fsub(client, m):
        return

    bot_name = app.name

    if m.chat.type == ChatType.PRIVATE:
        user_id = m.from_user.id
        await add_user(user_id, m.from_user.username or None)

        if STICKER and isinstance(STICKER, list):
            sticker_to_send = random.choice(STICKER)
            umm = await m.reply_sticker(sticker=sticker_to_send)
            await asyncio.sleep(1)
            await umm.delete()

        #
        log_msg = f"**✦ ηєᴡ ᴜsєʀ sᴛᴧʀᴛєᴅ ᴛʜє ʙσᴛ**\n\n**➻ ᴜsєʀ :** [{m.from_user.first_name}](tg://user?id={user_id})\n**➻ ɪᴅ :** `{user_id}`"
        await client.send_message(LOGGER_GROUP_ID, log_msg)


        accha = await m.reply_text(text="**ꜱᴛᴧʀᴛɪηɢ....🥀**")
        await asyncio.sleep(1)
        await accha.edit("**ᴘɪηɢ ᴘσηɢ...🍫**")
        await asyncio.sleep(0.5)
        await accha.edit("**ꜱᴛᴧʀᴛєᴅ.....😱**")
        await asyncio.sleep(0.5)
        await accha.delete()

        # ✅ Ensure `START_IMG` and `START` variables exist
        await m.reply_photo(
        photo=random.choice(IMG),
        caption=START,
        reply_markup=InlineKeyboardMarkup(STBUTTON),
    )

###** ###
@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    bot_id = (await client.get_me()).id
    new_members = message.new_chat_members

    if bot_id in [user.id for user in new_members]:
        chat_id = message.chat.id
        chat_title = message.chat.title or "Private Chat"
        chat_username = message.chat.username
        added_by = message.from_user.mention if message.from_user else "Unknown User"

        # Try to get invite link
        try:
            invite_link = await client.export_chat_invite_link(chat_id)
        except Exception:
            invite_link = "https://t.me/purvi_support"

        # DB में ग्रुप सेव करें
        await add_chat(chat_id, chat_title)

        # Welcome message - small caps text, simple plain text (no markdown/html)
        caption = (
            f"**✦ ʜᴇʟʟᴏ {added_by}**\n\n"
            f"**➻ ɴᴏᴡ ᴛʏᴘᴇ /SonaliChat ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛ ʙᴏᴛ.**\n\n"
            f"**💌 ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ {chat_title}**"
        )

        await message.reply_photo(
            photo=random.choice(IMG),
            caption=caption,
            parse_mode=None,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "ᴀᴅᴅ ᴍᴇ ɴᴏᴡ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"
                    ),
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/purvi_support")
                ]
            ])
        )

        # Logger message with group link - simple plain text (no html/markdown)
        log_msg = (
            f"✦ ʙᴏᴛ #ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɢʀᴏᴜᴘ\n\n"
            f"⚘ ɢʀᴏᴜᴘ ɴᴀᴍᴇ : {chat_title}\n"
            f"⚘ ɢʀᴏᴜᴘ ɪᴅ : {chat_id}\n"
            f"⚘ ᴜsᴇʀɴᴀᴍᴇ : @{chat_username if chat_username else 'N/A'}\n"
            f"⚘ ɢʀᴏᴜᴘ ʟɪɴᴋ : {invite_link}\n"
            f"⚘ ᴀᴅᴅᴇᴅ ʙʏ : {added_by}"
        )

        await app.send_photo(
            LOGGER_GROUP_ID,
            photo=random.choice(IMG),
            caption=log_msg,
            parse_mode=None,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ɢʀᴏᴜᴘ ʟɪɴᴋ", url=invite_link)]
            ])
        )
        
@app.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    if (await client.get_me()).id == message.left_chat_member.id:
        chat_id = message.chat.id
        chat_title = message.chat.title
        remove_by = message.from_user.mention if message.from_user else "Unknown User"
       
         # डेटाबेस से ग्रुप हटाएं
        await chatsdb.delete_one({"chat_id": chat_id})
        
        left_msg = (
            f"<b>✦ ʙᴏᴛ #ʟᴇғᴛ ᴀ ɢʀᴏᴜᴘ</b>\n\n"
            f"**⚘ ɢʀᴏᴜᴘ ɴᴀᴍᴇ :** {chat_title}\n"
            f"**⚘ ɢʀᴏᴜᴘ ɪᴅ :** {chat_id}\n"
            f"**⚘ ʀᴇᴍᴏᴠᴇᴅ ʙʏ :** {remove_by}"
        )
        
        await app.send_photo(
            LOGGER_GROUP_ID,
            photo=random.choice(IMG),
            caption=left_msg,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("sᴇᴇ ɢʀᴏᴜᴘ", url=f"https://t.me/{message.chat.username}" if message.chat.username else "https://t.me/purvi_support")]
            ])
        )



# Help command for displaying instructions
@app.on_message(filters.command("help"))
async def help_command(client, message):
    hmm = await message.reply_photo(
        photo=random.choice(IMG),
        caption=HELP_M,
        reply_markup=SONALI
    )
    


# Help callback handler
@app.on_callback_query(filters.regex('help'))
async def help_button(client, callback_query):
    help_text=HELP_READ
    
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ", callback_data="back"),
            InlineKeyboardButton("ᴊᴏɪɴ sᴜᴘᴘᴏʀᴛ", url="https://t.me/purvi_support")
        ]
    ])
    await callback_query.answer()
    await callback_query.message.edit_text(help_text, reply_markup=keyboard)

# Back to Menu callback handler
@app.on_callback_query(filters.regex('back'))
async def back_to_menu(client, callback_query):
       
    await callback_query.message.edit_text(
        text=START,
        reply_markup=InlineKeyboardMarkup(STBUTTON),
    )



# ✅ About Section Callback Handler
@app.on_callback_query(filters.regex('ABOUT'))
async def about_section(client, callback_query):
    about_text = HELP_ABOUT  
    
    keyboard = InlineKeyboardMarkup(ABOUT_BUTTON)
    
    await callback_query.answer()
    await callback_query.message.edit_text(about_text, reply_markup=keyboard)


# ✅ Help back Callback Handler
@app.on_callback_query(filters.regex('HELP_BACK'))
async def help_back(client, callback_query):
    await callback_query.message.edit_text(
        text=START,
        reply_markup=InlineKeyboardMarkup(STBUTTON)
    )

@app.on_callback_query(filters.regex('HELP_BASIC'))
async def help_basic(client, callback_query):
    await callback_query.message.edit_caption(
        caption=BASIC,
        reply_markup=HELP_BUTTON
    )

@app.on_callback_query(filters.regex('HELP_COUPLE'))
async def help_couple(client, callback_query):
    await callback_query.message.edit_caption(
        caption=COUPLE,
        reply_markup=HELP_BUTTON
    )

@app.on_callback_query(filters.regex('HELP_SonaliChat'))
async def help_SonaliChat(client, callback_query):
    await callback_query.message.edit_caption(
        caption=SonaliChat,
        reply_markup=HELP_BUTTON
    )

@app.on_callback_query(filters.regex('HELP_TOOLS'))
async def help_tools(client, callback_query):
    await callback_query.message.edit_caption(
        caption=TOOLS,
        reply_markup=HELP_BUTTON
    )

@app.on_callback_query(filters.regex('HELP_FUN'))
async def help_fun(client, callback_query):
    await callback_query.message.edit_caption(
        caption=FUN,
        reply_markup=HELP_BUTTON
    )

@app.on_callback_query(filters.regex('HELP_GAMES'))
async def help_games(client, callback_query):
    await callback_query.message.edit_caption(
        caption=GAMES,
        reply_markup=HELP_BUTTON
    )

@app.on_callback_query(filters.regex('HELP_SEARCH'))
async def help_search(client, callback_query):
    await callback_query.message.edit_caption(
        caption=SEARCH,
        reply_markup=HELP_BUTTON
    )

@app.on_callback_query(filters.regex('HELP_STICKER'))
async def help_sticker(client, callback_query):
    await callback_query.message.edit_caption(
        caption=STICKER,
        reply_markup=HELP_BUTTON
    )

@app.on_callback_query(filters.regex('HELP_GROUP'))
async def help_group(client, callback_query):
    await callback_query.message.edit_caption(
        caption=GROUP,
        reply_markup=HELP_BUTTON
    )


@app.on_callback_query(filters.regex('MAIN_HELP'))
async def main_help(client, callback_query):
    await callback_query.message.edit_caption(
    caption=HELP_M,
    reply_markup=ALPHA
)

@app.on_callback_query(filters.regex('close'))
async def close_callback(client, callback_query):
    try:
        await callback_query.message.delete()
    except Exception:
        # 
        pass
