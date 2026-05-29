import discord
from discord.ext import commands

ALLOWED_USERS = [
    1406960430554812508,  # Your ID
]

class DMControl(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def allowed(self, user):
        return user.id in ALLOWED_USERS

    # ===================================
    # 🌐 GET SERVER
    # ===================================
    def get_guild(self, guild_id):
        return self.bot.get_guild(guild_id)

    # ===================================
    # 👑 GIVE ROLE FROM DM
    # ===================================
    @commands.command()
    async def dm_giverole(
        self,
        ctx,
        guild_id: int,
        member_id: int,
        *,
        role_name
    ):

        # Only DM
        if ctx.guild is not None:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        guild = self.get_guild(guild_id)

        if not guild:
            return await ctx.send("❌ Guild not found")

        member = guild.get_member(member_id)

        if not member:
            return await ctx.send("❌ Member not found")

        role = discord.utils.get(guild.roles, name=role_name)

        if not role:
            return await ctx.send("❌ Role not found")

        await member.add_roles(role)

        await ctx.send(
            f"✅ Added role {role.name} to {member}"
        )

    # ===================================
    # 🗑️ DELETE CHANNEL FROM DM
    # ===================================
    @commands.command()
    async def dm_deletechannel(
        self,
        ctx,
        guild_id: int,
        channel_id: int
    ):

        if ctx.guild is not None:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        guild = self.get_guild(guild_id)

        channel = guild.get_channel(channel_id)

        if not channel:
            return await ctx.send("❌ Channel not found")

        name = channel.name

        await channel.delete(reason="Remote owner command")

        await ctx.send(f"🗑️ Deleted channel: {name}")

    # ===================================
    # 🔒 LOCK SERVER
    # ===================================
    @commands.command()
    async def dm_lockserver(self, ctx, guild_id: int):

        if ctx.guild is not None:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        guild = self.get_guild(guild_id)

        for channel in guild.text_channels:
            try:
                await channel.set_permissions(
                    guild.default_role,
                    send_messages=False
                )
            except:
                pass

        await ctx.send("🔒 Server locked")

    # ===================================
    # 🔓 UNLOCK SERVER
    # ===================================
    @commands.command()
    async def dm_unlockserver(self, ctx, guild_id: int):

        if ctx.guild is not None:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        guild = self.get_guild(guild_id)

        for channel in guild.text_channels:
            try:
                await channel.set_permissions(
                    guild.default_role,
                    send_messages=True
                )
            except:
                pass

        await ctx.send("🔓 Server unlocked")

    # ===================================
    # 📊 SERVER INFO
    # ===================================
    @commands.command()
    async def dm_serverinfo(self, ctx, guild_id: int):

        if ctx.guild is not None:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        guild = self.get_guild(guild_id)

        embed = discord.Embed(
            title=f"📊 {guild.name}",
            color=0x5865F2
        )

        embed.add_field(
            name="Members",
            value=guild.member_count
        )

        embed.add_field(
            name="Channels",
            value=len(guild.channels)
        )

        embed.add_field(
            name="Roles",
            value=len(guild.roles)
        )

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(DMControl(bot))
