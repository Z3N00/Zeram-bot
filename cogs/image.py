import discord
from discord.ext import commands

import asyncio

import random
import requests, json
import datetime
import aiohttp


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


    @commands.command()
    async def bunny(self, ctx):
        """Random bunny pics"""
        key ='jHpBGu-nSfzfwYw6VCM5PjEjnXhQC8__dTtaBW4_B7I'
        page_num = random.randint(1, 40)
        url = f'https://api.unsplash.com/search/photos?page={page_num}&query=bunny&client_id={key}'

        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        var = json.loads(response.text)
        pic_num = random.randint(0, 9)
        img_url = var['results'][pic_num]['urls']['raw']

        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value, timestamp=datetime.datetime.utcnow())
        embed.set_image(url=img_url)
        embed.set_footer(text=ctx.author)

        await ctx.send(embed=embed)


    @commands.command()
    async def lizard(self, ctx):
        """Random lizard pics"""
        key ='jHpBGu-nSfzfwYw6VCM5PjEjnXhQC8__dTtaBW4_B7I'
        page_num = random.randint(1, 100)
        url = f'https://api.unsplash.com/search/photos?page={page_num}&query=lizard&client_id={key}'

        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        var = json.loads(response.text)
        pic_num = random.randint(0, 9)
        img_url = var['results'][pic_num]['urls']['raw']

        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value, timestamp=datetime.datetime.utcnow())
        embed.set_image(url=img_url)
        embed.set_footer(text=ctx.author)
        await ctx.send(embed=embed)


    @commands.command(aliases=['xkcd', 'comic'])
    async def randomcomic(self, ctx):
        '''Get a comic from xkcd.'''
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://xkcd.com/info.0.json') as resp:
                data = await resp.json()
                currentcomic = data['num']
        rand = random.randint(0, currentcomic)  # max = current comic
        async with aiohttp.ClientSession() as session:
            async with session.get(f'http://xkcd.com/{rand}/info.0.json') as resp:
                data = await resp.json()
        em = discord.Embed(color=discord.Color.green())
        em.title = f"XKCD Number {data['num']}- \"{data['title']}\""
        em.set_footer(text=f"Published on {data['month']}/{data['day']}/{data['year']}")
        em.set_image(url=data['img'])
        await ctx.send(embed=em)




def setup(bot):
    bot.add_cog(Image(bot))
    print("Image is loaded")
