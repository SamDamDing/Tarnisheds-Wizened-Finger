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
  msggesture = 'NA') #If you want to add a gesture, like in Elden Ring, type the name of the gesture in all caps and it will be used. No image or animation. Just text
```
# Message Types
```
0. Message
1. Message and Gesture
2. Message Conjunction Message
3. Message Conjunction Message Gesture
```

# Templates
```
0. $word ahead
1. No $word ahead
2. $word required ahead
3. Be wary of $word
4. Try $word
5. Likely $word
6. First off, $word
7. Seek $word
8. Still no $word...
9. Why is it always $word?
10. If only I had a $word...
11. Didn't expect $word...
12. Visions of $word...
13. Could this be a $word?
14. Time for $word
15. $word, O $word
16. Behold, $word!
17. Offer $word
18. Praise the $word
19. Let there be $word
20. Ahh, $word...
21. $word
22. $word!
23. $word?
24. $word...
```

# To do:

- Make all input integer based?
- Command Line Arguments
- Images for Gestures
- Gui?
