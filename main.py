import discord
from dotenv import dotenv_values
from discord import option, SlashCommandOptionType as types
import datetime

env = dotenv_values(".env")
bot = discord.Bot(debug_guilds=[973656184076767322])


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
    await thread.add_user(ctx.interaction.user)
    await thread.remove_user(bot.user)
    # date_data = date.split('.')
    # date = datetime.datetime(int(date_data[2]),int(date_data[1]),int(date_data[0]))
    await ctx.respond("Task created!")

@bot.slash_command(name="check_task", description="Command for sending proof of completion. Use this command right after sending the proof")
async def check_task(ctx):
    thread = ctx.interaction.channel
    proof = thread.last_message
    if(len(proof.reactions) > 0):
        await thread.delete()
    else:
        await ctx.respond("Task not fulfilled")

bot.run(env['BOT_TOKEN'])
