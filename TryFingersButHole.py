from modules import genGesture
from modules import genMsgType
from modules import genTemplate
from modules import genWord
from modules import genConjunction

logging = True
msgHeader = "==========MESSAGE==========\n" #You can adjust these to whatever you want, or remove them if you wish. 
msgFooter = "\n==========MESSAGE=========="

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
    print("Message Type: " + str(msgtype))
    print("Message Template: " + str(msgtemplate))
    print("Message Word: " + str(msgword))
    print("Message Conjunction: " + str(msgconjunction))
    print("Message Gesture: " + str(msggesture))
    print("Message Template 2: " + str(msgtemplate2))
    print("Message Word 2: " + str(msgword2))
    """

    if msgtype == 0:
        Message = (
            msgHeader + 
            "\n" + msgtemplate.substitute(word = msgword) +
            "\n" + msgFooter + "\n")
        print(Message)
        if logging == True:
            f.write(Message)
    if msgtype == 1:
        Message = (
            msgHeader +
            "\n" + msgtemplate.substitute(word = msgword) + "\n" +
            "\n" + msggesture +
            "\n" + msgFooter + "\n")
        print(Message)
        if logging == True:
            f.write(Message)
    if msgtype == 2:
        if msgword2 == None:
            print("ERROR! Valid Second **** word needed for this message type")
            pass
        else:
            Message = (
                msgHeader +
                "\n" + msgtemplate.substitute(word = msgword) +
                msgconjunction +
                msgtemplate2.substitute(word = msgword2) +
                "\n" + msgFooter + "\n")
            print(Message)
            if logging == True:
                f.write(Message)
    if msgtype == 3:
        if msgword2 == None:
            print("ERROR! Valid Second **** word needed for this message type")
            pass
        else:
            Message = (
                msgHeader + 
                "\n" + msgtemplate.substitute(word = msgword) +
                msgconjunction +
                msgtemplate2.substitute(word = msgword2) + "\n" +
                "\n" + msggesture +
                "\n" + msgFooter + "\n")
            print(Message)
            if logging == True:
                f.write(Message)
    f.close()

genPhrase("r","r","r","r","r","r","r")
#genPhrase(0,"r","r",",\n","r","r","STRENGTH!")
#genPhrase(1,"r","r",",\n","r","r","STRENGTH!")
#genPhrase(2,"r","r",",\n","r","r","STRENGTH!")
#genPhrase(3,"r","r",",\n","r","r","STRENGTH!")
