id="l5wwl5"
from discord.ext import commands

class Temp(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

async def setup(bot):
    await bot.add_cog(Temp(bot))
import discord
from discord.ext import commands

class VerifyView(discord.ui.View):

    @discord.ui.button(
        label="Verify",
        style=discord.ButtonStyle.green
    )
    async def verify_button(self, interaction, button):

        role = discord.utils.get(
            interaction.guild.roles,
            name="Verified"
        )

        if role:
            await interaction.user.add_roles(role)

            await interaction.response.send_message(
                "✅ Verified successfully.",
                ephemeral=True
            )

class Verification(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def verifypanel(self, ctx):

        embed = discord.Embed(
            title="🔒 Verification",
            description="Click below to verify.",
            color=0x5865F2
        )

        await ctx.send(
            embed=embed,
            view=VerifyView()
        )

async def setup(bot):
    await bot.add_cog(Verification(bot))
