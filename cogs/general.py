import discord
from discord.ext import commands
import os

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Load blacklist inside the Cog
        # Ensure 'BLACKLIST' is defined in your .env file
        blacklist_env = os.getenv('BLACKLIST', '')
        self.blacklist = blacklist_env.split(',') if blacklist_env else []

    ## Message Events (Filtering)
    @commands.Cog.listener()
    async def on_message(self, message):
        # If author is bot ignore
        if message.author == self.bot.user:
            return
        
        # Racism filter
        content = message.content.lower()
        if any(word in content for word in self.blacklist):
            # Check if word is not just an empty string from .env split
            if content.strip(): 
                await message.delete()
                await message.channel.send(f"{message.author.mention}, racist remarks are blacklisted.")

    ## User Avatar Command
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        # Getting who the member is and url
        member = member or ctx.author
        avatar_url = member.display_avatar.url
        
        # Create Embed
        embed = discord.Embed(
            title=f"{member.name}'s Avatar",
            color=discord.Color.random()
        )
        embed.set_image(url=avatar_url)

        await ctx.send(embed=embed)

# Mandatory setup function for the main.py to load this file
async def setup(bot):
    await bot.add_cog(General(bot))

    