# cogs/admin/panel.py
import discord
from discord.ext import commands

OWNER_ID = 1406960430554812508  # change this

class OwnerPanel(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_owner(self, ctx):
        return ctx.author.id == OWNER_ID

    @commands.command()
    async def ownerpanel(self, ctx):

        if not self.is_owner(ctx):
            return await ctx.send("❌ Owner only command")

        embed = discord.Embed(
            title="👑 OWNER CONTROL PANEL",
            description="Server Management System",
            color=0xff0000
        )

        embed.add_field(
            name="🛡️ Safety",
            value=".lockserver\n.unlockserver\n.emergency",
            inline=False
        )

        embed.add_field(
            name="📊 Dashboard",
            value=".health\n.activity\n.roles",
            inline=False
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(OwnerPanel(bot))