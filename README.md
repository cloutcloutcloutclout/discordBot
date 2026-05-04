## Discord bot

Bot features:
- Racism filter
- Join / Leave messages
- Avatar command
- Banking {User Bank}

Coming soon <!>
- Money
- Latency
- Dice roll games -> money -> banking
- Daily commands / time cooldown commands




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
