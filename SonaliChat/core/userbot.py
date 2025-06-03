from pyrogram import Client
import config

assistants = []

class Userbot:
    def __init__(self):
        self.one = Client(
            name="SonaliAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=False,
        )

    async def start(self):
        print("Starting userbot session...")

        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("purvibots")
                await self.one.join_chat("purvi_support")
                await self.one.join_chat("purvi_updates")
                await self.one.join_chat("one_was_sigma")
            except Exception:
                pass

            me = await self.one.get_me()  # 

            self.one.id = me.id
            self.one.name = me.mention
            self.one.username = me.username

            assistants.append(self.one)

            print(f"Userbot started as {me.first_name}")

    async def stop(self):
        print("Stopping userbot session...")
        try:
            if config.STRING1:
                await self.one.stop()
        except Exception:
            pass
