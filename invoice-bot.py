#  https://www.youtube.com/watch?v=THj99FuPJmI&t=20s

# Imports - we just want to pull in the module and extract commands.
import discord
import random
import os
# import requests
from config import api_key
from discord.ext import commands, tasks
from itertools import cycle


status = cycle(["Managing the server", "Writing some music", "Making memes"])

client = commands.Bot(command_prefix='!')

# When the bot has the information it needs from Discord, the bot is in a ready state. It is ready to execute its function. Read docs for the on_ready state.

# If we assign the bot a role on the channel, it can do everything that a user with that role can do.


@client.event
async def on_ready():
    # await client.change_presence(status=discord.Status.idle, activity=discord.Game("Managing the server."))
    change_status.start()
    print("MomBot is ready.")


# I can use this for scheduling tasks in Discord. Maybe.
@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

# Loading and unloading: It appears that the load and unload commands are looking specifically for the filename, not the class inside the filename. Ergo the filename's capitalization matters. Filenames are going to be lowercase, but the classes will be capitalized.


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(extension)
    client.load_extension(extension)


@client.command()
async def pay_me(ctx):
    ctx.send(f"More information on how to get paid: https://www.outlierstudios.co/onboarding/invoicing (PASS: SamDev)")

# @client.command(aliases=["8ball", 'eight_ball', '8 ball'])
# async def _8ball(ctx, *, question):
#     responses = [
#         "It is certain",
#         "Without a doubt",
#         "You may rely on it",
#         "Reply hazy try again",
#         "Better not tell you now",
#         "Don't count on it",
#         "My reply is no",
#     ]
#     answer = random.choice(responses)

#     await print(f"Question: {question} \nAnswer: {answer}")
#     await ctx.send(f"Question: {question} \nAnswer: {answer}")


@client.event
async def on_command_error(ctx, error):
    pass
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Please try again.")


@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@client.command()
async def request(ctx):
    r = await request.get("http://www.tutorialspoint.com/python/")
    ctx.send(r[:300])
    print(r[:300])


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify a number of messages to delete.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# .run() will take the token as an identifying argument.
client.run(api_key)
