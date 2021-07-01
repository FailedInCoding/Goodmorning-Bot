import discord
import os
import importlib
import logging
from collections import Counter
import datetime
from discord.ext.commands import AutoShardedBot as Bot

TOKEN = ''

def get_prefix_callable(defaults):
    def callable(bot, msg):
        prefixes = ['{}'.format(bot.user.mention), '@!{}>'.format(bot.user.id)]

        if msg.guild:
            try:
                server= db.servers.find_one({ "_id": str(msg.guild.id) })
                if server:
                    for pf in server["prefixes"]:
                        prefixes.append(pf)
            except:
                pass
            return defaults + prefixes

        return callable

class GoodMorningClient(Bot):
    def __init__(self, *args, **kwargs):
        callable = get_prefix_callable(kwargs["default_prefixes"])

        super().__init__(command_prefix=callable)

        self.counter = Counter ()
        self.uptime = datetime.datetime.now()
        self.logger = logging.getLogger('GoodmMorning')
        self.default_cogs = kwargs["default_cogs"]

    def init_cogs(self):
        all_cogs = ['Cogs.' + os.path.splitext(x)[0] for x in os.listdir('/Cogs.') if x.endswith('.py')]
        defaults = [x for x in all_cogs if x.split('-')[1] in self.default_cogs]

        total = 0 
        for cog in defaults:
            self.load_extension(cog)
            total += 1

        print('Started {}/{} Default Cogs.'.format(total, len(defaults)))

    async def launch(self, TOKEN):
        self.init_cogs()
        await self.start(TOKEN)