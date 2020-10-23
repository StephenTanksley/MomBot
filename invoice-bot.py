#  https://www.youtube.c om/watch?v=THj99FuPJmI&t=20s

# Imports - we just want to pull in the module and extract commands.
import discord
import random
import os
from config import api_key
from discord.ext import commands

client = commands.Bot(command_prefix='!')

# When the bot has the information it needs from Discord, the bot is in a ready state. It is ready to execute its function. Read docs for the on_ready state.


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


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


# Grabbing a member as a discord.Member object allows us to access information about that user. This might be useful later on when I need to track which users have submitted invoices and which users haven't.
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    # .run() will take the token as an identifying argument.


for filename in os.listdir('./cogs')
if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(api_key)
