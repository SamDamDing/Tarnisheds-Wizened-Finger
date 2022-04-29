import logging
import asyncio
import discord
from discord.ext import commands
from dicts import Conjunctions, Gestures, MessageImageLinks, links, Categories
from modules import genMsgType, phraser, thresholdcheck, genGesture, genTemplate
logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG)

intents = discord.Intents.all()
guilds_ids = []
fMsgHeader = "Message:"
fMsgFooter = "Source Code: https://tinyurl.com/TFBHFMG"
fGestWidth = 100
fGestHeight = 100
emoji_list = ["👍", "👎"]
goodemoji = "👍"
bademoji = "👎"
appraisaltimeout = 15

async def func():
    for guild in bot.guilds:
        id = guild.id
        logging.debug(id) # As your BOT is in one single server, only one ID would be extracted and this can be used.
        guilds_ids.append(id)

bot = commands.Bot(command_prefix='$', intents=intents)
bot.author_id = 968856972281675856
@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)

@bot.command()
async def fingers(message, *args):
    global ctx
    global MsgEmbed

    msgtype =       "r"
    msgtemplate =   "r"
    msgword =       "r"
    msgconjunction ="r"
    msggesture =    "r"
    msgtemplate2 =  "r"
    msgword2 =      "r"

    appraisalcount = 0
    currenttier = thresholdcheck(appraisalcount)
    channel = message.channel
    try:
        argmsgtype = args[0]
        if genMsgType(argmsgtype) != None:
            msgtype = argmsgtype
    except:
        argmsgtype = genMsgType(msgtype)
        msgtype = argmsgtype
    try:
        argmsgtemplate = args[1]
        if genTemplate(argmsgtemplate) != None:
            msgtemplate = argmsgtemplate
    except:
        msgtemplate = msgtemplate
        pass
    try:
        argmsgword = args[2]
        if any(argmsgword in val for val in Categories.values()) == True:
            msgword = argmsgword
    except:
        msgword = msgword
        pass
    try:
        argmsgconjunction = args[3]
        if argmsgconjunction in Conjunctions:
            msgconjunction = argmsgconjunction
    except:
        msgconjunction = msgconjunction
        pass
    try:
        argmsgtemplate2 = args[4]
        if genTemplate(argmsgtemplate2) != None:
            msgtemplate2 = argmsgtemplate2
    except:
        pass
    try:
        argmsgword2 = args[5]
        if any(argmsgword2 in val for val in Categories.values()) == True:
            msgword2 = argmsgword2
    except:
        msgword2 = msgword2
        pass
    try:
        argmsggesture = args[6]
        if argmsggesture in Gestures:
            msggesture = argmsggesture
    except:
        pass
    if message.author == bot.user:
        return

    global fMsg
    global fType
    global fGest

    fMsg = phraser(msgtype,msgtemplate,msgword,msgconjunction,msgtemplate2,msgword2)
    fType = genMsgType(msgtype)
    fGest = genGesture(msggesture)
    
    MsgEmbed = discord.Embed(title = fMsgHeader, description = fMsg, color = 0x2a2823)
    MsgEmbed.set_footer(text = fMsgFooter)
    MsgEmbed.add_field(name="Appraisals: ", value=str(appraisalcount), inline=True)
    file = discord.File(links.get(fGest), filename="image.png")
    MsgEmbed.set_image(url="attachment://image.png")
    MsgEmbed.set_thumbnail(url=str(MessageImageLinks.get(currenttier)))

    if fType == 1 or fType == 3:
        MsgEmbed.add_field(name="Gesture:", value=fGest)
        ctx = await message.channel.send(file=file, embed=MsgEmbed)
    else:
        ctx = await message.channel.send(embed=MsgEmbed)    
    for i in emoji_list:
        await ctx.add_reaction(i)
    id = ctx.id
    await asyncio.sleep(appraisaltimeout)
    message = await channel.fetch_message(id)
    logging.debug(message.reactions)
    voters = []
    for reaction in message.reactions:
        if reaction.emoji == goodemoji:
            goodcount = reaction.count
            goodusers = [gooduser async for gooduser in reaction.users()]
            logging.debug("Goodcount: " + str(goodcount))
            for user in goodusers:
                logging.debug("Good Users: " + str(user.id))
                if user.id not in voters:
                    voters.append(user.id)
                await message.remove_reaction(reaction, user)
        if reaction.emoji == bademoji:
            badcount = reaction.count
            badusers = [baduser async for baduser in reaction.users()]
            logging.debug("Badcount: " + str(badcount))
            for user in badusers:
                logging.debug("Bad Users: " + str(user.id))
                if user.id not in voters:
                    voters.append(user.id)
                await message.remove_reaction(reaction, user)
    for voter in voters:
        logging.debug("Voter: " + str(voter))
    appraisalcount = len(voters)-1
    logging.debug("Total Appraisals: " + str(appraisalcount))
    currenttier = thresholdcheck(appraisalcount)
    MsgEmbed.set_thumbnail(url=str(MessageImageLinks.get(currenttier)))
    MsgEmbed.set_footer(text = fMsgFooter)
    MsgEmbed.set_field_at(index=0, name="Appraisals: ", value=str(appraisalcount), inline=True)
    UpdatedMsgEmbed = MsgEmbed
    await ctx.edit(embed = UpdatedMsgEmbed)
    await bot.process_commands(message)

bot.run('Your Token Here')
