import discord
from discord.ext import commands

OWNER_ID = 1406960430554812508  # replace with your Discord ID

class AdvancedModeration(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =========================
    # 🔐 OWNER CHECK
    # =========================
    def is_owner(self, user):
        return user.id == OWNER_ID

    # =========================
    # 👑 GIVE ANY ROLE
    # =========================
    @commands.command()
    async def giverole(self, ctx, member: discord.Member, *, role_name):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        role = discord.utils.get(ctx.guild.roles, name=role_name)

        if not role:
            return await ctx.send("❌ Role not found")

        try:
            await member.add_roles(role)
            await ctx.send(f"✅ Added role **{role.name}** to {member.mention}")

        except discord.Forbidden:
            await ctx.send("❌ I cannot assign this role")

    # =========================
    # ❌ REMOVE ANY ROLE
    # =========================
    @commands.command()
    async def takerole(self, ctx, member: discord.Member, *, role_name):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        role = discord.utils.get(ctx.guild.roles, name=role_name)

        if not role:
            return await ctx.send("❌ Role not found")

        try:
            await member.remove_roles(role)
            await ctx.send(f"🗑️ Removed role **{role.name}** from {member.mention}")

        except discord.Forbidden:
            await ctx.send("❌ Missing permissions")

    # =========================
    # 👑 GIVE ADMIN
    # =========================
    @commands.command()
    async def giveadmin(self, ctx, member: discord.Member):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        admin_role = discord.utils.get(ctx.guild.roles, name="Admin")

        if not admin_role:
            return await ctx.send("❌ Admin role not found")

        try:
            await member.add_roles(admin_role)
            await ctx.send(f"👑 {member.mention} is now Admin")

        except discord.Forbidden:
            await ctx.send("❌ Cannot assign Admin role")

    # =========================
    # 🤖 DISABLE ALL BOTS
    # =========================
    @commands.command()
    async def disablebots(self, ctx):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        count = 0

        for role in ctx.guild.roles:
            if role.permissions.administrator:
                try:
                    await role.edit(permissions=discord.Permissions.none())
                    count += 1
                except:
                    pass

        await ctx.send(f"🤖 Bot/admin permissions disabled for {count} roles")

    # =========================
    # 🗑️ DELETE CHANNEL
    # =========================
    @commands.command()
    async def deletechannel(self, ctx, channel: discord.TextChannel):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        try:
            name = channel.name
            await channel.delete(reason="Owner Command")
            await ctx.author.send(f"🗑️ Deleted channel: {name}")

        except:
            await ctx.send("❌ Failed to delete channel")

    # =========================
    # 🗂️ DELETE CATEGORY
    # =========================
    @commands.command()
    async def deletecategory(self, ctx, *, category_name):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        category = discord.utils.get(ctx.guild.categories, name=category_name)

        if not category:
            return await ctx.send("❌ Category not found")

        try:
            await category.delete(reason="Owner Command")
            await ctx.send(f"🗂️ Deleted category: {category.name}")

        except:
            await ctx.send("❌ Failed to delete category")

    # =========================
    # 🔒 DISABLE COMMANDS
    # =========================
    @commands.command()
    async def lockdown(self, ctx):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        for channel in ctx.guild.text_channels:
            try:
                await channel.set_permissions(
                    ctx.guild.default_role,
                    send_messages=False
                )
            except:
                pass

        await ctx.send("🔒 Full server lockdown enabled")

    # =========================
    # 🔓 UNLOCK SERVER
    # =========================
    @commands.command()
    async def unlockall(self, ctx):

        if not self.is_owner(ctx.author):
            return await ctx.send("❌ Owner only command")

        for channel in ctx.guild.text_channels:
            try:
                await channel.set_permissions(
                    ctx.guild.default_role,
                    send_messages=True
                )
            except:
                pass

        await ctx.send("🔓 Server unlocked")

async def setup(bot):
    await bot.add_cog(AdvancedModeration(bot))
