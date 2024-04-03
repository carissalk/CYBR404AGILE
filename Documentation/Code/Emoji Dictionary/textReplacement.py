import pandas as pd
from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
import sys
#from responses import get_response

"""
Current Issues:
- get_response function is not imported
- need to remove punctuation from user_message
- bot returns lowercase response instead of exact user input
- need to have underscores for multi-word emojis
"""

# get response function from get_responses.py (had issues importing it)
def get_response(user_message):
    words = user_message.split()

    # Replace any word that matches a key in the dictionary with the corresponding value
    words = [emoji_dict.get(word, word) for word in words]

    # Join the words back into a string and return it
    return ' '.join(words)


# Getting the dictionary/csv file and creating DataFrame
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'updatedDict.csv')
df = pd.read_csv(csv_path)
    

TOKEN = "token"

load_dotenv()
# TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

# bot setup

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Convert the DataFrame into a dictionary
emoji_dict = df.set_index('English Name')['Unicode'].to_dict()

# messaging

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Message is empty")
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:] # might be a 0 after 1:

    # Split the user's message into words
    words = user_message.split()

    # Create a separate variable for the lowercased words
    lower_words = [word.lower() for word in words]

    # Replace any word that matches a value in the dictionary with the corresponding key
    words = [emoji_dict.get(word, word) for word in lower_words]

    # Join the words back into a string
    user_message = ' '.join(words)

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# startup bot         
@client.event
async def on_ready() -> None:
    print(f'{client.user} is running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()