import random
from string import Template
from dicts import Conjunctions, NoNewLineConjunctions, Message_Types, Templates, Categories, Gestures, Word_Categories, TierThresholds
def genMsgType(msgtype):
    if msgtype == "r":
        lm = len(Message_Types)-1
        msgtype = random.randint(0,lm)
        return msgtype
    if msgtype == 0:
        return msgtype
    if msgtype == 1:
        return msgtype
    if msgtype == 2:
        return msgtype
    if msgtype == 3:
        return msgtype
    else:
        print("Message Type Invalid")
        print("Please choose a number between 0 and 3")
        return "Message Type Invalid"

def genTemplate(msgtemplate):
    lt = len(Templates)-1
    if msgtemplate == "r":
        rt = random.randint(0,lt)
        msgtemplate = Template(Templates[rt])
        #print(msgtemplate)
        #print(lt)
        return msgtemplate
    if msgtemplate == "NA":
        pass
    else:
        try:
            msgtemplate = Templates[msgtemplate]
            #print(msgtemplate)
            return msgtemplate
        except:
            #print("Template number is out of range")
            #print("Try a number between 0 and " + str(lt))
            return "Template Invalid"

def genWord(msgtype, msgword):
    valid = False
    if msgword == "r":
        rwordcat = random.choice(list(Categories))
        lw = len(Categories.get(rwordcat))-1
        rw = random.randint(0,lw)
        msgword = Categories.get(rwordcat)[rw]
        return msgword
    if msgtype == 2 or msgtype == 3:
        if msgword == "NA":
            pass
    else:
        for x in Categories:
            if msgword in Categories[x]:
                valid = True
        if valid == True:
            return msgword
        if valid != True:
            #print("Your **** is invalid.")
            #print("Please choose another")
            return "Word Invalid"

def genConjunction(msgtype, msgconjunction):
    lc = len(Conjunctions)-1
    if msgtype == 2 or msgtype == 3:
        if msgconjunction in Conjunctions:
            if msgconjunction in NoNewLineConjunctions:
                return msgconjunction
            else:
                return msgconjunction + "\n"
        if msgconjunction == "r":
            rc = random.randint(0,lc)
            #print(Conjunctions[rc])
            rconj = str(Conjunctions[rc])
            return rconj
        if msgconjunction == "NA":
            return ""
        if msgconjunction not in Conjunctions:
            print("Conjunction Invalid")
            print("Please Choose a Valid Conjunction")
            return "Conjunction Invalid"
    #else:
        #print("Conjunction are not needed for this Message Type")
        #print("Please Choose Another Message Type like 2 or 3")
        #return "NA"

def genGesture(msggesture):
    lg = len(Gestures)-1
    if msggesture == "r":
        rg = random.randint(0,lg)
        #print(Gestures[rg])
        return Gestures[rg]
    if msggesture == "NA":
        pass
    else:
        if msggesture in Gestures:
            #print(msggesture)
            return msggesture
        else:
            #print("Gesture is invalid")
            #print("Please try again")
            return "Gesture Invalid"

"""
These are some functions that list out all the possible parts of a message.
"""

y = -1

def listTemplates():
    y = -1
    for x in Templates:
        y=y+1
        print(str(y) + ". " + str(repr(x).replace("$word", "****")))

def listMessage_Types():
    y = -1
    for x in Message_Types:
        y = y+1
        print(str(y) + ". " + str(repr(x)))

def listWord_Categories():
    y = -1
    for x in Word_Categories:
        y = y+1
        print(str(y) + ". " + str(repr(x)))

def listConjunctions():
    y = -1
    for x in Conjunctions:
        y = y+1
        print(str(y) + ". " + str(repr(x)))

def listGestures():
    y = -1
    for x in Gestures:
        y = y+1
        #print(str(y) + ". " + str(repr(x)))
        print("- " + "`" + str(repr(x)) + "`")
def listWords():
    for item in Categories:
        #print("Word Category : {} \nWords : {}".format(str(repr(item)),str(repr(Categories[item]))) + "\n")
        print("{} \nWords : {}".format(str(repr(item)),str(repr(Categories[item]))) + "\n")

#listTemplates()
#listMessage_Types()
#listWord_Categories()
#listConjunctions()
#listGestures()
#listWords()

def thresholdcheck(appraisalcount):
    values = []
    for k, v in TierThresholds.items():
        if appraisalcount >= int(v):
            values.append(v)
    values.sort()
    y = values[-1]
    for k,v in TierThresholds.items():
        if y == v:
            return k
