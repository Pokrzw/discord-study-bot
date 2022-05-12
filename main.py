import discord
from dotenv import dotenv_values
env = dotenv_values(".env")

bot = discord.Bot()

# @bot.event
# async def on_ready():
#     print(f"We have logged in as {bot.user}")


# @bot.slash_command(guild_ids=[your, guild_ids, here])
# async def hello(ctx):
#     await ctx.respond("Hello!")

print(env['BOT_TOKEN'])
# bot.run("your token here")