# Try Fingers But Hole
Create Finger Messages like the ones in Elden Ring with Python

Using `genPhrase1("r","r","r",",","r","r","r")` will generate a random phrase.
```py
genPhrase1(
  msgtype #Accepts values 0-3.
  msgtemplate, #Accepts values 0-24.
  msgword, #If the word is a valid word, like in Elden Ring, it will be used in the template. 
  msgconjunction = 'NA', #If valid and the msgtype necessitates a conjunction, it will be used.
  msgtemplate2 = 'NA', #Accepts values 0-24 if msgtype necessitates this.
  msgword2 = 'NA', #If the word is a valid word, like in Elden Ring, it will be used in the second template. 
  msggesture = 'NA') #If you want to add a gesture, like in Elden Ring, type the name of the gesture in all caps and it will be used.
```

To do:

Command Line Arguments
Gui?
