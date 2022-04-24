from modules import genGesture
from modules import genMsgType
from modules import genTemplate
from modules import genWord
from modules import genConjunction

logging = True
msgHeader = "==========MESSAGE=========="
msgFooter = "==========MESSAGE=========="

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
    print("msgtype: " + str(msgtype))
    print("msgtemplate: " + str(msgtemplate))
    print("msgword: " + str(msgword))
    print("msgconjunction: " + str(msgconjunction))
    print("msggesture: " + str(msggesture))
    print("msgtemplate2: " + str(msgtemplate2))
    print("msgword2: " + str(msgword2))
    """
    if msgtype == 0:
        Message =(
            "\n" + msgHeader + 
            "\n" + msgtemplate.substitute(word = msgword) + 
            "\n" + msgFooter)
        print(Message)
        if logging == True:
            f.write(Message)
    if msgtype == 1:
        Message = (
            "\n" + msgHeader + 
            "\n" + msgtemplate.substitute(word = msgword) +  
            "\n" + msggesture + 
            "\n" + msgFooter)
        print(Message)
        if logging == True:
            f.write(Message)
    if msgtype == 2:
        if msgword2 == None:
            print("ERROR! Valid **** Second word needed for this message type")
            pass
        else:
            Message = (
                "\n" + msgHeader + 
                "\n" + msgtemplate.substitute(word = msgword) + 
                msgconjunction + " " + 
                msgtemplate2.substitute(word = msgword2) + 
                "\n" + msgFooter)
            print(Message)
            if logging == True:
                f.write(Message)
    if msgtype == 3:
        if msgword2 == None:
            print("ERROR! Valid Second **** word needed for this message type")
            pass
        else:
            Message = (
                "\n" + msgHeader + 
                "\n" + msgtemplate.substitute(word = msgword) + 
                msgconjunction + " " +
                msgtemplate2.substitute(word = msgword2) +   
                "\n" + msggesture +  
                "\n" + msgFooter)
            print(Message)
            if logging == True:
                f.write(Message)
    f.close()
    
genPhrase("r","r","r","r","r","r","r")
