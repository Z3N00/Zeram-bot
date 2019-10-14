import discord
from discord.ext import commands
import requests
import random
import json
import giphy_client
from giphy_client.rest import ApiException
from brainyquote import pybrainyquote
import pyaztro

class Fun(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def flip(self, ctx):
        Flip = random.choice(['Heads', 'Tails'])
        await ctx.send(Flip)


    @commands.command()
    async def reverse(self, ctx, *, message):
        rev = message[::-1]
        await ctx.send(rev)


    @commands.command()
    async def roll(self, ctx, dice: str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)


    @commands.command(description='For when you wanna settle the score some other way')
    async def choose(self, ctx, *choices: str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))


    @commands.command()
    async def repeat(self, ctx, times: int, *, content='repeating...'):
        """Repeats a message multiple times."""
        member = discord.Message
        if times <= 100:
            for i in range(times):
                await ctx.send(content)

        else:
            await ctx.send("You want to kill me? Noob!")


    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, question):
        """Chooses between multiple choices."""
        responses = json.loads(open('responses.json').read())
        reply = f'Question: {question}\nAnswer: {random.choice(responses)}'
        embed = discord.Embed(description=reply, title=":8ball: | Let me see :thinking:",
                            color=discord.Colour.dark_magenta())

        await ctx.send(embed=embed)



    async def search_gifs(self, query):
        giphy_token = 'AZJ12FRxeXdoCEkuEFD3CidxCIe5GmvD'
        api_instance = giphy_client.DefaultApi()

        try:
            response = api_instance.gifs_search_get(giphy_token, query, limit=100, rating='')
            lst = list(response.data)
            gif = random.choices(lst)

            return gif[0].url

        except ApiException as e:
            return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

    @commands.command()
    async def giphy(self, ctx, *, search):
        gifs = await self.search_gifs(search)
        await ctx.send(gifs)


    @commands.command()
    async def quote(self, ctx, topic=None):
        # popular_choice = ['motivational', 'life', 'positive', 'friendship', 'success', 'happiness', 'love']
        if topic is not None:
            data = pybrainyquote.get_quotes(topic)
        else:
            data = pybrainyquote.get_random_quote()
        quotation = data[0]
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(description=quotation, color=value)
        embed.set_author(name='Your Quote', icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)


    @commands.command()
    async def horoscope(self, ctx, sign):
        sign = sign.lower()
        horoscope = pyaztro.Aztro(sign=sign)
        embed = discord.Embed(title='Your Daily Horoscope: ', description=horoscope.description,
                            color=discord.Colour.dark_magenta())
        embed.add_field(name='Mood', value=horoscope.mood, inline=False)
        embed.add_field(name='Lucky Time', value=horoscope.lucky_time, inline=False)
        embed.add_field(name='Colour', value=horoscope.color, inline=False)
        embed.add_field(name='Compatibility', value=horoscope.compatibility, inline=False)
        embed.add_field(name='Current Date', value=horoscope.current_date, inline=False)
        embed.add_field(name='Lucky Number', value=horoscope.lucky_number, inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
