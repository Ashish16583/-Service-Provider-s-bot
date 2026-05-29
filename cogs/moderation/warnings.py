id="y21axu"
from discord.ext import commands

class Warnings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Warnings(bot))

