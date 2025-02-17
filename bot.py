import discord
from discord.commands import slash_command
import os

TOKEN = os.environ.get('TOKEN')

intents = discord.Intents.default()
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f'机器人已登录，用户名为 {bot.user}')

@slash_command(guild_ids=[1320038130551881759]) # 指定服务器 ID 列表
async def ping(ctx):
    """回复 Pong!"""
    await ctx.respond("Pong!")

bot.run(TOKEN)