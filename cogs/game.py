import discord
from discord.ext import commands
import random
import asyncio

class Game(commands.Cog):
    """Game Commands"""

    def __init__(self, bot):
        self.bot = bot

    def check(self, author):
        def inner_check(message):
            if message.author != author:
                return False
            try:
                int(message.content)
                return True
            except ValueError:
                return False
        return inner_check

    @commands.command()
    async def guess(self, ctx):
        """Number guessing game"""
        WINNING_NUMBER = random.randint(1, 100)
        print(WINNING_NUMBER)
        turn = 4
        while turn != -1:
            try:
                await ctx.send("Pick a number between 1 and 100")
                msg = await self.bot.wait_for('message', check=self.check(ctx.author), timeout=30)
                guess = int(msg.content)

                if turn == 0:
                    if guess == WINNING_NUMBER:
                        await ctx.send(f"You guessed it! Good job!")
                        return
                    else:
                        await ctx.send(f"You Lose! Answer is {WINNING_NUMBER}")
                        return

                if guess == WINNING_NUMBER:
                    await ctx.send(f"You guessed it! Good job!")
                    return

                elif guess < WINNING_NUMBER:
                    await ctx.send(str(turn)+ ' guesses left...')
                    await asyncio.sleep(1)
                    await ctx.send("Try going higher")
                    await asyncio.sleep(1)
                    turn = turn - 1


                elif guess > WINNING_NUMBER:
                    await ctx.send(str(turn) + ' guesses left...')
                    await asyncio.sleep(1)
                    await ctx.send('Try going lower')
                    await asyncio.sleep(1)
                    turn = turn - 1

            except asyncio.TimeoutError:
                await ctx.send(f"Times up! Answer is {WINNING_NUMBER}")
                return

def setup(bot):
    bot.add_cog(Game(bot))
    print("Game is loaded")
