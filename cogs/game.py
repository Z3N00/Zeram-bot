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


    def check1(self, author):
        def inner_check(message):
            if message.author != author:
                return False
            try:
                str(message.content)
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


    @commands.command()
    async def rps(self, ctx):
        """Rock Paper Scissor"""
        turn = 2
        compScore = 0
        userScore = 0
        author = ctx.author.mention
        value = random.randint(0, 0xffffff)
        while turn != -1:

            rps = ['rock', 'paper', 'scissor']
            computer = random.choice(rps)
            print("computer choice:", computer)

            embed = discord.Embed(color=value, description='Choose: 🌑 rock, 📄 paper, ✂️ scissor')

            await ctx.send(embed=embed)
            try:
                msg = await self.bot.wait_for('message', check=self.check1(ctx.author), timeout=30)

            except asyncio.TimeoutError:
                value = random.randint(0, 0xffffff)
                desc = 'I do not have a whole day to play with you! Loser 😠'
                embed = discord.Embed(color=value, description=desc)
                await ctx.send(embed=embed)
                return

            ans = str(msg.content).lower()

            print("Our choice: ", ans)
            print("----------------------")

            if ans == computer:
                await ctx.send(f"I choose {ans}! Its a tie! Noone gets a point")
                turn = turn - 1


            elif ans=='rock' and computer=='scissor':
                userScore += 1
                await ctx.send(f"I choose {computer}! {author} won 1 point")
                turn = turn - 1


            elif ans=='scissor' and computer=='paper':
                userScore += 1
                await ctx.send(f"I choose {computer}! {author} won 1 point")
                turn = turn - 1


            elif ans=='paper' and computer=='rock':
                userScore += 1
                await ctx.send(f"I choose {computer}! {author} won 1 point")
                turn = turn - 1


            else:
                compScore += 1
                await ctx.send(f"I choose {computer}! {author} lose, I won 1 point")
                turn = turn - 1
        result = f"Finale Score: {ctx.author.name} : {userScore} | Zeram : {compScore}"
        embed = discord.Embed(color=value, description=result, title='Match Results 😎')
        await asyncio.sleep(1)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Game(bot))
    print("Game is loaded")
