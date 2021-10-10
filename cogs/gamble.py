import asyncio
from random import randrange
import discord
from discord.ext import commands
from discord.ext.commands.core import command
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
        """To enter in gambling arena"""
        user_id = str(ctx.author.id)
        user = db.child("Users").get()
        userMoney = user.val()

        data = {
            "UserId" : user_id,
            "Name" : str(ctx.author),
            "Money" : "100"
        }

        if(user_id not in userMoney.keys()):
            db.child("Users").child(f"{user_id}").set(data)
            await ctx.send(f"Welcome to our gambling club {ctx.author.mention}")
        else:
            await ctx.send("You're already in our gambling club")

    @commands.command(aliases=['bal', 'money'])
    async def balance(self, ctx):
        """To check your balance"""
        user_id = str(ctx.author.id)
        user = db.child("Users").get()
        userMoney = user.val() #ordered dictionary
        if(user_id not in userMoney.keys()): #userMoney.keys() == only keys 
            await ctx.send(f"{ctx.author.mention} First Please use command `z.enter` to enter in our gambling club")
            return
        balance = userMoney[user_id]["Money"]
        embed = discord.Embed(description=f"💵 | {ctx.author.name}, you currently have : __**{str(balance)}**__ zenoency")
        await ctx.send(embed=embed)

    @commands.command(aliases=['cf'])
    async def coinflip(self, ctx, amount, choice=None ):
        """Flip your coin to test your luck"""
        user_id = str(ctx.author.id)
        user = db.child("Users").get()
        userMoney = user.val()
        balance = userMoney[user_id]["Money"]

        coinflips = ['head', 'tail']
        result = random.choice(coinflips)

        if(user_id not in userMoney.keys()):
            await ctx.send(f"{ctx.author.mention} First use the command `z.enter` to enter in our gambling club")
            return

        if (int(amount) > 50000):
            amount = "50000"

        elif(amount == "all"):
            if(int(amount) > 50000):
                amount = "50000"
            else:
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
    async def give(self, ctx, amount:int, receiver:discord.User):
        """Give money to the user"""
        user_id = str(ctx.author.id)
        
        
        user = db.child("Users").get()
        userMoney = user.val()
        
        
        if(str(receiver.id) not in userMoney.keys()):
            # print("true")
            await ctx.send(f"Ask {receiver.mention} to enter in our gambling arena")
            
        elif(user_id not in userMoney.keys()):
            await ctx.send(f"{ctx.author.mention} First use the command `z.enter` to enter in our gambling club")
            
        else:
            balance = userMoney[user_id]["Money"]
            receiver_balance = userMoney[str(receiver.id)]["Money"]

            new_balance_giver = int(balance) - amount

            db.child("Users").child(user_id).update({"Money": str(new_balance_giver)})

            new_balance_receiver = int(receiver_balance) + amount

            db.child("Users").child(str(receiver.id)).update({"Money": str(new_balance_receiver)})

            await ctx.send(f"{ctx.author.mention} give {amount} to {receiver.mention}")


    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def steal(self, ctx, member:discord.User):

        """Steal money from the user"""
        luck = [0, 1]
        chance = random.choice(luck)
        
        stealerId = str(ctx.author.id)
        userId = str(member.id)
        
        user = db.child("Users").get()
        userMoney = user.val()
        
        if(stealerId == userId):
            await ctx.send("You can not steal from yourself. Stupid...")
            return

        if(stealerId not in userMoney.keys()):
            await ctx.send(f"{ctx.author.mention} First use the command `z.enter` to enter in our gambling club")
            return
        elif(userId not in userMoney.keys()):
            await ctx.send(f"{member.mention} First use the command `z.enter` to enter in our gambling club")
            return
        else:
            getStealerMoney = userMoney[stealerId]['Money']
            getUserMoney = userMoney[userId]['Money']

            if(int(getUserMoney) == 0):
                await ctx.send(f"Poor {member.mention} has nothing to steal.")
                
            else:
                stealPercent = random.randint(1, 5)
                stealAmount = int(int(getUserMoney)*(stealPercent*10)/100)
                
                if(chance == 1):    
                    newUserMoney = int(int(getUserMoney) - stealAmount)
                    newStealerMoney = int(int(getStealerMoney) + stealAmount)
                    db.child("Users").child(stealerId).update({"Money": str(newStealerMoney)})
                    db.child("Users").child(userId).update({"Money": str(newUserMoney)})
                    await ctx.send(f"You succesfully stole {stealAmount} zenoency from {member.mention}.")
                else:
                    newStealerMoney = int(getStealerMoney) - stealAmount
                    db.child("Users").child(stealerId).update({"Money": str(newStealerMoney)})
                    await ctx.send(f"Police caught you. You bribe {int(stealAmount)} zenoency to the police ")
    @steal.error
    async def steal_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)} sec', delete_after=round(error.retry_after, 2))



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
