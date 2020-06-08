import discord
from discord.ext import commands
import random
from requests import get

class basic(commands.Cog):
    """Basic Commands"""

    def __init__(self, bot):
        self.bot = bot


    # @commands.command(name='repeat', aliases=['copy', 'mimic'])
    # async def do_repeat(self, ctx, *, our_input: str):
    #     await ctx.send(our_input)


    @commands.command()
    async def big(self, ctx):
        """Bot will say bang"""
        await ctx.send("Bang")

    @commands.command()
    async def hello(self, ctx):
        """Bot will say hello"""
        await ctx.send("hello " + ctx.author.mention)

    @commands.command()
    async def ip(self, ctx):
        ip = get('https://api.ipify.org').text
        await ctx.send(ip)
        
    @commands.command()
    async def ping(self, ctx):
        """Bot latency"""
        await ctx.send(f'pong! {round(self.bot.latency*1000)}ms')

def setup(bot):
    bot.add_cog(basic(bot))
    print("basic is loaded")
