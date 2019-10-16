import discord
from discord.ext import commands

class Moderation(commands.Cog):
    """Administrator Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        """Clear the chat history"""
        flag =False
        try:
            await ctx.channel.purge(limit=amount)
            await ctx.channel.send(f'{amount} message deleted', delete_after=2.0)
        except:
            flag = True

        if flag:
            await ctx.channel.send("You do not have sufficient privileges to access this command.", delete_after=3.0)


    @commands.command()
    @commands.has_permissions(kik_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick the user"""
        await member.kick(reason=reason)


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban the user"""
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')


    @commands.command()
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



def setup(bot):
    bot.add_cog(Moderation(bot))
    print("moderation is loaded")
