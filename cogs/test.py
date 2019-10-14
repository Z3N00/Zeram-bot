import discord
from discord.ext import commands

class TestCog(commands.Cog):
    """TestCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        embed = discord.Embed(description='Your avatar :flushed: ')

        if member == None:
            embed.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def test(self, ctx):
        await ctx.send("hello")

def setup(bot):
    bot.add_cog(TestCog(bot))
