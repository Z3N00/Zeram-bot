import discord
from discord.ext import commands
import random
class Reply(commands.Cog):
    """TestCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        value = message
        if message.author.id == self.bot.user.id:
            return
        if(message.author.bot):
            return

        if message.content.startswith('hello') or message.content.startswith('Hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))
            return

        capital = message.content.find('X')
        small = message.content.find('x')
        list = ['XD', 'xD', 'xp', 'xd']
        if capital != -1 or small != -1 :
            await message.channel.send(random.choice(list))

def setup(bot):
    bot.add_cog(Reply(bot))
