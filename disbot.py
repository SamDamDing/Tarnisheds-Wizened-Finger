import discord
from discord.ext import commands
import random
from TryFingersButHole import genPhrase
from TryFingersButHole import FingerMessage
from dicts import links

client = discord.Client()
fMsgHeader = "Finger Message Generator"
fMsgFooter = "Made by MercyMoon"
HAND = FingerMessage

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$fingers'):
        genPhrase("r","r","r","r","r","r","r")
        #hand = FingerMessage
        fMsg = HAND.Message
        fGest = HAND.Gesture
        fType = HAND.Type
        embedVar = discord.Embed(
            title = fMsgHeader, description = HAND.Message, color = 0x2a2823,
        )
        file = discord.File(links.get(HAND.Gesture), filename="image.png")
        embedVar.set_image(url="attachment://image.png")
        embedVar.set_footer(text = fMsgFooter)

        if fType == 1 or fType == 3:
            await message.channel.send(file=file, embed=embedVar)
        else:
            await message.channel.send(embed=embedVar)

        print(fMsg)

client.run('Your Token Here')
