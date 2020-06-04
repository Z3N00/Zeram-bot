import discord
from discord.ext import commands
import random
import asyncio, aiohttp, os, re
import json
import sqlite3

class Autoreply(commands.Cog):
    """Autoreply Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unbind(self, ctx, channel: discord.TextChannel):
        """Unbind the channel from auto reply"""
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {str(ctx.guild.id)}")
        result = cursor.fetchone()
        if result is None:
            await ctx.send("No channel is binded in this server")

        if result[0] != str(channel.id):
            await ctx.send("This channel is not binded")
        else:
            sql_delete_query = f"DELETE FROM main WHERE guild_id = {str(ctx.guild.id)}"
            cursor.execute(sql_delete_query)
            await ctx.send(f"Unbinded Successfully from {channel}")

        db.commit()
        cursor.close()
        db.close()


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def bind(self, ctx, channel:discord.TextChannel):
        """Bind the channel for auto reply"""
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {str(ctx.guild.id)}")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO main(guild_id, channel_id) VALUES(?,?)")
            val = (ctx.guild.id, channel.id)
            await ctx.send(f"Chat bot is bind to <#{str(channel.id)}>")
        elif result is not None:
            sql = ("UPDATE main SET channel_id = ? WHERE guild_id = ?")
            val = (channel.id, ctx.guild.id)
            await ctx.send(f"Chat bot is bind to <#{str(channel.id)}>")
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()


    @unbind.error
    @bind.error
    async def error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send(f'{ctx.author.mention} You need manage channel permission to access this command')


    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        # obj  = json.load(open("channel.json"))
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {str(message.guild.id)}")
        result = cursor.fetchone()
        # await message.channel.send(result[0])

        if result is not None and (str(channel.id) == result[0]):
            if not message.author.bot and self.bot.user.id:
                async with channel.typing():
                    try:
                        input = re.sub(f'<@{str(message.author.id)}>', '', message.content).strip()
                        params = {'botid': 'c867aeea4e345ad2', 'custid': message.author.id, 'input': input or 'Hello'}
                        async with aiohttp.ClientSession(headers={'User-agent': 'Zeram'}) as bot:
                            async with bot.get('https://www.pandorabots.com/pandora/talk-xml', params=params) as resp:
                                if resp.status == 200:
                                    text = await resp.text()
                                    text = text[text.find('<that>') + 6:text.rfind('</that>')]
                                    text = text.replace('&quot;', '"').replace('&lt;', '<').replace('&gt;','>').replace('&amp;', '&').replace('<br>', ' ')
                                    await message.channel.send(text)
                                else:
                                    await message.channel.send('Uh oh, I didn\'t quite catch that!')
                    except asyncio.TimeoutError:
                        await message.channel.send('Uh oh, I think my head is on backwards!')
            else:
                return
        else:
            return

        db.commit()
        cursor.close()
        db.close()

    @commands.command()
    async def channel(self, ctx):
        """To check which channel is binded"""
        channel = ctx.channel
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT channel_id FROM main WHERE guild_id = {str(channel.guild.id)}")
        result = cursor.fetchone()
        if result is None:
            await ctx.send("No channel is binded with the chat bot! Do z.bind #channel_name for binding")
        else:
            await ctx.send(f'<#{result[0]}> is binded with zeram autoreply')
        db.commit()
        cursor.close()
        db.close()

def setup(bot):
    bot.add_cog(Autoreply(bot))
    print("Autoreply is loaded")
