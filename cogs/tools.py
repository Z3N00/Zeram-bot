import discord
from discord.ext import commands
import random
import urbandict
import wikipedia
from googletrans import Translator

class Tools(commands.Cog):
    """Useful Commands"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        """Get user profile picture"""
        embed = discord.Embed(description='Your avatar :flushed: ')

        if member == None:
            embed.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)


    @commands.command()
    async def translate(self, ctx, *, message):
        """Translate any language"""
        icon = 'https://botlist.imgix.net/3605/c/discord_translator_avatar_v3-medium.jpg?auto=compress'
        value = random.randint(0, 0xffffff)
        translator = Translator()
        language = translator.detect(message)
        translation = translator.translate(message)
        ans = translation.text
        embed = discord.Embed(description='**' + ans + '**', color=value, title='Message: ' + message)
        embed.set_footer(text='Language detected: ' + language.lang, icon_url=icon)
        await ctx.send(embed=embed)


    @commands.command()
    async def define(self, ctx, *, term):
        """Define any word"""
        information = urbandict.define(term)
        data = information[0]
        embed = discord.Embed(description=data['def'] + "\n", color=discord.Colour.blue())
        embed.set_author(name='Definition of ' + term, icon_url=ctx.author.avatar_url)
        embed.add_field(name='Example', value='```' + data['example'] + '```', inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def invite(self, ctx):
        """Invite me in your server"""
        embed = discord.Embed(color=0xf41af4, description="[Invite Me! 😃 😱](https://discordapp.com/oauth2/authorize?client"
                                                      "_id=607611336268054563&scope=bot&permissions=2146958847)")

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
            await ctx.send("Sorry I am unable to find answers to your query... :grimacing:")
        else:
            Data = data.split("\n")

        for d in Data:
            await ctx.send("```" + d + "```")
        await ctx.send("I hope you found this answer convincing. :smiley:")


    @commands.command()
    async def hexcolor(self, ctx):
        """Get random Colour hex code"""
        value = random.randint(0, 0xffffff)
        embed = discord.Embed(title="Your Colour 🌈")
        img_url = f'https://dummyimage.com/500/{value}/&text=%20'
        embed.set_image(url=img_url)
        embed.set_footer(text=value)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Tools(bot))
    print("tools is loaded")
