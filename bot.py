import discord
import os
import random
import time
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

random.seed(time.time())

URL = "https://www.youtube.com/watch?v=1lsn2tT5yTc"

def get_bankai():
    bankai = ""
    try:
        file = open('bankai.txt', 'r', encoding='utf-8')
    except:
        print('Could not access file.')
    else:
        num = random.randint(0, 20)
        for i in range(num):
            file.readline()
        bankai += file.readline().rstrip('\n')

    return bankai

def get_lyrics():
    lyrics = []

    try:
        file = open('lyrics.txt', 'r')
    except:
        print('Could not access file.')
    else:
        lyrics = file.read().split(',')

    return lyrics

def find_lyrics(message):
    lyrics = get_lyrics()

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
        msg = get_bankai()
        await message.channel.send(msg)

    found = find_lyrics(text)
    if found:
        await message.channel.send(URL)

client.run(os.getenv("DISCORD_TOKEN"))