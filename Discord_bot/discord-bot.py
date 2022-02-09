import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!hi'):
        await message.channel.send(f' {message.author.mention} Hi!')

    if message.content.startswith('hihi'):
        await message.channel.send(f' {message.author.mention} Hi Hi 2x2 !')


client.run('OTMzNTgwMzQ1NTc4NzgyNzkw.Yejmcw.NqwQKOoV-LkX8R_pG19IgMobdV8')

# bot = commands.Bot(command_prefix='!')

# import discord
# from discord.ext import commands
#
# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')
#
#
#
# @bot.command()
# async def hihi(ctx):
#     await ctx.send('Hi Hi 4x4!')
#
#
# bot.run('OTMzNTgwMzQ1NTc4NzgyNzkw.Yejmcw.NqwQKOoV-LkX8R_pG19IgMobdV8')
