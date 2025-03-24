Bot for synchronizing chats between Telegram and Discord channels. You will need a hosting service or a Linux machine running continuously, otherwise,
the application will only work when manually launched. Use it wherever, however, and as much as you want.

**IMPORTANT:** 
The bot only forwards media from Discord to Telegram, not the other way around, due to Discord's 10MB media limit for non-Nitro users! 
It is recommended to disable media sending in the Telegram chat where the bot operates.

**Required libraries:**

sudo apt install python3  
sudo apt install python3-pip  
pip install aiogram  
pip install discord.py python-telegram-bot  

**How to use:**
1. Create a Discord bot and add it to your server (https://discord.com/developers/applications). 
   A good guide is available here (Russian language): https://habr.com/ru/articles/676390/ (Read up to the "Installing the library" section).

2. Create a Telegram bot using @BotFather. Grant it permissions and ensure it can read and send messages in the group.

3. Create a Discord channel from which messages will be relayed. Similarly, create a Telegram group (or use an existing one).

4. Now, when everything is ready, fill in these fields in app.py:
   
   DISCORD_TOKEN = Your Discord bot token (as described in the Habr guide linked above).
   
   TELEGRAM_TOKEN = Your Telegram bot token (the long key provided by @BotFather after setting the name and username, starting with "Congratulation!").
   
   TELEGRAM_CHAT_ID = Telegram chat ID (Get it using @getmy_id_bot by forwarding the chat.
   NOTE: After adding the bot and adjusting roles, the chat may become a "supergroup," changing its ID).
   
   DISCORD_CHANNEL_ID = Discord channel ID (as explained in the Habr guide under "Enabling Developer Mode").

6. Save changes and launch the app. If everything is set correctly, the relay will work in both directions (with the media limitation mentioned above).
   Otherwise, check the command line logs (a log file implementation will be added later) to troubleshoot issues.
