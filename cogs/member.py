import discord
from discord.ext import commands

class Member(commands.Cog):
    """TestCog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        embed = discord.Embed(description='Your avatar :flushed: ')

        if member == None:
            embed.set_image(url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    async def translate(self, ctx, *, message):
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
        information = urbandict.define(term)
        data = information[0]
        embed = discord.Embed(description=data['def'] + "\n", color=discord.Colour.blue())
        embed.set_author(name='Definition of ' + term, icon_url=ctx.author.avatar_url)
        embed.add_field(name='Example', value='```' + data['example'] + '```', inline=False)
        await ctx.send(embed=embed)


    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(color=0xf41af4, description="[Invite Me! 😃 😱](https://discordapp.com/oauth2/authorize?client"
                                                      "_id=607611336268054563&scope=bot&permissions=2146958847)")

        embed.set_footer(text="Discord bot invite link.")
        await ctx.send(embed=embed)


    @commands.command()
    async def search(self, ctx, *, query):
        flag = False

        await ctx.send("Searching your query...")
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




def setup(bot):
    bot.add_cog(Member(bot))
