import discord
from discord.ext import commands
import aiohttp
from bs4 import BeautifulSoup
import random
import json

class nsfw(commands.Cog):
    """Only high qualty ;)"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['porngif'])
    @commands.is_nsfw()
    async def pgif(self, ctx):
        """Shows some porn gifs"""
        colour = random.randint(0, 0xffffff)
        value1 = random.randint(1600, 1999)
        value2 = random.choice(['17A9', '17B9', '17C9', '17D9', '17E9', '17F9'])
        embed = discord.Embed(title='Here, take some gifs 😉', colour=colour)
        url1 = f'https://cdn.boob.bot/Gifs/{value1}.gif'
        url2 = f'https://cdn.boob.bot/Gifs/{value2}.gif'
        get_url = random.choice([url1, url2, url1, url1])
        embed.set_image(url=get_url)
        await ctx.send(embed=embed)


    @commands.command(aliases=['boob'])
    @commands.is_nsfw()
    async def boobs(self, ctx):
        """Shows some boobs"""
        try:
            search = ("http://api.oboobs.ru/boobs/{}".format(random.randint(0, 10394)))
            async with aiohttp.ClientSession() as cs:
                async with cs.get(search) as r:
                    result = await r.json()
                    boob = random.choice(result)
                    boob_img = "http://media.oboobs.ru/{}".format(boob["preview"])

        except Exception as e:
            await ctx.send("{} ` Error getting results.`".format(ctx.message.author.mention))
            return
        colour = random.randint(0, 0xffffff)
        embed = discord.Embed(title='your wish my command 😉', color=colour)
        embed.set_image(url=boob_img)
        await ctx.send(embed=embed)


    @commands.command()
    @commands.is_nsfw()
    async def ass(self, ctx):
        """Shows some ass"""
        try:
            search = ("http://api.obutts.ru/butts/{}".format(random.randint(0, 4378)))
            async with aiohttp.ClientSession() as cs:
                async with cs.get(search) as r:
                    result = await r.json()
                    butt = random.choice(result)
                    butt_img = "http://media.obutts.ru/{}".format(butt["preview"])

        except Exception as e:
            await ctx.send("{} ` Error getting results.`".format(ctx.message.author.mention))
            return
        colour = random.randint(0, 0xffffff)
        embed = discord.Embed(title='your wish my command 😉', color=colour)
        embed.set_image(url=butt_img)
        await ctx.send(embed=embed)



    @pgif.error
    @boobs.error
    @ass.error
    async def pgif_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send("NSFW commands are not allowed in this channel", delete_after=6.0)


def setup(bot):
    bot.add_cog(nsfw(bot))
    print("Nsfw is loaded")
