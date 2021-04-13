import discord
from discord.ext import commands
import json
import random
import praw
from discord.utils import get



reddit = praw.Reddit(
    client_id="client id",
    client_secret="client secret",
    user_agent="doraemon by /u/pr0grammingwizard",
)


class Fun(commands.Cog, name="Fun"):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["m"])
    async def monkeymeme(self, ctx):
        async with ctx.channel.typing():
            # sub = random.choice(["memes", "dankmemes"])
            subreddit = reddit.subreddit("monkememes")
            memes = []
            for submission in subreddit.hot(limit=100):
                if not submission.stickied:
                    memes.append(submission)

            choice = random.choice(range(len(memes)))
            title = memes[choice].title
            url = memes[choice].url
            permalink = memes[choice].permalink
            embed = discord.Embed(
                colour=ctx.author.colour,
                description=f"**[{title}](https://www.reddit.com{permalink})**",
            )
            embed.set_image(url=f"{url}")
        await ctx.send(embed=embed)
        
    
    @commands.command()
    async def profile(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            member = ctx.author if not member else member
            roles = [role for role in member.roles]

            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

            embed.set_author(name=f"User Info - {member}")
            embed.set_thumbnail(url=member.avatar_url)
            embed.set_footer(
                text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url
            )

            embed.add_field(name="ID:", value=member.id)
            embed.add_field(name="Name:", value=member.display_name)

            embed.add_field(
                name=f"Created at:",
                value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
            )
            embed.add_field(
                name=f"Joined at:",
                value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"),
            )

            embed.add_field(
                name=f"Roles({len(roles)})",
                value=" ".join([role.mention for role in roles]),
            )
            embed.add_field(name="Top role: ", value=member.top_role.mention)

            embed.add_field(name="Bot? ", value=member.bot)

        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Fun(client))
