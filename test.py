import asyncio
from telegram import Bot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
BOT_TOKEN = '7205895984:AAHlzpLt9ZRewpHDkWAaIBrsPEeIV7pIg4k' # Make sure to define your token here

# Replace 'CHAT_ID' with the chat ID where you want to send the message
CHAT_ID = '5296461748'  # Ensure this is the correct chat ID

# The message you want to send
MESSAGE = 'Daniel Kontol'

async def send_message():
    # Initialize the bot
    bot = Bot(token=BOT_TOKEN)
    
    # Send the message using await
    await bot.send_message(chat_id=CHAT_ID, text=MESSAGE)
    
    print("Message sent successfully!")

# Ensure the async function is properly run
if __name__ == "__main__":
    
    for i in range (1000):
        asyncio.run(send_message())
