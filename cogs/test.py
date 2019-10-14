import discord
from discord.ext import commands

class TestCog(commands.Cog):
    """TestCog"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='repeat', aliases=['copy', 'mimic'])
    async def do_repeat(self, ctx, *, our_input: str):
        await ctx.send(our_input)

    @commands.command()
    async def hi(self, ctx):
        await ctx.send("hello")

    @commands.command()
    async def greet(self, ctx):
        await ctx.send("hello")

def setup(bot):
    bot.add_cog(TestCog(bot))
