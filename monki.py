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

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.members = True

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
        activity=discord.Activity(name=f"{len(client.guilds)} monkey tribes | m+help", type=3),
    )
    print(f'Bot is running as "{client.user}"')
    print("=========================================")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    embed = discord.Embed(
        title="Oops, an error occured!",
        colour=0x1f8b4c,
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
        "balance": 0
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
        colour=0x1f8b4c,
        description=f"{error}",
    )
    embed.set_image(url="https://imgur.com/iPm0Fst.gif")
    await ctx.send(embed=embed)
    print(error)


@client.command()
async def help(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="**Help**",
            colour=0x1f8b4c,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="**:coin:Economy**",
            inline=False,
            value=f"`{ctx.prefix}economy` | A list of my Economy features ",
        )
        embed.add_field(
            name="**:musical_note:Music**",
            inline=False,
            value=f"`{ctx.prefix}music` | COMING SOON ",
        )
        embed.add_field(
            name="**:park:Gifs**",
            inline=False,
            value=f"`{ctx.prefix}gif` | A list of my Gifs ",
        )
        embed.add_field(
            name="**:red_circle:Live Footage**",
            inline=False,
            value=f"`{ctx.prefix}live` | A list of my Live Footage features ",
        )
        embed.add_field(
            name="**:tools:Utility**",
            inline=False,
            value=f"`{ctx.prefix}utility` | A list of my Utility commands ",
        )
        embed.add_field(
            name="**:rofl:Fun**",
            inline=False,
            value=f"`{ctx.prefix}fun` | A list of my Fun features ",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon... ",
        )
    await ctx.send(embed=embed)


@client.command()
async def economy(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x1f8b4c,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Economy ",
            inline=False,
            value=f"`{ctx.prefix}daily` - get 50 daily bananas\n `{ctx.prefix}search` - search for bananas\n`{ctx.prefix}steal" 
            f"<species>` - steal from a monkey\n`{ctx.prefix}bal` - see your balance ",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@client.command()
async def music(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x1f8b4c,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Music ",
            inline=False,
            value=f"`{ctx.prefix}play <link>` - COMING SOON\n`{ctx.prefix}stop` "
            f"- COMING SOON\n`{ctx.prefix}queue` - COMING SOON ",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@client.command()
async def gifs(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x1f8b4c,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Gifs",
            inline=False,
            value=f"`{ctx.prefix}taunt`\n`{ctx.prefix}hug`\n`{ctx.prefix}kiss` "
            f"\n`{ctx.prefix}flirt`\n`{ctx.prefix}shoot`\n`{ctx.prefix}slap` "
            f"\n`{ctx.prefix}dominate`\n`{ctx.prefix}flex`\n`{ctx.prefix}snipe` ",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@client.command()
async def gif(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x1f8b4c,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Gifs",
            inline=False,
            value=f"`{ctx.prefix}taunt`\n`{ctx.prefix}hug`\n`{ctx.prefix}kiss` "
            f"\n`{ctx.prefix}flirt`\n`{ctx.prefix}shoot`\n`{ctx.prefix}slap` "
            f"\n`{ctx.prefix}dominate`\n`{ctx.prefix}flex`\n`{ctx.prefix}snipe` ",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@client.command()
async def live(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x1f8b4c,
            description="Here is a list of commands you can use: ",
        )
        embed.add_field(
            name="Live Footage",
            inline=False,
            value=f"`{ctx.prefix}liveSD`\n`{ctx.prefix}liveBS`\n`{ctx.prefix}liveDET`\n`{ctx.prefix}liveHOU`\n`{ctx.prefix}liveKC` ",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@client.command()
async def utility(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x1f8b4c,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Utility",
            inline=False,
            value=f"\n`{ctx.prefix}ban`\n`{ctx.prefix}unban`\n`{ctx.prefix}clear`\n`{ctx.prefix}membercount`\n`{ctx.prefix}updates`\n`{ctx.prefix}support`\n`{ctx.prefix}clear` ",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)


@client.command()
async def fun(ctx):
    async with ctx.channel.typing():
        embed = discord.Embed(
            title="Help",
            colour=0x1f8b4c,
            description="Here is a list of commands you can use:",
        )
        embed.add_field(
            name="Fun",
            inline=False,
            value=f"\n`{ctx.prefix}monkirate` - Shows how close you are to monkey\n`{ctx.prefix}fact` - Posts a random monkey fact"
            f"\n`{ctx.prefix}rate <subject>` - give a rating out of 10 how good something or someone"
            f"\n`{ctx.prefix}truth` - Tells you a question that you must answer\n`{ctx.prefix}dare` - Tells you a dare that you must complete"
            f"\n`{ctx.prefix}8ball <yes or no question>` - Just like a magic 8ball! Tells you the future"
            f"\n`{ctx.prefix}monkeymeme` - Posts the most upvoted monkey meme on reddit!",
        )
        embed.add_field(
            name="\u200b", inline=False, value="More commands coming soon..."
        )
    await ctx.send(embed=embed)

  
@client.event
async def on_guild_join(guild):
    channel = guild.system_channel
    embed = discord.Embed(
        colour=0x1f8b4c,
        description="""Hello! Thanks for adding me!
        Ultimate Monki is a multipurpose Discord Bot that was specifically made for monkey themed discord servers!
        
        There are a lot of things you can do with Ultimate Monki, simply use the `m+help` command to see a list of commands you can use.
        """,
    )
    embed.add_field(
        name="**__Usefull Links__**",
        inline=False,
        value="""
    Consider voting on **[Ultimate Monki](https://top.gg/bot/787887645879435284/vote)** on Top.gg
    Have an bug or suggestion? Join the **[Support Server](https://discord.gg/sg25dQ6E3U)**
    """,
    )
    await channel.send(embed=embed)



@client.command()
async def liveSD(ctx):
    embed = discord.Embed(
        title="San Diego Zoo (Live Cam)",
        colour=0x1f8b4c,
        description="[San Diego Zoo Global](https://zoo.sandiegozoo.org/cams/ape-cam) is committed to saving species worldwide by uniting our expertise in animal care and conservation science with our dedication to inspiring passion for nature.",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveKC(ctx):
    embed = discord.Embed(
        title="Kansas City Zoo (Live Cam)",
        colour=0x1f8b4c,
        description="One of two subspecies of orangutan, Bornean orangutans are found natively on the island of Borneo. As frugivores, their diet includes over 400 types of fruit in the wild and they are important movers of seeds, passing them through their digestive system. You can find our group of six at Orangutan Canopy.\nhttps://www.kansascityzoo.org/animal-cam/orangutan-camera",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveDET(ctx):
    embed = discord.Embed(
        title="Detroit Zoo (Live Cam)",
        colour=0x1f8b4c,
        description="""The Japanese macaque habitat is home to six females and three males, whose social structure is built around lineage.
NOTE: This live stream will be active from 11:30 a.m. to 9:00 p.m. daily.
https://detroitzoo.org/snow-monkey-live-cam/""",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveHOU(ctx):
    embed = discord.Embed(
        title="Houston Zoo (Live Cam)",
        colour=0x1f8b4c,
        description="What’s going on in the chimpanzee habitat at the Houston Zoo right now? Find out with our live webcam below.\nCAMERA HOURS: LIVE FEED FROM 7 A.M. – 7 P.M. CST\nhttps://www.houstonzoo.org/explore/webcams/chimpanzee-cam/",
    )
    await ctx.send(embed=embed)


@client.command()
async def liveBS(ctx):
    embed = discord.Embed(
        title="Spider Monkey Cam",
        colour=0x1f8b4c,
        description="Camera Hours: Live Feed from 8:30AM-6:00PM\nPlease note that our animals are constantly on the move and may not always be visible on camera.\nhttps://www.beardsleyzoo.org/outdoor-spider-monkey-cam.html",
    )
    await ctx.send(embed=embed)


@client.command()
async def support(ctx):
    await ctx.send("https://discord.gg/sg25dQ6E3U")
    
    
@client.command()
async def invite(ctx):
    await ctx.send("https://discord.com/api/oauth2/authorize?client_id=787887645879435284&permissions=8&scope=bot")


@client.command()
async def updates(ctx):
    await ctx.send("**Currently working on music commands and welcome messages**")


@client.command()
async def taunt(ctx):
    await ctx.send("https://tenor.com/view/baboon-monkey-butt-slap-mock-gif-5498401")
  

@client.command()
async def hug(ctx):
    await ctx.send("https://tenor.com/view/monkey-hug-gif-7828637")
  

@client.command()
async def kiss(ctx):
    await ctx.send("https://tenor.com/view/monke-love-monkey-love-love-loves-kisses-gif-20204998")
  

@client.command()
async def flirt(ctx):
    await ctx.send("https://tenor.com/view/monkey-cool-hip-gif-7966528")
    

@client.command()
async def shoot(ctx):
    await ctx.send("https://tenor.com/view/planet-of-the-apes-monkey-gun-shooting-gif-17888605")
   

@client.command()
async def slap(ctx):
    await ctx.send("https://tenor.com/view/monkey-slap-annoy-lion-joke-gif-11793252")
   

@client.command()
async def dominate(ctx):
    await ctx.send("https://tenor.com/view/monkey-not-me-gif-13117917")
    

@client.command()
async def flex(ctx):
    await ctx.send("https://tenor.com/view/monkey-with-money-happy-withmoney-swag-dollars-more-money-gif-14116367")
    

@client.command()
async def snipe(ctx):
    await ctx.send("https://tenor.com/view/sniper-monkey-funny-monke-funny-kill-gif-20219406")
    

@client.command()
async def vote(ctx):
    await ctx.send(":heart:Thank you for voting :heart:!! https://top.gg/bot/787887645879435284/vote")
    

# @client.command()
# async def function(ctx):
#     embed = discord.Embed(
#         title="",
#         colour=0x1f8b4c,
#         description="",
#     )
#     await ctx.send(embed=embed)


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
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embed = discord.Embed(
                title="Banned",
                description=f'{user.mention} has been unbanned.')
            await ctx.send(embed=embed)
            return


@client.command()
async def membercount(ctx):
    embed = discord.Embed(
        colour=0x1f8b4c,
        title="Member Count",
        description=f"There are {len(ctx.guild.members)} members in this server") 
    await ctx.send(embed=embed)

    
@client.command()
async def fact(ctx):
   async with ctx.channel.typing():
     facts = ["Monkeys can understand written numbers and can even count. They can also understand basic parts of arithmetic and even, in rare cases, multiplication.", "To attract a female partner, male capuchin monkeys will urinate in their hands and then rub it thoroughly into their fur.", "The origins of the word monkey are unclear. It appears also to be related to manikin, from the Dutch manneken (little man). It could also be derived from the name of a popular medieval beast story  in which the son of an ape is named Moneke.", "A Colombian woman claimed that she was raised by a colony of capuchin monkeys after being kidnapped and abandoned in the jungle when she was just 4 years old.", "Raw and cooked brain of dead monkey is widely consumed in China and Malaysia.", "Scientists observed female monkeys teaching their young how to floss their teeth.", "The smallest monkey in the world is the pygmy marmoset, with a body as little as 5 inches (12 cm) and a tail length of about 7 inches (17 cm). As a comparison, they are about the size of a hamster, can fit in the palm of a human hand, and they weigh the same as a pack of cards.", "The most recently discovered monkey is the lesula monkey. It was discovered in 2007 in the Democratic Republic of the Congo in Africa.", "Diseases that can spread from monkey to humans include Ebola Reston, B virus (Cercopithecine herpesvirus 1), monkey pox, yellow fever, simian immunodeficiency virus, tuberculosis, and other diseases not yet known or identified.", "Uncle Fat is a morbidly obese monkey in Thailand who gorged himself on junk food and soda that tourists had left behind. As the leader of his troop, this gluttonous monkey also had subordinate monkeys bringing him goodies.", "Apes, gibbons, lemurs, and chimpanzees are not scientifically classified as monkeys. They are all primates, but, like humans, they have a different classification to monkeys.", "An abandoned medical research facility called the New York Blood Center used wild chimpanzees in its vaccination research in the 1970s. When the research facility shut down in 2005, the 66 remaining chimps were set free on a small land mass soon dubbed Monkey Island.", "At the tip of a monkey's tail is a patch of bare skin that acts similar to a human's fingertips. It is sensitive to touch and also has tiny ridges that gives the tail a better grip.", "In Hindu, Hanuman (disfigured jaw) is a human-like monkey god who commanded a monkey army. Interestingly, women were not allowed to worship the monkey god", "Monkeys are superior to Humans >:)", "Monkeys that live in Central and South America are called New World monkeys. Monkeys that live in Africa and Asia are called Old World monkeys", "Contrary to popular opinion, humans did not come from monkeys. Rather, humans and monkeys share a common ancestor 25-30 million years ago and then evolved from this animal in various different ways.", "Old World Monkeys have narrow noses that point down, don't hang in trees, are larger, don't have prehensile tails, and have strange sitting pads on their bottoms. New World monkeys have flatter noses, live in trees, and have prehensile tails.", "The female spider monkey has the longest tail of all the primates. Even though its body is only 2 feet long, its tail can reach 3 feet in length. Their tails can carry the the monkey's entire body weight and even pick up items as small as peanut.", "Mandrill monkeys have fangs that are longer than a lion's fangs. They also have multi-colored bottoms which makes them easier to see in the leafy gloom of the forest.", "The fastest primate on Earth is the patas monkey. It can reach speeds of 34 miles per hour (55 km/h)", "The uakari is one of the rarest and most unusual-looking of all the New World monkeys. While it looks similar to an orangutan, its face is pink, which often turns bright red when the animal becomes excited or angry. It also makes a noise similar to a human laughing.", "While monkeys and apes are related, they are very different from each other. Monkeys have tails, have snouts, and they are not as intelligent as apes. Additionally, apes are not found in North or South America or Europe, while monkeys are.", "The owl monkey (night monkey) is the only nocturnal New World monkey. They are also one of the few monkey species affected by malaria, which means they have been used in non-human primate malaria experiments.", "Africa's Namib Desert is home to the chacma baboons. One hardy chacma baboon troop survived 116 days without water in the desert by eating figs.", "The only wild monkey in Europe is the tailless Barbary macaque, which is found in parts of Northern Africa and the British territory of Gibraltar.", "The first primate in space was a rhesus macaque named Albert. On June 14, 1949, Albert was sent into space to test the effects of space travel on a body. While he survived the flight, he died when the rocket parachute failed.", "The Japanese macaque is the northernmost monkey and is capable of living in more than 3 feet of snow in as temperatures as low as 5 degrees Fahrenheit (-15 degrees Celsius).", "The largest monkey in the world is the male mandrill. It is almost 1 meter (3.3 feet) long and weighs about 35 kilograms (77 pounds).", "The ancient Egyptians considered the Hamadryas Baboon to be sacred. One of their gods, Thoth was regularly drawn as a man with the head of this baboon.", "The monkey is the 9th animal in the Chinese zodiac. People born in a year of the monkey are supposedly intelligent, lively, and creative, but might also be selfish and impatient.", "The capuchin monkey is the most common and the most intelligent of the New World monkeys.", "The spider monkey is the most acrobatic of the New World monkeys, and it has been know to leap across gaps as large as 35 feet.", "Monkeys are found almost everywhere on Earth, except for Australia and Antarctica.", "The Diana monkey was named for the Roman goddess of hunting because the stripe on its forehead resembles Diana bow.", "The male howler monkey has the loudest call of any other primate and is one of the loudest animals in the world. Interestingly, the louder the howler monkey, the smaller its testicles and the lower its sperm count.", "Capuchin monkeys are named after the 16th-century monks because the monkey's hair resembles the monks' hooded robes.", "Monkeys are long-lived, surviving in the wild anywhere between 10 and 50 years.", "Ethiopian geladas form the largest monkey troops in the world, numbering from 350 to 650 individuals.", "Ethiopian geladas form the largest monkey troops in the world, numbering from 350 to 650 individuals.", "Picking out parasites and dirts from each others' furs is a way for monkeys to communicate, form social hierarchies, and strengthen family and friendship bonds.", "Found only in the Chinese province of Yunnan, the black snub-nosed monkey lives at the higest altitudes, near 15,000 feet  (4,572 m) of any primate.", "A group of monkeys is variously called a troop, barrel, carload, cartload, or tribe.", "To identify themselves more easily, squirrel monkeys will smear food on their tails, much like how humans may wear name tags.", "Due to the loss of trees in their native habitat, only about 1,500 golden lion tamarins exist in the wild.", "Each year, about 55,000 primates are used as test animals in the U.S., and about 10,000 are used in Great Britain. Japan uses millions of primates.", "When researchers offered the Japanese macaque sweet potatoes during research in the 1940s, the monkeys didn't like the taste of the dirt on the veggies, so they washed it off. Now, generations later, washing food has become a learned behavior. No other monkeys in the world are known to wash their food before eating.", "HIV was created in the stomach of a chimp who had eaten two different types of monkeys that had two different viruses.  The two viruses combined to form a hybrid virus, which then spread through the chimp species, and then later was transmitted to humans.", "White-faced capuchin monkeys rub their fur with the Giant African Millipedes, which acts as a form of insect repellent.", "On the Yakushima island Japan, monkeys groom and share food with deer in exchange for a ride.", "After weeks of training, rhesus monkeys learned to recognize themselves in a mirror. The first thing they did was to promptly examined their genitals, every intimate nook and cranny.","The 'Monkey Orchid' is a flower that has evolved to look like the grinning face of a monkey. Ironically, instead of smelling like bananas, it smells like a ripe orange.", "Alexander I, the king of Greece, died from sepsis after being bit by one of his pet monkeys. His death led to a war that killed over 100,000 people.", "A recently discovered monkey, the Burmese sneezing monkey, sneezes whenever it rains.", "A group of 15 captive monkeys at a primate research institute in Japan used tree branches to fling themselves over a high voltage electric fence. They were later lured back to the research center with peanuts.", "To prove that children need a mother's love, scientist Harry Harlow subjected baby monkeys to horrific experiments in what was called the The Pit of Despair in which he isolated and tortured baby monkeys.", "The mustached emperor tamarin is believed to have been named for German Emperor Wilhelm II. Both have impressive mustaches.", "French surgeon Serge Voronoff (1866-1951) gained notoriety when he grafted monkey testicles into the the scrotum of human patients in an attempt to cure infertility and increase their sex drive.", "A 22-year-old primate researcher at Emory died after a rhesus monkey infected with the herpes B virus threw a tiny drop of fluid, mostly likely from  urine or feces, at her face as she was transporting the animal.", "Italian Professor Sergio Canavero claimed to have conducted the first monkey head transplant without any neurological injury to the animal. However, he did not connect the spinal cord, so the monkey was completely paralyzed. It was only kept alive for only 20 hours after the procedure for ethical reasons.", "Italian Professor Sergio Canavero claimed to have conducted the first monkey head transplant without any neurological injury to the animal. However, he did not connect the spinal cord, so the monkey was completely paralyzed. It was only kept alive for only 20 hours after the procedure for ethical reasons.", "Monkeys are better than Humans >:)", "Monkeys are better than Humans >:)", "The official way to say Monkey is actually Monke", "When you name yourself with the a name that has Monke, Monki, or Monkey you will get a role ;)"]
     fact = random.choice(facts)
     await ctx.send(fact)

@client.command()
async def dare(ctx):
   async with ctx.channel.typing():
     facts = ["Do a free-style rap for the 30 seconds", "Let another person post a status on your behalf.", "Screen share your phone and let another member send a single text saying anything they want to anyone they want.", "Let the other members go through your phone for one minute.", "Do an impression of another player until someone can figure out who it is.", "Imitate a YouTube star until another player guesses who you're portraying.", "Say `monke` at the end of every sentence you say until it's your turn again", "Call a friend or significant other and pretend it's their birthday, and sing them Happy Birthday to them.", "Repeat everything the member listed above your username says until your next turn.", "Show the most embarrassing photo on your phone", "Show the last five people you texted and what the messages said", "Let the group look in your Discord DMs", "Show us your screen time report", "Yell out the first word that comes to your mind", "Say two honest things about everyone else in the group", "Post the oldest selfie on your phone", "Post the first sentence that pops up in your head and then put it out of context", "Give a personalised insult to one person in the VC"]
     fact = random.choice(facts)
     await ctx.send(fact)


@client.command()
async def truth(ctx):
   async with ctx.channel.typing():
     facts = ["If you could be invisible, what is the first thing you would do?", "What is a secret you kept from your parents?", "What is the most embarrassing music you listen to?", "What is one thing you wish you could change about yourself?", "Who is your secret crush?", "If a genie granted you three wishes, what would you ask for?", "What is your biggest regret?", "Where is the weirdest place you've ever gone to the bathroom?", "Which member would survive a zombie apocalypse and which would be the first to go?", "What excuse have you used before to get out plans with a friend?", "Read the last thing you sent your best friend or significant other out loud.", "What is the most embarassing pickup line you've ever used?", "What's your biggest fear?", "What person do you text the most?", "If you could kill one membr in the server who would it be? Why?", "What's the strangest dream you've ever had?", "What is your biggest insecurity?", "What's your biggest fear?", "Whats the worst thing you've ever done?", "What's a secret you've never told anyone?", "Have you ever cheated in an exam or test?", "Have you ever stayed friends with someone because it benefitted you beyond just the friendship?", "What's one thing you hate people knowing about you?", "What's the worst thing anyone's ever done to you?", "What's the worst thing you've ever said to anyone?", "Do you have dreams about being a furry?", "What have you purchased that's been the biggest waste of money?"]
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
        colour=0x1f8b4c,
        description=f'Question: {question}\nAnswer: {random.choice(responses)}')
    await ctx.send(embed=embed)


@client.command()
async def rate(ctx, *, subject):
    responses = [
        'I rate it a 10/10.',
        'I rate it a 9/10.',
        'I rate it a 8/10.',
        'I rate it a 7/10.',
        'I rate it a 7/10.',
        'I rate it a 6/10.',
        'I rate it a 5/10.',
        'I rate it a 4/10.',
        'I rate it a 3/10.',
        'I rate it a 2/10.',
        'I rate it a 1/10',
    ]
    embed = discord.Embed(
        title="Rate",
        colour=0x1f8b4c,
        description=f'Subject: {subject}\nRate: {random.choice(responses)}')
    await ctx.send(embed=embed)


@client.command()
async def say(ctx, *, sentence):
    embed = discord.Embed(
        title="Rate",
        colour=0x1f8b4c,
        description=f'{sentence}')
    await ctx.send(embed=embed)


@client.command(aliases=['clear10'])
@commands.has_permissions(manage_messages=True)
async def clear_10(ctx, amount=11):
    await ctx.channel.purge(limit=amount)


@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=15):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=['clear30'])
@commands.has_permissions(manage_messages=True)
async def clear_30(ctx, amount=31):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=['clear50'])
@commands.has_permissions(manage_messages=True)
async def clear_50(ctx, amount=51):
    await ctx.channel.purge(limit=amount)


@client.command(aliases=['clear100'])
@commands.has_permissions(manage_messages=True)
async def clear_100(ctx, amount=101):
    await ctx.channel.purge(limit=amount)


@client.command()
async def monkirate(ctx):
    rate = random.choice(range(100))
    if ctx.author.id == 812078408091566081:
        return await ctx.send(f"Error! You are to much monke I can't process it")
    if ctx.author.id == 717524326458458113:
        return await ctx.send(f"You are 99% Monke")
    embed = discord.Embed(
        title="Monki Rate",
        colour=0x1f8b4c,
        description=f"You are {rate}% Monki")
    await ctx.send(embed=embed)

client.add_cog(Economy(client))
# client.add_cog(Commands(client))
client.add_cog(Fun(client))


client.run("BOT TOKEN")
