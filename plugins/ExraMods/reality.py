from pyrogram import Client, filters

@Client.on_message(filters.command("suchitha")) 
async def suchitha(_, message):
    pm = await message.reply.reply_text("FETURING ABOUT ME...............")
    await pm.edit(f"HI 👋👋\n\n MY NAME IS SUCHITHA. I KNOW YOU WILL THINK WHY MY NAME IS SUCHITHA . IT IS LONG LOVE STORY FOR MY CREATOR  <a href=https://t.me/sula20062007>𝗟𝗔𝗧𝗛𝗘𝗘𝗦𝗛</a>  . IT IS A SAD STORY FOR MY CREATOR . BUT DONT THINK THERE IS AN SAD ENDING FOR THIS STORY IT IS  STILL NOT YET GET ENDED. IF YOU WANT TO KNOW THE STORY OF THE NAME 'SUCHITHA' . I WAS FISRT BORN IN THE MONTH FEBRUARY OF 2023 . \n\n I AM MAINLY CREATED TO PRODUCE MOVIES . \n\n THANKS FOR YOUR PASSIONS IN LISTENING MY SOTRY ")
