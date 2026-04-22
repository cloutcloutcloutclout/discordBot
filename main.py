import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv() ## loading env and token
token = os.getenv('DISCORD_TOKEN')
BLACKLIST = os.getenv('BLACKLIST').split(',') # get racist word filter WORDS

## Channels
WELCOME_CHANNEL = int(os.getenv('WELCOME_CHANNEL'))





handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True ## handler + intents

bot = commands.Bot(command_prefix='$', intents=intents) ## Bot


## bot initialize
@bot.event
async def on_ready():
    print(f"{bot.user.name} is online.")


## if someone joins the server
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL)
    if channel:
        await channel.send(f"Welcome to the server {member.mention}")


## user messaging
@bot.event
async def on_message(message):

    ## if author is bot ignore
    if message.author == bot.user:
        return
    
    # racism filter {progress}
    content = message.content.lower()

    if any(word in content for word in BLACKLIST):
        await message.delete()
        await message.channel.send(f"{message.author.mention}, you are unable to send racist remarks on this server")

    await bot.process_commands(message) ## allows to continue handing message in the server by anyone else << 

## Users avatar
@bot.command()
async def avatar(ctx, member: discord.Member = None):
    ## getting who the member is and url
    member = member or ctx.author
    avatar_url = member.display_avatar.url
    ## embed
    embed = discord.Embed(
        title=f"{member.name}'s Avatar,",
        color=discord.Color.random()
    )

    embed.set_image(url=avatar_url)

    await ctx.send(embed=embed)









bot.run(token, log_handler=handler, log_level=logging.DEBUG)