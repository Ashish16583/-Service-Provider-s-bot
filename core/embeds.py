
import discord

def success_embed(description):
    return discord.Embed(
        description=f"✅ {description}",
        color=0x57F287
    )

def error_embed(description):
    return discord.Embed(
        description=f"❌ {description}",
        color=0xED4245
    )

def info_embed(description):
    return discord.Embed(
        description=f"ℹ️ {description}",
        color=0x5865F2
    )

