import discord
from discord.ext import commands
from aiogram import Bot, Dispatcher, types
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

DISCORD_TOKEN = 
TELEGRAM_TOKEN = 
TELEGRAM_CHAT_ID = 
DISCORD_CHANNEL_ID = 

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot_discord = commands.Bot(command_prefix="!", intents=intents)
bot_telegram = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

async def send_to_telegram(text: str):
    try:
        await bot_telegram.send_message(
            chat_id=TELEGRAM_CHAT_ID, 
            text=text[:4096]
        )
    except Exception as e:
        logging.error(f"Ошибка Telegram: {e}")
        channel.send(
            f"**Бот не смог переслать это сообщение. Возможно, количество символов в сообщении превысило 4000 знаков. Если нет - проблемы с ботом, скоро решим!**"
        )

@bot_discord.event
async def on_message(message):
    if message.author == bot_discord.user:
        return
    
    logging.info(f"Получено сообщение из Discord: {message.content}")

    username = message.author.display_name
    content = message.content or ""

    attachments = ""
    if message.attachments:
        attachments = "\n[Вложение] " + "\n[Вложение] ".join(
            [a.url for a in message.attachments]
        )

    full_text = f"{username}:\n\n{content}{attachments}"
    await send_to_telegram(full_text)

    await bot_discord.process_commands(message)

@dp.message()
async def telegram_handler(message: types.Message):
    if not message.text:
        return
    
    channel = bot_discord.get_channel(DISCORD_CHANNEL_ID)
    if not channel:
        return
    
    try:
        await channel.send(
            f"**{message.from_user.full_name}**:\n{message.text}"
        )
    except Exception as e:
        logging.error(f"Ошибка Discord: {e}")

async def main():
    await asyncio.gather(
        bot_discord.start(DISCORD_TOKEN),
        dp.start_polling(bot_telegram)
    )

if __name__ == "__main__":
    asyncio.run(main())