import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.messages import DeleteHistory

from SonaliChat import app
from SonaliChat.core.userbot import assistants, Userbot

@app.on_message(filters.command("sg"))
async def sg(client: Client, message: Message):
    # Input Validation
    if len(message.text.split()) < 2 and not message.reply_to_message:
        return await message.reply("sg username/id/reply")

    if not assistants:
        return await message.reply("Userbot is not started or connected!")

    # Get target user
    if message.reply_to_message:
        args = message.reply_to_message.from_user.id
    else:
        args = message.text.split()[1]

    lol = await message.reply("<code>Processing...</code>")

    try:
        user = await client.get_users(args)
    except Exception:
        return await lol.edit("<code>Please specify a valid user!</code>")

    sangmata_bots = ["sangmata_bot", "sangmata_beta_bot"]
    sg_bot = random.choice(sangmata_bots)

    ubot = assistants[0]  # Pick the first available userbot

    try:
        sent_msg = await ubot.send_message(sg_bot, str(user.id))
        await sent_msg.delete()
    except Exception as e:
        return await lol.edit(f"<code>{e}</code>")

    await asyncio.sleep(1)

    # Collect and forward message
    async for stalk in ubot.search_messages(sg_bot):
        if not stalk or not stalk.text:
            continue
        await message.reply(stalk.text)
        break  # Only first message
    else:
        await message.reply("No response received from the Sangmata bot.")

    # Clean chat
    try:
        peer = await ubot.resolve_peer(sg_bot)
        await ubot.send(DeleteHistory(peer=peer, max_id=0, revoke=True))
    except Exception:
        pass

    await lol.delete()
