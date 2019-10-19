import discord
import asyncio
import random

client = discord.Client()

copypastas = ["According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible.",
              "Hello am 48 year man from somalia. Sorry for my bed england. I selled my wife for internet connection for play 'conter strik' and i want to become the goodest player like you I play with 400 ping on brazil and i am global elite 2. pls no copy pasterio my story", "If 700,000 people die in hospitals every year. Why don´t we close down these hospitals and prevent those deaths? (つ ͡° ͜ʖ ͡°)つ", "I had a dream last night where Marshmello removed his helmet. It was at a concert, toward the end of the show. The crowd was gathering their things and getting ready to leave when one of the announcers came on the microphone. 'And now, Marshmello has a special surprise for all of you!' Marshmello returned to the stage to a cheering crowd, who were all expecting an encore or a new song. But the crowd fell dead silent as they watched the DJ slowly unclip the chin strap of his helmet. He grasped the helmet on both sides and slowly brought it straight up, and with a gasp from the crowd...'Hey, Vsauce! Michael here.'", "In Japan, heart surgeon. Number one. Steady hand. One day, Yakuza boss need new heart. I do operation. But, mistake! Yakuza boss die! Yakuza very mad. I hide in fishing boat, come to America. No english, no food, no money. Darryl give me job. Now I have house, American car, and new woman. Darryl save life. My big secret: I kill yakuza boss on purpose. I good surgeon. The best!"]


@client.event
async def on_ready():
    print("ready to play some football...")
    await client.change_presence(game=discord.Game(name="football with the lads..."))


@client.event
async def on_message(message):
    author = message.author

    if message.content == "this is so sad":
        await client.send_message(message.channel, "ALEXA, PLAY DESPACITO")
    elif message.content == "dab":
        await client.send_message(message.channel, "Stop it, see a doctor.")
    elif message.content == "gay":
        await client.send_message(message.channel, "No u.")
    elif message.content == "who am I?":
        await client.send_message(message.channel, author)
    elif message.content == "~copypasta":
        await client.send_message(message.channel, random.choice(copypastas))
    elif message.content == "uh oh":
        await client.send_message(message.channel, "stinky")
    else:
        return

client.run('TOKEN')
