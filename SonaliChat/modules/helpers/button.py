

from config import BOT_USERNAME, OWNER_ID, SUPPORT_GROUP
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

STBUTTON = [
  [
       InlineKeyboardButton(
    text="✙ ʌᴅᴅ ϻє ʙᴧʙʏ ✙",
    url=f"https://t.me/{BOT_USERNAME}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
        ),
  ],
  [
    InlineKeyboardButton(
      text="⌯ ❍ᴡɴᴇʀ ⌯",
      user_id=OWNER_ID,
    ),
      InlineKeyboardButton(
      text="⌯ ᴧʙσᴜᴛ ⌯",
      callback_data="ABOUT",
    ),
  ],
    [
        InlineKeyboardButton(text="⌯ ʜєʟᴘ ᴧηᴅ ᴄσϻϻᴧηᴅs ⌯", callback_data="MAIN_HELP"),
    ],
]

ABOUT_BUTTON = [
    [
        InlineKeyboardButton("⌯ 𝛅ᴜᴘᴘσʀᴛ ⌯", url="https://t.me/PURVI_SUPPORT"),
        InlineKeyboardButton("⌯ ᴜᴘᴅᴧᴛє ˼⌯", url="https://t.me/+gMy8Cp190ediNzZl")
    ],
    [
        InlineKeyboardButton("⌯ ʙᴧᴄᴋ ⌯", callback_data=f"HELP_BACK")
    ]
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="ʌᴅᴅ ϻє", 
            url=f"https://t.me/{BOT_USERNAME}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users"
        ),
        InlineKeyboardButton(
            text="⌯ 𝛅ᴜᴘᴘᴏʀᴛ ⌯", 
            url=f"https://t.me/{SUPPORT_GROUP}"
        ),
    ],
]



HELP_BACK = [

    [
        InlineKeyboardButton(text="𝛅ᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GROUP}"),
        InlineKeyboardButton(text="вᴧᴄᴋ", callback_data="HELP_BACK"),
    ],
]

HELP_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="MAIN_HELP"),
            InlineKeyboardButton(text="ᴄʟᴏsᴇ", callback_data="close"),
        ],
    ]
)

ALPHA = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ʙᴀsɪᴄ", callback_data="HELP_BASIC"),
        InlineKeyboardButton("ᴄᴏᴜᴘʟᴇ", callback_data="HELP_COUPLE"),
        InlineKeyboardButton("ᴄʜᴀᴛʙᴏᴛ", callback_data="HELP_SonaliChat")
    ],
    [
        InlineKeyboardButton("ᴛᴏᴏʟs", callback_data="HELP_TOOLS"),
        InlineKeyboardButton("ғᴜɴ", callback_data="HELP_FUN"),
        InlineKeyboardButton("ɢᴀᴍᴇs", callback_data="HELP_GAMES")
    ],
    [
        InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="HELP_SEARCH"),
        InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="HELP_STICKER"),
        InlineKeyboardButton("ɢʀᴏᴜᴘ", callback_data="HELP_GROUP")
    ],
    [
        InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="HELP_BACK")
    ]
])


SONALI = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("ʙᴀsɪᴄ", callback_data="HELP_BASIC"),
        InlineKeyboardButton("ᴄᴏᴜᴘʟᴇ", callback_data="HELP_COUPLE"),
        InlineKeyboardButton("ᴄʜᴀᴛʙᴏᴛ", callback_data="HELP_SonaliChat")
    ],
    [
        InlineKeyboardButton("ᴛᴏᴏʟs", callback_data="HELP_TOOLS"),
        InlineKeyboardButton("ғᴜɴ", callback_data="HELP_FUN"),
        InlineKeyboardButton("ɢᴀᴍᴇs", callback_data="HELP_GAMES")
    ],
    [
        InlineKeyboardButton("sᴇᴀʀᴄʜ", callback_data="HELP_SEARCH"),
        InlineKeyboardButton("sᴛɪᴄᴋᴇʀs", callback_data="HELP_STICKER"),
        InlineKeyboardButton("ɢʀᴏᴜᴘ", callback_data="HELP_GROUP")
    ],
    [
        InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close")
    ]
])
