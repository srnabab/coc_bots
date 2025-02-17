import discord
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

TOKEN = os.environ.get('TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')


if __name__ == "__main__":
    http_thread = Thread(target=run_http_server)
    http_thread.start()
    
    intents = discord.Intents.default()
    client = MyClient(intents=intents)
    client.run(TOKEN)
    