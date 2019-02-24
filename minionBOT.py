import discord
import asyncio
import os


client = discord.Client()

@client.event
async def on_ready():
    print("loigin")
    print(client.user.name)
    print(client.user.id)
    print("-------------------")
    await client.change_presence(game=discord.Game(name='바나나 먹는중..', type=1))


@client.event
async def on_message(message):
    if message.content.startswith('안녕 미니모'):
        await client.send_message(message.channel, "..안뇽")
    if message.content.startswith('미니모!'):
        await client.send_message(message.channel, "바냐냐 ㅎㅎ")
    if message.content.startswith('바나나?'):
        await client.send_message(message.channel, "미니모!")
    if message.content.startswith('출첵!'):
        await client.send_message(message.channel, "{@name}출첵 하셨습니다! :banana:")
        

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

