import discord
from discord.ext import commands

class Moderation(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def clear(self, ctx, amount=10):
        isAdmin = ctx.author.permissions_in(ctx.channel).administrator
        if not isAdmin:
            await ctx.send('You do not have sufficient privileges to access this command.')
            return
        await ctx.channel.purge(limit=amount)
        await ctx.channel.send(f'{amount} messages deleted', delete_after=2.0)


    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)


    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')


    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return



def setup(bot):
    bot.add_cog(Moderation(bot))
