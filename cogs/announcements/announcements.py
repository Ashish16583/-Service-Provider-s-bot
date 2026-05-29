
import discord
from discord.ext import commands
import asyncio

class Announcements(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scheduleannounce(
        self,
        ctx,
        seconds: int,
        channel: discord.TextChannel,
        *,
        message
    ):

        await ctx.send(
            f"⏳ Announcement scheduled in {seconds}s"
        )

        await asyncio.sleep(seconds)

        embed = discord.Embed(
            title="📢 Scheduled Announcement",
            description=message,
            color=0x00ffcc
        )

        await channel.send("@everyone", embed=embed)

async def setup(bot):
    await bot.add_cog(Announcements(bot))
