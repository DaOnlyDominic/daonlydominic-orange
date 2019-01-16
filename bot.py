import discord
import os
import random

client = discord.Client()
jokes = ["What do you call a dull pencil?", "What do you call a cow with no legs?", "", "", ""]
answers = ["Pointless!", "Ground beef!", "", "", ""]
what = "what"

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Python 3.6.7"))
    
#bot.hello
@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith('bot.hello'):
            msg = 'Hello {0.author.mention}'.format(message)
            await client.send_message(message.channel, msg)

#bot.joke
@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith('bot.joke'):
            rand = random.randint(0,1)
            client.send_message(message.channel, jokes[rand])
            async def on_messge(message):
                if message.author != client.user:
                    if what in message.content:
                        await client.send_message(message.channel, answers[rand])
                        await client.send_message(message.channel, 'HAHAHAHA!!')
            

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
