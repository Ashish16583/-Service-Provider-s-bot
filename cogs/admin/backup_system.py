
import discord
from discord.ext import commands
import json
import os

ALLOWED_USERS = [ 1406960430554812508
]

BACKUP_FOLDER = "backups"

class BackupSystem(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        if not os.path.exists(BACKUP_FOLDER):
            os.makedirs(BACKUP_FOLDER)

    def allowed(self, user):
        return user.id in ALLOWED_USERS

    # =========================
    # 📦 CREATE BACKUP
    # =========================
    @commands.command()
    async def dm_backup(self, ctx, guild_id: int):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        guild = self.bot.get_guild(guild_id)

        data = {
            "name": guild.name,
            "roles": [],
            "channels": [],
            "categories": []
        }

        # roles
        for role in guild.roles:
            data["roles"].append({
                "name": role.name,
                "permissions": role.permissions.value
            })

        # categories
        for category in guild.categories:
            data["categories"].append({
                "name": category.name
            })

        # channels
        for channel in guild.channels:
            data["channels"].append({
                "name": channel.name,
                "type": str(channel.type)
            })

        file_path = f"{BACKUP_FOLDER}/{guild.id}.json"

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        await ctx.send(f"✅ Backup created: {file_path}")

    # =========================
    # ♻️ RESTORE BACKUP
    # =========================
    @commands.command()
    async def dm_restore(self, ctx, guild_id: int):

        if ctx.guild:
            return

        if not self.allowed(ctx.author):
            return await ctx.send("❌ Unauthorized")

        file_path = f"{BACKUP_FOLDER}/{guild_id}.json"

        if not os.path.exists(file_path):
            return await ctx.send("❌ Backup not found")

        guild = self.bot.get_guild(guild_id)

        with open(file_path, "r") as f:
            data = json.load(f)

        # restore categories
        for category in data["categories"]:

            exists = discord.utils.get(
                guild.categories,
                name=category["name"]
            )

            if not exists:
                await guild.create_category(category["name"])

        # restore channels
        for channel in data["channels"]:

            exists = discord.utils.get(
                guild.channels,
                name=channel["name"]
            )

            if not exists:

                if channel["type"] == "text":
                    await guild.create_text_channel(
                        channel["name"]
                    )

        await ctx.send("♻️ Backup restored")

async def setup(bot):
    await bot.add_cog(BackupSystem(bot))
