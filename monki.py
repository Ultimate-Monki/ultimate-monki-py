import discord
from discord.ext import commands
from discord import Activity, ActivityType, AllowedMentions
from discord.ext import commands
from discord.ext.commands import when_mentioned_or
import database
import logging
import random
from economy import Economy
# from commands import Commands
from reddit import Fun
from newsletter import Newsletter

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.typing = True
intents.presences = False
# intents.members = True

client = commands.Bot(
    command_prefix=when_mentioned_or("m+"),
    help_command=None,
    allowed_mentions=AllowedMentions.none(),
    intents=intents,
)


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(name=f"{len(client.guilds)} tribes | m+help", type=3),
    )
    print(f'Bot is running as "{client.user}"')
    print("=========================================")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    embed = discord.Embed(
        title="Oops, an error occured!",
        colour=0x738d60,
        description=f"{error}",
    )
    embed.set_image(url="https://i.imgur.com/iPm0Fst.gif")
    await ctx.send(embed=embed)
    print(error)
   
   
@client.event
async def on_message(message):
    member = database.find_member(message.author.id)
    if member is None:
        profile = {
        "member_id": message.author.id,
        "balance": 0,
        "subscriptions": [],
        }
        database.add_member(profile)
        print(
                f"Profile has been created for member {message.author}:{message.author.id}"
            )
    await client.process_commands(message)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    embed = discord.Embed(
        title="Oops! I fell into an error!",
        colour=0x738d60,
        description=f"{error}",
    )
    embed.set_image(url="https://imgur.com/iPm0Fst.gif")
    await ctx.send(embed=embed)
    print(error)


@client.group()
async def help(ctx):
    if ctx.invoked_subcommand is None:
        async with ctx.channel.typing():
            embed = discord.Embed(
                title="Help",
                colour=0x738d60,
                description="""
    Here's the list of commands you can use:
    """,
            )
            embed.add_field(
                name=":speech_balloon:**__GENERAL__**",
                value="`m+help gen`",
            )
            embed.add_field(
                name=":tools:**__MODERATION__**",
                value="`m+help mod`",
            )

            embed.add_field(
                name=":monkey_face:**__GIF's__**",
                value="`m+help gif`",
            )
            embed.add_field(
                name=":coin:**__ECONOMY__**", 
                value="`m+help eco`"
            )
            embed.add_field(
                name=":red_circle:**__LIVE__**", 
                value="`m+help live`"
            )
            embed.add_field(
                name=":musical_note:**__MUSIC__**", 
                value="`coming soon!`"
            )
            embed.add_field(
                name=":wave:**__WELCOME__**", 
                value="`coming soon!`"
            )
            embed.add_field(
                name=":boom:**__FUN__**", 
                value="`m+help fun`"
            )
            embed.add_field(
                name=":microscope:**__EXP. FEATURES__**", 
                value="`m+help exp`"
            )
            embed.add_field(
                name="\u200b",
                inline=False,
                value="*Go to http://invite.ultimatemonki.live/ to invite Ultimate Monki*",
            )
        await ctx.send(embed=embed)


@help.command(aliases=["ECO"])
async def eco(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x738d60,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Economy ",
            inline=False,
            value=f"`{ctx.prefix}daily` - get 50 daily bananas\n `m+monthly` - get your monthly bananas\n `{ctx.prefix}adventure` - find new items, species, and animals for bananacoins\n`{ctx.prefix}hunt` - hunt for animals for bananacoins\n`{ctx.prefix}fish` - fish for bananacoins\n`{ctx.prefix}work` - help your tribe survive and get some resources!\n`{ctx.prefix}steal" 
            f" <species>` - steal from a monkey\n`<species>` = orangutan, chimp, gorilla, mandrill, tamarin, baboon, vervet, blue tail, human, gelada, magot, snow monkey, snub nosed, colobus, howler, spider monkey, marmoset, lemur, bushbaby\n`{ctx.prefix}bal` - see your balance\n`{ctx.prefix}give <#> @user` -"
            f" give a user bananas",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@help.command(aliases=["EXP"])
async def exp(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x738d60,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Experimental Features",
            inline=False,
            value=f"`{ctx.prefix}shop` - Added items but not connected to economy database\n`{ctx.prefix}map` - Soon will have land marks",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@help.command(aliases=["MOD"])
async def mod(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x738d60,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Moderation ",
            inline=False,
            value=f"`{ctx.prefix}clear <#>` - deletes a specific amount of messages\n`{ctx.prefix}deafen @user` - deafen a user in a vc\n`{ctx.prefix}undeafen @user` - undeafen a user in a vc\n`{ctx.prefix}kick @member` - Kicks a member from the server\n`{ctx.prefix}ban @user` - bans the member that was pinged\n`{ctx.prefix}softban @user` - bans a user then immediatly unbans them to delete all messages from them in the last 7 days \n`{ctx.prefix}unban <user ID>` - unbans a member\n`{ctx.prefix}lock` - makes the default role (@ everyone) not able to talk in the channel you sent the command in\n`{ctx.prefix}unlock` - makes the default role (@ everyone) able to talk in the channel you sent the command in\n`{ctx.prefix}mute @user` - Mutes a specific user making them not be able to talk\n`{ctx.prefix}unmute @user` - Unmutes a specific user making them able to talk again\n`{ctx.prefix}profile @user` - Shows infomormation on a member of the server\n`{ctx.prefix}membercount` - shows the member count of the server\n`{ctx.prefix}slowmode <seconds` - sets slow mode of channel (Max is 21600s)",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@help.command(aliases=["GIFS"])
async def gifs(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x738d60,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Gif's",
            inline=False,
            value=f"`{ctx.prefix}call` - Sends a GIF of you **calling**\n`{ctx.prefix}dominate` - Sends GIF of you **dominating**\n`{ctx.prefix}fistbump` - Sends a GIF of you **fistbumping**\n`{ctx.prefix}flex` - Sends GIF of you **flexing**\n`{ctx.prefix}flirt` - Sends GIF of you **flirting**\n`{ctx.prefix}hug` - Sends GIF of you **hugging**\n`{ctx.prefix}shoot` - Sends GIF of you **shooting**\n`{ctx.prefix}snipe` - Sends a GIF of you **sniping**\n`{ctx.prefix}slap` - Sends GIF of you **slapping**\n`{ctx.prefix}taunt` - Sends GIF of you **taunting**\n`{ctx.prefix}race` - Sends a GIF of you **racing**\n`{ctx.prefix}stonks` - Sends a GIF of  **stonks**\n`{ctx.prefix}evil` - Sends a GIF of you becoming **evil**\n`{ctx.prefix}suicide` - Sends a GIF of you commiting **suicide**\n`{ctx.prefix}danceparty` - Sends a GIF of you having a **danceparty**\n`{ctx.prefix}swim` - Sends a GIF of you **swimming**",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@help.command(aliases=["GIF"])
async def gif(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x738d60,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Gif's",
            inline=False,
            value=f"`{ctx.prefix}call` - Sends a GIF of you **calling**\n`{ctx.prefix}dominate` - Sends GIF of you **dominating**\n`{ctx.prefix}fistbump` - Sends a GIF of you **fistbumping**\n`{ctx.prefix}flex` - Sends GIF of you **flexing**\n`{ctx.prefix}flirt` - Sends GIF of you **flirting**\n`{ctx.prefix}hug` - Sends GIF of you **hugging**\n`{ctx.prefix}shoot` - Sends GIF of you **shooting**\n`{ctx.prefix}snipe` - Sends a GIF of you **sniping**\n`{ctx.prefix}slap` - Sends GIF of you **slapping**\n`{ctx.prefix}taunt` - Sends GIF of you **taunting**\n`{ctx.prefix}race` - Sends a GIF of you **racing**\n`{ctx.prefix}stonks` - Sends a GIF of  **stonks**\n`{ctx.prefix}evil` - Sends a GIF of you becoming **evil**\n`{ctx.prefix}suicide` - Sends a GIF of you commiting **suicide**\n`{ctx.prefix}danceparty` - Sends a GIF of you having a **danceparty**\n`{ctx.prefix}swim` - Sends a GIF of you **swimming**",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@help.command(aliases=["LIVE"])
async def live(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x738d60,
            description="Here is a list of commands you can use: ",
        )
        embed.add_field(
            name="Live",
            inline=False,
            value=f"`{ctx.prefix}liveARIZ` - Posts link to live footage **[Arizona]**\n`{ctx.prefix}liveBS` - Posts link to live footage **[Connecticut]**\n`{ctx.prefix}liveDET` - Posts link to live footage **[Michigan]**\n`{ctx.prefix}liveEP` - Posts link to live footage **[Chihuahua]**\n`{ctx.prefix}liveHOU` - Posts link to live footage **[Texas]**\n`{ctx.prefix}liveIN` - Posts link to live footage **[Indiana]**\n`{ctx.prefix}liveKC` - Posts link to live footage **[Missouri]**\n`{ctx.prefix}liveSD` - Posts link to live footage **[California]**",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@help.command(aliases=["GEN"])
async def gen(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x738d60,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="General",
            inline=False,
            value=f"\n`{ctx.prefix}support` - posts our support server invite\n`{ctx.prefix}github` - posts our github\n`{ctx.prefix}updates` - shows what the developers are working on\n`{ctx.prefix}ping` - Used for testing purposes shows how fast the bot is 'calculating'\n`{ctx.prefix}invite` - gives you the invite to the bot\n`{ctx.prefix}suggest <suggestion>` Sends us a suggestion you gave in our support server\n`{ctx.prefix}report <report>` - sends us a report for bugs in our support server\n",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@help.command(aliases=["FUN"])
async def fun(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x738d60,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Fun",
            inline=False,
            value=f"\n`{ctx.prefix}rate` - Shows how close you are to monkey\n`{ctx.prefix}fact` - Posts a random monkey fact"
            f"\n`{ctx.prefix}truth` - Tells you a question that you must answer\n`{ctx.prefix}dare` - Tells you a dare that you must complete"
            f"\n`{ctx.prefix}8ball <question>` - Just like a magic 8ball! Tells you the future"
            f"\n`{ctx.prefix}roll` - Roll a die!"
            f"\n`{ctx.prefix}monkeymeme` - Posts the most upvoted monkey meme on reddit!"
            f"`{ctx.prefix}rps` - play rock paper scissors!"
            f"\n`{ctx.prefix}say` - copies what ever you say",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@client.event
async def on_guild_join(guild):
    channel = guild.system_channel
    embed = discord.Embed(
        colour=0x738d60,
        description="""Hello! Thanks for adding me!
        Ultimate Monki is a multipurpose Discord Bot that is fully based on monkeys!
        
        There are a lot of things you can do with Ultimate Monki, simply use the `m+help` command to see a list of commands you can use.
        """,
    )
    embed.add_field(
        name="**__Usefull Links__**",
        inline=False,
        value="""
    Consider voting on **[Ultimate Monki](https://top.gg/bot/787887645879435284)** on Top.gg or on [Discordbotlist.com](https://discordbotlist.com/bots/ultimate-monki/upvote)
    Have an bug or suggestion? Join the **[Support Server](https://discord.gg/sg25dQ6E3U)**  
    Find source code on **[Ultimate Monki's Github page](https://github.com/Ultimate-Monki)**
    """,
    )
    await channel.send(embed=embed)



@client.command()
async def liveSD(ctx):
    embed = discord.Embed(
        title="San Diego",
        colour=0x738d60,
        description="San Diego Zoo is committed to saving species worldwide by uniting our expertise in animal care and conservation science with our dedication to inspiring passion for nature.\n**CAMERA HOURS:** 7:30AM-7:30PM PST\n**LINK:** https://zoo.sandiegozoo.org/cams/ape-cam",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveKC(ctx):
    embed = discord.Embed(
        title="Kansas City",
        colour=0x738d60,
        description="One of two subspecies of orangutan, Bornean orangutans are found natively on the island of Borneo. As frugivores, their diet includes over 400 types of fruit in the wild and they are important movers of seeds, passing them through their digestive system. You can find our group of six at Orangutan Canopy.\n**CAMERA HOURS:** 24/7\n**LINK:** https://www.kansascityzoo.org/animal-cam/orangutan-camera",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveDET(ctx):
    embed = discord.Embed(
        title="Detroit",
        colour=0x738d60,
        description="The Japanese macaque habitat is home to six females and three males, whose social structure is built around lineage.\n**CAMERA HOURS:** 11:30AM-9:00PM EST\n**LINK:** https://detroitzoo.org/snow-monkey-live-cam/",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveIN(ctx):
    embed = discord.Embed(
        title="Indiana",
        colour=0x738d60,
        description="Enjoy a virtual visit with your some of your favorite animals. Our webcams are a wild way to see what’s happening at the Zoo no matter where you are!\n**CAMERA HOURS:** 24/7\n**LINK:** https://www.indianapoliszoo.com/webcams/",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveHOU(ctx):
    embed = discord.Embed(
        title="Houston Zoo",
        colour=0x738d60,
        description="What’s going on in the chimpanzee habitat at the Houston Zoo right now? Find out with our live webcam below.\n**CAMERA HOURS:** 7 A.M. – 7 P.M. CST\n**LINK:** https://www.houstonzoo.org/explore/webcams/chimpanzee-cam/",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveBS(ctx):
    embed = discord.Embed(
        title="Beardsley",
        colour=0x738d60,
        description="Please note that our animals are constantly on the move and may not always be visible on camera.\n**CAMERA HOURS:** 8:30-6:00PM EST\n**LINK:** https://www.beardsleyzoo.org/outdoor-spider-monkey-cam.html",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveARIZ(ctx):
    embed = discord.Embed(
        title="Arizona",
        colour=0x738d60,
        description="These primates have an athletic body and limbs ideal for climbing and bounding from one tree to another. Their legs and strong hands give them the power to climb and hang. They have a non-prehensile tail, covered in characteristic black and white rings, that helps them balance while in the trees. Enjoy watching!\n**CAMERA HOURS:**  9 A.M. – 4 P.M. MST\n**LINK:** http://reidparkzoo.org/cameras/lemur-cam/",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveEP(ctx):
    embed = discord.Embed(
        title="El Paso",
        colour=0x738d60,
        description="The El Paso Zoo celebrates the value of animals and natural resources and creates opportunities for people to rediscover their connection to nature.\n**CAMERA HOURS:** 24/7\n**LINK:** http://www.elpasozoo.org/zoo-cameras/siamangs-playground",
    )
    await ctx.send(embed=embed)


@client.command()
async def support(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Support Server",
            colour=0x738d60,
            description="Here is our [Support Server!](https://discord.gg/sg25dQ6E3U) to your server!",
        )
    await ctx.send(embed=embed)


@client.command()
async def invite(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Invite",
            colour=0x738d60,
            description="[Invite me](http://invite.ultimatemonki.live/) to your server!",
        )
    await ctx.send(embed=embed)


@client.command()
async def update(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="New Update!",
            colour=0x738d60,
            description="**UPDATED COMMAND**\n`m+steal` has more species! All of them are listed in economy help command.\nMORE GIFS\n\n**ADDED COMMAND**\n`m+adventure`\n`m+fish`\n`m+hunt`\nThis replaces `m+search`\n\n**Last Restarted:** `7/5/21 9:55 AM EST`",
        )
    await ctx.send(embed=embed)



@client.command()
async def github(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Github",
            colour=0x738d60,
            description="Here is our [Github](https://github.com/Ultimate-Monki/)!",
        )
    await ctx.send(embed=embed)


@client.command()
async def taunt(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} taunted {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/596e44ed64d2e3d90dd6d1f53ba6838c/tenor.gif?itemid=9704814")
        await ctx.send(embed=embed)


@client.command()
async def hug(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} hugged {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/81a599fa44c084bb3675ba1699154082/tenor.gif?itemid=5415807")
        await ctx.send(embed=embed)


@client.command()
async def kiss(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} kissed {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media.tenor.com/images/82fb02af3ecaf782b764c75c743089cc/tenor.gif")
        await ctx.send(embed=embed)


@client.command()
async def flirt(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} flirted with {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media.tenor.com/images/5b25ee40103b0a2be754485e47eddeac/tenor.gif")
        await ctx.send(embed=embed)


@client.command()
async def shoot(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} shooted {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media.tenor.com/images/608378240db890e2acac36cba80800ff/tenor.gif")
        await ctx.send(embed=embed)


@client.command()
async def snipe(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} sniped {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/ca14214ee3983b285a73056d3d408827/tenor.gif?itemid=20219406")
        await ctx.send(embed=embed)


@client.command()
async def call(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} called {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/6100ca9212bd9254f1303e921667d7bb/tenor.gif?itemid=4577639")
        await ctx.send(embed=embed)


@client.command()
async def fistbump(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} fistbumped {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/e12dfb1b5588171beae2baddfdb20565/tenor.gif?itemid=16712819")
        await ctx.send(embed=embed)


@client.command()
async def slap(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} slapped {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media.tenor.com/images/0025118143c207f6f2c8f9c7b59c7410/tenor.gif")
        await ctx.send(embed=embed)


@client.command()
async def dominate(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} showed they're dominance between {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/b88d182acdc669511b7122609bfd3aab/tenor.gif?itemid=8291564")
        await ctx.send(embed=embed)


@client.command()
async def flex(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} flexed they're wealth between {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/ae96ee628ef967b0e7dcdc4b3dbff0e8/tenor.gif?itemid=14116367")
        await ctx.send(embed=embed)


@client.command()
async def race(ctx, *, user: discord.Member):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} is racing against {user.name}", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/09cbebc82bbda1312196d6cbe860943d/tenor.gif?itemid=22123868")
        await ctx.send(embed=embed)


@client.command()
async def stonks(ctx):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} is talking about STONKS", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/ad33c670a1c619f09e80b5e055838a63/tenor.gif?itemid=10070498")
        await ctx.send(embed=embed)


@client.command()
async def evil(ctx):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} has become evil", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/29798b1b7c5885c6370d507684e2a26a/tenor.gif?itemid=9680625")
        await ctx.send(embed=embed)


@client.command()
async def suicide(ctx):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} has commited suicide", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/74508c532e65d735b0c00fa541b6f165/tenor.gif?itemid=21228020")
        await ctx.send(embed=embed)


@client.command()
async def danceparty(ctx):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} is hosting a dance party", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/7745752757232a125df86e3a4745ccb5/tenor.gif?itemid=14656700")
        await ctx.send(embed=embed)


@client.command()
async def swim(ctx):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"{ctx.author.name} is swimming with the fishies", colour=0x738d60
            )
            embed.set_image(url="https://media1.tenor.com/images/fbb8c0a796f675bcfa5828909ec60dea/tenor.gif?itemid=22072831")
        await ctx.send(embed=embed)


@client.command()
async def map(ctx):
        async with ctx.channel.typing():
            
            embed = discord.Embed(
                title=f"The map of Monke Islands", colour=0x738d60
            )
            embed.set_image(url="https://i.imgur.com/imKlvs8.jpg")
        await ctx.send(embed=embed)


@client.command()
async def vote(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title=":heart: Thank you for voting :heart:!",
            colour=0x738d60,
            description="Vote Perks will be added soon! \n[Top.gg](https://top.gg/bot/787887645879435284/vote)\n[Discordbotlist.com](https://discordbotlist.com/bots/ultimate-monki/upvote)",
        )
    await ctx.send(embed=embed)


@client.command(aliases=["suggestion"])
async def suggest(ctx, *, suggestion: str = None):
    if suggestion is not None:
        async with ctx.channel.typing():
            channel = client.get_channel(id=787540023523803136)
            embed = discord.Embed(
                title="New Suggestion",
                colour=0x738d60,
                description=suggestion,
            )
            embed.set_author(
                name=ctx.author.name,
                url=discord.Embed.Empty,
                icon_url=ctx.author.avatar_url,
            )
        sus_monke = await channel.send(embed=embed)
        sus_monke.add_reaction("✅️")
        sus_monke.add_reaction("❌️")
        return await ctx.send("Thank You for giving us your feedback!")
    return await ctx.send("`m+suggest <suggestion>`")


@client.command()
async def report(ctx, *, report: str = None):
    if report is not None:
        async with ctx.channel.typing():
            channel = client.get_channel(id=787540193384726552)
            embed = discord.Embed(
                title="New Bug Report",
                colour=0x738d60,
                description=report,
            )
            embed.set_author(
                name=ctx.author.name,
                url=discord.Embed.Empty,
                icon_url=ctx.author.avatar_url,
            )
        await channel.send(embed=embed)
        return await ctx.send("Thank You for giving us your feedback!")
    return await ctx.send("`m+report <report>`")


@client.command()
async def ping(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Ping",
            colour=0x738d60,
            description=f"Lookin Good!\n `Latency: {round(client.latency * 1000)} ms`",
        )
    await ctx.send(embed=embed)


@client.command()
async def shop(ctx):
    if ctx.invoked_subcommand is None:
        async with ctx.channel.typing():
            embed = discord.Embed(
                title="Shop",
                colour=0x738d60,
                description="""
    Here's the shop preview it hasnnt been implemented yet. Ty for your patience
    """,
            )
            embed.add_field(
                name="<:Monkees_Album:858346064737075240>**__Monkee's album__**", 
                value="10% booster gives better findings when you do m+fish and m+hunt\nCOST: 10,000<:Tails_BCoin:857952573791928330>\n`ID:album`",
            )
            embed.add_field(
                name="<:Peanut:858335229953572866>**__Nut's__**", 
                value="Doesn't do anything. Just a collectable!\nCOST: 150<:Tails_BCoin:857952573791928330>\n`ID:nut`",
            )
            embed.add_field(
                name="<:Stick:858327203460546582>**__Stick__**", 
                value="Better chances on finding ants!\nCOST: 8,000<:Tails_BCoin:857952573791928330>\n`ID:stick`",
            )
            embed.add_field(
                name="<:Lottery_Ticket:858776561205772328>**__Lottery_Ticket__**", 
                value="Buy a lottery ticket and you might win!\nCOST: 300<:Tails_BCoin:857952573791928330>\n`ID:ticket`",
            )
            embed.add_field(
                name="<:Golden_Banana:858338416751411200>**__Golden Banana__**", 
                value="Die a lot? Buy it then you won't need to worry! It's a life saver\nCOST: 9,000<:Tails_BCoin:857952573791928330>\n`ID:banana`",
            )
        await ctx.send(embed=embed)
    

# @client.command()
# async def function(ctx):
#     embed = discord.Embed(
#         title="",
#         colour=0x738d60,
#         description="",
#     )
#     await ctx.send(embed=embed)


@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="Muted", description=f"{member.mention} was muted ", colour=0x738d60)
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" You have been muted in {guild.name} reason: {reason}")


@client.command()
async def tempmute(ctx, member: discord.Member, time: int, d, *, reason=None):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)

            embed = discord.Embed(title="Muted", description=f"{member.mention} was temporarily muted ", colour=0x738d60)
            embed.add_field(name="reason:", value=reason, inline=False)
            embed.add_field(name="time left for the mute:", value=f"{time}{d}", inline=False)
            await ctx.send(embed=embed)

            if d == "s":
                await asyncio.sleep(time)

            if d == "m":
                await asyncio.sleep(time*60)

            if d == "h":
                await asyncio.sleep(time*60*60)

            if d == "d":
                await asyncio.sleep(time*60*60*24)

            await member.remove_roles(role)

            embed = discord.Embed(title="unmute (temp) ", description=f"unmuted -{member.mention} ", colour=0x738d60)
            await ctx.send(embed=embed)

            return


@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f" You have unmuted from {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}", colour=0x738d60)
   await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def deafen(ctx, member: discord.Member):
    embed = discord.Embed(title="Deafen", description=f"{member.mention} has been deafened", colour=0x738d60)
    await member.edit(deafen=True)
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def undeafen(ctx, member: discord.Member):
    embed = discord.Embed(title="Undeafen", description=f"{member.mention} has been undeafened", colour=0x738d60)
    await member.edit(deafen=False)
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member):
    embed = discord.Embed(
        title="Warned",
        description=f'{member.mention}has been warned.')
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    embed = discord.Embed(
        title="Kicked",
        description=f'{member.mention} has been kicked.')
    await member.kick(reason=reason)
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    embed = discord.Embed(
        title="Banned",
        description=f'{member.mention} has been banned.')
    await member.ban(reason=reason)
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member, *, reason=None):
    embed = discord.Embed(
        title="Softbanned",
        colour=0x738d60,
        description=f'{member.mention} has been softbanned.',
    )
    await member.ban(
        reason=reason, 
        delete_message_days=7,
    )
    await member.unban()
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(
                title="Unbanned",
                colour=0x738d60,
                description=f'{user.mention} has been unbanned.')
            await ctx.send(embed=embed)
            return


@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    async with ctx.channel.typing():
        embed = discord.Embed(
            colour=0x738d60,
            description="You have locked this channel!",
        )
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    async with ctx.channel.typing():
        embed = discord.Embed(
            colour=0x738d60,
            description="You have unlocked this channel!",
        )
    await ctx.send(embed=embed)


@client.command()
async def slowmode(ctx, seconds: int):
    embed = discord.Embed(
        title="Slowmode",
        colour=0x738d60,
        description=f'I have set the slowmode to {seconds} seconds')
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send (embed=embed)


async def membercount(ctx):
    embed = discord.Embed(
        colour=0x738d60,
        title="Member Count",
        description=f"There are {len(ctx.guild.members)} members in this server") 
    await ctx.send(embed=embed)

    
@client.command()
async def fact(ctx):
   async with ctx.channel.typing():
     facts = ["Monkeys can understand written numbers and can even count. They can also understand basic parts of arithmetic and even, in rare cases, multiplication.", "To attract a female partner, male capuchin monkeys will urinate in their hands and then rub it thoroughly into their fur.", "The origins of the word monkey are unclear. It appears also to be related to manikin, from the Dutch manneken (little man). It could also be derived from the name of a popular medieval beast story  in which the son of an ape is named Moneke.", "A Colombian woman claimed that she was raised by a colony of capuchin monkeys after being kidnapped and abandoned in the jungle when she was just 4 years old.", "Raw and cooked brain of dead monkey is widely consumed in China and Malaysia.", "Scientists observed female monkeys teaching their young how to floss their teeth.", "The smallest monkey in the world is the pygmy marmoset, with a body as little as 5 inches (12 cm) and a tail length of about 7 inches (17 cm). As a comparison, they are about the size of a hamster, can fit in the palm of a human hand, and they weigh the same as a pack of cards.", "The most recently discovered monkey is the lesula monkey. It was discovered in 2007 in the Democratic Republic of the Congo in Africa.", "Diseases that can spread from monkey to humans include Ebola Reston, B virus (Cercopithecine herpesvirus 1), monkey pox, yellow fever, simian immunodeficiency virus, tuberculosis, and other diseases not yet known or identified.", "Uncle Fat is a morbidly obese monkey in Thailand who gorged himself on junk food and soda that tourists had left behind. As the leader of his troop, this gluttonous monkey also had subordinate monkeys bringing him goodies.", "Apes, gibbons, lemurs, and chimpanzees are not scientifically classified as monkeys. They are all primates, but, like humans, they have a different classification to monkeys.", "An abandoned medical research facility called the New York Blood Center used wild chimpanzees in its vaccination research in the 1970s. When the research facility shut down in 2005, the 66 remaining chimps were set free on a small land mass soon dubbed Monkey Island.", "At the tip of a monkey's tail is a patch of bare skin that acts similar to a human's fingertips. It is sensitive to touch and also has tiny ridges that gives the tail a better grip.", "In Hindu, Hanuman (disfigured jaw) is a human-like monkey god who commanded a monkey army. Interestingly, women were not allowed to worship the monkey god", "Monkeys are superior to Humans >:)", "Monkeys that live in Central and South America are called New World monkeys. Monkeys that live in Africa and Asia are called Old World monkeys", "Contrary to popular opinion, humans did not come from monkeys. Rather, humans and monkeys share a common ancestor 25-30 million years ago and then evolved from this animal in various different ways.", "Old World Monkeys have narrow noses that point down, don't hang in trees, are larger, don't have prehensile tails, and have strange sitting pads on their bottoms. New World monkeys have flatter noses, live in trees, and have prehensile tails.", "The female spider monkey has the longest tail of all the primates. Even though its body is only 2 feet long, its tail can reach 3 feet in length. Their tails can carry the the monkey's entire body weight and even pick up items as small as peanut.", "Mandrill monkeys have fangs that are longer than a lion's fangs. They also have multi-colored bottoms which makes them easier to see in the leafy gloom of the forest.", "The fastest primate on Earth is the patas monkey. It can reach speeds of 34 miles per hour (55 km/h)", "The uakari is one of the rarest and most unusual-looking of all the New World monkeys. While it looks similar to an orangutan, its face is pink, which often turns bright red when the animal becomes excited or angry. It also makes a noise similar to a human laughing.", "While monkeys and apes are related, they are very different from each other. Monkeys have tails, have snouts, and they are not as intelligent as apes. Additionally, apes are not found in North or South America or Europe, while monkeys are.", "The owl monkey (night monkey) is the only nocturnal New World monkey. They are also one of the few monkey species affected by malaria, which means they have been used in non-human primate malaria experiments.", "Africa's Namib Desert is home to the chacma baboons. One hardy chacma baboon troop survived 116 days without water in the desert by eating figs.", "The only wild monkey in Europe is the tailless Barbary macaque, which is found in parts of Northern Africa and the British territory of Gibraltar.", "The first primate in space was a rhesus macaque named Albert. On June 14, 1949, Albert was sent into space to test the effects of space travel on a body. While he survived the flight, he died when the rocket parachute failed.", "The Japanese macaque is the northernmost monkey and is capable of living in more than 3 feet of snow in as temperatures as low as 5 degrees Fahrenheit (-15 degrees Celsius).", "The largest monkey in the world is the male mandrill. It is almost 1 meter (3.3 feet) long and weighs about 35 kilograms (77 pounds).", "The ancient Egyptians considered the Hamadryas Baboon to be sacred. One of their gods, Thoth was regularly drawn as a man with the head of this baboon.", "The monkey is the 9th animal in the Chinese zodiac. People born in a year of the monkey are supposedly intelligent, lively, and creative, but might also be selfish and impatient.", "The capuchin monkey is the most common and the most intelligent of the New World monkeys.", "The spider monkey is the most acrobatic of the New World monkeys, and it has been know to leap across gaps as large as 35 feet.", "Monkeys are found almost everywhere on Earth, except for Australia and Antarctica.", "The Diana monkey was named for the Roman goddess of hunting because the stripe on its forehead resembles Diana bow.", "The male howler monkey has the loudest call of any other primate and is one of the loudest animals in the world. Interestingly, the louder the howler monkey, the smaller its testicles and the lower its sperm count.", "Capuchin monkeys are named after the 16th-century monks because the monkey's hair resembles the monks' hooded robes.", "Monkeys are long-lived, surviving in the wild anywhere between 10 and 50 years.", "Ethiopian geladas form the largest monkey troops in the world, numbering from 350 to 650 individuals.", "Ethiopian geladas form the largest monkey troops in the world, numbering from 350 to 650 individuals.", "Picking out parasites and dirts from each others' furs is a way for monkeys to communicate, form social hierarchies, and strengthen family and friendship bonds.", "Found only in the Chinese province of Yunnan, the black snub-nosed monkey lives at the higest altitudes, near 15,000 feet  (4,572 m) of any primate.", "A group of monkeys is variously called a troop, barrel, carload, cartload, or tribe.", "To identify themselves more easily, squirrel monkeys will smear food on their tails, much like how humans may wear name tags.", "Due to the loss of trees in their native habitat, only about 1,500 golden lion tamarins exist in the wild.", "Each year, about 55,000 primates are used as test animals in the U.S., and about 10,000 are used in Great Britain. Japan uses millions of primates.", "When researchers offered the Japanese macaque sweet potatoes during research in the 1940s, the monkeys didn't like the taste of the dirt on the veggies, so they washed it off. Now, generations later, washing food has become a learned behavior. No other monkeys in the world are known to wash their food before eating.", "HIV was created in the stomach of a chimp who had eaten two different types of monkeys that had two different viruses.  The two viruses combined to form a hybrid virus, which then spread through the chimp species, and then later was transmitted to humans.", "White-faced capuchin monkeys rub their fur with the Giant African Millipedes, which acts as a form of insect repellent.", "On the Yakushima island Japan, monkeys groom and share food with deer in exchange for a ride.", "After weeks of training, rhesus monkeys learned to recognize themselves in a mirror. The first thing they did was to promptly examined their genitals, every intimate nook and cranny.","The 'Monkey Orchid' is a flower that has evolved to look like the grinning face of a monkey. Ironically, instead of smelling like bananas, it smells like a ripe orange.", "Alexander I, the king of Greece, died from sepsis after being bit by one of his pet monkeys. His death led to a war that killed over 100,000 people.", "A recently discovered monkey, the Burmese sneezing monkey, sneezes whenever it rains.", "A group of 15 captive monkeys at a primate research institute in Japan used tree branches to fling themselves over a high voltage electric fence. They were later lured back to the research center with peanuts.", "To prove that children need a mother's love, scientist Harry Harlow subjected baby monkeys to horrific experiments in what was called the The Pit of Despair in which he isolated and tortured baby monkeys.", "The mustached emperor tamarin is believed to have been named for German Emperor Wilhelm II. Both have impressive mustaches.", "French surgeon Serge Voronoff (1866-1951) gained notoriety when he grafted monkey testicles into the the scrotum of human patients in an attempt to cure infertility and increase their sex drive.", "A 22-year-old primate researcher at Emory died after a rhesus monkey infected with the herpes B virus threw a tiny drop of fluid, mostly likely from  urine or feces, at her face as she was transporting the animal.", "Italian Professor Sergio Canavero claimed to have conducted the first monkey head transplant without any neurological injury to the animal. However, he did not connect the spinal cord, so the monkey was completely paralyzed. It was only kept alive for only 20 hours after the procedure for ethical reasons.", "Italian Professor Sergio Canavero claimed to have conducted the first monkey head transplant without any neurological injury to the animal. However he did not connect the spinal cord so the monkey was completely paralyzed. It was only kept alive for only 20 hours after the procedure for ethical reasons", "Monkeys are better than Humans >:)", "Monkeys are better than Humans >:)", "The official way to say Monkey is actually Monke", "When you react with :banana: 45 times you will get a role ;)", "Monkeys belong to the order of mammals called primates. Humans also belong to this order, along with apes, tarsiers, lorises, and lemurs.", "Monkeys often live in groups. A group of monkeys is called a troop, which can consist of up to 500 individuals. Some troops come together to form larger groups called tribes.", "Baby monkeys are called infants, just like human babies. Like human babies, they are born with their eyes closed and without any teeth. They are quite helpless, which is why they cling to their mother’s belly during the first few weeks of life.", "Monkeys communicate in various ways. They make different sounds like screeches and hoots in order to alert others to danger and to keep other monkeys away from their territory. They can also use body language. For example, they bob their heads to show that they are angry, or smack their lips to show that they are happy.", "A monkey’s average day is spent looking for food, eating, resting or sleeping, and grooming. Grooming is not just a way for monkeys to keep each other clean, but also to strengthen their bonds.", "Monkeys are omnivorous, meaning they eat both plants and other animals. They prefer to eat plants, though–specifically fruits, leaves, and nuts, while eating insects, bird eggs, spiders, snails, and lizards on occasion.", "The average lifespan of a monkey depends on its species. Some monkeys live for only ten years, while others can live for up to fifty years.", "Monkeys are classified into two types – New World monkeys and Old World monkeys. New World monkeys can be found mostly in Central and South America.", "New World monkeys tend to be smaller than Old World monkeys. In fact, most New World monkeys are less than two feet long.", "New World monkeys have noses that are flat and narrow, with nostrils pointing toward the sides. The name of their superfamily, Platyrrhini, means ‘flat-nosed’.", "New World monkeys have long tails that can grow almost as long as their bodies and are sometimes prehensile. Prehensile means that the tail is able to grasp objects like tree branches or leaves.", "When it comes to breeding, most New World monkeys have only one mate at a time. When the baby monkey is born, both the male and female monkey care of it until it is old enough to take care of itself.", "Most New World monkeys have claw-like nails called tegulae, which are only present on a few fingers and toes. They are used to grip tree branches. Old World monkeys, in contrast, have blunt nails called ungulae.", "Old World monkeys can be found in Asia and Africa. Some of them are arboreal, living mostly in trees, while others are terrestrial, spending most of their life on the ground.", "Old World monkeys range from medium to large in size, with most being over two feet long. The largest monkey, the mandrill, is an Old World monkey.", "Old World monkeys have wider noses with the nostrils located closer to each other and pointing downwards – much like our noses. Old World monkeys have longer tails than apes, but shorter tails than New World monkeys. Their tails are never prehensile.", "Male Old World monkeys and some females can have several mates at a time. When the baby is born, the female takes care of it. If it is a daughter, it will stay with her for the rest of her life, but if it is a son, there is a chance that it will leave in order to establish its own territory and start its own troop.", "Monkeys are superior to humans :smirk:", "Unlike New World monkeys, Old World monkeys have opposable thumbs. This means that they can move their thumb forward and backward and touch their other fingers with it, just like we can. They also have nails on all of their fingers and toes.", "Monkeys belong to the order of mammals called primates. Humans also belong to this order, along with apes, tarsiers, lorises, and lemurs.", "Monkeys often live in groups. A group of monkeys is called a troop, which can consist of up to 500 individuals. Some troops come together to form larger groups called tribes.", "Baby monkeys are called infants, just like human babies. Like human babies, they are born with their eyes closed and without any teeth. They are quite helpless, which is why they cling to their mother’s belly during the first few weeks of life.", "Monkeys communicate in various ways. They make different sounds like screeches and hoots in order to alert others to danger and to keep other monkeys away from their territory. They can also use body language. For example, they bob their heads to show that they are angry, or smack their lips to show that they are happy.", "A monkey’s average day is spent looking for food, eating, resting or sleeping, and grooming. Grooming is not just a way for monkeys to keep each other clean, but also to strengthen their bonds.", "Monkeys are omnivorous, meaning they eat both plants and other animals. They prefer to eat plants, though–specifically fruits, leaves, and nuts, while eating insects, bird eggs, spiders, snails, and lizards on occasion.", "The average lifespan of a monkey depends on its species. Some monkeys live for only ten years, while others can live for up to fifty years.", "Monkeys are classified into two types – New World monkeys and Old World monkeys. New World monkeys can be found mostly in Central and South America.", "New World monkeys tend to be smaller than Old World monkeys. In fact, most New World monkeys are less than two feet long.", "New World monkeys have noses that are flat and narrow, with nostrils pointing toward the sides. The name of their superfamily, Platyrrhini, means ‘flat-nosed’.", "New World monkeys have long tails that can grow almost as long as their bodies and are sometimes prehensile. Prehensile means that the tail is able to grasp objects like tree branches or leaves.", "When it comes to breeding, most New World monkeys have only one mate at a time. When the baby monkey is born, both the male and female monkey care of it until it is old enough to take care of itself.", "Most New World monkeys have claw-like nails called tegulae, which are only present on a few fingers and toes. They are used to grip tree branches. Old World monkeys, in contrast, have blunt nails called ungulae.", "Old World monkeys can be found in Asia and Africa. Some of them are arboreal, living mostly in trees, while others are terrestrial, spending most of their life on the ground.", "Old World monkeys range from medium to large in size, with most being over two feet long. The largest monkey, the mandrill, is an Old World monkey.", "Old World monkeys have wider noses with the nostrils located closer to each other and pointing downwards – much like our noses. Old World monkeys have longer tails than apes, but shorter tails than New World monkeys. Their tails are never prehensile.", "Male Old World monkeys and some females can have several mates at a time. When the baby is born, the female takes care of it. If it is a daughter, it will stay with her for the rest of her life, but if it is a son, there is a chance that it will leave in order to establish its own territory and start its own troop.", "Unlike New World monkeys, Old World monkeys have opposable thumbs. This means that they can move their thumb forward and backward and touch their other fingers with it, just like we can. They also have nails on all of their fingers and toes.", "Cheek pouches are another trait Old World monkeys have that New World monkeys do not. They can make their cheeks larger, like hamsters, in order to store food for them to eat later.", "Some Old World monkeys have distinct ischial callosities. This means that they have a hairless rump which is covered with small bumps. This is particularly prominent in the baboon, and has been making children point and laugh for hundreds of years!", "Baboons are the most terrestrial monkeys, which means, they spend more time on the ground than any other monkey. They are able to climb trees, though, especially when they can’t outrun an enemy.", "Baboons are some of the largest monkeys. Because of their size, baboons will prey on smaller animals, even smaller monkeys. They are even willing to fight leopards if a leopard threatens their young.", "Infanticide – the killing of the young – is common among baboons, particularly among chacma baboons. Interestingly, though, chacma baboons are also more open to adopting orphaned young.", "Hamadryas baboons, which are found in North Africa, were sacred to the ancient Egyptians. They were associated with the god Thoth, who helped maintain the order of the universe, sorted out quarrels between other gods, and judged the dead.", "Male Hamadryas baboons can be easily distinguished from the females, not just because they are twice as large, but because they have silvery white fur, as well as a mane and a mantle. Females are light brown, while infants are a dark shade of brown, only becoming lighter with age", "The bald uakari gets its name from its hairless head and face – a contrast to the rest of its body, which is covered in thick white, brown, or reddish fur. Its face appears scarlet red, as a result of the lack of skin pigment and the abundance of blood vessels just below the skin.", "The bald uakari’s red face is actually an indication of its health. The redder the face – the healthier the monkey. This plays an important role when it comes to mating, since females only mate with healthy males who, in turn, can give them healthy offspring.", "Bald uakaris have a powerful lower jaw, which allows them to open nuts and unripe fruits with their mouths. It is no wonder, then, that their diet consists mostly of seeds, nuts, and fruits.", "The Barbary macaque is the only monkey that can be found in Europe, and the only macaque that can be found outside Asia. Over two hundred of them can be found on the island of Gibraltar, near Spain, where they are a popular attraction.", "Male Barbary macaques are known for the outstanding care they give to their young. Whereas other male monkeys spend only a little time caring for their young, or none at all, male Barbary macaques spend a lot of time grooming their young and watching over them.", "Capuchin monkeys get their name from the patch of hair on their heads that resembles the hood Capuchin monks wore. They are considered one of the most intelligent New World monkeys, since they have been observed to use tools frequently.", "The cotton-top tamarin is one of the smallest monkeys, weighing only about a pound, and never growing much more than ten inches or about the length of a woman’s foot.", "The cotton-top tamarin is named for its white crest. It also has fine white hairs on its face, but these are so fine that they are difficult to see, making the cotton-top tamarin’s face look hairless. It is different from other New World monkeys in that it has only four molars – the grinding teeth at the back of the mouth – instead of six.", "Cotton-top tamarins also have a unique social structure. Like other monkeys, they live in groups, but their groups are led by a dominant male and female. The dominant pair are the only ones allowed to breed. The female gives birth to about four infants a year and they are cared for by the rest of the group.", "Currently, the cotton-top monkey is listed as a Critically Endangered species and in fact, is numbered among the world’s 25 most endangered primates, with only about 6,000 remaining in the wild.", "Crab-eating macaques are so named because in Indonesia they are often seen diving into the water in search of crabs. They do not eat just crabs, though, but eat just about anything from fruits and seeds to birds, small mammals, and insects.", "In Thailand, crab-eating macaques have been observed to use tools. They use stones to open nuts and oysters, and wash fruits before eating them.", "Like rhesus monkeys, crab-eating macaques are also extensively used in medical experiments, and have been used as space test flight animals. This is because they share many physical similarities with humans and so can be afflicted with the same infections.", "Douc monkeys are monkeys native to Southeast Asia. They are known for having legs that are a different color from the rest of their bodies. Red-shanked doucs, for example, have bright maroon legs.", "The gray-shanked douc monkey is one of the most endangered monkeys in the world, and can be found only in Vietnam. It has a population of less than 700 animals.", "Gee’s golden langur is a monkey found in India which has long been considered sacred by the people of the Himalayas. Adult males have beautiful golden fur, while females and juveniles have silvery white fur.", "Gee’s golden langur takes its name from its vibrant fur and the explorer, E.P. Gee. Gee was a British tea planter living in India who, after hearing reports of an unusually colored primate in the area of Assam, organized an expedition to find the animal and observe it. Three years later, Gee’s golden langur was announced as a new species.", "The golden lion tamarin or golden marmoset also gets its name from its bright golden fur. Scientists believe its color may come from sunlight reacting with the plants it eats.", "At night, golden lion tamarins sleep together in groups in trees, preferring those that are 11 to 15 meters off the ground. They are known to use the same sleeping site over and over, which unfortunately, makes them easy to find for predators such as birds of prey, snakes, pumas and jaguars.", "Geladas, or gelada baboons, eat mostly grass. They have small fingers that are built for pulling grass out, and small, narrow teeth made for chewing it.", "Geladas have an hourglass-shaped patch on their chests, which is a brighter shade of red in males. When a female is ready to breed, her patch becomes covered in blisters, making it more noticeable and an invitation to the males of the group.", "Adult geladas are covered in dark brown hair, but infants are completely black. At birth, a gelada infant weighs less than 500 grams. Its mother keeps it close for the first few weeks to keep it safe, both from predators and from other females in the group who might kidnap it!", "Howler monkeys are the loudest land animals, their deep howls can be heard up to three miles away. These howls are usually made at dawn and dusk to warn other animals to stay out of their territory.", "Of all the New World monkeys, howler monkeys are the only exclusive folivores, which means they eat only leaves. They are careful not to eat too many of the same kind of leaf in one sitting, though, to avoid getting poisoned.", "Howler monkeys have a very keen sense of smell. In fact, they can smell food from over a mile away.", "The Mayans had a pair of howler monkey gods that were revered as gods of the arts. Statues of them have been found in Copan, a Mayan archaeological site in Honduras.", "Apart from howling, mantled howler monkeys use certain gestures to communicate. For example, females smack their lips or stick out their tongues to let males know they are ready to breed, while the young ones shake branches to show that they want to play.", "Black howler monkeys are quite lazy, resting or sleeping for more than sixteen hours each day. They stay in trees and hardly come down, even to drink, since they get their water from the leaves they eat. During rainy season, they rub their hands with the wet leaves and then lick the water off their hands.", "Japanese macaques are native to Japan and are sometimes called snow monkeys. They are often found in Japan’s colder areas, with their thick fur meaning they are well-adapted to temperatures that can dip to twenty degrees Celsius below zero.", "Female Japanese macaques spend more time in the trees, while the males spend more time on the ground. They are good leapers and are also good swimmers, able to swim up to half a kilometer.", "Japanese macaques have been observed to be very intelligent–washing their food before eating, and even dipping it into salty sea water for seasoning. They are also very playful, bathing in hot springs, and even rolling snowballs to throw during winter.", "Mandrills are among the largest monkeys. The males weigh about thirty-two kg (seventy pounds) on average and can grow up to nearly a meter in length which is about the height of a four year old human.", "More than their size, mandrills are known for their color. Their muzzles are red and blue, their beard yellow, and their bellies white, while their rumps are scarlet, pink, blue, and purple.", "Unlike other monkeys, mandrills mean no harm when they bare their teeth. When they are angry, they stare, bob their heads, and beat the ground while making grunting sounds.", "The proboscis monkey is known for its unusually large nose, with males having even larger ones than females, so large in fact, that they droop past their mouths. The word ‘proboscis’ literally means ‘nose’.", "Proboscis monkeys are also called monyet belanda or orang belanda by the locals, which means, ”Dutch monkey” and ”Dutchman” respectively. The locals thought the monkeys looked like the Dutch colonizers of Indonesia who were considered to have large noses and big bellies!", "Proboscis monkeys live in groups, which can come together to form bands – communicating through various sounds. Male proboscis monkeys make particularly loud noises, all aided of course by their large noses. They honk to announce the status of their group, and also give a special soothing honk to reassure the infants.", "Proboscis monkeys like to stay near the water and spend a lot of time swimming, which is probably why they have developed webbed feet. They are often seen jumping off tree branches into the river, and they can swim underwater, too.", "The pygmy marmoset is the smallest monkey in the world, measuring a maximum of six inches in length and weighing only 100 grams. It is native to the Amazon rainforests.", "Pygmy marmosets spend most of their time up in the trees to avoid predators. To help with this task, they can rotate their head up to 180 degrees while perched on a tree branch.", "Pygmy marmosets have teeth and stomachs specially made for chewing tree gum, which makes up the bulk of their diet.", "Pygmy marmosets usually give birth to twins. Unlike most monkeys, the male monkey is the one who carries the infants on his back, not the female.", "The first monkeys to return to Earth after traveling in space were Able, a rhesus monkey, and Miss Baker, a squirrel monkey. They returned to Earth on May 28, 1959 aboard the Jupiter AM-18."]
     fact = random.choice(facts)
     await ctx.send(fact)

@client.command()
async def dare(ctx):
   async with ctx.channel.typing():
     facts = ["Do a free-style rap for the 30 seconds", "Let another person post a status on your behalf.", "Screen share your phone and let another member send a single text saying anything they want to anyone they want.", "Let the other members go through your phone for one minute.", "Do an impression of another player until someone can figure out who it is.", "Imitate a YouTube star until another player guesses who you're portraying.", "Say `monke` at the end of every sentence you say until it's your turn again", "Call a friend or significant other and pretend it's their birthday, and sing them Happy Birthday to them.", "Repeat everything the member listed above your username says until your next turn.", "Show the most embarrassing photo on your phone", "Show the last five people you texted and what the messages said", "Let the group look in your Discord DMs", "Show us your screen time report", "Yell out the first word that comes to your mind", "Say two honest things about everyone else in the group", "Post the oldest selfie on your phone", "Post the first sentence that pops up in your head and then put it out of context", "Give a personalised insult to one person in the VC", "Go on a walk around your block/area and turn on face cam while doing it", "Rate everyone in the VC 1-10 in terms of personality.", "Sing the Chorus of Never Gonna Give you Up", "Sing a song but the group decides", "Make an anime noise", "Group decides 1 video you must watch", "Watch the GrubHub ad\nhttps://youtu.be/G-T3qKl6y-c", "Show everyone here your last 10 google searches.", "unfriend someone on your friend's list", "How would you describe everyone here in 1 sentence to a stranger?", "Show the funniest picture on your camera roll.", "Send a text to your crush explaining your favorite movie plot in vivid detail.", "Turn on your face cam for the rest of the round", "Call the first person on your contacts and hold a conversation for a minute", "Let the group look through your phone for 1 minute", "You have 10 seconds to right at least 3 lines of poetry", "List your top 5 favorite members on the server", "Send something in chat and make at least 1 person laugh", "Rickroll the 5th person in your dms", "For the rest of the game the group decides your discord status", "Tell a dirty joke.", "Send your partner a fake break up message.", "Show everyone the recent picture in your camera roll.", "Do an impression of a character the group decides"]
     fact = random.choice(facts)
     await ctx.send(fact)


@client.command()
async def truth(ctx):
   async with ctx.channel.typing():
     facts = ["If you could be invisible, what is the first thing you would do?", "What is a secret you kept from your parents?", "What is the most embarrassing music you listen to?", "What is one thing you wish you could change about yourself?", "Who is your secret crush?", "If a genie granted you three wishes, what would you ask for?", "What is your biggest regret?", "Where is the weirdest place you've ever gone to the bathroom?", "Which member would survive a zombie apocalypse and which would be the first to go?", "What excuse have you used before to get out plans with a friend?", "Read the last thing you sent your best friend or significant other out loud.", "What is the most embarassing pickup line you've ever used?", "What's your biggest fear?", "What person do you text the most?", "If you could kill one membr in the server who would it be? Why?", "What's the strangest dream you've ever had?", "What is your biggest insecurity?", "What's your biggest fear?", "Whats the worst thing you've ever done?", "What's a secret you've never told anyone?", "Have you ever cheated in an exam or test?", "Have you ever stayed friends with someone because it benefitted you beyond just the friendship?", "What's one thing you hate people knowing about you?", "What's the worst thing anyone's ever done to you?", "What's the worst thing you've ever said to anyone?", "Do you have dreams about being a furry?", "What have you purchased that's been the biggest waste of money?", " What scene from a video game made you the most emotional", "What is child trauma", "If you could only watch one movie for your whole life, what movie would you choose?", "Whats your faviorte book", "Out of everyone in the VC, who do you think would most likely do drugs", "Whats your favorite band/singer", "Show the list of people in your DMs.", "What TV channel did you grow up watching?", "Show everyone your suggested emoji list", "What is your favorite Disney movie?", "If you had to kill 1 person here who would it be?", "What’s 1 trait you find super unattractive?", "Who would you sacrifice your life for on this server?", "Have you ever had a near death experience?", "If you could meet one online friend on this server (not including people you know in real life or your relationship partners) who would it be?", "How many people have you dated?", "What is your favorite color?", "How many pets do you have?"]
     fact = random.choice(facts)
     await ctx.send(fact)


@client.command()
async def diceroll(ctx):
   async with ctx.channel.typing():
     facts = ["You rolled a 1!", "You rolled a 2!", "You rolled a 3!", "You rolled a 4!", "You rolled a 5!", "You rolled a 6!"]
     fact = random.choice(facts)
     await ctx.send(fact)


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        'It is certain.',
        'As I see it, yes.',
        'Reply hazy, try again.',
        "Don't count on it.",
        'It is decidedly so.',
        'Most likely.',
        'Ask again later.',
        'My reply is no.',
        'Without a doubt.',
        'Outlook good.',
        'Better not tell you now.',
        'My sources say no.',
        'Yes – definitely.',
        'Yes.',
        'Cannot predict now.',
        'Outlook not so good.',
        'You may rely on it.',
        'Signs point to yes.',
        'Concentrate and ask again.',
        'Very doubtful.',
    ]
    embed = discord.Embed(
        title="Magic 8 Ball",
        colour=0x738d60,
        description=f'Question: {question}\nAnswer: {random.choice(responses)}')
    await ctx.send(embed=embed)


@client.command()
async def rps(ctx, *, choice):
    choices = ["rock", "paper", "scissors"]
    if choice.lower() not in choices:
        return await ctx.send("LOL you suck, Say rock, paper, or scissors instead")
    else:
        embed = discord.Embed(
            title="Rock, Paper, Scissors",
            colour=0x738d60,
            description=f'Your Move: {choice}\nMy Move: {random.choice(choices)}'
        )
        await ctx.send(embed=embed)


@client.command()
async def say(ctx, *, sentence=None):
    if sentence is None:
        return
    await ctx.send(sentence)
    await ctx.message.delete()

@client.command()
async def flip(ctx, *, choice):
    choices = ["heads", "tails"]
    if choice.lower() not in choices:
        return await ctx.send("LMAO get rekt, Say heads or tails instead")
    else:
        embed = discord.Embed(
            colour=0x738d60,
            description=f'You bet: {choice}\nYou flipped: {random.choice(choices)}')
        await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=26):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=['mr'])
async def rate(ctx):
    rate = random.choice(range(100))
    if ctx.author.id == 812078408091566081:
        return await ctx.send(f"Error! You are to much monke I can't process it")
    if ctx.author.id == 717524326458458113:
        return await ctx.send(f"You are 99% Monke")
    embed = discord.Embed(
        title="Monki Rate",
        colour=0x738d60,
        description=f"You are {rate}% Monki")
    await ctx.send(embed=embed)

client.add_cog(Economy(client))
client.add_cog(Newsletter(client))
client.add_cog(Fun(client))


client.run("BOT TOKEN")
