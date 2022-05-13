import random
import discord
from discord.ext import commands
from discord.ui import Button,View,Select,modal
from dicts import Conjunctions, Gestures, MessageImageLinks, links, Categories, Templates,EnemiesCat,PeopleCat,ThingsCat,Battle_TacticsCat,ActionsCat,SituationsCat,PlacesCat,DirectionsCat,Body_PartsCat,AffinitiesCat,ConceptsCat,PhrasesCat,Message_Types
from modules import genConjunctionNew, genMsgType, genWordNew, phraser, thresholdcheck, genGesture, genTemplate,genConjunction,genWord
from typing import List
from string import Template
import shelve
from discord import app_commands

appraisaltimeout = 10
fMsgHeader = "Message:"
fMsgFooter = "Source Code: https://tinyurl.com/TFBHFMG"
CategoriesSplit={}
GesturesSplit={}
def yield_chunks(lst, chunk_size):
    i = 0
    while i < len(lst):
        yield lst[i:min(len(lst), i + chunk_size)]
        i += chunk_size

for x in Categories:
    i=1
    category = Categories.get(x)
    for y in yield_chunks(Categories.get(x),24):
        #print("\n" + str(x) + str("_" + str(i) + ": ") + str(y))
        if i == 1:
            catname = (str(x))
            CategoriesSplit.update({catname:y})
        else:
            catname = (str(x) + str(" pt. " + str(i)))
            CategoriesSplit.update({catname:y})
        i += 1

chunked_list = [Gestures[i:i+24] for i in range(0, len(Gestures), 24)]
gi = 1
for x in chunked_list:
    if gi == 1:
        catname = ("Gestures")
        GesturesSplit.update({catname:x})
    else:
        catname = ("Gestures") + str(" pt. " + str(gi))
        GesturesSplit.update({catname:x})
    gi +=1

global selfcat
global word
global buttons
global wordbuttonstr
global word2
word = "word"
buttons = []
word2=[]
gesturelist=[]
guild_ids = []
guild_names =[]
#TEST_GUILD = discord.Object(id=840071998599069696)

class MyClient(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.all()
        super().__init__(application_id=968856972281675856, intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        print('Currently added to ' + str(len(self.guilds)) + " Servers")
        for guild in self.guilds:
            id = guild.id
            name = guild.name
            guild_ids.append(id)
            guild_names.append(name)
            print(f'{name} : {id}')

    async def setup_hook(self) -> None:
        await self.tree.sync()

"""
====================
Template Section
====================
"""
class TemplateMenuButton(Button):
    def __init__(self,label:str,style=discord.ButtonStyle.green):
        super().__init__(label=label, style=style, custom_id=label, emoji='👉')
    async def callback(self,interaction: discord.Interaction):
        view = TemplateSelectView()
        await interaction.response.edit_message(view=view)

class TemplateSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(TemplateSelect())
        self.add_item(BackButton(label="Go Back"))

class TemplateSelect(discord.ui.Select):
    def __init__(self):
        options = []
        for k in Templates:
            k = discord.SelectOption(label=k.replace('$word','****'),description=k.replace('$word','****'))
            if k not in options:
                options.append(k)
        super().__init__(placeholder="Select a template",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        with shelve.open('UserMessageCache', writeback = True) as umc:
            umc[str(interaction.user.id)][0] = str(self.values[0])
            umc.close()
        await interaction.response.edit_message(view=MainMenu(str(interaction.user.id)))

"""
====================
Template 2 Section
====================
"""
class Template2MenuButton(Button):
    def __init__(self,label:str,style=discord.ButtonStyle.green):
        super().__init__(label=label, style=style, custom_id=label + "_2", emoji='👉')
    async def callback(self,interaction: discord.Interaction):
        view = Template2SelectView()
        await interaction.response.edit_message(view=view)

class Template2SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Template2Select())
        self.add_item(BackButton(label="Go Back"))

class Template2Select(discord.ui.Select):
    def __init__(self):
        options = []
        for k in Templates:
            k = discord.SelectOption(label=k.replace('$word','****'),description=k.replace('$word','****'))
            if k not in options:
                options.append(k)
        super().__init__(placeholder="Select a template",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        with shelve.open('UserMessageCache',writeback = True) as umc:
            umc[str(interaction.user.id)][3] = str(self.values[0])
            umc.close()
        await interaction.response.edit_message(view=MainMenu(str(interaction.user.id)))

"""
====================
Conjunction Section
====================
"""
class ConjunctionMenuButton(Button):
    def __init__(self,label:str,style=discord.ButtonStyle.green):
        super().__init__(label=label, style=style, custom_id=label, emoji='👉')
    async def callback(self,interaction: discord.Interaction):
        view = ConjunctionSelectView()
        await interaction.response.edit_message(view=view)

class ConjunctionSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(ConjunctionSelect())
        self.add_item(BackButton(label="Go Back"))

class ConjunctionSelect(discord.ui.Select):
    def __init__(self):
        options = []
        for k in Conjunctions:
            k = discord.SelectOption(label=k,description=k)
            if k not in options:
                options.append(k)
        super().__init__(placeholder="Select a conjunction",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        with shelve.open('UserMessageCache',writeback = True) as umc:
            umc[str(interaction.user.id)][2] = str(self.values[0])
            umc.close()
        await interaction.response.edit_message(view=MainMenu(str(interaction.user.id)))

"""
====================
Word Section
====================
"""
class WordMenuButton(Button):
    def __init__(self,label:str,style=discord.ButtonStyle.green):
        super().__init__(label=label, style=style, custom_id=label, emoji='👉')
    async def callback(self,interaction: discord.Interaction):
        view = WordCategorySelectView()
        await interaction.response.edit_message(view=view)

class WordCategorySelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(SelectWordCategory())
        self.add_item(BackButton(label="Go Back"))

class SelectWordCategory(discord.ui.Select):
    selfcat = ""
    def __init__(self):
        options = []
        for k, v in CategoriesSplit.items():
            start=str(v[0])
            end=str(v[-1])
            k = discord.SelectOption(label=k,description=start + " - " + end)
            if k not in options:
                options.append(k)
        super().__init__(placeholder="Select a word category",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        buttons = []
        selfcat = self.values[0]
        if type(CategoriesSplit.get(selfcat)) == list:
            for word in CategoriesSplit.get(selfcat):
                if word not in buttons and word != None:
                    buttons.append(word)
        if type(CategoriesSplit.get(selfcat)) == str and CategoriesSplit.get(selfcat) not in buttons and CategoriesSplit.get(selfcat) != None:
            buttons.append(CategoriesSplit.get(selfcat))
        await interaction.response.edit_message(view=WordSelectDropdownView(buttons))

class WordSelectDropdownView(discord.ui.View):
    def __init__(self, options):
        super().__init__()
        self.add_item(WordSelect(options))
        self.add_item(BackButton(label="Go Back"))

class WordSelect(discord.ui.Select):
    def __init__(self, options):
        woptions = []
        for k in options:
            k = discord.SelectOption(label=k,description=k)
            if k not in options:
                woptions.append(k)
        super().__init__(placeholder="Select a word",max_values=1,min_values=1,options=woptions)
    async def callback(self, interaction: discord.Interaction):
        with shelve.open('UserMessageCache',writeback = True) as umc:
            umc[str(interaction.user.id)][1] = str(self.values[0])
            umc.close()
        await interaction.response.edit_message(view=MainMenu(str(interaction.user.id)))

"""
====================
Word 2 Section
====================
"""
class Word2MenuButton(Button):
    def __init__(self,label:str,style=discord.ButtonStyle.green):
        super().__init__(label=label, style=style, custom_id=label + "_2", emoji='👉')
    async def callback(self,interaction: discord.Interaction):
        view = Word2CategorySelectView()
        await interaction.response.edit_message(view=view)

class Word2CategorySelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(SelectWord2Category())
        self.add_item(BackButton(label="Go Back"))

class SelectWord2Category(discord.ui.Select):
    selfcat2 = ""
    def __init__(self):
        options = []
        for k, v in CategoriesSplit.items():
            start=str(v[0])
            end=str(v[-1])
            k = discord.SelectOption(label=k,description=start + " - " + end)
            if k not in options:
                options.append(k)
        super().__init__(placeholder="Select a word category",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        word2=[]
        selfcat2 = self.values[0]
        if type(CategoriesSplit.get(selfcat2)) == list:
            for word in CategoriesSplit.get(selfcat2):
                if word not in word2:
                    word2.append(word)
            await interaction.response.edit_message(view=Word2SelectDropdownView(word2))
        if type(CategoriesSplit.get(selfcat2)) == str and CategoriesSplit.get(selfcat2) not in word2:
            word2.append(CategoriesSplit.get(selfcat2))
            await interaction.response.edit_message(view=Word2SelectDropdownView(word2))

class Word2SelectDropdownView(discord.ui.View):
    def __init__(self, options):
        super().__init__()
        self.add_item(Word2Select(options))
        self.add_item(BackButton(label="Go Back"))

class Word2Select(discord.ui.Select):
    def __init__(self, options):
        woptions = []
        for k in options:
            k = discord.SelectOption(label=k,description=k)
            if k not in options:
                woptions.append(k)
        super().__init__(placeholder="Select a word",max_values=1,min_values=1,options=woptions)
    async def callback(self, interaction: discord.Interaction):
        with shelve.open('UserMessageCache',writeback = True) as umc:
            umc[str(interaction.user.id)][4] = str(self.values[0])
            umc.close()
        await interaction.response.edit_message(view=MainMenu(str(interaction.user.id)))

"""
====================
Gesture Section
====================
"""
class GestureMenuButton(Button):
    def __init__(self,label:str,style=discord.ButtonStyle.green):
        super().__init__(label=label, style=style, custom_id=label,emoji='👉')
    async def callback(self,interaction: discord.Interaction):
        view = GestureCategorySelectView()
        await interaction.response.edit_message(view=view)

class GestureCategorySelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(SelectGestureCategory())
        self.add_item(BackButton(label="Go Back"))

class SelectGestureCategory(discord.ui.Select):
    selfcat2 = ""
    def __init__(self):
        options = []
        for k, v in GesturesSplit.items():
            start=str(v[0])
            end=str(v[-1])
            k = discord.SelectOption(label=k,description=start + " - " + end)
            if k not in options:
                options.append(k)
        super().__init__(placeholder="Select a Gesture category",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        gesturelist=[]
        selfcat2 = self.values[0]
        if type(GesturesSplit.get(selfcat2)) == list:
            for word in GesturesSplit.get(selfcat2):
                if word not in gesturelist:
                    gesturelist.append(word)
            await interaction.response.edit_message(view=GestureSelectView(gesturelist))
        if type(GesturesSplit.get(selfcat2)) == str and GesturesSplit.get(selfcat2) not in gesturelist:
            gesturelist.append(GesturesSplit.get(selfcat2))
            await interaction.response.edit_message(view=GestureSelectView(gesturelist))

class GestureSelectView(discord.ui.View):
    def __init__(self, options):
        super().__init__()
        self.add_item(GestureSelect(options))
        self.add_item(BackButton(label="Go Back"))

class GestureSelect(discord.ui.Select):
    def __init__(self, options):
        woptions = []
        for k in options:
            k = discord.SelectOption(label=k,description=k)
            if k not in options:
                woptions.append(k)
        super().__init__(placeholder="Select a Gesture",max_values=1,min_values=1,options=woptions)
    async def callback(self, interaction: discord.Interaction):
        with shelve.open('UserMessageCache',writeback = True) as umc:
            umc[str(interaction.user.id)][5] = str(self.values[0])
            umc.close()
        await interaction.response.edit_message(view=MainMenu(str(interaction.user.id)))

"""
====================
Embed Section
====================
"""
class EmbedView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.count = 0
        self.voters = []
    
    @discord.ui.button(label="Applaud",style=discord.ButtonStyle.green, emoji='👍',row=1)
    async def ApplaudButton(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user.id not in self.voters:
            self.count = self.count + 1
            self.voters.append(interaction.user.id)
        currenttier = thresholdcheck(self.count)
        embed=interaction.message.embeds[0]
        embed.set_field_at(index=0, name="Appraisals: ", value=str(self.count), inline=True)
        embed.set_thumbnail(url=str(MessageImageLinks.get(currenttier)))
        await interaction.response.edit_message(view=self,embed=embed, attachments =[])
    
    @discord.ui.button(label="Disparage",style=discord.ButtonStyle.red, emoji='👎',row=1)
    async def DisparageButton(self, interaction:discord.Interaction, button:discord.ui.Button):
        if interaction.user.id not in self.voters:
            self.count = self.count + 1
            self.voters.append(interaction.user.id)
        currenttier = thresholdcheck(self.count)
        embed=interaction.message.embeds[0]
        embed.set_field_at(index=0, name="Appraisals: ", value=str(self.count), inline=True)
        embed.set_thumbnail(url=str(MessageImageLinks.get(currenttier)))
        await interaction.response.edit_message(view=self, embed=embed, attachments =[])

"""
====================
Main Menu Section
====================
"""
class BackButton(Button):
    def __init__(self,label:str,style=discord.ButtonStyle.red):
        super().__init__(label=label, style=style, custom_id=label, emoji='🔙')
    async def callback(self,interaction: discord.Interaction):
        view = MainMenu(str(interaction.user.id))
        await interaction.response.edit_message(view=view)

class MainMenu(discord.ui.View):
    def __init__(self,userid):
        #TemplateSelect.__init__(self,values)
        super().__init__()
        with shelve.open('UserMessageCache',writeback = True) as umc:
            Template_Label     = umc[userid][0]
            Word_Label         = umc[userid][1]
            Conjunction_Label  = umc[userid][2]
            Template2_Label    = umc[userid][3]
            Word2_Label        = umc[userid][4]
            Gesture_Label      = umc[userid][5]
            umc.close()
        self.Template_Label   = Template_Label   
        self.Word_Label       = Word_Label       
        self.Conjunction_Label= Conjunction_Label
        self.Template2_Label  = Template2_Label  
        self.Word2_Label      = Word2_Label      
        self.Gesture_Label    = Gesture_Label    
        msggesture=self.Gesture_Label
        msgtemplate = self.Template_Label.replace('****','$word')
        msgtemplate=genTemplate(msgtemplate)
        msgword = genWordNew(self.Word_Label)
        msgconjunction = genConjunctionNew(self.Conjunction_Label)
        msgtemplate2 = self.Template2_Label.replace('****','$word')
        msgtemplate2 = genTemplate(msgtemplate2)
        msgword2 = genWordNew(self.Word2_Label) 
        print(msgtemplate)
        print(msgword)
        print(msgconjunction)
        print(msgtemplate2)
        print(msgword2)
        if (msgword != None) and hasattr(msgtemplate,'substitute')==True:
            Message = (msgtemplate.substitute(word = msgword))
            self.Message = Message
        if (msgword2 != None) and (msgword != None) and hasattr(msgtemplate,'substitute')==True and hasattr(msgtemplate2,'substitute') ==True and msgconjunction != None:
            Message = (
                msgtemplate.substitute(word = msgword) +
                msgconjunction +
                msgtemplate2.substitute(word = msgword2))
            self.Message = Message
        self.count = 0
        self.add_item(TemplateMenuButton(label=self.Template_Label,style=discord.ButtonStyle.blurple))
        self.add_item(WordMenuButton(label=self.Word_Label,style=discord.ButtonStyle.blurple))
        self.add_item(ConjunctionMenuButton(label=self.Conjunction_Label,style=discord.ButtonStyle.blurple))
        self.add_item(Template2MenuButton(label=self.Template2_Label,style=discord.ButtonStyle.blurple))
        self.add_item(Word2MenuButton(label=self.Word2_Label,style=discord.ButtonStyle.blurple))
        self.add_item(GestureMenuButton(label=self.Gesture_Label,style=discord.ButtonStyle.blurple))
    
    """
    Random Message
    """
    @discord.ui.button(label="Random", style=discord.ButtonStyle.blurple, emoji='🔄', row = 2)
    async def RandomMessage(self, interaction:discord.Interaction,button:discord.ui.Button):
        with shelve.open('UserMessageCache', writeback = True) as umc:
            rng = random.randint(0,3)
            umc[str(interaction.user.id)] = [
            "Template",
            "Word",
            "Conjunction",
            "Template 2",
            "Word 2",
            "Gesture",]
            umc[str(interaction.user.id)][0] = random.choice(Templates).replace('$word','****')
            umc[str(interaction.user.id)][1] = genWordNew("r")
            if rng == 2 or rng == 3:
                umc[str(interaction.user.id)][2] = random.choice(Conjunctions)
                umc[str(interaction.user.id)][3] = random.choice(Templates).replace('$word','****')
                umc[str(interaction.user.id)][4] = genWordNew("r")
            if rng == 1 or rng == 3:
                umc[str(interaction.user.id)][5] = genGesture("r")
            umc.close()
        view = MainMenu(str(interaction.user.id))
        await interaction.response.edit_message(view=view)

    """
    Reset Message
    """
    @discord.ui.button(label="Reset",style=discord.ButtonStyle.gray, emoji='🔄', row=2)
    async def ResetMessage(self, interaction:discord.Interaction, button:discord.ui.Button, ):
        with shelve.open('UserMessageCache', writeback=True) as umc:
            umc[str(interaction.user.id)] = [
            "Template",
            "Word",
            "Conjunction",
            "Template 2",
            "Word 2",
            "Gesture",]
            umc.close()
        await interaction.response.edit_message(view=MainMenu(str(interaction.user.id)), embed = None, attachments = [])
    """
    Construct and Send Message
    """
    @discord.ui.button(label="Send",style=discord.ButtonStyle.gray, emoji = '✅', row=2)
    async def ConstructMessage(self, interaction:discord.Interaction, button:discord.ui.Button):
        CMessage=self.Message
        appraisalcount = self.count
        currenttier = thresholdcheck(appraisalcount)
        MsgEmbed = discord.Embed(title = fMsgHeader, description = CMessage, color = 0x2a2823)
        MsgEmbed.set_footer(text = fMsgFooter)
        MsgEmbed.add_field(name="Appraisals: ", value=str(appraisalcount), inline=True)
        try:
            fGest = genGesture(self.Gesture_Label)
            self.file = discord.File(links.get(fGest), filename="image.png")
            MsgEmbed.add_field(name="Gesture:", value=fGest)
        except:
            pass
        MsgEmbed.set_image(url="attachment://image.png")
        MsgEmbed.set_thumbnail(url=str(MessageImageLinks.get(currenttier)))
        self.MsgEmbed = MsgEmbed
        MainMenu.MsgEmbed=MsgEmbed
        view = EmbedView()
        try:
            await interaction.response.send_message(view=view, embed=self.MsgEmbed, files = [self.file])
        except:
            await interaction.response.send_message(view=view, embed=self.MsgEmbed)
        return self.MsgEmbed
    """
    Load Message
    """
    @discord.ui.button(label="Load",style=discord.ButtonStyle.gray, emoji = '📂', row=2)
    async def LoadMessage(self, interaction:discord.Interaction, button:discord.ui.Button, ):
        with shelve.open('SavedMessages',writeback = True) as smdb:
            with shelve.open('UserMessageCache',writeback = True) as umc:
                umc[str(interaction.user.id)][0] = smdb[str(interaction.user.id)][0]
                umc[str(interaction.user.id)][1] = smdb[str(interaction.user.id)][1]
                umc[str(interaction.user.id)][2] = smdb[str(interaction.user.id)][2]
                umc[str(interaction.user.id)][3] = smdb[str(interaction.user.id)][3]
                umc[str(interaction.user.id)][4] = smdb[str(interaction.user.id)][4]
                umc[str(interaction.user.id)][5] = smdb[str(interaction.user.id)][5]
                smdb.close()
                umc.close()
        view = MainMenu(str(interaction.user.id))
        await interaction.response.edit_message(view=view)
    """
    Save Message
    """
    @discord.ui.button(label="Save",style=discord.ButtonStyle.gray, emoji = '💾', row=2)
    async def SaveMessage(self, interaction:discord.Interaction, button:discord.ui.Button, ):
        with shelve.open('SavedMessages',writeback = True) as smdb:
            smdb[str(interaction.user.id)] = [
            self.Template_Label,
            self.Word_Label,
            self.Conjunction_Label,
            self.Template2_Label,
            self.Word2_Label,
            self.Gesture_Label,]
            smdb.close()
        view = MainMenu(str(interaction.user.id))
        await interaction.response.edit_message(view=view)

client = MyClient()

@client.tree.command(name = "Finger Message Generator", description="Try Fingers But Hole!")
async def fingers(interaction: discord.Interaction):
    with shelve.open('UserMessageCache') as umc:
            umc[str(interaction.user.id)] = [
            "Template",
            "Word",
            "Conjunction",
            "Template 2",
            "Word 2",
            "Gesture",]
            umc.close()
    await interaction.response.send_message(view=MainMenu(str(interaction.user.id)), ephemeral=True)

token='Your Token Here'
client.run(token)
