from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton(" Update Channel", url="https://t.me/Bx_Botz")],[InlineKeyboardButton("Support Group", url="https://t.me/BxSupport")]])

    welcomed = f"Hai <b>{message.from_user.first_name}</b>\nHai ᴍʜᴅ ᴍᴜꜰᴀᴢ!!
I'm simple YouTube converter I Will Convert Youtube Link to Video/File/Mp3

For more details /help"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
