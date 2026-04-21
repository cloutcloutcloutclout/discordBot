## importing key dependencies

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

## loading token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

## handler + intents
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

## Bot

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} swear is filtered")

    await bot.process_commands(message) ## allows to continue handing message in the server by anyone else << 







bot.run(token, log_handler=handler, log_level=logging.DEBUG)