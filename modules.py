import random
from re import A
from string import Template
from dicts import Conjunctions, NoNewLineConjunctions, Message_Types, Templates, Categories, Gestures, Word_Categories, TierThresholds
def genMsgType(msgtype):
    if type(msgtype) == str:
        if msgtype == "r":
            lm = len(Message_Types)-1
            msgtype = random.randint(0,lm)
            return msgtype
        if msgtype.isdigit() == True:
            msgtype = int(msgtype)
            print(type(msgtype))
            genMsgType(msgtype)
        else:
            return NameError("Message Type Invalid. Please choose a number between 0 and 3")
    if type(msgtype) == int:
        if len(Message_Types)-len(Message_Types) <= msgtype <= len(Message_Types)-1:
            return msgtype
        else:
            msgtype = "r"
            return genMsgType(msgtype)
            #return NameError("Message Type Invalid. Please choose a number between 0 and 3")

def genTemplate(msgtemplate):
    lt = len(Templates)-1
    if msgtemplate == "r":
        rt = random.randint(0,lt)
        msgtemplateTrue = Template(Templates[rt])
        return msgtemplateTrue
    if msgtemplate == "NA":
        pass
    else:
        if msgtemplate in Templates:
            i = Templates.index(msgtemplate)
            msgtemplateTrue = Template(Templates[i])
            return msgtemplateTrue
        else:
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
        try:
            if msgword == "NA":
                #print("NA: " + msgword)
                pass
            if any(msgword in val for val in Categories.values()) == True:
                return msgword
        except NameError:
            print("Word Invalid")
    if msgtype == 0 or msgtype == 1:
        if any(msgword in val for val in Categories.values()) == True:
            return msgword
def genWordNew(msgword):
    if msgword == "r":
        rwordcat = random.choice(list(Categories))
        lw = len(Categories.get(rwordcat))-1
        rw = random.randint(0,lw)
        msgword = Categories.get(rwordcat)[rw]
        return msgword
    if any(msgword in val for val in Categories.values()) == True:
        return msgword
def genConjunction(msgtype, msgconjunction):
    lc = len(Conjunctions)-1
    if msgtype == 2 or msgtype == 3:
        if msgconjunction in Conjunctions:
            if msgconjunction in NoNewLineConjunctions:
                return msgconjunction + "\n"
            else:
                return " \n" + msgconjunction + " "
        if msgconjunction == "r":
            rc = random.randint(0,lc)
            msgconjunction = str(Conjunctions[rc])
            if msgconjunction in NoNewLineConjunctions:
                return msgconjunction + "\n"
            else:
                return " \n" + msgconjunction + " "
        if msgconjunction == "NA":
            return ""
        if msgconjunction not in Conjunctions:
            print(msgconjunction)
            print("Conjunction Invalid")
            print("Please Choose a Valid Conjunction")
            return "Conjunction Invalid"
def genConjunctionNew(msgconjunction):
    lc = len(Conjunctions)-1
    if msgconjunction in Conjunctions:
        if msgconjunction in NoNewLineConjunctions:
            return msgconjunction + "\n"
        else:
            return " \n" + msgconjunction + " "
    if msgconjunction == "r":
        rc = random.randint(0,lc)
        msgconjunction = str(Conjunctions[rc])
        if msgconjunction in NoNewLineConjunctions:
            return msgconjunction + "\n"
        else:
            return " \n" + msgconjunction + " "
    if msgconjunction == "NA":
        return ""
    if msgconjunction not in Conjunctions:
        #print(msgconjunction)
        #print("Conjunction Invalid")
        #print("Please Choose a Valid Conjunction")
        return "Conjunction Invalid"
def genGesture(msggesture):
    lg = len(Gestures)-1
    if msggesture == "r":
        rg = random.randint(0,lg)
        return Gestures[rg]
    if msggesture == "NA":
        pass
    else:
        if msggesture in Gestures:
            return msggesture
        else:
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
    if len(values)>0:
        y = values[-1]
        for k,v in TierThresholds.items():
            if y == v:
                return k

def phraser(msgtype, msgtemplate, msgword, msgconjunction = 'NA', msgtemplate2 = 'NA', msgword2 = 'NA'):
    msgtype =        genMsgType(msgtype)
    msgtemplate =    genTemplate(msgtemplate)
    msgword =        genWord(msgtype, msgword)
    msgconjunction = genConjunction(msgtype, msgconjunction)
    msgtemplate2 =   genTemplate(msgtemplate2)
    msgword2 =       genWord(msgtype, msgword2)
    
    if (msgtype == 0 or msgtype == 1) and (msgword != None):
        Message = (msgtemplate.substitute(word = msgword))
        return Message
    if (msgtype == 2 or msgtype == 3) and (msgword2 != None):
        Message = (
            msgtemplate.substitute(word = msgword) +
            msgconjunction +
            msgtemplate2.substitute(word = msgword2))
        return Message
