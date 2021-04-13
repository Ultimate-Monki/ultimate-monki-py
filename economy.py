import discord
from discord.ext import commands
import database
import random


class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(aliases=["bal"])
    async def balance(self, ctx, *, user: discord.Member=None):
    	if user is None:
    		balance = database.get_bal(ctx.author.id)
    		return await ctx.send(f"You have {balance}🍌")
    	balance = database.get_bal(user.id)
    	return await ctx.send(f"{user} has {balance}🍌")

    @commands.command()
    async def give(self, ctx, amount: int, *, user: discord.Member):
    	balance = database.get_bal(ctx.author.id)
    	if balance >= amount and amount > 0:
    		balance = balance - amount
    		database.set_bal(ctx.author.id, balance)
    		database.inc_bal(user.id, amount)
    		return await ctx.send(f"You gave {amount}🍌 to {user}")
    	return await ctx.send("You don't have enough bananas.")

    @commands.command()
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def daily(self, ctx):
    	database.inc_bal(ctx.author.id, 50)
    	return await ctx.send(f"You have collected your daily 50🍌")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def search(self, ctx):
    	amount = random.choice(range(20))
    	database.inc_bal(ctx.author.id, amount)
    	return await ctx.send(f"You have found {amount}🍌")

    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def steal(self, ctx, *, species: str):
        if database.get_bal(ctx.author.id) < 50:
            return await ctx.send("You don't have enough money to steal, you need atleast 50 🍌 to steal.")
        monki_species = {
        "gorilla": 10,
        "chimp": 28,
        "chimpanzee": 28,
        "mandrill": 11,
        "tamarin": 43,
        "baboon": 32,
        "orangutan": 45,
        }
        species = species.lower()
        monki = monki_species.get(species, None)
        if monki is not None:
            chance = random.choice(range(100))
            caught = [0, 100]
            if chance in caught:
                new_balance = balance - 50
                database.set_bal(ctx.author.id, balance)
                return await ctx.send(f"You have been caught and had to pay 50 🍌 to the {species} tribe.")
            if chance <= monki:
                database.inc_bal(ctx.author.id, chance)
                return await ctx.send(f"You stole {chance}🍌")
            return await ctx.send("Better Luck next time!")
        return await ctx.send("No such species found.")
