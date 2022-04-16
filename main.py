
import os
from dotenv import load_dotenv
from music_cog import Music
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", description='Yet another music bot.')
bot.add_cog(Music(bot))


@ bot.event
async def on_ready():
    #print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))
    print("bot online")

bot.run(TOKEN)
