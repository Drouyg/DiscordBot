import discord
from discord.ext import commands

import random
import time
from datetime import date
import calendar


des = 'Le meilleur des bots de test dans ton jardin'

prefix = ''

client = commands.Bot(description=des, command_prefix=prefix)



@client.event
async def on_ready():
    print('It works')


"""

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('greet'):
        await client.send_message(message.channel, 'Say hello!')



@client.command(pass_context=True)
async def ping(ctx):
    await client.say('pong')

@client.command(pass_context=True)
async def Ping(ctx):
    await client.say('pong')

@client.command(pass_context=True)
async def slap(ctx,args):
    await client.say('You slapped {}'.format(args))

"""



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()


    if msg.startswith('ping'):
        await client.send_message(message.channel, 'pong')

    if msg.startswith('slap'):
        if len(msg)<5:
            await client.send_message(message.channel, 'Hey, <@'+str(message.author.id)+'>, can slap who you want, just tell me.')
        else:
            await client.send_message(message.channel, '<@'+str(message.author.id)+'> slapped' + msg[4:])

    if msg.startswith('quoi ?'):
        rand = random.randint(1,5)
        if rand == 1:
            await client.send_message(message.channel, 'WHAAAAAAT ?')
        elif rand == 2:
            await client.send_message(message.channel, 'NANI ?!')
        elif rand == 3:
            await client.send_message(message.channel, 'Et pour le fromage ?')
        elif rand == 4:
            await client.send_message(message.channel, 'Comment ?')
        else:
            await client.send_message(message.channel, 'https://giphy.com/gifs/reaction-learning-charlottesville-pfAKetMYidBjq')

    if 'temps' in msg:
        today = date.today().isoweekday()
        if today == 1:
            await client.send_message(message.channel, 'On est lundi, et oui !')
        elif today == 2:
            await client.send_message(message.channel, 'Nous sommes mardi.')
        elif today == 3:
            await client.send_message(message.channel, "C'est mercredi !")
        elif today == 4:
            await client.send_message(message.channel, "On est jeudi aujourd'hui !")
        elif today == 5:
            await client.send_message(message.channel, "Le vendredi, c'est tout de suite !")
        elif today == 6:
            await client.send_message(message.channel, 'On est un samedi.')
        else:
            await client.send_message(message.channel, "Dimanche, le jour d'aujourd'hui est.")

    if random.randint(1, 50) == 1:
        rand = random.randint(1, 3)
        if rand == 1:
            await client.send_message(message.channel, 'Yeah, Whatever.')
        elif rand == 2:
            await client.send_message(message.channel, "Qui s'en fout ? \o/")
        else:
            await client.send_message(message.channel, "Comme disait mon père : on s'en bat les cou*lles, frère.")






client.run('MzQ4MTUzOTU1MTEwNjE3MDg4.DHizMw.lztjQN51KNLu4Zqi8McYC_9cQVo')
