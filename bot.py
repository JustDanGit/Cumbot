import discord
from discord.ext import commands

# Bot prefix
PREFIX = "!"

# Create a bot instance with a specified command prefix
bot = commands.Bot(command_prefix=PREFIX)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot with your Discord bot token
bot.run('MTIyNTUwOTc2MzM5MjIwODk1OA.GtJ7Mn.3U9rM0nVHwPkcYd8tEmVp-EyvlduBchBlhRoaM')
