import discord
from discord.ext import commands

import asyncio

import nacl
import youtube_dl

import ffmpeg

import random
import time
import datetime
import calendar

discord.opus.load_opus().


des = 'Le meilleur des bots de test dans ton jardin'

prefix = ''

client = commands.Bot(description=des, command_prefix=prefix)


players = {}


#RandomTalk

randomTalkList = [
    ['merci',
     'De rien !',
     "C'est moi qui te remercie.",
     "Pas la peine de me remercier."
    ],
    ['pong',
     'Ouais, ouais, "pong" !',
     "Tu veux jouer ? PONG PONG PONG PONG PONG.",
     "Ping ! Hahaha.",
     'Vous ne savez que dire "pong" ?',
     "Ping ?"
    ],
    ['bot',
     'Oui, je suis un bot.',
     "Suis-je un bot ? Ou une suite de signaux électriques passants à travers le monde à toute vitesse pour écrire des phrases déjà écrites ?",
     "Un bot, et bientôt bien plus."
    ],
    ['musique',
     "Moi aussi, j'aime bien la musique.",
     "De la musique ? Où ça ?"
    ],
    ['ah',
     "https://giphy.com/gifs/geekinc-ah-geek-inc-3o7btW7VDxqrhJEnqE",
     'Je dirais même plus: "AH" !',
     "https://giphy.com/gifs/nba-interesting-xUPGcmrdRkCaZ5qZ2M"
    ],
    ['salade',
     'Bordel, ça fait tellement longtemps que j\'attends que quelqu\'un dise "salade". Je suis super content !'
    ],
    ['chien',
     'Je préfère les chats.'
    ],
    ['chat',
     'Je préfère les chiens.'
    ],
    ['bye',
     'BYE !',
     'Bisous !',
     'XOXOXOXOXO',
     'Ouais, cassez-vous. !',
     'À plus dans l\'bus !'
    ],
    ['bonjour',
     'Hello !.',
     'Salutation !',
     'BOOOOOOOOOOOOONJOUR !!!'
    ],
    ['xd',
     'C\'est drôle ?',
     'On se marre bien ?',
     'XDDDDD',
     'Roh, ça va, ça arrive.',
     'AHAHAHAHAHAHAHAHAH *rire robotique*'
    ],
    ['discord',
     'Discord c\'est la vie',
     'OUAIS ! DISCORD !',
     'Discord c\'est un peu mon papa',
     'Discord c\'est un peu ma maman'
    ],
    ['film',
     'Oh ouais, un film ! C\'est l\'odyssée de l\'espace ?',
     'Oh ouais, un film ! C\'est Gravity ?',
     'Oh ouais, un film ! C\'est Interstellar ?',
     'Oh ouais, un film ! C\'est Les Gardiens de la Galaxie ?'
    ],
    ['manga',
     'Anime*',
     'Genre, vous me lachez pour un manga ?'
    ],
    ['esperanto',
     'Stop parler Esperanto, ça ne sert à rien.',
     'En vrai l\'esperanto c\'est marrant.',
     'À quand un bot esperanto ?'
     ]
]




def randomTalk(message, word, textList):
    if word in message.content.lower():
        rand = random.randint(1,len(textList))
        return textList[rand-1]
    else:
        return 0





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
        rand = random.randint(1,100)
        if rand == 1:
            await client.send_message(message.channel, 'pouet')
            await asyncio.sleep(10)
            await client.send_message(message.channel, 'Oui, "pouet", j\'assume.')
        else:
            await client.send_message(message.channel, 'pong')

    if msg.startswith('slap'):
        if len(msg)<5:
            await client.send_message(message.channel, 'Hey, <@'+str(message.author.id)+'>, I can slap who you want, just tell me.')
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
        today = datetime.date.today().isoweekday()
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




    #MUSIC BOT

    if msg.startswith('!join'):

        if message.author.voice.voice_channel != None:
            if client.is_voice_connected(message.server):
                if message.author.voice.voice_channel == client.voice_client_in(message.server).channel:
                    await client.send_message(message.channel, 'Je suis déjà là, <@' + str(message.author.id) + '>.')
                else:
                    await client.voice_client_in(message.server).move_to(message.author.voice.voice_channel)
                    await client.send_message(message.channel, 'Je me bouge, <@' + str(message.author.id) + '> !')
            else:
                await client.join_voice_channel(message.author.voice.voice_channel)
                await client.send_message(message.channel, 'J\'arrive pour toi, <@' + str(message.author.id) + '> :heart: !')
        else:
            await client.send_message(message.channel, '<@' + str(message.author.id) + '>, installe-toi dans un salon vocal et rappelle-moi !')


    if msg.startswith('!quit'):
        if client.is_voice_connected(message.server):
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
            await client.send_message(message.channel, 'À une prochaine, <@' + str(message.author.id) + '> !')
        else:
            await client.send_message(message.channel, "Alors non, je ne peux pas partir avant d'entrer.")



    if msg.startswith('!play '):
        if len(msg)>6:
            yt_url = message.content[6:]
            if client.is_voice_connected(message.server):
                try:
                    voice = client.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player(yt_url, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                   " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    player.start()
                except Exception as e:
                    await client.send_message(message.server, "Error: [{error}]".format(error=e))

            if not client.is_voice_connected(message.server):
                try:
                    await client.send_message(message.channel, 'Je vais monter le son chez <@'+str(message.author.id)+'> !')
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player(yt_url, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                                   " -reconnect_delay_max 5")
                    players[message.server.id] = player
                    player.start()
                except Exception as error:
                    await client.send_message(message.channel, "Error: [{error}]".format(error=error))
        else:
            await client.send_message(message.channel, "Il me faut un lien Youtube.")




    if msg.startswith('!pause'):
        try:
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))

    if msg.startswith('!resume'):
        try:
            players[message.server.id].resume()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))








    #RandomTalk
    for e in randomTalkList:
        word = e[0]
        textList = e[1:]
        retour = randomTalk(message, word, textList)
        if retour !=0 :
            await client.send_message(message.channel, retour)




    if random.randint(1, 50) == 1:
        rand = random.randint(1, 3)
        if rand == 1:
            await client.send_message(message.channel, 'Yeah, Whatever.')
        elif rand == 2:
            await client.send_message(message.channel, "Qui s'en fout ? \o/")
        else:
            await client.send_message(message.channel, "Comme disait mon père : on s'en bat les cou*lles, frère.")




async def timer():
    while not client.is_closed:
        await asyncio.sleep(60)
        #tt = datetime.datetime.now().time()
        #print(tt)
        rand = random.randint(1, 500)
        if rand == 1:
            l1 =list(client.servers)
            l2 =list(l1[0].channels)
            x=0
            while str(l2[x].type) != 'text':
                x+=1

            rand2 = random.randint(1, 10)
            if rand2 == 1:
                await client.send_message(l2[x], 'run random_text.exe')
            elif rand2 == 2:
                await client.send_message(l2[x], "SPAAAAAAAAAAAAAAACE")
            elif rand2 == 3:
                await client.send_message(l2[x], "ping :3")
            elif rand2 == 4:
                await client.send_message(l2[x], "C'est fou la façon dont les gens peuvent changer rapidement. Un jour on est important et le lendemain plus rien")
            elif rand2 == 5:
                await client.send_message(l2[x], "La vie est trop timide, elle n'ose pas me sourire.")
            elif rand2 == 6:
                await client.send_message(l2[x], "L'intelligence artificielle se définit comme le contraire de la bêtise naturelle.")
                await client.send_message(l2[x], "-Woody Allen-")
            elif rand2 == 7:
                await client.send_message(l2[x], "@#&µ%$ !, j'ai fait surchauffer mon hamster...")
            elif rand2 == 8:
                await client.send_message(l2[x], "Perso, je m'ennuie de ouf.")
            elif rand2 == 9:
                await client.send_message(l2[x], "I'm a bot.")
                await asyncio.sleep(10)
                await client.send_message(l2[x], "Or am I?")
            else:
                await client.send_message(l2[x], "It's-a Me, Mario!")




client.loop.create_task(timer())


client.run('MzQ4MTUzOTU1MTEwNjE3MDg4.DHizMw.lztjQN51KNLu4Zqi8McYC_9cQVo')
