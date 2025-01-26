import discord
import os
import random
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

bankai = ['Daiguren Hyōrinmaru', 'Enma Kōrogi', 'Hakka no Togame', \
            'Hihiō Zabimaru', 'Jakuhō Raikōben', 'Kamishini no Yari', \
            'Katen Kyōkotsu: Karamatsu Shinjū', 'Kinshara Butōdan', 'Kokujō Tengen Myō\'ō', \
            'Kokujō Tengen Myō\'ō: Dangai Jōe', 'Konjiki Ashisogi Jizō', 'Konjiki Ashisogi Jizō: Matai Fukuin Shōtai', \
            'Kōkō Gonryō Rikyū', 'Minazuki', 'Ryūmon Hōzukimaru', \
            'Senbonzakura Kageyoshi', 'Shatatsu Karagara Shigarami no Tsuji', 'Sōō Zabimaru', \
            'Tekken Tachikaze', 'Tensa Zangetsu', 'Zanka no Tachi']

lyrics = ['if', 'you', 'wanna', 'see', 'some', 'action', 'gotta', 'be', 'the', \
            'center', 'of', 'attraction', 'make', 'sure', 'that', 'they', 'got', \
            'their', 'eyes', 'on', 'you', 'like', 'face', 'every', 'magazine', 'focus', \
            'attention', 'name', 'one', 'must', 'mention', 'come', 'out', 'from', 'shadows', \
            'it\'s', 'your', 'time', 'cause', 'tonight', 'is', 'night', 'for', 'everyone', \
            'to', 'natural', 'know', 'this', 'where', 'be', 'it', 'destiny', 'sensational', \
            'and', 'believe', 'what', 'you\'ve', 'waited', 'all', 'adore', 'so', 'baby', 'now', \
            'feel', 'number', 'shining', 'bright', 'living', 'fantasy', 'brightest', 'star', \
            'that\'s', 'ever', 'been']

URL = "https://www.youtube.com/watch?v=1lsn2tT5yTc"

def find_lyrics(message):
    sentence = message.split(" ")
    count = 0

    for w in sentence:
        for l in lyrics:
            if w == l:
                count += 1

    if count >= 5:
        return True
    else:
        return False

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    text = message.content.lower()

    if 'bankai' in text:
        num = random.randint(0, len(bankai) - 1)
        await message.channel.send(bankai[num])

    found = find_lyrics(text)
    if found:
        await message.channel.send(URL)

client.run(os.getenv("DISCORD_TOKEN"))