id="inv001"
import discord
from discord.ext import commands

class InviteTracker(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.invites = {}

    @commands.Cog.listener()
    async def on_ready(self):

        for guild in self.bot.guilds:

            self.invites[guild.id] = await guild.invites()

    @commands.Cog.listener()
    async def on_member_join(self, member):

        guild = member.guild

        new_invites = await guild.invites()

        old_invites = self.invites.get(guild.id, [])

        used_invite = None

        for new in new_invites:
            for old in old_invites:

                if new.code == old.code and new.uses > old.uses:
                    used_invite = new
                    break

        self.invites[guild.id] = new_invites

        if used_invite:

            channel = discord.utils.get(guild.text_channels, name="logs")

            if channel:
                await channel.send(
                    f"📊 {member} joined using invite by **{used_invite.inviter}**"
                )

async def setup(bot):
    await bot.add_cog(InviteTracker(bot))
