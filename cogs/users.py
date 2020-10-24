import discord
from discord.ext import commands


class Users(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Users Cog is loaded.")

    @commands.command()
    async def users_ping(self, ctx):
        await ctx.send(f"Pong! Latency: {round(self.client.latency * 1000)}ms")


def setup(client):
    client.add_cog(Users(client))
