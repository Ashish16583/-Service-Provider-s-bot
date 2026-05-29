id="wc001"
import discord
from discord.ext import commands

WELCOME_CHANNEL_ID = 1509148966485233715  # change this

WELCOME_MESSAGE = """
🎉 Welcome to Service Provider’s

🌐 The ultimate marketplace for:
💻 Website Development
🤖 Discord Bots
🎨 Graphic Design
⛏️ Minecraft Services
🔐 Cyber Security
☁️ Hosting & More

📌 Please read:
📜 Rules
🛠️ How-To-Order
🎫 Support Section

🚀 Enjoy your stay and grow with our community!
"""

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        # ======================
        # SERVER WELCOME MESSAGE
        # ======================

        channel = self.bot.get_channel(WELCOME_CHANNEL_ID)

        if channel:

            embed = discord.Embed(
                title="👋 Welcome!",
                description=WELCOME_MESSAGE.format(user=member.mention),
                color=0x00ffcc
            )

            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text=f"Member #{member.guild.member_count}")

            await channel.send(
                content=f"🎉 Welcome {member.mention}!",
                embed=embed
            )

        # ======================
        # DM WELCOME MESSAGE
        # ======================

        try:
            dm_embed = discord.Embed(
                title="👋 Welcome to Service Provider’s!",
                description=WELCOME_MESSAGE.format(user=member.name),
                color=0x5865F2
            )

            dm_embed.set_footer(text="We’re happy to have you here ❤️")

            await member.send(embed=dm_embed)

        except discord.Forbidden:
            # User has DMs closed
            pass

async def setup(bot):
    await bot.add_cog(Welcome(bot))


