from bot import bot
from pyrogram import filters


@bot.on_message(
    filters.command("start")
)
async def alive(_, message):
    await message.reply(
        f"Hi {message.from_user.mention}, This is an unofficial Shazam Telegram Bot.\n\nℹ️ You can send me an audio, video or a voice note so that I can parse to Shazam and send you the results."
    )