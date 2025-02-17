import discord
import os

TOKEN = os.environ.get('TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

intents = discord.Intents.default()

client = MyClient(intents=intents)
client.run(TOKEN)