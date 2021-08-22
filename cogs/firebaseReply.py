from discord.ext.commands.core import Command
import pyrebase
import discord
from discord.ext import commands
import random
import asyncio, aiohttp, os, re
import json

config = {
    "apiKey": "AIzaSyC1sFYKj4YArVA2H05O7d8b0qaTNkMNngg",
    "authDomain": "zeram-discord-bot.firebaseapp.com",
    "databaseURL": "https://zeram-discord-bot-default-rtdb.firebaseio.com",
    "projectId": "zeram-discord-bot",
    "storageBucket": "zeram-discord-bot.appspot.com",
    "messagingSenderId": "182331448519",
    "appId": "1:182331448519:web:68849d49452506580f32e2",
    "measurementId": "G-B8WPW2420M"
  }
firebase = pyrebase.initialize_app(config)
db = firebase.database()

class firebaseReply(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

   

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def bind(self, ctx, channel: discord.TextChannel):
        guild_id = str(ctx.guild.id)
        channel_id = str(channel.id)

        data = {
            guild_id : channel_id
        }
        
        db.child("Servers").child(f"{guild_id}").set(data)
        await ctx.send(f"Chat bot is bind to <#{channel_id}>")


    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unbind(self, ctx, channel: discord.TextChannel):
        guild_id = str(ctx.guild.id)
        channel_id = str(channel.id)
        servers = db.child("Servers").get()

        obj = servers.val()

        if(guild_id in obj.keys()):
            if channel_id == obj[guild_id][guild_id]:
                db.child("Servers").child(guild_id).remove()
                await ctx.send(f"Unbinded Successfully from {channel}")
            else:
                await ctx.send("This channel is not binded")
        else:
            await ctx.send("No channel is binded in this server")

    @unbind.error
    @bind.error
    async def error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send(f'{ctx.author.mention} You need manage channel permission to access this command')


    @commands.Cog.listener()
    async def on_message(self, message):
        channel = message.channel
        guild_id = str(message.guild.id)
        channel_id = str(channel.id)
        servers = db.child("Servers").get()

        obj = servers.val()

        if ((guild_id in obj[guild_id]) and (channel_id == obj[guild_id][guild_id])):
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
    
    @commands.command()
    async def channel(self, ctx):
        channel = ctx.channel

        servers = db.child("Servers").get()
        name = servers.val()

        if str(channel.guild.id) in name[str(channel.guild.id)].keys():
            await ctx.send(f'<#{name[str(channel.guild.id)][str(channel.guild.id)]}> is binded with zeram autoreply')
        else:
            await ctx.send("No channel is binded! Do z.bind #channel_name for binding")


def setup(bot):
    bot.add_cog(firebaseReply(bot))
    print("firebaseReply is loaded")
