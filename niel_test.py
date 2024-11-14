import asyncio
import pandas as pd
from telegram import Bot
from niel_telegram_bot import send_telegram_message, get_telegram_updates, read_excel_data, update_excel_with_responses, format_message

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7498425907:AAEENff8XhbnpaoxrbKcZDLigjpa65H6QzY'

# Path to your Excel file
EXCEL_FILE = 'list_diff.xlsx'

async def main():
    # Read the Excel data
    df = read_excel_data(EXCEL_FILE)

    # Filter rows where the "response" column is blank
    df_to_process = df[df['response'].isna()]

    # Verify that the filtered data is correct
    print(f"Filtered data to process:\n{df_to_process}")

    # Sending messages to all outlets where "response" is blank
    for _, row in df_to_process.iterrows():
        # Make sure 'chat_id' column exists and is not empty
        if pd.isna(row['chat_id']):
            print(f"Skipping row due to missing chat_id: {row}")
            continue

        # Format the message to send
        message = format_message(row)
        chat_id = row['chat_id']

        # Print debugging information
        print(f"Sending message to {chat_id}: {message}")

        # Send the message asynchronously
        await send_telegram_message(BOT_TOKEN, chat_id, message)

    # Pause for a while to allow responses to come in
    await asyncio.sleep(10)  # Adjust sleep time as necessary

    # Get updates from Telegram
    updates = get_telegram_updates(BOT_TOKEN)

    # Print debugging information
    print(f"Updates received:\n{updates}")

    # Update Excel file with responses
    update_excel_with_responses(EXCEL_FILE, df, updates)

# Ensure the async function is properly run
if __name__ == "__main__":
    asyncio.run(main())

