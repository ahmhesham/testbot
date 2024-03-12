import json
import os
import time
import requests
from dotenv import dotenv_values, load_dotenv
from pathlib import Path
import asyncio
import inspect
from typing import Optional
from asgiref.sync import sync_to_async
import discord
from discord.ext import commands
from discord import Option
from discord.commands import Option
import json
import requests
import random
import string
from PIL import Image, ImageDraw, ImageFont
import asyncio
from asgiref.sync import async_to_sync









bot = discord.Bot(intents=discord.Intents.all())






@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await bot.wait_until_ready()
    total_members = 0
    for guild in bot.guilds:
        total_members += guild.member_count
    print(total_members)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.users)}"))

@bot.event
async def on_guild_join(guild):
    print(f"Joined guild: {guild.name} ({guild.id})")
    print(f"Guild icon URL: {guild.icon}")
    print(f"Guild owner ID: {guild.owner_id}")


@bot.slash_command()
async def ping(interaction: discord.Interaction):
    """Gets the pot ping"""
    await interaction.response.send_message(f"Ping Is `{round(bot.latency*1000)}` ms")





bot.run('')
