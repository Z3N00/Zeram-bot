import discord
from discord.ext import commands
import requests
import random
import json

class actions(commands.Cog):
    """Actions Commands"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def slap(self, ctx, *, member:discord.Member):
        """Slap Someone"""
        apikey = "2MNXIESVXKVS"  # test value
        lmt = 50
        search_term = 'anime slap'

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            value = random.randint(0, 0xffffff)
            embed = discord.Embed(color=value)
            embed.set_author(name=f'{ctx.author.name} slaps {member.name}', icon_url=ctx.author.avatar_url)
            top_8gifs = json.loads(r.content)
            my_dict = top_8gifs

            gifs = my_dict['results'][random.randint(0, 50)]['media'][0]['gif']['url']
            embed.set_image(url=gifs)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No result found")


    @commands.command()
    async def hug(self, ctx, *, member:discord.Member):
        """Hug Someone"""
        apikey = "2MNXIESVXKVS"  # test value
        lmt = 50
        search_term = 'anime hug'

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            value = random.randint(0, 0xffffff)
            embed = discord.Embed(color=value)
            embed.set_author(name=f'{ctx.author.name} hugs {member.name}!! cute', icon_url=ctx.author.avatar_url)
            top_8gifs = json.loads(r.content)
            my_dict = top_8gifs

            gifs = my_dict['results'][random.randint(0, 50)]['media'][0]['gif']['url']
            embed.set_image(url=gifs)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No result found")

    @commands.command()
    async def kiss(self, ctx, *, member:discord.Member):
        """Kiss Someone"""
        apikey = "2MNXIESVXKVS"  # test value
        lmt = 50
        search_term = 'anime kiss'

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            value = random.randint(0, 0xffffff)
            embed = discord.Embed(color=value)
            embed.set_author(name=f'{ctx.author.name} kiss {member.name}!! awww..', icon_url=ctx.author.avatar_url)
            top_8gifs = json.loads(r.content)
            my_dict = top_8gifs

            gifs = my_dict['results'][random.randint(0, 50)]['media'][0]['gif']['url']
            embed.set_image(url=gifs)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No result found")


    @commands.command()
    async def stare(self, ctx, *, member:discord.Member):
        """Stare Someone"""
        apikey = "2MNXIESVXKVS"  # test value
        lmt = 50
        search_term = 'anime stare'

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            value = random.randint(0, 0xffffff)
            embed = discord.Embed(color=value)
            embed.set_author(name=f'{ctx.author.name} stares {member.name}!!cute', icon_url=ctx.author.avatar_url)
            top_8gifs = json.loads(r.content)
            my_dict = top_8gifs

            gifs = my_dict['results'][random.randint(0, 50)]['media'][0]['gif']['url']
            embed.set_image(url=gifs)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No result found")


    @commands.command(aliases=['snuggle'])
    async def cuddle(self, ctx, *, member:discord.Member):
        """cuddle Someone"""
        apikey = "2MNXIESVXKVS"  # test value
        lmt = 50
        search_term = 'anime cuddle'

        r = requests.get(
            "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

        if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            value = random.randint(0, 0xffffff)
            embed = discord.Embed(color=value)
            embed.set_author(name=f'{ctx.author.name} cuddle {member.name}', icon_url=ctx.author.avatar_url)
            top_8gifs = json.loads(r.content)
            my_dict = top_8gifs

            gifs = my_dict['results'][random.randint(0, 50)]['media'][0]['gif']['url']
            embed.set_image(url=gifs)
            await ctx.send(embed=embed)
        else:
            await ctx.send("No result found")



def setup(bot):
    bot.add_cog(actions(bot))
    print("actions is loaded")
