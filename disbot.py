import random
from TryFingersButHole import genPhrase
from TryFingersButHole import FingerMessage
from dicts import links
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow, create_button, create_actionrow, wait_for_component

client = discord.Client()
fMsgHeader = "Finger Message Generator"
#https://github.com/SamDamDing/TryFingersButHole
#https://tinyurl.com/FingerMessageGenerator
#https://tinyurl.com/TFBHFMG
fMsgFooter = "Source Code: https://tinyurl.com/TFBHFMG"
fGestWidth = 100
fGestHeight = 100

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    HAND = FingerMessage
    if message.author == client.user:
        return

    if message.content.startswith('$fingers'):
        genPhrase("r","r","r","r","r","r","r")
        fMsg = HAND.Message
        fGest = HAND.Gesture
        fType = HAND.Type
        embedVar = discord.Embed(
            title = fMsgHeader, description = HAND.Message, color = 0x2a2823,
        )
        file = discord.File(links.get(HAND.Gesture), filename="image.png")
        embedVar.set_image(url="attachment://image.png")
        embedVar.set_footer(text = fMsgFooter)
        #used for determining if we need a gesture image or not.
        if fType == 1 or fType == 3:
            embedVar.add_field(name="Gesture:", value=fGest)
            msgctx = await message.channel.send(file=file, embed=embedVar )
        else:
            msgctx = await message.channel.send(embed=embedVar)
        print(fMsg)

client.run('Your Token Here')
