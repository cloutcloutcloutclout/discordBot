import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

load_dotenv() ## loading env and token
token = os.getenv('DISCORD_TOKEN')


## bot class and async funcs
class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
    
        super().__init__(command_prefix="$", intents=intents) ## cmd prefix

    async def setup_hook(self):
        # load .py files into cogs folder
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded Cog: {filename}')

    async def on_ready(self):
        print(f"{self.user.name} is online.")



## bot handling / instantiate
bot = Bot()
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

## token
async def main():
    async with bot:
        await bot.start(token)

## name = main running 
if __name__ == '__main__':
    asyncio.run(main())