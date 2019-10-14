import discord
from discord.ext import commands
import pyjokes
import aiohttp
import random
import requests
import json

class Joke(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        list = ['https://www.reddit.com/r/memes/hot.json',
                'https://www.reddit.com/r/dankmemes/new.json?sort=hot',
                'https://www.reddit.com/r/dank_meme/hot.json']
        url = random.choice(list)
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command()
    async def gif(self, ctx, *, search_term):

        apikey = "2MNXIESVXKVS"  # test value
        lmt = 25

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            value = random.randint(0, 0xffffff)
            embed = discord.Embed(title="Your Gif", color=value)
            top_8gifs = json.loads(r.content)
            my_dict = top_8gifs

            gifs = my_dict['results'][random.randint(0, 24)]['media'][0]['gif']['url']
            embed.set_image(url=gifs)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No result found")


    @commands.command()
    async def chucknorris(self, ctx):
        url = 'http://api.icndb.com/jokes/random'
        value = random.randint(0, 0xffffff)
        resp = requests.get(url=url)
        data = resp.json()
        joke = data['value']['joke']
        embed = discord.Embed(description=joke, color=value, title=':punch: ' + 'Chuck Norris ' + ':punch:')

        await ctx.send(embed=embed)


    @commands.command()
    async def geekjoke(self, ctx):
        value = random.randint(0, 0xffffff)
        image = 'https://images.discordapp.net/avatars/563434444321587202/ea95e92cbbedade1d5d06c7a34067e58.png?size=512'
        embed = discord.Embed(description='**' + pyjokes.get_joke() + '**', color=value)
        embed.set_footer(text="These jokes are not for normie people!", icon_url=image)
        await ctx.send(embed=embed)


    @commands.command()
    async def joke(self, ctx):
        value = random.randint(0, 0xffffff)
        source = 'Source:https://icanhazdadjoke.com'
        image = 'https://avatars.slack-edge.com/2016-08-13/69162711190_9ce4a3707b47d2a5a8d4_512.png'
        r = requests.get('https://icanhazdadjoke.com', headers={"Accept": "application/json"})
        raw_joke = r.json()
        joke = raw_joke['joke']
        embed = discord.Embed(description='**' + joke + '**', color=value)
        embed.set_footer(text=source, icon_url=image)

        await ctx.send(embed=embed)


    @commands.command()
    async def roast(self, ctx, member=None):
        roasts = json.loads(open('roast.json').read())
        reply = random.choice(roasts)

        await ctx.send(reply)


def setup(bot):
    bot.add_cog(Joke(bot))
