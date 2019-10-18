import discord
from discord.ext import commands
import random
class Reply(commands.Cog):
    """Reply on message not for users"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content.lower()
        if message.author.id == self.bot.user.id:
            return

        if(message.author.bot):
            return

        if msg.startswith(("hello", "hi")):
            await message.channel.send('Hello {0.author.mention}'.format(message))
            return

        value = msg.find("x")
        list = ['XD', 'xD', 'xp', 'xd']
        if value != -1:
            await message.channel.send(random.choice(list))
            return

        value2 = msg.find("lol")
        if value2 != -1:
            await message.channel.send("Hahahaha...😂")
            return



def setup(bot):
    bot.add_cog(Reply(bot))
    print("reply is loaded")
