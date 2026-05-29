
import discord
from discord.ext import commands
import asyncio

ALLOWED_USERS = [
    1406960430554812508
]
class RemoteAnnouncements(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def allowed(self, user):
        return user.id in ALLOWED_USERS

    @commands.command()
    async def dm_announce(
        self,
        ctx,
        guild_id: int,
        channel_id: int,
        *,
        message
    ):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return

        guild = self.bot.get_guild(guild_id)

        channel = guild.get_channel(channel_id)

        embed = discord.Embed(
            title="📢 Announcement",
            description=message,
            color=0x00ffcc
        )

        await channel.send("@everyone", embed=embed)

        await ctx.send("✅ Announcement Sent")

    @commands.command()
    async def dm_scheduleannounce(
        self,
        ctx,
        guild_id: int,
        channel_id: int,
        seconds: int,
        *,
        message
    ):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return

        await ctx.send(f"⏳ Scheduled in {seconds}s")

        await asyncio.sleep(seconds)

        guild = self.bot.get_guild(guild_id)

        channel = guild.get_channel(channel_id)

        embed = discord.Embed(
            title="📢 Scheduled Announcement",
            description=message,
            color=0xff0000
        )

        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RemoteAnnouncements(bot))
