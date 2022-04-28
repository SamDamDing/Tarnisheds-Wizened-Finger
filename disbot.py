import asyncio
import discord
import random
from discord import Embed
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_select, create_select_option, create_button, create_actionrow, wait_for_component
from dicts import MessageImageLinks, links, TierThresholds
from TryFingersButHole import genPhrase, FingerMessage
from modules import thresholdcheck


client = discord.Client()
fMsgHeader = "Finger Message Generator"
#https://github.com/SamDamDing/TryFingersButHole
#https://tinyurl.com/FingerMessageGenerator
#https://tinyurl.com/TFBHFMG
fMsgFooter = "Source Code: https://tinyurl.com/TFBHFMG"
fGestWidth = 100
fGestHeight = 100
emoji_list = ["👍", "👎"]
appraisaltimeout = 30

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    appraisalcount = 0
    currenttier = thresholdcheck(appraisalcount)
    
    channel = message.channel
    if message.author == client.user:
        return

    if message.content.startswith('$fingers'):
        genPhrase("r","r","r","r","r","r","r")
        HAND = FingerMessage
        fMsg = HAND.Message
        fGest = HAND.Gesture
        fType = HAND.Type
        
        embedVar = discord.Embed(title = fMsgHeader, description = HAND.Message, color = 0x2a2823)
        embedVar.set_footer(text = fMsgFooter)
        embedVar.add_field(name="Appraisals: ", value=str(appraisalcount), inline=True)
        
        try:
            file = discord.File(links.get(HAND.Gesture), filename="image.png")
            embedVar.set_image(url="attachment://image.png")
            embedVar.set_thumbnail(url=str(MessageImageLinks.get(currenttier)))
        except:
            pass
        if fType == 1 or fType == 3:
            try:
                embedVar.add_field(name="Gesture:", value=fGest)
                msgctx = await message.channel.send(file=file, embed=embedVar)
            except:
                pass
        else:
            msgctx = await message.channel.send(embed=embedVar)
        for i in emoji_list:
            await msgctx.add_reaction(i)
        await asyncio.sleep(5)
        
        message_1 = await msgctx.channel.fetch_message(msgctx.id)
        tally = {x: 0 for x in emoji_list}
        voters = []
        for reaction in message_1.reactions:
            if reaction.emoji in emoji_list:
                reactors = await reaction.users().flatten()
                for reactor in reactors:
                    if reactor.id not in voters:
                        if message_1.author != reactor:
                            tally[reaction.emoji] += 1
                            voters.append(reactor.id)
                    await reaction.remove(reactor)
        for x in voters:
            appraisalcount =+ 1
        currenttier = thresholdcheck(appraisalcount)
        embedVar.set_thumbnail(url=str(MessageImageLinks.get(currenttier)))
        embedVar.set_footer(text = fMsgFooter)
        embedVar.set_field_at(index=0, name="Appraisals: ", value=str(appraisalcount), inline=True)
        embed_1 = embedVar
        await msgctx.edit(embed = embed_1)
        print(fMsg)

client.run('Your Token Here')
