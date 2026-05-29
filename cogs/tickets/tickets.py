import discord
from discord.ext import commands

class Tickets(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # =========================
    # 🎫 CREATE PANEL
    # =========================
    @commands.command()
    async def ticketpanel(self, ctx):

        embed = discord.Embed(
            title="🎫 Support Tickets",
            description="Click buttons below",
            color=0x5865F2
        )

        view = TicketView()

        await ctx.send(embed=embed, view=view)

    # =========================
    # 👑 CLAIM
    # =========================
    @commands.command()
    async def claim(self, ctx):

        await ctx.send(
            f"👑 {ctx.author.mention} claimed this ticket"
        )

    # =========================
    # 🔒 CLOSE
    # =========================
    @commands.command()
    async def close(self, ctx):

        await ctx.send("🔒 Closing ticket in 5 seconds...")

        await discord.utils.sleep_until(
            discord.utils.utcnow()
        )

        await ctx.channel.delete()

class TicketView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Create Ticket",
        style=discord.ButtonStyle.green
    )
    async def create_ticket(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        guild = interaction.guild

        category = discord.utils.get(
            guild.categories,
            name="Tickets"
        )

        if not category:
            category = await guild.create_category("Tickets")

        channel = await guild.create_text_channel(
            name=f"ticket-{interaction.user.name}",
            category=category
        )

        await channel.send(
            f"🎫 Ticket created for {interaction.user.mention}"
        )

        await interaction.response.send_message(
            f"✅ Ticket: {channel.mention}",
            ephemeral=True
        )

async def setup(bot):
    await bot.add_cog(Tickets(bot))

