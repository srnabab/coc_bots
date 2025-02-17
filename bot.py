import discord
from discord.commands import slash_command
import os

# 替换成你的机器人 Token
TOKEN = os.environ.get('TOKEN')

intents = discord.Intents.default() # 默认 intents 通常足够 Slash Commands 使用
bot = discord.Bot(intents=intents)

# 当机器人成功连接到 Discord 时触发
@bot.event
async def on_ready():
    print(f'机器人已登录，用户名为 {bot.user}')

@slash_command(guild_ids=[...]) # 注册 Slash Command
async def ping(ctx):
    """回复 Pong!"""
    await ctx.respond("Pong!")

# 运行机器人
bot.run(TOKEN)