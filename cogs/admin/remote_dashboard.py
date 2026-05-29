import discord
from discord.ext import commands
import psutil

ALLOWED_USERS = [
    1406960430554812508
]

class RemoteDashboard(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def allowed(self, user):
        return user.id in ALLOWED_USERS

    @commands.command()
    async def dm_dashboard(self, ctx, guild_id: int):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return

        guild = self.bot.get_guild(guild_id)

        online = sum(
            1 for m in guild.members
            if m.status != discord.Status.offline
        )

        embed = discord.Embed(
            title=f"📊 {guild.name}",
            color=0x5865F2
        )

        embed.add_field(
            name="👥 Members",
            value=guild.member_count
        )

        embed.add_field(
            name="🟢 Online",
            value=online
        )

        embed.add_field(
            name="💎 Boosts",
            value=guild.premium_subscription_count
        )

        embed.add_field(
            name="📺 Channels",
            value=len(guild.channels)
        )

        embed.add_field(
            name="🎭 Roles",
            value=len(guild.roles)
        )

        embed.add_field(
            name="💻 CPU",
            value=f"{psutil.cpu_percent()}%"
        )

        embed.add_field(
            name="🧠 RAM",
            value=f"{psutil.virtual_memory().percent}%"
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RemoteDashboard(bot))