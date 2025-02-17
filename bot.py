import discord
from discord import app_commands
import os
import http.server
import socketserver
from threading import Thread

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_http_server():
    with socketserver.TCPServer(("0.0.0.0", 8080), MyHandler) as httpd:
        httpd.serve_forever()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        guild = discord.Object(id=1320038130551881759) # 替换为你的服务器 ID
        tree.copy_global_to(guild=guild) # 将全局命令复制到指定服务器，方便测试
        await tree.sync(guild=guild) # 同步命令到指定服务器
        print("斜杠命令已同步!")

if __name__ == "__main__":
    http_thread = Thread(target=run_http_server)
    http_thread.start()

    intents = discord.Intents.default()
    client = MyClient(intents=intents)
    tree = app_commands.CommandTree(client)
    
    @tree.command(name="helo", description="Helo!") # name 是命令的名字，description 是描述
    async def hello_command(interaction: discord.Interaction): # interaction 代表用户的交互
        await interaction.response.send_message(f"Helo! {interaction.user.mention}!") # 回复用户

    TOKEN = os.environ.get('TOKEN')

    client.run(TOKEN)