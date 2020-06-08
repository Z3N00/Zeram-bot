import discord
from discord.ext import commands
import random
import asyncio, aiohttp, os, re
import mysql.connector
from mysql.connector import Error

class Autoreply(commands.Cog):
    """Autoreply Commands"""

    def __init__(self, bot):
        self.bot = bot




    def mydb(self):

        mydb = mysql.connector.connect(
            host="sql12.freesqldatabase.com",
            user="sql12346462",
            password="M88h5rI97r",
            database='sql12346462'
            )
        return mydb

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def bind(self, ctx, channel: discord.TextChannel):
        """Bind the channel for auto reply"""
        guild_id = str(ctx.guild.id)
        channel_id = str(channel.id)

        try:
            db = self.mydb()
            mycursor = db.cursor()
            mycursor.execute("SELECT channel_id from channel WHERE guild_id ='" + guild_id + "'")
            result = mycursor.fetchall()
            #print(len(result))
            if len(result) == 0:
                mycursor.execute("INSERT INTO channel(guild_id, channel_id) VALUES(%s, %s)", (guild_id, channel_id))
                db.commit()
                await ctx.send(f"Chat bot is bind to <#{str(channel.id)}>")
            else:
                mycursor.execute("UPDATE channel SET channel_id=%s WHERE guild_id=%s ", (channel_id, guild_id))
                db.commit()
                await ctx.send(f"Chat bot is bind to <#{str(channel.id)}>")

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if (db.is_connected()):
                mycursor.close()
                db.close()
                #print("MySQL connection is closed")



    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unbind(self, ctx, channel: discord.TextChannel):
        """Unbind the channel from auto reply"""
        guild_id = str(ctx.guild.id)
        channel_id = str(channel.id)
        try:
            db = self.mydb()
            mycursor = db.cursor()
            mycursor.execute(f"SELECT channel_id FROM channel WHERE guild_id = {guild_id}")
            result = mycursor.fetchall()
            if len(result) == 0:
                await ctx.send("No channel is binded in this server")

            if result[0][0] != channel_id:
                await ctx.send("This channel is not binded")
            else:
                sql_delete_query = f"DELETE FROM channel WHERE guild_id = {guild_id}"
                mycursor.execute(sql_delete_query)
                db.commit()
                await ctx.send(f"Unbinded Successfully from {channel}")

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if (db.is_connected()):
                mycursor.close()
                db.close()
                #print("MySQL connection is closed")


    @unbind.error
    @bind.error
    async def error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send(f'{ctx.author.mention} You need manage server permission to access this command')

    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        # obj  = json.load(open("channel.json"))
        db = self.mydb()
        mycursor = db.cursor()
        mycursor.execute(f"SELECT channel_id FROM channel WHERE guild_id = {str(message.guild.id)}")
        result = mycursor.fetchall()
        # await message.channel.send(result[0])

        if len(result) != 0 and (str(channel.id) == result[0][0]):
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
                                    text = text.replace('&quot;', '"').replace('&lt;', '<').replace('&gt;',
                                                                                                    '>').replace(
                                        '&amp;', '&').replace('<br>', ' ')
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




    @commands.command()
    async def channel(self, ctx):
        """To check which channel is binded"""
        channel = ctx.channel
        db = self.mydb()
        mycursor = db.cursor()
        mycursor.execute(f"SELECT channel_id FROM channel WHERE guild_id = {str(channel.guild.id)}")
        result = mycursor.fetchall()
        if len(result) == 0:
            await ctx.send("No channel is binded with the chat bot! Do z.bind #channel_name for binding")
        else:
            await ctx.send(f'<#{result[0][0]}> is binded with zeram autoreply')


def setup(bot):
    bot.add_cog(Autoreply(bot))
    print("Autoreply is loaded")
