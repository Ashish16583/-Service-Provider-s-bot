id="help001"
import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="commands")
    async def commands_list(self, ctx):

        embed = discord.Embed(
            title="📜 Active Commands List",
            description="Only working commands on this bot",
            color=0x00ffcc
        )

        # ======================
        # MODERATION
        # ======================
        moderation = []

        for cmd in self.bot.commands:
            if cmd.cog_name and "moderation" in cmd.cog_name.lower():
                moderation.append(f".{cmd.name}")

        if moderation:
            embed.add_field(
                name="🛡️ Moderation",
                value="\n".join(moderation[:15]) or "No commands",
                inline=False
            )

        # ======================
        # ECONOMY
        # ======================
        economy = []

        for cmd in self.bot.commands:
            if cmd.cog_name and "economy" in cmd.cog_name.lower():
                economy.append(f".{cmd.name}")

        if economy:
            embed.add_field(
                name="💰 Economy",
                value="\n".join(economy[:15]) or "No commands",
                inline=False
            )

        # ======================
        # TICKETS
        # ======================
        tickets = []

        for cmd in self.bot.commands:
            if cmd.cog_name and "ticket" in cmd.cog_name.lower():
                tickets.append(f".{cmd.name}")

        if tickets:
            embed.add_field(
                name="🎫 Tickets",
                value="\n".join(tickets[:15]) or "No commands",
                inline=False
            )

        # ======================
        # ANNOUNCEMENTS / UTILITY
        # ======================
        utility = []

        for cmd in self.bot.commands:
            if cmd.cog_name and (
                "utility" in cmd.cog_name.lower() or
                "announcement" in cmd.cog_name.lower()
            ):
                utility.append(f".{cmd.name}")

        if utility:
            embed.add_field(
                name="📢 Utility",
                value="\n".join(utility[:15]) or "No commands",
                inline=False
            )

        embed.set_footer(text="Service Provider’s Bot • Auto Command List")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
