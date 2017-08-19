import discord
from discord.ext import commands

des = 'Le meilleur des bots de test dans ton jardin'

prefix = ''

client = commands.Bot(description=des, command_prefix=prefix)

@client.event
async def on_ready():
    print('It works')


@client.command(pass_context=True)
async def ping(ctx):
    await client.say('pong')

@client.command(pass_context=True)
async def Ping(ctx):
    await client.say('pong')

@client.command(pass_context=True)
async def slap(ctx,args):
    await client.say('You slapped {}'.format(args))


client.run('MzQ4MTUzOTU1MTEwNjE3MDg4.DHizMw.lztjQN51KNLu4Zqi8McYC_9cQVo')