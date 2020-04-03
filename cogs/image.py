import discord
from discord.ext import commands

import asyncio

import random
import requests, json
import datetime



class Image(commands.Cog):
    """Image Commands"""

    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    async def dog(self, ctx):
        """Random Dog Pics"""
        url = 'https://dog.ceo/api/breeds/image/random'
        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        var = json.loads(response.text)
        img_url = var['message']
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value, title='🐶| Bork Bork', timestamp=datetime.datetime.utcnow())
        embed.set_image(url=img_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        """Random Cat Pics"""
        url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        var = json.loads(response.text)
        img_url = var[0]['url']
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value, title='🐱| Meow Meow', timestamp=datetime.datetime.utcnow())
        embed.set_image(url=img_url)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Image(bot))
    print("Image is loaded")
