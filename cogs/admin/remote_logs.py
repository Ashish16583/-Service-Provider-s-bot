import discord
from discord.ext import commands
import datetime

LOG_CHANNEL_NAME = "remote-logs"

class RemoteLogs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def send_log(self, guild, user, action, target):

        log_channel = discord.utils.get(
            guild.text_channels,
            name=LOG_CHANNEL_NAME
        )

        if not log_channel:
            return

        embed = discord.Embed(
            title="📩 Remote Action Log",
            color=0xff0000,
            timestamp=datetime.datetime.utcnow()
        )

        embed.add_field(
            name="👤 User",
            value=str(user),
            inline=False
        )

        embed.add_field(
            name="⚡ Action",
            value=action,
            inline=False
        )

        embed.add_field(
            name="🎯 Target",
            value=target,
            inline=False
        )

        await log_channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RemoteLogs(bot))
