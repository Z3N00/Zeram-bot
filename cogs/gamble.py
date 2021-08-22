import asyncio
from random import randrange
import discord
from discord.ext import commands
from pyasn1.type.univ import Null
import pyrebase
import random

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

# config = {
#     "apiKey": "AIzaSyBFl-UXYUYK-HoQgDCaNAGNknZmmP5o-Gs",
#     "authDomain": "test-eba3f.firebaseapp.com",
#     "projectId": "test-eba3f",
#     "storageBucket": "test-eba3f.appspot.com",
#     "messagingSenderId": "637418244602",
#     "appId": "1:637418244602:web:72b781fb4eff2eb1ddfc43",
#     "measurementId": "G-4F834M34NX",
#     "databaseURL" : "https://test-eba3f-default-rtdb.firebaseio.com/"
# }

firebase = pyrebase.initialize_app(config)
db = firebase.database()


class GambleCog(commands.Cog):
    """GambleCog"""

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(aliases=['enter'])
    async def entergamble(self, ctx):

        user_id = str(ctx.author.id)
        user = db.child("Users").get()
        userMoney = user.val()

        data = {
            "UserId" : user_id,
            "Name" : str(ctx.author),
            "Money" : "0"
        }

        if(user_id not in userMoney.keys()):
            db.child("Users").child(f"{user_id}").set(data)
            await ctx.send(f"Welcome to our gambling club {ctx.author.mention}")
        else:
            await ctx.send("You're already in our gambling group")

    @commands.command(aliases=['bal', 'money'])
    async def balance(self, ctx):
        user_id = str(ctx.author.id)
        user = db.child("Users").get()
        userMoney = user.val()
        if(user_id not in userMoney.keys()):
            await ctx.send(f"{ctx.author.mention} First Please use command `z.enter` to enter in our gambling club")
            return
        balance = userMoney[user_id]["Money"]
        embed = discord.Embed(description=f"💵 | {ctx.author.name}, you currently have : __**{str(balance)}**__ zenoency")
        await ctx.send(embed=embed)

    @commands.command(aliases=['cf'])
    async def coinflip(self, ctx, amount, choice=None ):

        user_id = str(ctx.author.id)
        user = db.child("Users").get()
        userMoney = user.val()
        balance = userMoney[user_id]["Money"]

        coinflips = ['head', 'tail']
        result = random.choice(coinflips)

        if(user_id not in userMoney.keys()):
            await ctx.send(f"{ctx.author.mention} First use the command `z.enter` to enter in our gambling club")
            return

        if(amount == "all"):
            amount = balance

        if(int(balance)<int(amount)):
            await ctx.send(f"Poor {ctx.author.mention}!! You don't have a sufficient balance")
            return

        if(choice == None):
            choice = random.choice(coinflips)
        elif(choice == 'h'):
            choice = 'head'
        elif(choice == 't'):
            choice = 'tail'
        await ctx.send(f"{ctx.author.name} spent 💵 {amount} and chose {choice}")
        message = await ctx.send(f"The coin spins...")

        await asyncio.sleep(3)

        if(result == choice):
            winAmount = int(amount) * 2
            await message.edit(content = f"The coin spins...🪙 and You won 💵 {winAmount}")
            new_balance = int(balance) + int(amount)
            db.child("Users").child(user_id).update({"Money": str(new_balance)})
        else:
            await message.edit(content=f"The coin spins...🪙 and you lost it all...")
            loseAmount = int(balance) - int(amount)
            balance = str(loseAmount)
            db.child("Users").child(user_id).update({"Money": balance})

    @commands.command()
    async def give(self, ctx, amount:int, receiver:discord.Member):
        user_id = str(ctx.author.id)
        user = db.child("Users").get()
        userMoney = user.val()
        balance = userMoney[user_id]["Money"]
        receiver_balance = userMoney[str(receiver.id)]["Money"]
        if(str(receiver.id) not in userMoney.keys()):
            await ctx.send(f"Ask {receiver.mention} to enter in our gambling club")
        else:
            new_balance_giver = int(balance) - amount

            db.child("Users").child(user_id).update({"Money": str(new_balance_giver)})

            new_balance_receiver = int(receiver_balance) + amount

            db.child("Users").child(str(receiver.id)).update({"Money": str(new_balance_receiver)})

            await ctx.send(f"💵 | {ctx.author.name} sent {amount} zurrency to {receiver.mention}")


    # @commands.command()
    # async def test(self, ctx, user:discord.Member):
    #     await ctx.send(f"user name: {ctx.author}")
    #     await ctx.send(f"User id: {ctx.author.id}")
    #     await ctx.send(f"member id: {user.id}")


    # @commands.command()
    # async def edit(self, ctx):
    #     message = await ctx.send("hello")
    #     await asyncio.sleep(1)
    #     await message.edit(content=f"newcontent")

def setup(bot):
    bot.add_cog(GambleCog(bot))
    print("Gamble is loaded")
