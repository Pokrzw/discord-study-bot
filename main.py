import discord
from dotenv import dotenv_values
from discord import option, SlashCommandOptionType as types
import datetime

env = dotenv_values(".env")
bot = discord.Bot(debug_guilds=[973656184076767322])

listened_threads = []
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(name="add_task", description="Command for adding tasks. Add them in format: [task] [date]. Date in format day.month.year")
@option("task", types.string, description="Enter the task you want to do")
@option("date", types.string, description="Enter the deadline (day.month.year)")
async def add_task(ctx, task: str, date: str):
    channel = ctx.interaction.channel
    message = await channel.send(f"{task} {date}")
    thread = await channel.create_thread(name=task, message=message)
    original_poster = ctx.interaction.message
    print(original_poster)
    await thread.add_user(ctx.interaction.user)
    await thread.remove_user(bot.user)
    date_data = date.split('.')
    print(date_data)
    date = datetime.datetime(int(date_data[2]),int(date_data[1])-1,int(date_data[0]))
    await ctx.respond("Task created!")


#submit_for_revision -> daje powiadomienia na kanale
@bot.slash_command(name="submit_for_revision", description="Use when you submit a proof o completion")
async def submit_for_revision(ctx):
    channel = ctx.interaction.channel.channel_id
    listened_threads.push(channel)
    original_poster = ctx.interaction.user
    await ctx.respond(f"@everyone  {original_poster.name} has just posted a proof of completion. Give them a reaction if they completed it! ")
bot.run(env['BOT_TOKEN'])
