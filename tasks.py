import discord
from discord.ext import tasks, commands
from datetime import datetime

TOKEN = ''

bot = commands.Bot(command_prefix='$')

client = discord.Client()

@tasks.loop(minutes=10)
async def yourhairlooksnice():
    channel = client.get_channel(827659439330426884)
    await channel.send("your hair looks nice")

@client.event
async def on_ready():
    yourhairlooksnice.start()

client.run(TOKEN)