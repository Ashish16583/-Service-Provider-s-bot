id="eco001"
import discord
from discord.ext import commands
import aiosqlite
import random

class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def ensure_user(self, user_id):

        async with aiosqlite.connect("economy.db") as db:

            await db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    balance INTEGER DEFAULT 0
                )
            """)

            await db.execute(
                "INSERT OR IGNORE INTO users (user_id, balance) VALUES (?, ?)",
                (user_id, 0)
            )

            await db.commit()

    @commands.command()
    async def balance(self, ctx):

        await self.ensure_user(ctx.author.id)

        async with aiosqlite.connect("economy.db") as db:

            cursor = await db.execute(
                "SELECT balance FROM users WHERE user_id=?",
                (ctx.author.id,)
            )

            data = await cursor.fetchone()

        await ctx.send(f"💰 Balance: {data[0]} coins")

    @commands.command()
    async def daily(self, ctx):

        await self.ensure_user(ctx.author.id)

        reward = random.randint(100, 500)

        async with aiosqlite.connect("economy.db") as db:

            await db.execute(
                "UPDATE users SET balance = balance + ? WHERE user_id=?",
                (reward, ctx.author.id)
            )

            await db.commit()

        await ctx.send(f"🎁 You got {reward} coins!")

async def setup(bot):
    await bot.add_cog(Economy(bot))
