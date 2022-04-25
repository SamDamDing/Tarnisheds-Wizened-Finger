# Try Fingers
# But Hole
### A Discord bot to create random Finger Messages like the ones in Elden Ring with Python.

Using `genPhrase("r", "r", "r", "r", "r", "r", "r")` in `TryFingersButHole.py` will generate a random phrase. Can also change the args to generate a message.
```py
genPhrase(
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
# Conjunctions
### Note: You must leave the `\n` as part of the message
- `'\nand then '`
- `'\nor '`
- `'\nbut '`
- `'\ntherefore '`
- `'\nin short '`
- `'\nexcept '`
- `'\nby the way '`
- `'\nso to speak '`
- `'\nall the more '`
- `',\n'`

# Gestures

- `'AS YOU WISH'`
- `'BALLED UP'`
- `'BECKON'`
- `'BOW'`
- `'BRAVO!'`
- `'BY MY SWORD'`
- `'CALM DOWN!'`
- `'CASUAL GREETING'`
- `'CROSSED LEGS'`
- `'CURTSY'`
- `'DEJECTION'`
- `'DESPERATE PRAYER'`
- `'DOZING CROSS-LEGGED'`
- `'ERUDITION'`
- `'EXTREME REPENTANCE'`
- `'FANCY SPIN'`
- `'FINGER SNAP'`
- `'FIRE SPUR ME'`
- `'GOLDEN ORDER TOTALITY'`
- `'GROVEL FOR MERCY'`
- `'HEARTENING CRY'`
- `"HOSLOW'S OATH"`
- `'INNER ORDER'`
- `'JUMP FOR JOY'`
- `'MY LORD'`
- `'MY THANKS'`
- `'NOD IN THOUGHT'`
- `'OUTER ORDER'`
- `"PATCHES' CROUCH"`
- `'POINT DOWNWARDS'`
- `'POINT FORWARDS'`
- `'POINT UPWARDS'`
- `'POLITE BOW'`
- `'PRAYER'`
- `'RALLYING CRY'`
- `'RAPTURE'`
- `'REST'`
- `'REVERENTIAL BOW'`
- `'SITTING SIDEWAYS'`
- `'SPREAD OUT'`
- `'STRENGTH!'`
- `'THE RING'`
- `'TRIUMPHANT DELIGHT'`
- `'WAIT!'`
- `'WARM WELCOME'`
- `'WAVE'`
- `'WHAT DO YOU WANT?'`

# Words
### Enemies

```
'enemy', 'weak foe', 'strong foe', 'monster', 'dragon', 'boss', 'sentry', 'group', 'pack', 'decoy', 'undead', 'soldier', 'knight', 'cavalier', 'archer', 'sniper', 'mage', 'ordnance', 'monarch', 'lord', 'demi-human', 'outsider', 'giant', 'horse', 'dog', 'wolf', 'rat', 'beast', 'bird', 'raptor', 'snake', 'crab', 'prawn', 'octopus', 'bug', 'scarab', 'slug', 'wraith', 'skeleton', 'monstrosity', 'ill-omened creature'
```

### People

```
'Tarnished', 'warrior', 'swordfighter', 'knight', 'samurai', 'sorcerer', 'cleric', 'sage', 'merchant', 'teacher', 'master', 'friend', 'lover', 'old dear', 'old codger', 'angel', 'fat coinpurse', 'pauper', 'good sort', 'wicked sort', 'plump sort', 'skinny sort', 'lovable sort', 'pathetic sort', 'strange sort', 'nimble sort', 'laggardly sort', 'invisible sort', 'unfathomable sort', 'giant sort', 'sinner', 'thief', 'liar', 'dastard', 'traitor', 'pair', 'trio', 'noble', 'aristocrat', 'hero', 'champion', 'monarch', 'lord', 'god'
```

### Things

```
'item', 'necessary item', 'precious item', 'something', 'something incredible', 'treasure chest', 'corpse', 'coffin', 'trap', 'armament', 'shield', 'bow', 'projectile weapon', 'armor', 'talisman', 'skill', 'sorcery', 'incantation', 'map', 'material', 'flower', 'grass', 'tree', 'fruit', 'seed', 'mushroom', 'tear', 'crystal', 'butterfly', 'bug', 'dung', 'grace', 'door', 'key', 'ladder', 'lever', 'lift', 'spiritspring', 'sending gate', 'stone astrolabe', 'Birdseye Telescope', 'message', 'bloodstain', 'Erdtree', 'Elden Ring'
```

### Battle_Tactics

```
'close-quarters battle', 'ranged battle', 'horseback battle', 'luring out', 'defeating one-by-one', 'taking on all at once', 'rushing in', 'stealth', 'mimicry', 'confusion', 'pursuit', 'fleeing', 'summoning', 'circling around', 'jumping off', 'dashing through', 'brief respite'
```

### Actions

```
'attacking', 'jump attack', 'running attack', 'critical hit', 'two-handing', 'blocking', 'parrying', 'guard counter', 'sorcery', 'incantation', 'skill', 'summoning', 'throwing', 'healing', 'running', 'rolling', 'backstepping', 'jumping', 'crouching', 'target lock', 'item crafting', 'gesturing'
```

### Situations

```
'morning', 'noon', 'evening', 'night', 'clear sky', 'overcast', 'rain', 'storm', 'mist', 'snow', 'patrolling', 'procession', 'crowd', 'surprise attack', 'ambush', 'pincer attack', 'beating to a pulp', 'battle', 'reinforcements', 'ritual', 'explosion', 'high spot', 'defensible spot', 'climbable spot', 'bright spot', 'dark spot', 'open area', 'cramped area', 'hiding place', 'sniping spot', 'recon spot', 'safety', 'danger', 'gorgeous view', 'detour', 'hidden path', 'secret passage', 'shortcut', 'dead end', 'looking away', 'unnoticed', 'out of stamina'
```

### Places

```
'high road', 'checkpoint', 'bridge', 'castle', 'fort', 'city', 'ruins', 'church', 'tower', 'camp site', 'house', 'cemetery', 'underground tomb', 'tunnel', 'cave', 'evergaol', 'great tree', 'cellar', 'surface', 'underground', 'forest', 'river', 'lake', 'bog', 'mountain', 'valley', 'cliff', 'waterside', 'nest', 'hole'
```

### Directions

```
'east', 'west', 'south', 'north', 'ahead', 'behind', 'left', 'right', 'center', 'up', 'down', 'edge'
```

### Body_Parts

```
'head', 'stomach', 'back', 'arms', 'legs', 'rump', 'tail', 'core', 'fingers'
```

### Affinities

```
'physical', 'standard', 'striking', 'slashing', 'piercing', 'fire', 'lightning', 'magic', 'holy', 'poison', 'toxic', 'scarlet rot', 'blood loss', 'frost', 'sleep', 'madness', 'death'
```

### Concepts
```
'life', 'Death', 'light', 'dark', 'stars', 'fire', 'Order', 'chaos', 'joy', 'wrath', 'suffering', 'sadness', 'comfort', 'bliss', 'misfortune', 'good fortune', 'bad luck', 'hope', 'despair', 'victory', 'defeat', 'research', 'faith', 'abundance', 'rot', 'loyalty', 'injustice', 'secret', 'opportunity', 'pickle', 'clue', 'friendship', 'love', 'bravery', 'vigor', 'fortitude', 'confidence', 'distracted', 'unguarded', 'introspection', 'regret', 'resignation', 'futility',
'on the brink', 'betrayal', 'revenge', 'destruction', 'recklessness', 'calmness', 'vigilance', 'tranquility', 'sound', 'tears', 'sleep', 'depths', 'dregs', 'fear', 'sacrifice', 'ruin'
```

### Phrases
```
'good luck', 'look carefully', 'listen carefully', 'think carefully', 'well done', 'I did it!', "I've failed...", 'here!', 'not here!', "don't you dare!", 'do it!', "I can't take this...", "don't think", 'so lonely...', 'here again...', 'just getting started', 'stay calm', 'keep moving', 'turn back', 'give up', "don't give up", 'help me...', "I don't believe it...", 'too high up', 'I want to go home...', "it's like a dream...", 'seems familiar...', 'beautiful...', 
"you don't have the right", 'are you ready?'
```
# To do:
- Appraisal reactions
- Appraisal system
- Appraisal rewards?
- Add a limiter to prevent spam
- Role permissions
- Cleanup code
- Transparent gesture images
- Downscale gesture images (probably controlled by a variable)
- User argument input (like `/fingers "r", "r", "r", "r", "r", "r", "r"`)
- Add info about who ordered the message in the embed footer.
- A method so that all messages must be sent in Fingers format. (Could be funny)
- Fork this into a Twitch bot?
- ~Images for Gestures~
- ~Discord bot?~
