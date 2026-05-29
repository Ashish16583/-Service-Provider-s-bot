import discord
from discord.ext import commands
import time

# 🔐 CONFIG
WHITELIST = set()  # add admin IDs here
LIMIT_WINDOW = 10  # seconds
MAX_ACTIONS = 3    # anti spam limit

class AntiNuke(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

        # tracking
        self.actions = {}

    # =========================
    # 🚨 RAID DETECTION SYSTEM
    # =========================
    def check_raid(self, user_id):

        now = time.time()

        if user_id not in self.actions:
            self.actions[user_id] = []

        self.actions[user_id].append(now)

        # keep only last 10 sec actions
        self.actions[user_id] = [
            t for t in self.actions[user_id]
            if now - t < LIMIT_WINDOW
        ]

        if len(self.actions[user_id]) >= MAX_ACTIONS:
            return True

        return False

    # =========================
    # 🔥 PUNISH SYSTEM
    # =========================
    async def punish(self, guild, user):

        if user.id in WHITELIST:
            return

        try:
            await guild.ban(user, reason="🚨 Anti-Nuke Protection Triggered")
        except:
            pass

    # =========================
    # 🧨 CHANNEL DELETE
    # =========================
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):

        async for entry in channel.guild.audit_logs(
            limit=1,
            action=discord.AuditLogAction.channel_delete
        ):

            user = entry.user

            if self.check_raid(user.id):
                await self.punish(channel.guild, user)

    # =========================
    # 🧨 ROLE DELETE
    # =========================
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):

        async for entry in role.guild.audit_logs(
            limit=1,
            action=discord.AuditLogAction.role_delete
        ):

            user = entry.user

            if self.check_raid(user.id):
                await self.punish(role.guild, user)

    # =========================
    # 🧨 WEBHOOK ATTACK
    # =========================
    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):

        async for entry in channel.guild.audit_logs(
            limit=1,
            action=discord.AuditLogAction.webhook_create
        ):

            user = entry.user

            if self.check_raid(user.id):
                await self.punish(channel.guild, user)

async def setup(bot):
    await bot.add_cog(AntiNuke(bot))
