import discord
from discord.ext import commands
import asyncio
import datetime

class Help(commands.Cog):
    """Help Message"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx, command=None):
        """Gets all cogs and commands of mine."""
        author = ctx.message.author
        if command is None:

            embed = discord.Embed(description=' Use z.help {command}, For more info on a specific command', color=0x00FF00)
            embed.set_author(name='Command List', icon_url=ctx.author.avatar_url)

            basic = f'`ping`  `big`  `hello`'
            embed.add_field(name=f'😊 **Basic**', value=basic, inline=True)

            game = f'`guess`  `rps`'
            embed.add_field(name=f'🎲 **Games**', value=game, inline=False)

            autoreply = f'`bind`  `unbind`  `channel`'
            embed.add_field(name=f'🤖 **Chat Bot**', value=autoreply, inline=False)

            image = f'`meme`  `gif`  `emoji`  `comic`  `dog`  `cat`  `fox`  `panda`  `koala`  `redpanda`  `bird`  `bunny`  `lizard`'
            embed.add_field(name=f'📸 **Image**', value=image, inline=False)

            fun = f"`flip`  `reverse`  `roll`  `choose`  `repeat`  `8ball`  `giphy`  `ship`  `howgay`  `gender`  `quote`  `horoscope`  `numberfact`  `pickupline`  `wallpaper`  `poem`"
            embed.add_field(name=f'⚽ **Fun**', value=fun, inline=False)

            joke = f"`chucknorris`  `geekjoke`  `joke`  `roast`  `asktrump`  `insult`"
            embed.add_field(name=f'🎭 **Joke**', value=joke, inline=False)

            tools = f"`avatar`  `userinfo`  `serverinfo`  `translate`  `define`  `weather`  `search`  `poll`  `datetime`  `invite`  `vote`  `join`  `suggest`"
            embed.add_field(name=f'🔧 **Tools**', value=tools, inline=False)

            moderation = f"`clear`  `kick`  `ban`  `unban`  `mute`  `unmute`  `warn`"
            embed.add_field(name=f'🔨 **Moderation**', value=moderation, inline=False)

            actions = f"`cuddle`  `hug`  `kiss`  `lick`  `nom`  `pat`  `poke`  `slap`  `stare`  `highfive` `bite` `greet`  `punch`  `handholding`  `tickle`  `kill`  `hold`  `wave`  `boop`"
            embed.add_field(name=f'🤗 **Actions**', value=actions, inline=False)

            emotes = f"`blush`  `dance`  `lewd`  `pout`  `shrug`  `sleepy`  `smile`  `smug`  `thumbsup`  `wag` `thinking`  `triggered`  `teehee`  `deredere`  `scoff`  `happy`  `grin`"
            embed.add_field(name=f'😁 **Emotes**', value=emotes, inline=False)

            corona = f'`coronavirus`  `cvlb`  `cvh`'
            embed.add_field(name=f'😷 **Corona Stats**', value=corona, inline=False)

            nsfw = f'`pgif`  `boobs`  `ass`'
            embed.add_field(name=f'💦 **NSFW**', value=nsfw, inline=False)


            embed.set_footer(text="More commands coming soon!")

            await ctx.send(embed=embed)

        elif command is not None:
            await ctx.send_help(command)

    # @commands.command()
    # async def help (self, ctx, *cog):
    #     """Get all Bot commands"""
    #     if not cog:
    #
    #         embed = discord.Embed(description='Do '+'``'+'z.help <Command name>'+'``'+ ' for commands', color=0x437840)
    #
    #         cogs_desc = ''
    #         for x in self.bot.cogs:
    #             cogs_desc += ('**{}** - {}'.format(x, self.bot.cogs[x].__doc__)+'\n')
    #         embed.add_field(name='Commands Menu', value=cogs_desc[0:len(cogs_desc)-1], inline=False)
    #         await ctx.message.add_reaction(emoji='✅')
    #         await ctx.send(embed=embed)
    #     else:
    #         if len(cog) > 1:
    #             embed = discord.Embed(title='Error!', description='Too many cogs!', color=0x437840)
    #             await ctx.message.author.send('', embed=embed)
    #         else:
    #             found = False
    #             for x in self.bot.cogs:
    #                 for y in cog:
    #                     if x == y:
    #                         embed = discord.Embed(color=0x437840)
    #                         scog_info = ''
    #                         for c in self.bot.get_cog(y).get_commands():
    #                             if not c.hidden:
    #                                 scog_info += f'**{c.name}** - {c.help}\n'
    #                         embed.add_field(name=f'{cog[0]} - {self.bot.cogs[cog[0]].__doc__}', value=scog_info)
    #                         embed.set_footer(text='<z.help command> for syntax')
    #                         found = True
    #         if not found:
    #             for x in self.bot.cogs:
    #                 for c in self.bot.get_cog(x).get_commands():
    #
    #                     if c.name == cog[0]:
    #                         embed = discord.Embed(color=0x437840)
    #                         embed.add_field(name=f'{c.name} - {c.help}', value=f'Proper Syntax:\n`{c.qualified_name} {c.signature}`')
    #                         embed.set_footer(text='<z.command name>')
    #                 found = True
    #
    #             if not found:
    #                 embed = discord.Embed(title='Error!', description='How do you even use "'+cog[0]+'"?', color=0x437840)
    #         else:
    #             await ctx.message.add_reaction(emoji='✅')
    #         await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
    print("help is loaded")
