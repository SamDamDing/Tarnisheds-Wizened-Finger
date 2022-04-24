from modules import genGesture
from modules import genMsgType
from modules import genTemplate
from modules import genWord
from modules import genConjunction
msgHeader = "==========MESSAGE==========\n"
msgFooter = "\n==========MESSAGE=========="

def genPhrase1(msgtype, msgtemplate, msgword, msgconjunction = 'NA', msgtemplate2 = 'NA', msgword2 = 'NA', msggesture = 'NA'):
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
        print(msgHeader + 
        msgtemplate.substitute(word = msgword) + 
        msgFooter)
    if msgtype == 1:
        print(msgHeader + 
        msgtemplate.substitute(word = msgword) + "\n" + 
        msggesture + 
        msgFooter)
    if msgtype == 2:
        if msgword2 == None:
            print("ERROR! Valid **** Second word needed for this message type")
            pass
        else:
            print(msgHeader + 
            msgtemplate.substitute(word = msgword) + 
            msgconjunction + "\n" + 
            msgtemplate2.substitute(word = msgword2) + 
            msgFooter)
    if msgtype == 3:
        if msgword2 == None:
            print("ERROR! Valid Second **** word needed for this message type")
            pass
        else:
            print(msgHeader + 
            msgtemplate.substitute(word = msgword) + 
            msgconjunction + "\n" + 
            msgtemplate2.substitute(word = msgword2) + "\n" + 
            msggesture +  
            msgFooter)

genPhrase1(0,"r","r",",","r","r","r")
