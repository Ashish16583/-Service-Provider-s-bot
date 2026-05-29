import discord
from discord.ext import commands

LOG_CHANNEL = 1509471190677196851

class Logs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def send_log(self, guild, embed):

        channel = guild.get_channel(LOG_CHANNEL)

        if channel:
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        embed = discord.Embed(
            title="🗑️ Message Deleted",
            description=message.content,
            color=0xED4245
        )

        await self.send_log(
            message.guild,
            embed
        )

async def setup(bot):
    await bot.add_cog(Logs(bot))

