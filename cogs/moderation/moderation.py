id="l5wwl5"
from discord.ext import commands

class Temp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Temp(bot))
import discord
from discord.ext import commands
from core.embeds import success_embed, error_embed

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.ban(reason=reason)

        await ctx.send(
            embed=success_embed(
                f"{member} has been banned."
            )
        )

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason"):
        await member.kick(reason=reason)

        await ctx.send(
            embed=success_embed(
                f"{member} has been kicked."
            )
        )

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)

        msg = await ctx.send(
            embed=success_embed(
                f"Deleted {amount} messages."
            )
        )

        await msg.delete(delay=3)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
