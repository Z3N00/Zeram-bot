import discord
from discord.ext import commands
import random
import urbandict
import wikipedia
from googletrans import Translator
import requests
import pytz
import datetime
import urbandictionary_python

class tools(commands.Cog):
    """Useful Commands"""
    def __init__(self, bot):
        self.bot = bot



    @commands.command(aliases=['av', 'pfp'])
    async def avatar(self, ctx, member: discord.User = None):
        """Get user profile picture"""
        embed = discord.Embed(description='Your avatar 😳 ')

        if member == None:
            embed.set_image(url=ctx.author.avatar.url)
            await ctx.send(embed=embed)
        else:
            embed.set_image(url=member.avatar.url)
            await ctx.send(embed=embed)



    @commands.command(aliases=['t'])
    async def translate(self, ctx, *, message):
        """Translate any language"""
        icon = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.U8k9cD9ed7f4JOONNJ3uXQAAAA%26pid%3DApi&f=1'
        value = random.randint(0, 0xffffff)
        translator = Translator()
        language = translator.detect(message)
        await ctx.send(language)
        translation = translator.translate(message)
        await ctx.send(translation)
        ans = translation.text
        embed = discord.Embed(description='**' + ans + '**', color=value, title='Message: ' + message)
        embed.set_footer(text='Language detected: ' + language.lang, icon_url=icon)
        await ctx.send(embed=embed)


    @commands.command()
    async def define(self, ctx, *, term):
        """Define any word"""
        information = urbandictionary_python.UrbanDictionary(term)
        # print(information)
        # await ctx.send(information)
        data = information.meaning()
        embed = discord.Embed(description=data + "\n", color=discord.Colour.blue())
        embed.set_author(name='Definition of ' + term, icon_url=ctx.author.avatar.url)
        embed.add_field(name='Example', value='```' + information.example() + '```', inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def invite(self, ctx):
        #https://discordapp.com/oauth2/authorize?client_id=607611336268054563&scope=bot&permissions=8206
        """Invite me in your server"""
        embed = discord.Embed(color=0xf41af4, description="[Invite Me! 😃 😱](https://discordapp.com/oauth2/authorize?client"
                                                      "_id=607611336268054563&scope=bot&permissions=8206)")

        embed.set_footer(text="Discord bot invite link.")
        await ctx.send(embed=embed)


    @commands.command()
    async def vote(self, ctx):
        """Vote for the bot"""
        vote_link = 'https://top.gg/bot/607611336268054563/vote'
        embed = discord.Embed(description=f"[Vote Me 😊]({vote_link})", color=0xf41af4)
        embed.set_footer(text="Daily vote 🙏")
        await ctx.send(embed=embed)


    @commands.command()
    async def search(self, ctx, *, query):
        """Search from wikipedia"""
        flag = False

        await ctx.channel.send("Searching your query...", delete_after=1.0)
        try:
            data = wikipedia.summary(query)
        except:
            flag = True
            # print(data)
        if flag:
            await ctx.send("Sorry! I am unable to find answers to your query...:grimacing:")
        else:
            Data = data.split("\n")

       # for d in Data:
        await ctx.send("```" + data + "```")
        await ctx.send(f"I hope you found this answer convincing. For more information go to {data.url} :smiley:")
    @search.error
    async def search_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("")


    @commands.command()
    async def poll(self, ctx, question, *choices: str):
        """Take a Poll (example "question" "choice1" "choice2" ...)"""
        emoji = ['1\N{combining enclosing keycap}', '2\N{combining enclosing keycap}',
               '3\N{combining enclosing keycap}', '4\N{combining enclosing keycap}',
               '5\N{combining enclosing keycap}', '6\N{combining enclosing keycap}',
               '7\N{combining enclosing keycap}', '8\N{combining enclosing keycap}',
               '9\N{combining enclosing keycap}', '10\N{combining enclosing keycap}']
        emoji_len = len(emoji)
        choice_len = len(choices)
        msg = ""
        value = random.randint(0, 0xffffff)
        for i in range(choice_len):
            msg = msg + f"{emoji[i]} {choices[i]}"+'\n'
        embed = discord.Embed(title=f"📊 {question}", description=msg, color=value)
        msg = await ctx.send(embed=embed)
        for i in range(choice_len):
            await msg.add_reaction(emoji=emoji[i])


    @commands.command()
    async def hexcolor(self, ctx):
        """Get random Colour hex code"""
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(title="Your Colour 🌈")
        img_url = f'https://dummyimage.com/500/{value}/&text=%20'
        embed.set_image(url=img_url)
        embed.set_footer(text=value)
        await ctx.send(embed=embed)


    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        """Get the User information"""
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)

        embed.set_author(name=f'User Info - {member}')
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)

        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Guild name", value=member.display_name)

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined at", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top role:", value=member.top_role.mention)

        embed.add_field(name="Bot?", value=member.bot)

        await ctx.send(embed=embed)


    @commands.command(aliases=['si', 'server'])
    async def serverinfo(self, ctx):
        '''Get server info'''
        guild = ctx.guild
        guild_age = (ctx.message.created_at - guild.created_at).days
        created_at = f"Server created on {guild.created_at.strftime('%b %d %Y at %H:%M')}. That\'s over {guild_age} days ago!"
        color = discord.Color.green()
       
        # count = 0
        # for member in ctx.guild.members:  # .members was added
        #   if member.status != discord.Status.offline:
        #     count =+ 1
        # print(f"count: {count}" )
        em = discord.Embed(description=created_at, color=color)
        em.add_field(name='Online Members', value=len([m.id for m in guild.members if m.status is not discord.Status.offline]))
        em.add_field(name='Total Members', value=guild.member_count)
        em.add_field(name='Text Channels', value=len(guild.text_channels))
        em.add_field(name='Voice Channels', value=len(guild.voice_channels))
        em.add_field(name='Roles', value=len(guild.roles))
        em.add_field(name='Owner', value=f"<@{guild.owner_id}>")

        em.set_thumbnail(url=None or guild.icon.url)
        em.set_author(name=guild.name, icon_url=None or guild.icon.url)
        await ctx.send(embed=em)



    @commands.command(aliases=['w'])
    async def weather(self, ctx, city_name):
        """Check Weather condition """
        api_key = "d7f2ea77494b015b990af5a12e4a1d85"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        response = requests.get(complete_url)

        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature = current_temperature - 273.15
            current_temperature = float("{:.2f}".format(current_temperature))

            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            value = random.randint(0, 0xffffff)
            embed = discord.Embed(color=value, title=f'⛈️| Weather Report: {city_name.upper()}')
            embed.add_field(name='Temperature', value=f"{current_temperature}°C", inline=False)
            embed.add_field(name='Pressure', value=f"{current_pressure} hpa", inline=True)
            embed.add_field(name='Humidity', value=f"{current_humidiy}%", inline=True)
            embed.add_field(name='Condition', value=f"{weather_description}", inline=True)

            await ctx.send(embed=embed)

        else:
            await ctx.send("City not found")


    @commands.command()
    async def join(self, ctx):
        """Join zeram support server for more help and more info"""
        await ctx.send("https://discord.gg/Ey5wqJy")


    @commands.command(aliases=['dt'])
    async def datetime(self, ctx, tz=None):
        """Get the current date and time for a time zone or UTC."""
        now = datetime.datetime.now(tz=pytz.UTC)
        all_tz = 'https://github.com/cree-py/RemixBot/blob/master/data/timezones.json'
        em = discord.Embed(color=discord.Color.red())
        if tz:
            try:
                now = now.astimezone(pytz.timezone(tz))
            except:
                em.title = "Invalid timezone"
                em.description = f'Please take a look at the [list]({all_tz}) of timezones.'
                return await ctx.send(embed=em)
        em.description = f'It is currently {now:%A, %B %d, %Y} at {now:%I:%M:%S %p}.'
        await ctx.send(embed=em)

    @commands.command()
    async def suggest(self, ctx, *, idea: str):
        """Suggest an idea. Your idea will be sent to the developer server."""
        suggest = self.bot.get_channel(700271848050655252)
        em = discord.Embed(color=discord.Color.green())
        em.title = f"{ctx.author} | User ID: {ctx.author.id}"
        em.description = idea
        em.set_footer(text=f"From {ctx.author.guild} | Server ID: {ctx.author.guild.id}", icon_url=ctx.guild.icon_url)
        await suggest.send(embed=em)
        await ctx.send("Your idea has been successfully sent to support server. Thank you!")





    @commands.command(name='me', aliases=['owner'])
    @commands.is_owner()
    async def only_me(self, ctx):
        """A simple command which only responds to the owner of the bot."""

        await ctx.send(f"Hello {ctx.author.mention}, You're my owner!!")



def setup(bot):
    bot.add_cog(tools(bot))
    print("tools is loaded")
