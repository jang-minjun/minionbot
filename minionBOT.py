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
    if message.content.startswith('미니모?'):
        await client.send_message(message.channel, "바냐냐 ㅎㅎ")
    if message.content.startswith('바나나 먹자!'):
        await client.send_message(message.channel, "미니모!!")
    if message.content.startswith('출첵!'):
        await client.send_message(message.channel, "{@name}출첵 하셨습니다! :banana:")
        
    if message.content.startswith('미니모주사위'):
        roll = message.content.split(" ")
        rolld = roll[1].split("o")
        dice = 0
        for i in range(1, int(rolld[0])+1):
            dice = dice + random.randint(1, int(rolld[1]))
        await client.send_message(message.channel, str(dice))

    if message.content.startswith('미니모 골라'):
        choice = message.content.split(",")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await client.send_message(message.channel, choiceresult)

    if message.content.startswith('미니모 뭐먹지?'):
        food = "짜장면 짭뽕 라면 밥 물만먹어"
        foodchoice = food.split(" ")
        foodnumber = random.randint(1, len(foodchoice))
        foodresult = foodchoice[foodnumber-1]
        await client.send_message(message.channel, foodresult)
        
        
        
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

