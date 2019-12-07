import discord
from discord.ext import commands
import requests
import random
import json

class actions(commands.Cog):
    """Actions Commands"""

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


    @commands.command(aliases=['snuggle'])
    async def cuddle(self, ctx, *, member:discord.Member):
        """Cuddle with someone"""
        result = await self.action('anime cuddle')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} cuddle {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)


    @commands.command()
    async def hug(self, ctx, *, member:discord.Member):
        """Hugs are always better"""
        result = await self.action('anime hug')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} hugs {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, *, member:discord.Member):
        """Kiss to someone"""
        result = await self.action('anime kiss')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} kissed {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def lick(self, ctx, *, member:discord.Member):
        """Lick to someone"""
        result = await self.action('anime lick')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} licks {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def nom(self, ctx, *, member:discord.Member):
        """Take a bite"""
        result = await self.action('anime nom')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} noms on {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command(aliases=['pats'])
    async def pat(self, ctx, *, member:discord.Member):
        """Pat someone"""
        result = await self.action('anime pat')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} pats {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def poke(self, ctx, *, member:discord.Member):
        """Poke someone"""
        result = await self.action('anime poke')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} pokes {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, *, member:discord.Member):
        """slap someone"""
        result = await self.action('anime slap')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} slaps {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def stare(self, ctx, *, member:discord.Member):
        """Stare someone"""
        result = await self.action('anime stare')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} stares at {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def highfive(self, ctx, *, member:discord.Member):
        """Give a highfive"""
        result = await self.action('anime highfive')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} highfives {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def bite(self, ctx, *, member:discord.Member):
        """Bite someone"""
        result = await self.action('anime bite')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} bite on {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command(aliases=['hi'])
    async def greet(self, ctx, *, member:discord.Member):
        """Greet someone"""
        result = await self.action('anime hi')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} says hi to {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def punch(self, ctx, *, member:discord.Member):
        """Punch someone"""
        result = await self.action('anime punch')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} punch {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command(aliases=['holdhand'])
    async def handholding(self, ctx, *, member:discord.Member):
        """Hold hands"""
        result = await self.action('anime hold hands')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f"{ctx.author.name} hold {member.name}'s' hand", icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def tickle(self, ctx, *, member:discord.Member):
        """Tickle someone"""
        result = await self.action('anime tickle')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} tickle {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, *, member:discord.Member):
        """Kill someone"""
        result = await self.action('anime kill')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} killed {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def hold(self, ctx, *, member:discord.Member):
        """Hold someone"""
        result = await self.action('anime hold')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f"{ctx.author.name} grabs {member.name}'s hand'", icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def wave(self, ctx, *, member:discord.Member):
        """Wave someone"""
        result = await self.action('anime wave')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} waves to {member.name}', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)

    @commands.command()
    async def boop(self, ctx, *, member:discord.Member):
        """Boop someone"""
        result = await self.action('anime boop')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        embed.set_author(name=f'{ctx.author.name} boops {member.name} ;)', icon_url=ctx.author.avatar_url)
        embed.set_image(url=result)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(actions(bot))
    print("actions is loaded")
