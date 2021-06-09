from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Just Send any YouTube link then see magic😎
Note: Didn't work YouTube playlist link"
    await message.reply_text(helptxt)
