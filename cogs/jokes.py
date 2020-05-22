import discord
from discord.ext import commands
import pyjokes
import aiohttp
import random
import requests
import json

class joke(commands.Cog):
    """Joke Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        """Choose some random meme"""
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
        """Some more gifs"""
        apikey = "2MNXIESVXKVS"  # test value
        lmt = 50

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            value = random.randint(0, 0xffffff)
            embed = discord.Embed(title="Your Gif", color=value)
            top_8gifs = json.loads(r.content)
            my_dict = top_8gifs

            gifs = my_dict['results'][random.randint(0, 50)]['media'][0]['gif']['url']
            embed.set_image(url=gifs)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No result found")


    @commands.command()
    async def chucknorris(self, ctx):
        """Chucknorris is the best"""
        url = 'http://api.icndb.com/jokes/random'
        value = random.randint(0, 0xffffff)
        resp = requests.get(url=url)
        data = resp.json()
        joke = data['value']['joke']
        embed = discord.Embed(description=joke, color=value, title=':punch: ' + 'Chuck Norris ' + ':punch:')

        await ctx.send(embed=embed)


    @commands.command()
    async def geekjoke(self, ctx):
        """Nerdy jokes"""
        value = random.randint(0, 0xffffff)
        image = 'https://images.discordapp.net/avatars/563434444321587202/ea95e92cbbedade1d5d06c7a34067e58.png?size=512'
        embed = discord.Embed(description='**' + pyjokes.get_joke() + '**', color=value)
        embed.set_footer(text="These jokes are not for normie people!", icon_url=image)
        await ctx.send(embed=embed)


    @commands.command()
    async def joke(self, ctx):
        """Random jokes"""
        value = random.randint(0, 0xffffff)
        source = 'Source:https://icanhazdadjoke.com'
        image = 'https://avatars.slack-edge.com/2016-08-13/69162711190_9ce4a3707b47d2a5a8d4_512.png'
        r = requests.get('https://icanhazdadjoke.com', headers={"Accept": "application/json"})
        raw_joke = r.json()
        joke = raw_joke['joke']
        embed = discord.Embed(description='**' + joke + '**', color=value)
        await ctx.send(embed=embed)


    @commands.command()
    async def roast(self, ctx, member=None):
        """Get burned"""
        roasts = json.loads(open('roast.json').read())
        reply = random.choice(roasts)

        await ctx.send(reply)


    @commands.command(aliases=['trump', 'trumpquote'])
    async def asktrump(self, ctx, *, question):
        '''Ask Donald Trump a question!'''
        async with aiohttp.ClientSession() as session:
            async with session.get(f'https://api.whatdoestrumpthink.com/api/v1/quotes/personalized?q={question}') as resp:
                file = await resp.json()
        quote = file['message']
        em = discord.Embed(color=discord.Color.green())
        em.title = "What does Trump say?"
        em.description = quote
        em.set_footer(text="Made possible by whatdoestrumpthink.com", icon_url="https://images.unsplash.com/photo-1580128660010-fd027e1e587a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyNjEzMn0")
        await ctx.send(embed=em)


    @commands.command()
    async def insult(self, ctx, *, member=None):
        """Insult Someone"""
        value = random.randint(0, 0xffffff)
        url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
        r = requests.get(url)
        if r.status_code == 200:
            content = json.loads(r.content)
            insult = content['insult']
            embed = discord.Embed(description=insult, color=value)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(joke(bot))
    print("jokes is loaded")
