import discord
from discord.ext import commands
import aiohttp
import asyncio
import corona_api


class Corona(commands.Cog):
    """Corons Stats"""

    def __init__(self, bot):
        self.bot = bot
        self.corona = corona_api.Client()


    # @commands.command()
    # async def hi(self, ctx):
    #     await ctx.send("hello")

    @commands.command(aliases=["cv", "corona"])
    async def coronavirus(self, ctx, country=None, *, state=None):

        """
        Get the statistics for Coronavirus (COVID-19) for a specified country.
        Params:
            ctx:
                The context for the command
            country:
                The country to get the stats for. If None, get global stats
            state:
                The US state to get the stats for.
        """

        if not country:
            data = await self.corona.all()

        elif country.lower() == "czech":
            country = "czech republic"

        elif (country.lower() == "us" or country.lower() == "usa"):
            if state:
                data = await self.corona.get_state_info(state)

            else:
                data = await self.corona.get_country_data(country)

        else:
            data = await self.corona.get_country_data(country)

        embed = discord.Embed(title="Coronavirus (COVID-19) stats", color=65280)
        embed.set_footer(text="These stats are what has been officially confirmed. It is possible that real figures are different.")

        embed.add_field(name="Total cases", value = corona_api.format_number(data.cases))
        embed.add_field(name="Cases today", value = corona_api.format_number(data.today_cases))
        embed.add_field(name="Total deaths", value = corona_api.format_number(data.deaths))
        embed.add_field(name="Deaths today", value = corona_api.format_number(data.today_deaths))
        embed.add_field(name="Total recoveries", value = corona_api.format_number(data.recoveries))

        if not isinstance(data, corona_api.StateStatistics):
            embed.add_field(name="Total critical cases", value = corona_api.format_number(data.critical))

        if isinstance(data, corona_api.GlobalStatistics):
            embed.add_field(name="Last updated", value = corona_api.format_date(data.updated))

        elif isinstance(data, corona_api.CountryStatistics):
            embed.add_field(name="Cases per million people", value = corona_api.format_number(data.cases_per_million))
            embed.description = "**Country: {}**".format(data.name)
            embed.set_thumbnail(url=data.flag)

        else:
            embed.add_field(name="Active cases", value=corona_api.format_number(data.active))
            embed.description = "**State: {}**".format(data.name)

        await ctx.send(embed=embed)


    @commands.command(aliases=["cvlb", "coronatop", "cvtop"])
    async def coronavirusleaderboard(self, ctx):
        """Get the Leaderboard Results"""
        data = await self.corona.get_sorted_data("cases")

        embed = discord.Embed(title="Top 15 cases", description="", color=65280)
        embed.set_footer(text='These stats are what has been officially confirmed. It is possible that real figures are different.')

        for i in range(1,16): #top 15
            country = data[i-1]
            name = country.name
            #sometimes the stats are null/None.
            if country.cases is None:
                cases = 'Unknown'
            else:
                cases = corona_api.format_number(country.cases)
            if country.deaths is None:
                deaths = 'Unknown'
            else:
                deaths = corona_api.format_number(country.deaths)

            embed.description = '{}**{}. {}:** {} cases, {} deaths.\n'.format(
                embed.description, i, name, cases, deaths
            )

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Corona(bot))
    print("Corona is loaded")