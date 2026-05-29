import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio

# LOAD ENV
load_dotenv()

TOKEN = os.getenv("TOKEN")

# PREFIX SYSTEM
async def get_prefix(bot, message):
    prefixes = ["."]
    return commands.when_mentioned_or(*prefixes)(bot, message)

# INTENTS
intents = discord.Intents.all()

# BOT SETUP
bot = commands.Bot(
    command_prefix=get_prefix,
    intents=intents,
    help_command=None
)

# READY EVENT
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# LOAD COGS
async def load_cogs():

    for root, dirs, files in os.walk("cogs"):

        for file in files:

            if file.endswith(".py") and not file.startswith("__"):

                path = os.path.join(root, file)

                extension = (
                    path.replace("\\", ".")
                    .replace("/", ".")
                    .replace(".py", "")
                )

                print(f"Loading: {extension}")

                try:
                    await bot.load_extension(extension)
                    print(f"✅ Loaded {extension}")

                except Exception as e:
                    print(f"❌ Failed {extension}")
                    print(e)

# MAIN
async def main():

    async with bot:

        await load_cogs()

        await bot.start(TOKEN)

# START BOT
asyncio.run(main())
