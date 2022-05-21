import Pyment
import discord
from discord import File
import random, string
import asyncio



client = discord.Client()
card = Pyment.card()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if "paycard1" in message.content:
        img = await loop.run_in_executor(None,card.paypay,"True",message.author.avatar_url,"sinc","100")
        file = discord.File(img,filename="paycard.png")
        await message.channel.send(file=file)
    elif "paycard2" in message.content:
        img = await loop.run_in_executor(None,card.paypay,False,message.author.avatar_url,message.author.name,str(random.randrange(100000)))

        file = discord.File(img,filename="paycard.png")
        await message.channel.send(file=file)
    else:
        pass

loop=asyncio.get_event_loop()
client.run('token')
