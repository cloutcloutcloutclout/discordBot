## Discord bot

Just a random bot with:

- Money
- Join message
- Chat filter

More features soon <!>




### Notes

#### Quick Cog Syntax Guide
Command Decorators
@bot.command()  —>  @commands.command()

Event Listeners
@bot.event  —>  @commands.Cog.listener()

Function Definitions
async def setup(ctx):  —>  async def setup(self, ctx):

Bot References
bot.user  —>  self.bot.user

Variable Storage
points = 0  —>  self.points = 0
