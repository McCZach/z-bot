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

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == 'bankai':
        num = random.randint(0, len(bankai))
        await message.channel.send(bankai[num])

client.run(os.getenv("DISCORD_TOKEN"))