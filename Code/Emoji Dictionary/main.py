import pandas as pd
from typing import Final
import os
from discord import Intents, Client, Message
import string
#from responses import get_response

"""
Current Issues:
- get_response function is not imported
- need to remove punctuation from user_message
- bot returns lowercase response instead of exact user input
- need to have underscores for multi-word emojis
       -check if word is converted and if not try to add the next (up to 3 times)
"""

punctuation = ['.', ',', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}', '\\', '|', '<', '>', '@', '#', '$', '%', '^', '&', '*', '~', '`', 'underscore', '+', '=']


# response function
def get_response(user_message):
    words = user_message.split()
    words = [''.join(ch for ch in word if ch not in string.punctuation) for word in words]

    # Create a separate variable for the lowercased words
    lower_words = [word.lower() for word in words]

    # Replace any word that matches a key in the dictionary with the corresponding value
    words = [emoji_dict.get(word, word) for word in lower_words]

    # Join the words back into a string and return it
    return ' '.join(words)


# Getting the dictionary/csv file and creating DataFrame
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'updatedDict.csv')
df = pd.read_csv(csv_path)

tokenTrick = "MTIyMjU3MTY4M'DA1NzI2MjEyMQ.Gm4V-v.XF68jpU4u4BYw8OqKP7IhlUCK'4ofYzq6yJkk-s"
tokenTrick = tokenTrick.replace("'", "")
TOKEN = tokenTrick
print("Token: ", TOKEN)


# bot setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Convert the DataFrame into a dictionary
emoji_dict = df.set_index('English Name')['Unicode'].to_dict()

# Text to Emoji toggle
replace_text = True

# messaging
async def send_message(message: Message, user_message: str) -> None:
    global replace_text

    # Text to Emoji toggle 
    if user_message == "/TTEtoggle":
        replace_text = not replace_text
        await message.channel.send(f"Text to Emoji is now {'enabled' if replace_text else 'disabled'}")
        return
    if not user_message or not replace_text:
        print("Message is empty or text to emoji is disabled")
        return
    
    if not user_message:
        print("Message is empty")
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:] # might be a 0 after 1:

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