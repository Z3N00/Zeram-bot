import discord
from discord.ext import commands
import sys, traceback
import sqlite3
token = 'MJ-Wjxz7u4NRQRJcQsTVG9Ff5hA.g8FAVX.zYTN0UDM4YjM2MzMxEjN3AjN'
initial_extensions = ['cogs.basic',
                      'cogs.actions',
                      'cogs.emotes',
                      'cogs.fun',
                      'cogs.jokes',
                      'cogs.tools',
                      'cogs.game',
                      'cogs.moderation',
                      'cogs.nsfw',
                      'cogs.help',
                      'cogs.reply',
                      'cogs.autoreply',
                      'cogs.corona',
                      'cogs.image']
bot = commands.Bot(command_prefix=commands.when_mentioned_or('z.', 'Z.'), description='Basic commands for Zeram')
bot.remove_command('help')
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()
@bot.event
async def on_ready():
    # db = sqlite3.connect('main.sqlite')
    # cursor = db.cursor()
    # cursor.execute('''
    #    CREATE TABLE IF NOT EXISTS main(
    #    guild_id TEXT,
    #    channel_id TEXT
    #    )
    #    ''')
    guild = len(bot.guilds)
    activity = discord.Activity(name='z.help | ' + str(guild) + ' servers', type=discord.ActivityType.listening)
    await bot.change_presence(activity=activity)

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')





bot_token = token[::-1]
bot.run(bot_token, bot=True, reconnect=True)
