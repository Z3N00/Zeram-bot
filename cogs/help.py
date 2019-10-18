import discord
from discord.ext import commands
import asyncio
import datetime

class Help(commands.Cog):
    """Help Message"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help (self, ctx, *cog):
        """Get all Bot commands"""
        if not cog:

            embed = discord.Embed(description='Do '+'``'+'z.help <Command name>'+'``'+ ' for commands', color=0x437840)

            cogs_desc = ''
            for x in self.bot.cogs:
                cogs_desc += ('**{}** - {}'.format(x, self.bot.cogs[x].__doc__)+'\n')
            embed.add_field(name='Commands Menu', value=cogs_desc[0:len(cogs_desc)-1], inline=False)
            await ctx.message.add_reaction(emoji='✅')
            await ctx.send(embed=embed)
        else:
            if len(cog) > 1:
                embed = discord.Embed(title='Error!', description='Too many cogs!', color=0x437840)
                await ctx.message.author.send('', embed=embed)
            else:
                found = False
                for x in self.bot.cogs:
                    for y in cog:
                        if x == y:
                            embed = discord.Embed(color=0x437840)
                            scog_info = ''
                            for c in self.bot.get_cog(y).get_commands():
                                if not c.hidden:
                                    scog_info += f'**{c.name}** - {c.help}\n'
                            embed.add_field(name=f'{cog[0]} Module - {self.bot.cogs[cog[0]].__doc__}', value=scog_info)
                            embed.set_footer(text='<z.help command> for syntax')
                            found = True
            if not found:
                for x in self.bot.cogs:
                    for c in self.bot.get_cog(x).get_commands():

                        if c.name == cog[0]:
                            embed = discord.Embed(color=0x437840)
                            embed.add_field(name=f'{c.name} - {c.help}', value=f'Proper Syntax:\n`{c.qualified_name} {c.signature}`')
                            embed.set_footer(text='<z.command name>')
                    found = True

                if not found:
                    embed = discord.Embed(title='Error!', description='How do you even use "'+cog[0]+'"?', color=0x437840)
            else:
                await ctx.message.add_reaction(emoji='✅')
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
    print("help is loaded")
