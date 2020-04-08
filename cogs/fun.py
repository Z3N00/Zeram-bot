import discord
from discord.ext import commands
import requests
import random
import json
import giphy_client
from giphy_client.rest import ApiException
from brainyquote import pybrainyquote
import pyaztro
from bs4 import BeautifulSoup

class fun(commands.Cog):
    """Some fun commands"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def flip(self, ctx):
        """Coin Flip"""
        Flip = random.choice(['Heads', 'Tails'])
        await ctx.send(Flip)


    @commands.command()
    async def reverse(self, ctx, *, message):
        """Reverse the message"""
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
        if times <= 10:
            for i in range(times):
                await ctx.send(content)

        else:
            await ctx.send("You want to kill me? Noob!")


    @commands.command(name='8ball')
    async def _8ball(self, ctx, *, question):
        """Ask your question from legendary 8ball"""
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
        """Get some gifs"""
        gifs = await self.search_gifs(search)
        await ctx.send(gifs)


    @commands.command()
    async def quote(self, ctx, topic=None):
        """Get random quote or of your choice"""
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
        """Get your daily Horoscope"""
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


    @commands.command()
    async def pickupline(self, ctx, member=None):
        """Get best Pickup Lines"""
        URL = "http://www.pickuplinegen.com/"
        r = requests.get(URL)

        soup = BeautifulSoup(r.content, 'html.parser')
        line = soup.findAll('div')
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(description=line[1].getText(), color=value)
        await ctx.send(embed=embed)


    @commands.command()
    async def wallpaper(self, ctx):
        """Get best Wallpapers """
        url = 'https://www.reddit.com/r/wallpapers.json?limit=100'
        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        value = random.randint(0, 0xffffff)
        data = response.json()['data']['children']
        i = random.randint(0, 100)
        current_post = data[i]['data']
        image_url = current_post['url']
        if '.png' in image_url:
            extension = '.png'
        elif '.jpg' in image_url or '.jpeg' in image_url:
            extension = '.jpeg'
        elif 'imgur' in image_url:
            image_url += '.jpeg'
            extension = '.jpeg'

        embed = discord.Embed(color=value)
        embed.set_image(url=image_url)

        await ctx.send(embed=embed)


    @commands.command()
    async def poem(self, ctx):
        """Get your daily Poems"""
        def tag_visible(element):
            if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                return False
            if isinstance(element, Comment):
                return False
            return True


        def text_from_html(body):
            soup = BeautifulSoup(body, 'html.parser')
            texts = soup.findAll('div',{"class": "elementor-shortcode"})
            # visible_texts = filter(tag_visible, texts)
            # return u" ".join(t.strip() for t in visible_texts)
            return texts
        html = text_from_html(requests.get('http://poems.com/todays-poem/').text)
        kavita = ''

        for elem in (html):

            if(elem.p):
                for text in elem.findAll("p"):
                    kavita = kavita + f'{text.text}'
        embed = discord.Embed(title='Your daily poem', description=f'```{kavita}```')
        await ctx.send(embed=embed)


    @commands.command(aliases=['gay'])
    async def howgay(self, ctx, member:discord.Member=None):
        """Gay Meter"""
        result = random.randint(1, 100)
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(color=value)
        if member is None:
            if ctx.author.id == 348349907746291722:
                mari = "You're 100% gay 😎🤙🏻"
                embed.add_field(name='Gay Meter 🏳️‍🌈', value=mari)
                await ctx.send(embed=embed)
            else:
                rest = f"You're {result}% gay"
                embed.add_field(name='Gay Meter 🏳️‍🌈', value=rest)
                await ctx.send(embed=embed)
        else:
            if member.id == 348349907746291722:
                mari = "You're 100% gay 😎🤙🏻"
                embed.add_field(name='Gay Meter 🏳️‍🌈', value=mari)
                await ctx.send(embed=embed)
            else:
                rest = f"{member.name} is {result}% gay"
                embed.add_field(name='Gay Meter 🏳️‍🌈', value=rest)
                await ctx.send(embed=embed)


    @commands.command()
    async def gender(self, ctx, name:str):
        """Determines the gender """

        url = f'https://api.genderize.io?name={name}'

        response = requests.get(url, headers = {'User-agent': 'Zeram'})
        var = json.loads(response.text)
        gender = var['gender']
        probability = int(var['probability']*100)
        msg = f"I am sure you're {probability}% {gender}"
        embed = discord.Embed(description=msg)

        await ctx.send(embed=embed)



    @commands.command()
    async def ship(self, ctx, name1, name2):
        """Check love Percentage"""

        def sumOfDigits(num):
            sum = 0
            while num > 0:
                sum += (num%10)
                num /= 10
            return sum

        name1 = name1.lower()
        name2 = name2.lower()
        sum1 = 0
        for i in range(len(name1)):
            sum1 += ord(name1[i])

        sum2 = 0
        for i in range(len(name2)):
            sum2 += ord(name2[i])

        perc =int((sumOfDigits(sum1) + sumOfDigits(sum2)) + 40);

        value = 0
        emoji = '🤍'
        str = '----------'
        s = list(str)
        if perc > 100:
            perc =  100
            value = 10
        else:
            value = int(perc/10)

        for i in range(value):
            s[i] = emoji
        bar = "".join(s)
        shipName = name1[:1]+name2[1:]
        desc = f" **💑 Love calculator**\n\n ``{name1}`` 💕 ``{name2}`` \t [{bar}] {perc}% \n\n They make ``{shipName}`` together"
        embed = discord.Embed(description=desc, color=0xFA8072)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
    print("fun is loaded")
