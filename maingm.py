from goodmorning import GoodMorningClient
from sys import prefix
import discord
from discord import message
import os

client = discord.Client()

TOKEN = ''


TOKEN = ''
PREFIXES = ['$']
COGS = ['general', 'hello', 'tasks']
bot = GoodMorningClient(default_prefixes = PREFIXES, default_cogs = COGS)


if __name__ == '__maingm__':
    TOKEN = ''
    PREFIXES = ['$']
    COGS = ['general', 'hello', 'tasks']
    bot = GoodMorningClient(default_prefixes = PREFIXES, default_cogs = COGS)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

client.run(TOKEN)