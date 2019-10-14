import discord
from discord.ext import commands
import sys, traceback

token = 'MJ-Wjxz7u4NRQRJcQsTVG9Ff5hA.g8FAVX.zYTN0UDM4YjM2MzMxEjN3AjN'
initial_extensions = ['cogs.fun',
                      'cogs.basic',
                      'cogs.reply',
                      'cogs.jokes',
                      'cogs.utility',
                      'cogs.moderation']
bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'))
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()
@bot.event
async def on_ready():
    guild = len(bot.guilds)
    activity = discord.Activity(name='z.help | ' + str(guild) + ' servers', type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')

bot_token = token[::-1]
bot.run(bot_token, bot=True, reconnect=True)
