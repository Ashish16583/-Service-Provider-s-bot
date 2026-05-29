import discord
from discord.ext import commands

class Announcement(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def announce(self, ctx, channel: discord.TextChannel, *, message):

        embed = discord.Embed(
            title="📢 Announcement",
            description=message,
            color=0x5865F2
        )

        embed.set_footer(
            text=f"Sent by {ctx.author}",
            icon_url=ctx.author.display_avatar.url
        )

        try:
            await channel.send(
                content="@everyone",
                embed=embed,
                allowed_mentions=discord.AllowedMentions(everyone=True)
            )

            await ctx.send(
                "✅ Announcement sent successfully!"
            )

        except discord.Forbidden:
            await ctx.send(
                "❌ I don't have permission to send messages in that channel."
            )

        except Exception as e:
            await ctx.send(f"❌ Error: {e}")

async def setup(bot):
    await bot.add_cog(Announcement(bot))
