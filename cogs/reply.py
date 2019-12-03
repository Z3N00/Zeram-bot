import discord
from discord.ext import commands
import random
class reply(commands.Cog):
    """Reply on message not for users"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            if hasattr(ctx.command, 'on_error'):
                return
            else:
                embed = discord.Embed(title=f'Error in {ctx.command}', description=f'`{ctx.command.qualified_name} {ctx.command.signature}`\n{error}', color=0xff0000)
                await ctx.send(embed=embed)
        except:
            embed = discord.Embed(title=f'Error in {ctx.command}', description=f'{error}', color=0xff0000)
            await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_message(self, message):
        msg = message.content.lower()
        if message.author.id == self.bot.user.id:
            print("exc 1")
            return

        if(message.author.bot):
            print("exc 2")
            return

        if msg.startswith(("hello", "hi")):
            list = ['Hello', 'Hola', 'Bonjour']
            reply = random.choice(list)
            await message.channel.send('Hello {0.author.mention}'.format(message))
            print("exc 3")
            return

        if msg.startswith("hola"):
            list = ['Hello', 'Hola', 'Bonjour']
            await message.channel.send('Hola {0.author.mention}'.format(message))
            print("exc 3")
            return

        value1 = msg.find("x")
        list = ['XD', 'xD', 'xp', 'xd']
        if value1 != -1:
            await message.channel.send(random.choice(list))
            print("exc 4")
            return

        value2 = msg.find("lol")
        if value2 != -1:
            await message.channel.send("Hahahaha...😂")
            print("exc 5")
            return

        # value3 = msg.find("sometimes")
        # if value3 != -1:
        #     await message.channel.send("Some Crimes")



def setup(bot):
    bot.add_cog(reply(bot))
    print("reply is loaded")
