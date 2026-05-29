# cogs/admin/safety.py
import discord
from discord.ext import commands

OWNER_ID = 1406960430554812508

class Safety(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.locked = False

    def check_owner(self, ctx):
        return ctx.author.id == OWNER_ID

    # 🔒 LOCK SERVER
    @commands.command()
    async def lockserver(self, ctx):

        if not self.check_owner(ctx):
            return

        self.locked = True

        for channel in ctx.guild.text_channels:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)

        await ctx.send("🔒 Server Locked!")

    # 🔓 UNLOCK SERVER
    @commands.command()
    async def unlockserver(self, ctx):

        if not self.check_owner(ctx):
            return

        self.locked = False

        for channel in ctx.guild.text_channels:
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)

        await ctx.send("🔓 Server Unlocked!")

    # 🚨 EMERGENCY MODE
    @commands.command()
    async def emergency(self, ctx):

        if not self.check_owner(ctx):
            return

        for channel in ctx.guild.channels:
            try:
                await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            except:
                pass

        await ctx.send("🚨 EMERGENCY LOCKDOWN ACTIVE")

async def setup(bot):
    await bot.add_cog(Safety(bot))