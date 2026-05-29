import discord
from discord.ext import commands

ALLOWED_USERS = [ 1406960430554812508
]

class RemoteTickets(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def allowed(self, user):
        return user.id in ALLOWED_USERS

    # =========================
    # 🎫 CLOSE TICKET
    # =========================
    @commands.command()
    async def dm_closeticket(self, ctx, channel_id: int):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        channel = self.bot.get_channel(channel_id)

        if not channel:
            return await ctx.send("❌ Ticket channel not found")

        await channel.send("🔒 Ticket closed by remote admin")

        await channel.edit(
            name=f"closed-{channel.name}"
        )

        await ctx.send("✅ Ticket closed")

    # =========================
    # 🗑️ DELETE TICKET
    # =========================
    @commands.command()
    async def dm_deleteticket(self, ctx, channel_id: int):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        channel = self.bot.get_channel(channel_id)

        if not channel:
            return await ctx.send("❌ Channel not found")

        name = channel.name

        await channel.delete()

        await ctx.send(f"🗑️ Deleted ticket: {name}")

    # =========================
    # 👑 CLAIM TICKET
    # =========================
    @commands.command()
    async def dm_claimticket(self, ctx, channel_id: int):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        channel = self.bot.get_channel(channel_id)

        if not channel:
            return await ctx.send("❌ Ticket not found")

        embed = discord.Embed(
            title="👑 Ticket Claimed",
            description=f"{ctx.author.mention} claimed this ticket.",
            color=0x00ffcc
        )

        await channel.send(embed=embed)

        await ctx.send("✅ Ticket claimed")

async def setup(bot):
    await bot.add_cog(RemoteTickets(bot))