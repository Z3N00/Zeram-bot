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

    @commands.command(aliases=['emojify'])
    async def emoji(self, ctx, emoji:discord.Emoji):
        """Emojify the custom emojis"""
        id = emoji.id
        url=f'https://cdn.discordapp.com/emojis/{id}.png?v=1'
        embed = discord.Embed(color=0x696969)
        embed.set_image(url=url)
        await ctx.send(embed=embed)

    @commands.command()
    async def fox(self, ctx):
        """Random fox images"""
        url = 'https://randomfox.ca/floof/?ref=apilist.fun'
        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        var = json.loads(response.text)
        image = var['image']
        value = random.randint(0, 0xffffff)
        embed=discord.Embed(color=value, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'{ctx.author}')
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def panda(self, ctx):
        """Random panda images"""
        url = 'https://some-random-api.ml/img/panda'
        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        var = json.loads(response.text)
        image = var['link']
        value = random.randint(0, 0xffffff)
        embed=discord.Embed(color=value, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'{ctx.author}')
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def redpanda(self, ctx):
        """Random redpanda images"""
        url = 'https://some-random-api.ml/img/red_panda'
        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        var = json.loads(response.text)
        image = var['link']
        value = random.randint(0, 0xffffff)
        embed=discord.Embed(color=value, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'{ctx.author}')
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def bird(self, ctx):
        """Random bird images"""
        url = 'https://some-random-api.ml/img/birb'
        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        var = json.loads(response.text)
        image = var['link']
        value = random.randint(0, 0xffffff)
        embed=discord.Embed(color=value, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'{ctx.author}')
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def koala(self, ctx):
        """random koala images"""
        url = 'https://some-random-api.ml/img/koala'
        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        var = json.loads(response.text)
        image = var['link']
        value = random.randint(0, 0xffffff)
        embed=discord.Embed(color=value, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f'{ctx.author}')
        embed.set_image(url=image)
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Image(bot))
    print("Image is loaded")
