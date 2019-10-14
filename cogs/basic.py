import discord
from discord.ext import commands
import random
class Basic(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    # @commands.command(name='repeat', aliases=['copy', 'mimic'])
    # async def do_repeat(self, ctx, *, our_input: str):
    #     await ctx.send(our_input)


    @commands.command()
    async def big(self, ctx):
        await ctx.send("Bang")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("hello " + ctx.author.mention)

    @commands.command()
    async def greet(self, ctx, member):
        msg = random.choice(['Sup ', 'Wassup ', 'Hello ', 'Hi ', 'Namaste '])
        await ctx.send(msg + member)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong! {round(self.bot.latency*1000)}ms')

def setup(bot):
    bot.add_cog(Basic(bot))
