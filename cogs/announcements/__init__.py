id="l5wwl5"
from discord.ext import commands

class Temp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Temp(bot))