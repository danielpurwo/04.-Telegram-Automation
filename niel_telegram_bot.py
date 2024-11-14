# Niel bot --> kk_test_1 token: 7498425907:AAEENff8XhbnpaoxrbKcZDLigjpa65H6QzY
# Niel tele --> username : https://t.me/kk_kk_test1_bot 
# Niel env --> tele_test

# I do testing using my telegram apps, and I already put the chat_id into my excel file (list diff.xlsx) but my script didn't send any messages to my telegram.

import pandas as pd
import requests
import json
import asyncio
from datetime import datetime
from telegram import Bot

# Asynchronous function to send a message via the Telegram bot
async def send_telegram_message(bot_token, chat_id, message):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)
    print(f"Message sent successfully to {chat_id}!")

# Function to format the message
def format_message(row):
    return f"""
    Hi {row['pic_name']}!

    We need confirmation about a difference in sales with the information below:

    store_ID    : {row['store_id']}
    txn_date    : {row['txn_date']}
    amount_diff : IDR {row['amount_diff']}

    Please respond to this message by replying with your reason statement.
    """

# Function to get updates from the Telegram bot
def get_telegram_updates(bot_token):
    response = requests.get(f'https://api.telegram.org/bot{bot_token}/getUpdates')
    updates = response.json()
    return updates

# Function to read data from Excel file
def read_excel_data(file_name):
    df = pd.read_excel(file_name)
    return df

# Function to process and update responses in Excel
def update_excel_with_responses(file_name, df, updates):
    if 'result' not in updates:
        print(f"Error in getting updates: {updates}")
        return

    for update in updates['result']:
        if 'message' in update and 'text' in update['message']:
            chat_id = update['message']['chat']['id']
            message_text = update['message']['text']
            timestamp = datetime.fromtimestamp(update['message']['date']).strftime('%Y-%m-%d %H:%M:%S')

            # Find the corresponding row in the DataFrame
            index = df[(df['chat_id'] == chat_id) & (df['response'] != 'Received')].index
            if not index.empty:
                # Update the response and timestamp in the DataFrame
                df.at[index[0], 'response'] = 'Received'
                df.at[index[0], 'reason'] = message_text
                df.at[index[0], 'ts_response'] = timestamp

    # Save the updated DataFrame back to Excel
    df.to_excel(file_name, index=False)
    print("Excel file updated with responses.")
