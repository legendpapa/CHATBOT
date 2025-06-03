import asyncio
from pyrogram import filters, Client 
from pyrogram.enums import ChatMembersFilter
import random
from pyrogram.errors import FloodWait

from SonaliChat import app as Client
#from SonaliChat.database import is_admins

SPAM_CHATS = []
EMOJI = [  
    "😊", "😍", "😘", "🥰", "😻", "💖", "💕", "💓", "💗", "💞", "💟",  
    "🌸", "🌺", "🌷", "🌹", "💐", "🌼", "🌻", "🍀", "🍁", "🍂", "🍃",  
    "🌿", "🌱", "🌴", "🌳", "🌲", "🌵", "🦋", "🐦", "🐾", "🌞", "🌝",  
    "🌛", "🌜", "🌕", "🌙", "🌟", "🌠", "🌌", "✨", "💫", "⭐️", "☀️",  
    "🌤", "⛅️", "🌥", "🌦", "🌧", "🌨", "🌩", "⛈", "🌪", "🌫", "🌬",  
    "☔️", "❄️", "🌈", "⛄️", "🌊", "🌋", "🏞", "🏔", "🌏", "🌍", "🌎",  
    "🎆", "🎇", "🎑", "🏵", "🏅", "🎖", "🎗", "🎐", "🎀", "🎁", "🎊",  
    "🎉", "🦢", "🦚", "🦜", "🕊", "🐇", "🐚", "🌠", "🌉", "🌃", "🌌"  
]  


async def is_admin(client, chat_id, user_id):
    try:
        admin_ids = [
            admin.user.id
            async for admin in client.get_chat_members(
                chat_id, filter=ChatMembersFilter.ADMINISTRATORS
            )
        ]
        if user_id in admin_ids:
            return True
        return False
    except Exception:
        if user_id == chat_id:
            return True
        return False


@Client.on_message(
    filters.command(["all", "allmention", "mentionall", "tagall"], prefixes=["/", "@"])
)
async def tag_all_users(client, message):
    admin = await is_admin(client, message.chat.id, message.from_user.id)
    if not admin:
        return await message.reply_text("**You are not admin baby, Please dont use this command**")

    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        try:
            await message.reply_text(
                "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@all Hi Friends`"
            )
            return
        except Exception:
            return
    if replied:
        usernum = 0
        usertxt = ""
        try:
            SPAM_CHATS.append(message.chat.id)
            async for m in client.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{random.choice(EMOJI)}](tg://user?id={m.user.id})"
                if usernum == 7:
                    await replied.reply_text(
                        usertxt,
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""

            if usernum != 0:
                await replied.reply_text(
                    usertxt,
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        try:
            usernum = 0
            usertxt = ""
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            async for m in client.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{random.choice(EMOJI)}](tg://user?id={m.user.id})"
                if usernum == 7:
                    try:
                        await client.send_message(
                            message.chat.id,
                            f"**{text}**\n\n{usertxt}",
                            disable_web_page_preview=True,
                        )
                    except Exception:
                        return 
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                await client.send_message(
                    message.chat.id,
                    f"**{text}**\n\n{usertxt}",
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


async def tag_all_admins(client, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@admins Hi Friends`"
        )
        return
    if replied:
        usernum = 0
        usertxt = ""
        try:
            SPAM_CHATS.append(message.chat.id)
            async for m in client.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{random.choice(EMOJI)}](tg://user?id={m.user.id})"
                if usernum == 7:
                    await replied.reply_text(
                        usertxt,
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                await replied.reply_text(
                    usertxt,
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        usernum = 0
        usertxt = ""
        try:
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            async for m in client.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                usertxt += f"[{random.choice(EMOJI)}](tg://user?id={m.user.id})"
                if usernum == 7:
                    await client.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                await client.send_message(
                    message.chat.id,
                    f"{text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@Client.on_message(
    filters.command(["admin", "admins", "report"], prefixes=["/", "@"]) & filters.group
)
async def admintag_with_reporting(client, message):
    if not message.from_user:
        return
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    admins = [
        admin.user.id
        async for admin in client.get_chat_members(
            chat_id, filter=ChatMembersFilter.ADMINISTRATORS
        )
    ]
    if message.command[0] == "report":
        if from_user_id in admins:
            try:
                return await message.reply_text(
                    "ᴏᴘᴘs! ʏᴏᴜ ᴀʀᴇ ʟᴏᴏᴋs ʟɪᴋᴇ ᴀɴ ᴀᴅᴍɪɴ!\nʏᴏᴜ ᴄᴀɴ'ᴛ ʀᴇᴘᴏʀᴛ ᴀɴʏ ᴜsᴇʀs ᴛᴏ ᴀᴅᴍɪɴ"
                )
            except Exception:
                return

    if from_user_id in admins:
        return await tag_all_admins(client, message)

    if len(message.text.split()) <= 1 and not message.reply_to_message:
        try:
            return await message.reply_text("Reply to a message to report that user.")
        except Exception:
            return
    reply = message.reply_to_message or message
    reply_user_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
    linked_chat = (await client.get_chat(chat_id)).linked_chat
    if reply_user_id == client.me.id:
        try:
            return await message.reply_text("Why would I report myself?")
        except Exception:
            return
    if (
        reply_user_id in admins
        or reply_user_id == chat_id
        or (linked_chat and reply_user_id == linked_chat.id)
    ):
        try:
            return await message.reply_text(
                "Do you know that the user you are replying to is an admin?"
            )
        except Exception:
            return

    user_mention = reply.from_user.mention if reply.from_user else "the user"
    text = f"Reported {user_mention} to admins!."

    for admin in admins:
        admin_member = await client.get_chat_member(chat_id, admin)
        if not admin_member.user.is_bot and not admin_member.user.is_deleted:
            text += f"[\u2063](tg://user?id={admin})"

    try:
        await reply.reply_text(text)
    except Exception:
        return

@Client.on_message(
    filters.command(
        [
            "stopmention",
            "cancel",
            "stop",
            "cancelmention",
            "offmention",
            "mentionoff",
            "allstop",
            "stopall",
            "allcancel",
            "mentionstop",
            "stoptagall",
            "tagallstop",
            "canceltagall",
            "tagallcancel",
            "cancelall",
        ],
        prefixes=["/", "@"],
    )
)
async def cancelcmd(client, message):
    chat_id = message.chat.id
    admin = await is_admin(client, chat_id, message.from_user.id)
    if not admin:
        return await message.reply_text("**You are not admin baby, Please dont use this command**")

    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")

    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
        return


