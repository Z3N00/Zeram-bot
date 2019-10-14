import discord
from discord.ext import commands

class TestCog(commands.Cog):
    """TestCog"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def test(self, ctx):
        await ctx.send("hello")

def setup(bot):
    bot.add_cog(TestCog(bot))
