import discord
from discord.ext import commands

class Moderation(commands.Cog):
    """Administrator Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        """Erase the chat history"""

        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(f'{amount} message deleted', delete_after=2.0)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send(f'{ctx.author.mention} You have no permission for this command', delete_after=5.0)



    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick the user"""
        await member.kick(reason=reason)
        await ctx.channel.send(f'{member.name}#{member.discriminator} has been kicked from the server!', delete_after=5.0)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send(f'{ctx.author.mention} You have no permission for this command', delete_after=5.0)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban the user"""
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')
        await ctx.channel.send(f'{member.name}#{member.discriminator} is banned from the server!', delete_after=5.0)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send(f'{ctx.author.mention} You have no permission for this command', delete_after=5.0)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """Unban the user"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send(f'{ctx.author.mention} You have no permission for this command', delete_after=5.0)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member:discord.Member=None):
        """Mute the user"""
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not role:

            muted = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted, send_messages=False,
                                            read_message_history=True,
                                            read_messages=True)

            await member.add_roles(muted)

        else:
            await member.add_roles(role)
            await ctx.send(f'{member.mention} has been muted', delete_after=5.0)


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member:discord.Member=None):
        """Unmute the user"""
        await member.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted"))
        await ctx.send(f'{member.mention} has been unmuted', delete_after=5.0)

    @mute.error
    @unmute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send(f'{ctx.author.mention} You have no permission')


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, user: discord.Member, *, reason: str):
        '''Warn a member via DMs'''
        warning = f'You have been warned in **{ctx.guild}** by **{ctx.author}** for {reason}'
        if not reason:
            warning = f'You have been warned in **{ctx.guild}** by **{ctx.author}**'
        try:
            await user.send(warning)
        except discord.Forbidden:
            return await ctx.send('The user has disabled DMs for this guild or blocked the bot.')
        await ctx.send(f'**{user}** has been **warned**')

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.channel.send(f'{ctx.author.mention} You have no permission for this command')






def setup(bot):
    bot.add_cog(Moderation(bot))
    print("moderation is loaded")
