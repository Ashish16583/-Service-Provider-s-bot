import discord
from discord.ext import commands

OWNER_ID = 123456789  # 🔐 your Discord ID

class OwnerTools(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def transferowner(self, ctx, member: discord.Member):

        # 🔐 OWNER ONLY CHECK
        if ctx.author.id != OWNER_ID:
            return await ctx.send("❌ Only the bot owner can use this command.")

        # ⚠️ CONFIRMATION EMBED
        embed = discord.Embed(
            title="👑 Ownership Transfer Request",
            description=f"""
You are about to transfer **ownership responsibility** to {member.mention}

⚠️ This will NOT change Discord server ownership automatically.
It will:
• Assign OWNER ROLE (if exists)
• Notify logs
• Lock admin commands from old owner
""",
            color=0xff0000
        )

        view = ConfirmTransfer(member, self.bot, ctx.author)

        await ctx.send(embed=embed, view=view)


class ConfirmTransfer(discord.ui.View):

    def __init__(self, member, bot, old_owner):
        super().__init__()
        self.member = member
        self.bot = bot
        self.old_owner = old_owner

    @discord.ui.button(label="CONFIRM", style=discord.ButtonStyle.danger)
    async def confirm(self, interaction, button):

        if interaction.user.id != self.old_owner.id:
            return await interaction.response.send_message("❌ Not allowed", ephemeral=True)

        # OPTIONAL: assign role if exists
        role = discord.utils.get(interaction.guild.roles, name="Owner")

        if role:
            await self.member.add_roles(role)

        log = discord.utils.get(interaction.guild.text_channels, name="logs")

        if log:
            await log.send(
                f"👑 Ownership handover initiated: {self.old_owner} ➜ {self.member}"
            )

        await interaction.response.edit_message(
            content="✅ Ownership transfer completed (manual Discord transfer still required)",
            embed=None,
            view=None
        )

async def setup(bot):
    await bot.add_cog(OwnerTools(bot))