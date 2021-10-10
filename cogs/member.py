import discord
from discord.ext import commands
import urbandict
import wikipedia
import translators as ts
import random

class Member(commands.Cog):
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
    async def translate(self, ctx, *, message):
        value = random.randint(0, 0xffffff)
        translation = ts.google(message)
        embed = discord.Embed(description='Translation: ' + '**' + translation + '**', color=value, title='Message: ' + message)
        await ctx.send(embed=embed)


    @commands.command()
    async def define(self, ctx, *, term):
        information = urbandict.define(term)
        
        data1 = information[0]
        data2 = information[1]
        embed = discord.Embed(description= "1. " + data1['def'] + "\n" + "2. " + data2['def'], color=discord.Colour.blue())
        
        embed.add_field(name='Example 1', value='```' + data1['example'] + '```', inline=False)
        embed.add_field(name='Example 2', value='```' + data2['example'] + '```', inline=False)
        embed.set_author(name='Definition of ' + term, icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)


    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(color=0xf41af4, description="[Invite Me! 😃 😱](https://discordapp.com/oauth2/authorize?client"
                                                      "_id=607611336268054563&scope=bot&permissions=2146958847)")

        embed.set_footer(text="Discord bot invite link.")
        await ctx.send(embed=embed)


    @commands.command()
    async def search(self, ctx, *, query):
        flag = False

        await ctx.send("Searching your query...")
        try:
            data = wikipedia.summary(query)
        except:
            flag = True
            # print(data)
        if flag:
            failQuery = wikipedia.page(query)
            await ctx.send("Sorry I am unable to find answers to your query... :grimacing:")
            await ctx.send(f"You can click on this link for your answer: {failQuery.url} :smiley:")
        else:
            Data = data.split("\n")

        for d in Data:
            await ctx.send("```" + d + "```")
        await ctx.send("I hope you found this answer convincing. :smiley:")




def setup(bot):
    bot.add_cog(Member(bot))
