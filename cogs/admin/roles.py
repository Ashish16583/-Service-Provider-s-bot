import discord
from discord.ext import commands

OWNER_ID = 1406960430554812508  # 🔐 replace with your ID

class RoleManager(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def is_owner(self, user):
        return user.id == OWNER_ID

    # =========================
    # 👑 ADD ROLE
    # =========================
    @commands.command()
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        try:
            await member.add_roles(role)
            await ctx.send(f"✅ Added {role.name} to {member.mention}")

        except discord.Forbidden:
            await ctx.send("❌ I don't have permission to add this role")

    # =========================
    # ❌ REMOVE ROLE
    # =========================
    @commands.command()
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        try:
            await member.remove_roles(role)
            await ctx.send(f"🗑️ Removed {role.name} from {member.mention}")

        except discord.Forbidden:
            await ctx.send("❌ Missing permissions")

    # =========================
    # 👑 PROMOTE TO ADMIN ROLE
    # =========================
    @commands.command()
    async def promote(self, ctx, member: discord.Member):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        admin_role = discord.utils.get(ctx.guild.roles, name="Admin")

        if not admin_role:
            return await ctx.send("❌ Admin role not found")

        try:
            await member.add_roles(admin_role)
            await ctx.send(f"👑 {member.mention} promoted to Admin")

        except discord.Forbidden:
            await ctx.send("❌ I cannot assign Admin role (check role hierarchy)")

    # =========================
    # 📉 DEMOTE USER (REMOVE ADMIN)
    # =========================
    @commands.command()
    async def demote(self, ctx, member: discord.Member):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        admin_role = discord.utils.get(ctx.guild.roles, name="Admin")

        if not admin_role:
            return await ctx.send("❌ Admin role not found")

        try:
            await member.remove_roles(admin_role)
            await ctx.send(f"📉 {member.mention} removed from Admin")

        except discord.Forbidden:
            await ctx.send("❌ Missing permission")

async def setup(bot):
    await bot.add_cog(RoleManager(bot))