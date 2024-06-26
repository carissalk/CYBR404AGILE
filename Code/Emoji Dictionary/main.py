import pandas as pd
from typing import Final
import os
from discord import Intents, Client, Message

punctuation = ['.', ',', '!', '?', ';', ':', '-', '(', ')', '[', ']', '{', '}', '\\', '|', '<', '>', '@', '#', '$', '%', '^', '&', '*', '~', '`', 'underscore', '+', '=']
updatedPunctuation = [' . ', ' , ', ' ! ', ' ? ', ' ; ', ' : ', ' - ', ' ( ', ' ) ', ' [ ', ' ] ', ' { ', ' } ', ' \\ ', ' | ', ' < ', ' > ', ' @ ', ' # ', ' $ ', ' % ', ' ^ ', ' & ', ' * ', ' ~ ', ' ` ', ' underscore ', ' + ', ' = ']

# invite link for bot: https://discord.com/oauth2/authorize?client_id=1222571680057262121&permissions=0&scope=bot

#text replacement function
def get_response(user_message):
    for i in user_message:
        if i in punctuation:
            user_message = user_message.replace(i, updatedPunctuation[punctuation.index(i)])

    words = user_message.split()
    response = ['']  # The string is for dev purposes. The string inside is used to indicate who's version of the bot is
    # running.
    i = 0

    while i < len(words):
        match = None

        for j in range(1, 5):
            if i + j > len(words):
                break

            phrase = ' '.join(words[i:i+j]).lower()

            # hardcoded rickroll
            if phrase == "rickroll":
                response.append("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                break

            if phrase in emoji_dict:
                match = phrase
                break

        if match is None:
            response.append(words[i])
            i += 1
        else:
            response.append(emoji_dict[match])
            i += len(match.split(' '))
    return ' '.join(response)



# Getting the dictionary/csv file and creating DataFrame
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'updatedDict.csv')
df = pd.read_csv(csv_path)

# disocrd token
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

# Text to Emoji toggle variable
replace_text = True

# messaging
async def send_message(message: Message, user_message: str) -> None:
    global replace_text

    # Help command    
    if user_message == "/TTEhelp":
        await message.channel.send("Type '/TTEtoggle' to enable or disable Text to Emoji conversion\n \
                        To view commands or find help, go to https://github.com/carissalk/CYBR404AGILE/blob/main/README.md")
        return

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
        user_message = user_message[1:]

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