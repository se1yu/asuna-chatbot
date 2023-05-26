import discord
from discord.ext import tasks

client = commands.Bot(command_prefix="!")

@tasks.loop(hours=1.0) #without quotation marks Reddit won't let me use the at sign without them

async def send_message()

channel = client.get_channel(channelId)

channel.send("Message")



@client.event

async def on_ready()

send_message.start()