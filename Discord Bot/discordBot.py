import sys
import discord
from discord.ext import commands

# Create a new bot instance
intents = discord.Intents.default()
intents.message_content = True
intents.application_commands = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: on_ready
@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

# Command: !hello
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm your Discord bot!")

# Command: !shutdown
@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Shutting down the bot...")
    await bot.logout()
    sys.exit(0)





# Run the bot
TOKEN = "TOKEN"
bot.run(TOKEN)


