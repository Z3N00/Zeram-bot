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
            return

        if(message.author.bot):
            return

        if msg.startswith(("hello", "hi", "hola")):
            reply = random.choice(['Hello', 'Hola', 'Hi', 'Wassup'])
            await message.channel.send(f'{reply} {message.author.mention}')
            return

        value1 = msg.find("x")
        list = ['XD', 'xD', 'xp', 'xd']
        if value1 != -1:
            await message.channel.send(random.choice(list))
            return

        value2 = msg.find(("oh"))
        if value2 != -1:
            await message.channel.send("What Ohhh? ")
            return

        value3 = msg.find(("aww"))
        if value3 != -1:
            await message.channel.send("🥺")
            return

        value4 = msg.find("sometimes")
        if value3 != -1:
            await message.channel.send("Some Crimes")


        words = ["lmfao", "lmao", "lolo"]
        if any(c in msg for c in words):
            await message.channel.send("Hahahaha...😂")

        words2 = ["hehe", "hahaha"]
        if any(c in msg for c in words2):
            await message.channel.send("Lmao you so funny!")

        words3 = [":3", ":0", ":p", ":!", ":|", ":/", ":v", ":o", ";"]
        if any(c in msg for c in words3):
            await message.channel.send(":3")

        words4 = ["fuck", "shit", "asshole"]
        if any(c in msg for c in words4):
            await message.channel.send("God is watching you 😠", delete_after=4.0)

def setup(bot):
    bot.add_cog(reply(bot))
    print("reply is loaded")
