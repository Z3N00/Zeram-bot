import discord
from discord.ext import commands
import random
class Basic(commands.Cog):
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
    async def greet(self, ctx, member):
        """Greet the mention user"""
        msg = random.choice(['Sup ', 'Wassup ', 'Hello ', 'Hi ', 'Namaste '])
        await ctx.send(msg + member)

    @commands.command()
    async def ping(self, ctx):
        """"Bot latency"""
        await ctx.send(f'pong! {round(self.bot.latency*1000)}ms')

def setup(bot):
    bot.add_cog(Basic(bot))
    print("basic is loaded")
