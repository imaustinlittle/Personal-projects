import discord
from discord.ext import commands

# Create a new bot instance
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: on_ready
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

# Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm your Discord bot!")

# Run the bot
TOKEN = "MTA4NjM1NjEzMDA0Mjc2MTM1Mw.GtEz-5.eabgdze0vvk_fWlO_pkkUhyexJTSFtpSLsIJCE"
bot.run(TOKEN)
