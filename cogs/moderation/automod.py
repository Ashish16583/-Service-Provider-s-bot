import discord
from discord.ext import commands

BAD_WORDS = ["Fuck", "sex"]
SCAM_LINKS = ["discord.gg/", "free-nitro", "gift"]

class AutoMod(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        content = message.content.lower()

        # 🚫 BAD WORD FILTER
        for word in BAD_WORDS:
            if word in content:
                await message.delete()
                await message.channel.send(
                    f"⚠️ {message.author.mention} no bad words allowed.",
                    delete_after=5
                )
                return

        # 🚨 SCAM FILTER
        for link in SCAM_LINKS:
            if link in content:
                await message.delete()
                await message.channel.send(
                    f"🚨 {message.author.mention} scam link detected!",
                    delete_after=5
                )
                return

        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(AutoMod(bot))

