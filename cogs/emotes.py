import discord
from discord.ext import commands
import requests
import random
import json


class emotes(commands.Cog):
    """Emote Commands"""

    def __init__(self, bot):
        self.bot = bot


    async def action(self, search_term):

        apikey = "2MNXIESVXKVS"  # test value
        lmt = 50

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes

            top_8gifs = json.loads(r.content)
            my_dict = top_8gifs

            gifs = my_dict['results'][random.randint(0, 50)]['media'][0]['gif']['url']
            return gifs

        else:
            return "No result found"



    @commands.command()
    async def blush(self, ctx):
        """Blushes"""
        result = await self.action('anime blush')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} is blushing!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)


    @commands.command()
    async def cry(self, ctx):
        """Cry"""
        result = await self.action('anime cry')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} is crying!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)


    @commands.command()
    async def dance(self, ctx):
        """Dance"""
        result = await self.action('anime dance')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} is dancing!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)


    @commands.command()
    async def lewd(self, ctx):
        """Lewd"""
        result = await self.action('anime lewd')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} says, thats lewd!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def pout(self, ctx):
        """Pout"""
        result = await self.action('anime pout')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} pouts!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command(aliases=['shrugs'])
    async def shrug(self, ctx):
        """Shrugs"""
        result = await self.action('anime shrug')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} shrugs wew!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command(aliases=['sleep'])
    async def sleepy(self, ctx):
        """Sleep"""
        result = await self.action('anime sleep')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} is sleeping!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def smile(self, ctx):
        """Smiles"""
        result = await self.action('anime smile')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} is smiling!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)


    @commands.command()
    async def smug(self, ctx):
        """Smug"""
        result = await self.action('anime smug')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} has a smug look!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command(aliases=['thumb'])
    async def thumbsup(self, ctx):
        """Thumbsup"""
        result = await self.action('anime thumbsup')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} has a thumbs up!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def wag(self, ctx):
        """Wags"""
        result = await self.action('anime wag')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} Wags!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)


    @commands.command()
    async def thinking(self, ctx):
        """thinking"""
        result = await self.action('anime thinking')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} is thinking!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)


    @commands.command()
    async def triggered(self, ctx):
        """Triggered"""
        result = await self.action('anime triggered')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} is now triggered!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def teehee(self, ctx):
        """Teehee"""
        result = await self.action('anime teehee')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} :3!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def deredere(self, ctx):
        """Deredere"""
        result = await self.action('anime deredere')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} awhhh!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def scoff(self, ctx):
        """Scoff"""
        result = await self.action('anime scoff')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} tsk!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def happy(self, ctx):
        """Happy"""
        result = await self.action('anime happy')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} is happy!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def grin(self, ctx):
        """Grin"""
        result = await self.action('anime grin')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} uff..!', icon_url=ctx.author.avatar.url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(emotes(bot))
    print('emotes is loaded')
