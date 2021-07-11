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
    		return await ctx.send(f"You have {balance} <:Tails_BCoin:857952573791928330>")
    	balance = database.get_bal(user.id)
    	return await ctx.send(f"{user} has {balance} <:Tails_BCoin:857952573791928330>")

    @commands.command()
    async def give(self, ctx, amount: int, *, user: discord.Member):
    	balance = database.get_bal(ctx.author.id)
    	if balance >= amount and amount > 0:
    		balance = balance - amount
    		database.set_bal(ctx.author.id, balance)
    		database.inc_bal(user.id, amount)
    		return await ctx.send(f"You gave {amount} <:Tails_BCoin:857952573791928330> to {user}")
    	return await ctx.send("You don't have enough bananas.")

    @commands.command()
    @commands.cooldown(1, 43200, commands.BucketType.user)
    async def daily(self, ctx):
    	database.inc_bal(ctx.author.id, 50)
    	return await ctx.send(f"You have collected your daily 50 <:Tails_BCoin:857952573791928330>")


    @commands.command()
    @commands.cooldown(1, 2592000, commands.BucketType.user)
    async def monthly(self, ctx):
    	database.inc_bal(ctx.author.id, 125)
    	return await ctx.send(f"You have collected your monthly 125 <:Tails_BCoin:857952573791928330>\n When we restart the bot it will restart all cooldown's, do `m+update` to find out when it was restarted") 


    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def fish(self, ctx):
        amount = random.choice(range(30))
        if amount <= 15:
            database.inc_bal(ctx.author.id, amount)
            lines = [f"You fished, and found {amount} <:Tails_BCoin:857952573791928330>", f"Your 5<:Tails_BCoin:857952573791928330> from the Alouatta Fountain has payed off! You fished {amount} <:Tails_BCoin:857952573791928330>", f"You cast out your line and found {amount} <:Tails_BCoin:857952573791928330>", f"You cast out your line only to find a jellyfish trying to sting you! Luckily you sold it to someone in a dark alley and got {amount} <:Tails_BCoin:857952573791928330>...", f"You went in freestyle! You dived into a lake and caught 2 fish! You earned {amount} <:Tails_BCoin:857952573791928330>"]
            return await ctx.send(f"{random.choice(lines)}")
        return await ctx.send("You fished for 3 hours and found NOTHING!")



    @commands.command()
    @commands.cooldown(1, 25, commands.BucketType.user)
    async def hunt(self, ctx):
        amount = random.choice(range(35))
        if amount <= 25:
            database.inc_bal(ctx.author.id, amount)
            lines = [f"You hunted a lion and got {amount} <:Tails_BCoin:857952573791928330>", f"You killed a beatle! It dropped {amount} <:Tails_BCoin:857952573791928330>", f"You we're hunting in the savana and found a lizard! It dropped {amount} <:Tails_BCoin:857952573791928330>", f"You killed a wild dog! How brave are you?! You earned {amount} <:Tails_BCoin:857952573791928330>", f"You we're hunting in the tundra, you found a few shrubs to eat! Your tribe gave you {amount} <:Tails_BCoin:857952573791928330> for your hard work", f"You killed an elephant! Wow so merciless. You should be ashamed you we're given {amount} <:Tails_BCoin:857952573791928330> for this horrible act"]
            return await ctx.send(f"{random.choice(lines)}")
        return await ctx.send("You we're scared off by a small black and blue tailed monkey, wonder what that could be...")


    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def adventure(self, ctx):
        amount = random.choice(range(20))
        if amount <= 20:
            database.inc_bal(ctx.author.id, amount)
            lines = [f"You found a new item! BEHOLD a eagle feather, so majestic. You we're given {amount} <:Tails_BCoin:857952573791928330>", f"You found a new species! BEHOLD a Python! They constricted movement of a rat! They seem hostile, I suggest not going near them. You we're given {amount} <:Tails_BCoin:857952573791928330> for some useful info", f"You found a new rock! Intresting, it's very dark colors. You found a coal ore! You we're given {amount} <:Tails_BCoin:857952573791928330>", f"You found a new tree! Its very tall! It's a red wood tree! You we're given {amount} <:Tails_BCoin:857952573791928330>"]
            return await ctx.send(f"{random.choice(lines)}")
        return await ctx.send("You we're adventuring for several hours and found no new info!")


    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def work(self, ctx):
        database.inc_bal(ctx.author.id, 15)
        lines = [f"You have groomed the royal family and we're tipped 15 <:Tails_BCoin:857952573791928330>", f"You gathered some sticks for to keep your tribe warm at night and we're tipped 15 <:Tails_BCoin:857952573791928330>", f"You grabbed some leaves for the Orangutan Tribe so they can sleep they tipped you 15 <:Tails_BCoin:857952573791928330> ", f"You got some food for your tribe and we're tipped 15 <:Tails_BCoin:857952573791928330> ", f"You found some rocks for your tribe to get some nuts! They said Thank you. You we're tipped 15 <:Tails_BCoin:857952573791928330>", f"You guarded the royal cave and we're tipped 15 <:Tails_BCoin:857952573791928330>"]
        return await ctx.send(f"{random.choice(lines)}")


    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def steal(self, ctx, *, species: str=None):
        if species is None:
            return await ctx.send("You didnt include a tribe name dumb monki! To find a list of tribes, say `m+help eco`.")
        if database.get_bal(ctx.author.id) < 50:
            return await ctx.send("You need atleast 50 <:Tails_BCoin:857952573791928330> to steal.")
        monki_species = {
        "gorilla": 10,
        "chimp": 3,
        "chimpanzee": 3,
        "mandrill": 20,
        "tamarin": 43,
        "baboon": 32,
        "orangutan": 45,
        "vervet": 30,
        "blue tail": 20,
        "human": 1,
        "gelada": 30,
        "magot": 50,
        "snow monkey": 5,
        "snub nosed": 37,
        "colobus": 75,
        "howler": 40,
        "spider monkey": 40,
        "marmoset": 15,
        "lemur": 20,
        "bushbaby": 60,
        }
        species = species.lower()
        monki = monki_species.get(species, None)
        if monki is not None:
            chance = random.choice(range(100))
            caught = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
            if chance in caught:
                balance = database.get_bal(ctx.author.id)
                new_balance = balance - 50
                database.set_bal(ctx.author.id, new_balance)
                return await ctx.send(f"You have been caught and had to pay 50 <:Tails_BCoin:857952573791928330> to the {species} tribe.")
            if chance <= monki:
                database.inc_bal(ctx.author.id, chance)
                return await ctx.send(f"You stole {chance} <:Tails_BCoin:857952573791928330>")
            return await ctx.send("Better Luck next time!")
        return await ctx.send("No such species found.")
