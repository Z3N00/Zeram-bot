import discord
from discord.ext import commands
import random
import urbandict
import wikipedia
from googletrans import Translator

class tools(commands.Cog):
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
            await ctx.send("Sorry! I am unable to find answers to your query...:grimacing:")
        else:
            Data = data.split("\n")

        for d in Data:
            await ctx.send("```" + d + "```")
        await ctx.send("I hope you found this answer convincing. :smiley:")
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
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID", value=member.id)
        embed.add_field(name="Guild name", value=member.display_name)

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined at", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top role:", value=member.top_role.mention)

        embed.add_field(name="Bot?", value=member.bot)

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(tools(bot))
    print("tools is loaded")
