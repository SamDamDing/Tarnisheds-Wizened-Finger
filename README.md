### A Python based Discord bot to create Finger Messages like the ones in Elden Ring
### Add: https://discord.com/api/oauth2/authorize?client_id=968116912196313169&permissions=8&scope=applications.commands%20bot
### You may also have to give the bot the highest role in your server settings. This is probably because of the usage of app commands. idk tbh...
### Use /fingers or /fingersmenu to access the message constructor.

Using `phraser("r", "r", "r", "r", "r", "r")` in `modules.py` will generate a random phrase.

You can use `/fingers` or `/fingersmenu` to display an ephemeral message constructor in the discord chat. You can click some buttons and dropdowns to set whatever message you want, use the `Save` button to save the message for later, use the `Load` button to load that saved message, `Reset` to reset the message constructor, `Random` to randomize the message constructor settings, and `Send` to send an embed of that constructed message along with a gesture if you so choose.


# Appraisal System
By setting the `appraisaltimeout` variable in `main.py`, you can change how long the message will accept appraisals. All unique user's appraisals will be counted and the embed will be updated. The amount of appraisals will determine the thumbnail image, just like how your message will appear brighter in game with more appraisals. The threshold values for this are set in `dicts.py` under `TierThresholds`




```py
phraser(
  msgtype #Accepts values 0-3.
  msgtemplate, #Accepts a templates.
  msgword, #If the word is a valid word, like in Elden Ring, it will be used in the template. 
  msgconjunction = 'NA', #If valid and the msgtype necessitates a conjunction, it will be used.
  msgtemplate2 = 'NA', #Accepts a template if msgtype necessitates this.
  msgword2 = 'NA') #If the word is a valid word, like in Elden Ring, it will be used in the second template. 
```
# Message Types

- `0` Message
- `1` Message and Gesture
- `2` Message Conjunction Message
- `3` Message Conjunction Message Gesture
### Anything invalid will make the message type random.


# Templates
- `"$word ahead"`
- `"No $word ahead"`
- `"$word required ahead"`
- `"Be wary of $word"`
- `"Try $word"`
- `"Likely $word"`
- `"First off, $word"`
- `"Seek $word"`
- `"Still no $word..."`
- `"Why is it always $word?"`
- `"If only I had a $word..."`
- `"Didn't expect $word..."`
- `"Visions of $word..."`
- `"Could this be a $word?"`
- `"Time for $word"`
- `"$word, O $word"`
- `"Behold, $word!"`
- `"Offer $word"`
- `"Praise the $word"`
- `"Let there be $word"`
- `"Ahh, $word..."`
- `"$word"`
- `"$word!"`
- `"$word?"`
- `"$word..."`

# Conjunctions

- `'and then'`
- `'or'`
- `'but'`
- `'therefore'`
- `'in short'`
- `'except'`
- `'by the way'`
- `'so to speak'`
- `'all the more'`
- `','`

# Gestures

- `"As You Wish"`
- `"Balled Up"`
- `"Beckon"`
- `"Bow"`
- `"Bravo!"`
- `"By My Sword"`
- `"Calm Down!"`
- `"Casual Greeting"`
- `"Crossed Legs"`
- `"Curtsy"`
- `"Dejection"`
- `"Desperate Prayer"`
- `"Dozing Cross-Legged"`
- `"Erudition"`
- `"Extreme Repentance"`
- `"Fancy Spin"`
- `"Finger Snap"`
- `"Fire Spur Me"`
- `"Golden Order Totality"`
- `"Grovel For Mercy"`
- `"Heartening Cry"`
- `"Hoslow'S Oath"`
- `"Inner Order"`
- `"Jump For Joy"`
- `"My Lord"`
- `"My Thanks"`
- `"Nod In Thought"`
- `"Outer Order"`
- `"Patches' Crouch"`
- `"Point Downwards"`
- `"Point Forwards"`
- `"Point Upwards"`
- `"Polite Bow"`
- `"Prayer"`
- `"Rallying Cry"`
- `"Rapture"`
- `"Rest"`
- `"Reverential Bow"`
- `"Sitting Sideways"`
- `"Spread Out"`
- `"Strength!"`
- `"The Ring"`
- `"Triumphant Delight"`
- `"Wait!"`
- `"Warm Welcome"`
- `"Wave"`
- `"What Do You Want?"`

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
- ~Appraisal reactions~
- ~Appraisal system~
- ~Appraisal rewards?~
- ~Buttons and Dropdowns~
- Server Settings
- Add a limiter to prevent spam
- Role permissions
- Cleanup code
- ~Transparent gesture images~
- Make gestures gifs?
- Personalized gesture images? That's a feasible stretch goal.
- Downscale gesture images? (probably controlled by a variable)
- ~User argument input (like `/fingers "r", "r", "r", "r", "r", "r", "r"`)~
- Add info about who ordered the message in the embed footer.
- A method so that all messages must be sent in Fingers format. (Could be funny)
- ~Add ability to save messages and recall with seed. `/fingers save saved_message` and `/fingers write saved_message`. Could add a reaction button to save too.~
- Fork this into a Twitch bot?
- Some kind of cross server message system like how messages can appear in a world from other players in their own world?
- ~Images for Gestures~
- ~Discord bot?~
