import discord
from discord.ext import commands
import os

class MemberList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Load your IDs from the .env file
        # We wrap them in int() because IDs must be numbers
        self.welcome_channel_id = int(os.getenv('WELCOME_CHANNEL'))
        self.leave_channel_id = int(os.getenv('LEAVE_CHANNEL'))

    # Use .listener() for events like joining/leaving
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(self.welcome_channel_id)
        if channel:
            await channel.send(f"Welcome to the server {member.mention}!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(self.leave_channel_id)
        if channel:
            await channel.send(f"{member.name} has left the server.")

# This setup function is MANDATORY for every cog file
async def setup(bot):
    await bot.add_cog(MemberList(bot))