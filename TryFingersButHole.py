from modules import genGesture
from modules import genMsgType
from modules import genTemplate
from modules import genWord
from modules import genConjunction

class FingerMessage:
    def __init__(self):
        genPhrase("r","r","r","r","r","r","r")
        self.Type = ""
        self.Message = ""
        self.Gesture = ""

logging = True
msgHeader = ""
msgFooter = ""

def genPhrase(msgtype, msgtemplate, msgword, msgconjunction = 'NA', msgtemplate2 = 'NA', msgword2 = 'NA', msggesture = 'NA'):
    if logging == True:
        f = open("log.txt", "a")
    msgtype =        genMsgType(msgtype)
    msgtemplate =    genTemplate(msgtemplate)
    msgword =        genWord(msgtype, msgword)
    msgconjunction = genConjunction(msgtype, msgconjunction)
    msggesture =     genGesture(msggesture)
    msgtemplate2 =   genTemplate(msgtemplate2)
    msgword2 =       genWord(msgtype, msgword2)

    """
    print("Message Type: " + str(FingerMessage.msgtype))
    print("Message Template: " + str(FingerMessage.msgtemplate))
    print("Message Word: " + str(FingerMessage.msgword))
    print("Message Conjunction: " + str(FingerMessage.msgconjunction))
    print("Message Gesture: " + str(FingerMessage.msggesture))
    print("Message Template 2: " + str(FingerMessage.msgtemplate2))
    print("Message Word 2: " + str(FingerMessage.msgword2))
    """

    if msgtype == 0:
        Message = (msgtemplate.substitute(word = msgword))
        FingerMessage.Type = msgtype
        FingerMessage.Message = Message
        print(FingerMessage.Message)
        if logging == True:
            f.write(Message)
        return Message
    if msgtype == 1:
        Message = (msgtemplate.substitute(word = msgword))
        Gesture = msggesture
        FingerMessage.Type = msgtype
        FingerMessage.Message = Message
        FingerMessage.Gesture = Gesture
        print(FingerMessage.Message)
        print(FingerMessage.Gesture)
        
        if logging == True:
            f.write(Message)
        return Message, Gesture
    if msgtype == 2:
        if msgword2 == None:
            print("ERROR! Valid Second **** word needed for this message type")
        else:
            Message = (
                msgtemplate.substitute(word = msgword) +
                msgconjunction +
                msgtemplate2.substitute(word = msgword2))
            FingerMessage.Type = msgtype
            FingerMessage.Message = Message
            print(FingerMessage.Message)
            if logging == True:
                f.write(Message)
            return Message
    if msgtype == 3:
        if msgword2 == None:
            print("ERROR! Valid Second **** word needed for this message type")
        else:
            Message = (
                msgtemplate.substitute(word = msgword) +
                msgconjunction +
                msgtemplate2.substitute(word = msgword2))
                
            Gesture = msggesture
            FingerMessage.Type = msgtype
            FingerMessage.Message = Message
            FingerMessage.Gesture = Gesture
            print(FingerMessage.Message)
            print(FingerMessage.Gesture)
            if logging == True:
                f.write(Message)
            return Message, Gesture
    f.close()

genPhrase("r","r","r","r","r","r","r")
