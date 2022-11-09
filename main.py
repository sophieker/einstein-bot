import discord
from discord.ext import commands
import random
import datetime
import os 
from os.path import join, dirname 
from dotenv import load_dotenv 

load_dotenv()

TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'ur':
        await message.channel.send('mom')

    if message.content == 'shut up and study':
        await message.channel.send('no u')

    if (message.author.id == 751060501445869569):
        start = datetime.time(16, 0, 0)
        end = datetime.time(23, 0, 0)
        now = datetime.datetime.now().time()
        if (start <= now <= end):
            await message.channel.send('go to bed wand')

    if message.content == 'gn':
        await message.channel.send('goodnight')

    if message.content == 'be nice for once':
        await message.channel.send('everyday I wake up thinking of you as my sunshine, that\'s why i\'m always up at night and sleeping all morning')

    if client.user.mentioned_in(message):

        if (message.author.id == 716084360348041358):
            await message.channel.send('you\'re the best, yoonjj')
        else:
            x = random.randint(0, 6)
            if x == 0:
                await message.channel.send('When I look at you, I wish I could meet you again for the first time… and walk past.')
            if x == 1:
                await message.channel.send('You are the sun in my life… now get 93 million miles away from me.')
            if x == 2:
                await message.channel.send('I can’t wait to spend my whole life without you.')
            if x == 3:
                await message.channel.send('I don’t hate you, but if you were drowning, I would give you a high five.')
            if x == 4:
                await message.channel.send('Sorry I can’t think of an insult dumb enough for you to understand.')
            if x == 5:
                await message.channel.send('The last time I saw something like you, it was behind metal grids.')
            if x == 6:
                await message.channel.send('You were so happy for the negativity of your Covid test, we didn’t want to spoil the happiness by telling you it was IQ test.')
        
        

client.run(TOKEN)