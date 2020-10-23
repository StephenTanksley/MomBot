# Imports - we just want to pull in the module and extract commands.
import discord
import random
from config import api_key
from discord.ext import commands

client = commands.Bot(command_prefix='!')

# When the bot has the information it needs from Discord, the bot is in a ready state. It is ready to execute its function. Read docs for the on_ready state.


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server. Welcome!')


@client.event
async def on_member_remove(member):
    print(f'{member} has left a server. Bye!')

# I can hide commands so only authorized parties can see it.


@client.command()
async def ping(ctx):
    # context needs to be passed into the function declaration, not in the client.command() method.
    # When the command is run, the bot will say "Pong!"
    await ctx.send(f'Pong! Latency: {round(client.latency * 1000)}ms')


@client.command()
async def dirty(ctx):
    # context needs to be passed into the function declaration, not in the client.command() method.
    # When the command is run, the bot will say "Pong!"
    await ctx.send('Wash the dishes! Clean your room!')


@client.command(aliases=["8ball", 'eight_ball', '8 ball'])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain",
        "Without a doubt",
        "You may rely on it",
        "Reply hazy try again",
        "Better not tell you now",
        "Don't count on it",
        "My reply is no",
    ]

    answer = random.choice(responses)

    await ctx.send(f"Question: {question} \nAnswer: {answer}")


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    # .run() will take the token as an identifying argument.
client.run("NzE3MTY3Mjc5MjU0Nzk4MzY2.XtWYEw.7eN5RN8M8eGGnD8OvedItFesq-M")
