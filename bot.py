import discord
from keep_alive import keep_alive

client = discord.Client()
remove = "GREEN.directmessage "

@client.event
async def on_ready():
  print("I ready.")
  await client.change_presence(game=discord.Game(name="Ur mom"))



@client.event
async def on_message(message):
  if "GREEN.directmessage" in message.content:
    if message.author != client.user:
      await client.send_message(message.author, message.content)

"""@client.command(pass_context=True)
async def yt(ctx, url):
    url = 'https://www.youtube.com/watch?v=GRxofEmo3HA'

    author = ctx.message.author
    voice_channel = author.voice_channel
    vc = await client.join_voice_channel(voice_channel)

    player = await vc.create_ytdl_player(url)
    player.start()"""

@client.event
async def on_message(message):
  if "GREEN.say" in message.content:
    if message.author != client.user:
      await client.send_message(message.channel, message.content.strip("GREEN.say "))



keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
