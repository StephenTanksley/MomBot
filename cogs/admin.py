import discord
from discord.ext import commands, tasks
from itertools import cycle

status = cycle(["Managing the server", "Writing some music", "Making memes"])


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin Cog is loaded.")

    # Listeners won't show up in a list of commands.
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server. Welcome!')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server. Bye!')

    # Command will show up when we run the !help command.
    @commands.command()
    async def admin_ping(self, ctx):
        await ctx.send(f"Pong! Latency: {round(self.client.latency * 1000)}ms")

    # Grabbing a member as a discord.Member object allows us to access information about that user. This might be useful later on when I need to track which users have submitted invoices and which users haven't.

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
                return

    @commands.command()
    async def invoice_new(self, ctx):
        # Currently this is a manual process. Ideally I can make this automatic.
        date = input(
            "What date is this invoice due by? (e.g. mm-dd-yyyy)? \n> ")
        await ctx.send(f"Don't forget to turn in your invoices to Daniel (dciurlizza@outlierstudios.co) by the end of the day on {date}")


def setup(client):
    client.add_cog(Admin(client))
