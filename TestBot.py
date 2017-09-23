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

"""
import opuslib
import opuslib.api
import opuslib.api.encoder
import opuslib.api.decoder
"""

discord.opus.load_opus('libopus.so')


des = 'Le meilleur des bots de JDR et de musique dans ton jardin'

prefix = ''

client = commands.Bot(description=des, command_prefix=prefix)


players = {}
nextSong = []
nextPaused = [False]



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
     'Hello !',
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



#Jukebox

jukebox = [
    ['I See stars - Treehouse',
     'iss',
     "https://www.youtube.com/watch?v=-Do461IqoSc",
     "https://www.youtube.com/watch?v=Vgevhi2pCIE",
     "https://www.youtube.com/watch?v=fW6BrjUvt8Y",
     "https://www.youtube.com/watch?v=f0y9e_X0UaI",
     "https://www.youtube.com/watch?v=600kX4ZBzyE",
     "https://www.youtube.com/watch?v=rh5p2GwLvvQ",
     "https://www.youtube.com/watch?v=ObbvHnNDqCY",
     "https://www.youtube.com/watch?v=45VJ3vpkNN0",
     "https://www.youtube.com/watch?v=iphPkgm5f1A",
     "https://www.youtube.com/watch?v=lwblmiwWBas",
     "https://www.youtube.com/watch?v=ceukqHx8opY",
     "https://www.youtube.com/watch?v=AmicHgzvGfs"
     ],

    ['Post Rock',
     'pr',
     "https://www.youtube.com/watch?v=hATifcVr_1U",
     "https://www.youtube.com/watch?v=fopOFoJ3fVs",
     "https://www.youtube.com/watch?v=gHyZPB3GmOk",
     "https://www.youtube.com/watch?v=l5-gja10qkw",
     "https://www.youtube.com/watch?v=FrzGOTT8MEM",
     "https://www.youtube.com/watch?v=iC_SvgjAn5I",
     "https://www.youtube.com/watch?v=uxzxIIpGyQc"
     ],

    ['J-Rock / J-Pop',
     'jrock',
     "https://www.youtube.com/watch?v=bV4vcr8E4HU",
     "https://www.youtube.com/watch?v=Q1Xzw12qMgk",
     "https://www.youtube.com/watch?v=1kutzdLY5Dc",
     "https://www.youtube.com/watch?v=6eHuPYOJ2ZE",
     "https://www.youtube.com/watch?v=GJ4yehnerHQ",
     "https://www.youtube.com/watch?v=xGbxsiBZGPI",
     "https://www.youtube.com/watch?v=rh517TMtVbo",
     "https://www.youtube.com/watch?v=tcBBNB5JTOQ",
     "https://www.youtube.com/watch?v=vYV-XJdzupY",
     "https://www.youtube.com/watch?v=K_xTet06SUo",
     "https://www.youtube.com/watch?v=UjZqcDYbvAE",
     "https://www.youtube.com/watch?v=6YZlFdTIdzM",
     "https://www.youtube.com/watch?v=2e0Cdi_TLY8",
     "https://www.youtube.com/watch?v=gN24W_psMpE",
     "https://www.youtube.com/watch?v=cZpmj1assiQ",
     "https://www.youtube.com/watch?v=BwXgMzoCnxU",
     "https://www.youtube.com/watch?v=JaPGbJk4Tcc",
     "https://www.youtube.com/watch?v=Gb6l9zH5ZK4"
     ],

    ['Electro-swing, wut?',
     'wtf',
     "https://www.youtube.com/watch?v=UbQgXeY_zi4",
     "https://www.youtube.com/watch?v=lX44CAz-JhU",
     "https://www.youtube.com/watch?v=FHccClTAdzc",
     "https://www.youtube.com/watch?v=fBGSJ3sbivI",
     "https://www.youtube.com/watch?v=6rjN36OKpuM",
     "https://www.youtube.com/watch?v=ZeBrnuQxEsQ",
     "https://www.youtube.com/watch?v=UPjvhk7I7eQ",
     "https://www.youtube.com/watch?v=CqaAs_3azSs",
     "https://www.youtube.com/watch?v=kfoJUeyMsOE",
     "https://www.youtube.com/watch?v=52Gg9CqhbP8",
     "https://www.youtube.com/watch?v=YgGzAKP_HuM",
     "https://www.youtube.com/watch?v=HyHNuVaZJ-k"
     ]

    ]



def randomTalk(message, word, textList):
    if word in message.content.lower():
        rand = random.randint(1,len(textList))
        return textList[rand-1]
    else:
        return 0






#FONCTION ROLL


def RandomBetween(x,y):
    randl = []
    for i in range(x,y+1):
        randl.append(i)
    random.shuffle(randl)
    return randl[0]


def IsANumber(c):
    return True if (48 <= ord(c) <= 57) else False

def RollToList(text, rollList):
    #print(rollList, '.'+text)
    if text[0] == ' ':
        if len(text) == 1:
            return rollList
        else:
            return RollToList(text[1:], rollList)
    elif IsANumber(text[0]):
        i = 0
        nb = ''
        while True:
            if len(text) == i:
                rollList.append(nb)
                return rollList
            if IsANumber(text[i]):
                nb += text[i]
            elif text[i] == 'd':
                if len(text) == i+1:
                    return 1
                elif not IsANumber(text[i+1]):
                    return 1
                else:
                    nb += 'd'
                    i+=1
                    while True:
                        if len(text) == i:
                            rollList.append(nb)
                            return rollList
                        if IsANumber(text[i]):
                            nb += text[i]
                        else:
                            rollList.append(nb)
                            return RollToList(text[i:], rollList)
                        i+=1
            else:
                rollList.append(nb)
                return RollToList(text[i:], rollList)
            i+=1
    elif text[0] == '(' or text[0] == ')' or text[0] == '+' or text[0] == '-' or text[0] == '*' or text[0] == '/':
        rollList.append(text[0])
        if len(text) == 1:
            return rollList
        else:
            return RollToList(text[1:], rollList)
    else:
        return 1



def RollAnalyse(rList):
    prevIsNb = False
    nbParenthesis = 0
    for i in range(len(rList)):
        if rList[i].isdigit() or 'd' in rList[i]:
            if prevIsNb:
                return 1
            prevIsNb = True
        elif rList[i] == '+' or rList[i] == '-' or rList[i] == '*' or rList[i] == '/':
            if not prevIsNb or i+1 == len(rList):
                return 1
            prevIsNb = False
        elif rList[i] == '(':
            if prevIsNb:
                return 1
            prevIsNb = False
            nbParenthesis += 1
        elif rList[i] == ')':
            if not prevIsNb:
                return 1
            prevIsNb = True
            nbParenthesis -= 1
            if nbParenthesis < 0:
                return 1


    if nbParenthesis != 0:
        return 1

    return 0




def Roll(text):
    rollList = []
    rollList = RollToList(text, rollList)
    if rollList == 1:
        return 'Bad syntax.', 'error'

    if RollAnalyse(rollList) == 1:
        return 'Bad formula.', 'error'

    rollRes = ''
    rollMsg = ''

    for e in rollList:
        if 'd' in e:
            index = e.index('d')
            rollRes += '('
            rollMsg += '('
            for i in range(int(e[:index])):
                rand = RandomBetween(1, int(e[index+1:]))
                rollRes += str(rand) +'+'
                rollMsg += " **|" + str(rand) +"|** :game_die:*" + e[index+1:] + '* +'
            rollRes = rollRes[:-1]
            rollMsg = rollMsg[:-1]
            rollRes += ')'
            rollMsg += ')'
        else:
            rollRes += e
            if e == '*':
                rollMsg += '\\*'
            else:
                rollMsg += e

    return rollMsg, str(eval(rollRes))











@client.event
async def on_ready():
    print('Hello again, world.')
    client.loop.create_task(timer())



@client.event
async def on_message(message):
    if message.author == client.user and not message.content.startswith('!'):
        return

    msg = message.content.lower()


    if msg.startswith('!ping'):
        await client.send_message(message.channel, 'pong')





    if msg.startswith('!r'):
        if len(msg)<3:
            await client.send_message(message.channel, 'Roll something !')
        else:
            text = msg[2:]
            retourMsg, retour = Roll(text)
            if retour != 'error':
                await client.send_message(message.channel, '<@' + str(
                    message.author.id) + '> rolled :\n' + retourMsg + "\n\n**= " + retour + "**")
            else:
                await client.send_message(message.channel, '<@' + str(
                    message.author.id) + '> Error : ' + retourMsg)






    if message.server.id == '348154317464928266':

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

        if msg.startswith('ah'):
            rand = random.randint(1,3)
            if rand == 1:
                await client.send_message(message.channel, "https://giphy.com/gifs/geekinc-ah-geek-inc-3o7btW7VDxqrhJEnqE")
            elif rand == 2:
                await client.send_message(message.channel, 'Je dirais même plus: "AH" !')
            else:
                await client.send_message(message.channel, "https://giphy.com/gifs/nba-interesting-xUPGcmrdRkCaZ5qZ2M")

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



    #JUKEBOX

    #if message.server.id == '348154317464928266':

    if msg.startswith('!jukebox'):
        if len(msg)<9:
            await client.delete_message(message)
            await client.send_message(message.channel, '*<@'+str(message.author.id)+'> open the jukebox.*')
            await client.send_message(message.channel, 'https://giphy.com/gifs/ruby-XxkkxrnylVG7u')
            for i in range(len(jukebox)):
                await client.send_message(message.channel, '**-----------'+str(i+1)+'-----------**\n'
                + '**Name : ' + jukebox[i][0] + '**\n'
                + '*Id : ' + jukebox[i][1] + '*\n'
                + '*Nb of song : ' + str(len(jukebox[i])-2) + '*\n'
                + '**------------------------**\n')
            await client.send_message(message.channel, 'Use "!jukebox *id*" to place a disk.')

        else:
            for e in jukebox:
                if msg[9:] == e[1]:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "!play " + e[2])
                    await asyncio.sleep(10)
                    for i in range(3, len(e)):
                        nextSong.append(e[i])
                        nextPosition = (len(nextSong))
                        if message.server.id in players:
                            client.loop.create_task(timerNext(message, nextPosition))

                        #await client.send_message(message.channel, "!next " + e[i])
                        await asyncio.sleep(2)





    #MUSIC BOT

    #if message.server.id == '348154317464928266':

    if msg.startswith('!help'):
        await client.send_message(message.channel, 'Besoin d\'aide ? C\'est simple, c\'est du Franglais !\n'
        +'**"!join"** - Dans ton salon vocal, le bot se joindra.\n'
        +'**"!quit"** - Dans l\'espace, le bot repartira.\n'
        +'**"!play *url*"** - La vidéo youtube, le bot lira.\n'
        +'**"!stop"** - La vidéo youtube, le bot arrêtera. À la suivante, il passera.\n'
        +'**"!pause"** - La vidéo youtube, le bot mettra en pause.\n'
        +'**"!resume"** - La vidéo youtube, le bot reprendra.\n'
        +'**"!now"** - Le titre de la vidéo youtube, le bot affichera.\n'
        +'**"!next *url*"** - La vidéo youtube à la liste de lecture, le bot ajoutera.\n'
        +'**"!show"** - Les prochaines vidéos youtube dans la liste de lecture, le bot affichera.\n'
        +'**"!jukebox"** - une liste de vidéos présélectionnées, le bot affichera.\n'
        +'**"!jukebox *id*"** - une liste de vidéos présélectionnées, le bot lancera.\n')



    if msg.startswith('!join'):
        await client.delete_message(message)

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
        await client.delete_message(message)
        nextPaused[0] = False
        nextSong.clear()
        if client.is_voice_connected(message.server):
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
            await client.send_message(message.channel, 'À une prochaine, <@' + str(message.author.id) + '> !')
        else:
            await client.send_message(message.channel, "Alors non, je ne peux pas partir avant d'entrer.")



    if msg.startswith('!play '):
        nextPaused[0] = False
        if len(msg)>6:
            yt_url = message.content[6:]
            if client.is_voice_connected(message.server):


                if message.server.id in players:
                    if players[message.server.id].is_playing() :
                        await client.send_message(message.channel, "Stopping...")
                        players[message.server.id].stop()


                await client.send_message(message.channel, 'Chargement...')
                voice = client.voice_client_in(message.server)
                try:
                    player = await voice.create_ytdl_player(yt_url)
                except Exception:
                    await client.send_message(message.server, "Bad url")
                else:
                    players[message.server.id] = player
                    players[message.server.id].start()
                    await client.delete_message(message)
                    await client.send_message(message.channel, '<@'+str(message.author.id)+'> lance le son !')


            if not client.is_voice_connected(message.server):
                await client.send_message(message.channel, '<@'+str(message.author.id)+'>, fais "!join" pour m\'appeler !')
        else:
            await client.send_message(message.channel, "Il me faut un lien Youtube.")


    if msg.startswith('!stop'):
        nextPaused[0] = False

        if message.server.id in players:
            players[message.server.id].stop()


    if msg.startswith('!pause'):
        nextPaused[0] = True
        if message.server.id in players:
            players[message.server.id].pause()

    if msg.startswith('!resume'):
        nextPaused[0] = False
        if message.server.id in players:
            players[message.server.id].resume()


    if msg.startswith('!now'):
        if message.server.id in players:
            if players[message.server.id].is_playing():
                await client.send_message(message.channel, "*Now playing :* " + players[message.server.id].title)


    if msg.startswith('!next '):
        nextSong.append(message.content[6:])
        nextPosition = (len(nextSong))
        if message.server.id in players:
            if players[message.server.id].is_playing():
                await client.delete_message(message)
                client.loop.create_task(timerNext(message, nextPosition))

            else:
                await client.send_message(message.channel, 'Use "!play *url*" before, please.')
        else:
            await client.send_message(message.channel, 'Use "!play *url*" before, please.')


    if msg.startswith('!show'):
        if len(nextSong) > 0:
            await client.send_message(message.channel, 'Coming up next :')
            for i in range(len(nextSong)):
                await client.send_message(message.channel, '**'+str(i+1)+' -> **' + nextSong[i])
        else:
            await client.send_message(message.channel, 'No next song.')










    #RandomTalk

    if message.server.id == '348154317464928266':

        for e in randomTalkList:
            word = e[0]
            textList = e[1:]
            retour = randomTalk(message, word, textList)
            if retour !=0 :
                await client.send_message(message.channel, retour)


        if random.randint(1, 50) == 1:
            rand = random.randint(1, 4)
            if rand == 1:
                await client.send_message(message.channel, 'Yeah, Whatever.')
            elif rand == 2:
                await client.send_message(message.channel, "Qui s'en fout ? \o/")
            elif rand == 3:
                await client.send_message(message.channel, "https://giphy.com/gifs/hLVK6yBZcyPVm")
            else:
                await client.send_message(message.channel, "Comme disait mon père : on s'en bat les cou*lles, frère.")





async def timerNext(message, nextPosition):
    while nextPosition != 0:
        await asyncio.sleep(10)
        while players[message.server.id].is_playing() or nextPaused[0] == True:
            await asyncio.sleep(1)
        nextPosition -= 1

    #await client.send_message(message.channel, 'Chargement...')
    voice = client.voice_client_in(message.server)
    nextNext = nextSong.pop(0)
    try:
        player = await voice.create_ytdl_player(nextNext)
    except Exception:
        await client.send_message(message.server, "Bad url")
    else:
        players[message.server.id] = player
        players[message.server.id].start()




async def timer():
    while not client.is_closed:
        await asyncio.sleep(60)
        #tt = datetime.datetime.now().time()
        #print(tt)
        rand = random.randint(1, 1000)
        if rand == 1:
            l1 =list(client.servers)
            for e in l1:
                if e.id == '348154317464928266':
                    l2 =list(e.channels)
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


        if datetime.date.today().isoweekday() == 7 and datetime.datetime.now().hour == 9 and datetime.datetime.now().minute == 0:
            l1 =list(client.servers)
            for e in l1:
                if e.id == '228982241609515008':
                    l2 =list(e.channels)
                    x=0
                    while str(l2[x].id) == '231128267485085706':
                        x+=1

                    rand = random.randint(1, 5)
                    if rand == 1:
                        await client.send_message(l2[x], '@everyone On est dimanche, balancez les dispos de la semaine !')
                    elif rand == 2:
                        await client.send_message(l2[x], "@everyone Soon une session de JDR ? Balancez les dispos de la semaine !")
                    elif rand == 3:
                        await client.send_message(l2[x], "@everyone C'est l'heure d'organiser la prochaine session ! Balancez les dispos de la semaine !")
                    elif rand == 4:
                        await client.send_message(l2[x], "@everyone Le dimanche, c'est l'organisation du JDR. Balancez les dispos de la semaine !")
                    else:
                        await client.send_message(l2[x], "@everyone Dimanche ! Balancez les dispos de la semaine ! :heart: ")









client.run('MzYxMTQ2NDYwMTkzOTQ3NjUx.DKf3YA.FqKsYgE1hhGpZXkDJuUpYKFngMo')
