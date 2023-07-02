const Globals = {
  title: "Dollhouse",
  welcome: "Welcome to the Dollhouse",
  ellipsis: "...",
  terminate: ".",
  done: "\n*\n",
  about: "Dollhouse is a Hollow Earth Expedition. Navigate its intricate system of rooms, cavities and shattered halls in this Mundus Subterraneus to find the channel of water connecting its poles. Utter incantations to unlock ancient knowledge, forbidden to your caste, by the overloads, Monarchs and Kings who once tore these words from your soul. Assume the final room is a prime number. Abandon hope all ye who enter here.",
  help: `
General:
  I, INFO   - Type INFO to read the game description
  H, HELP   - Type HELP to print this help message
  R, ROOM   - Type ROOM to print information about the current chamber
  T, TILES  - Type TILES to print the floor tile dimensions of the current chamber (helpful for DIG)
  K, KEYS   - Type KEYS to list the KEYS in your inventory
  C, CHESTS - Type CHESTS to list the CHESTS in your inventory
  Q, QUIT   - Type QUIT to exit the current game

Movement:
  N, NORTH  - Try walking NORTH
  S, SOUTH  - Try walking SOUTH
  E, EAST   - Try walking EAST
  W, WEST   - Try walking WEST

Actions:
  F, FEEL   - Feel your way through the dark by commanding an object (helpful for finding KEYS). Examples: 'FEEL WALLS', 'FEEL GROUND', 'FEEL SOUTH DOOR',
  D, DIG    - Dig in the Hollow Earth for buried treasure at a specified position by commanding its x,y coordinates. Example 'DIG 2,3'
  U, UTTER  - Utter an incantation, or spell, by commanding its password (find KEYS to learn incantations). Example: 'UTTER ABRACADABRA'
  O, OPEN   - Open a CHEST by commanding its name and password. Example: 'OPEN CHEST LESSER PASSWORD123'
  L, LOOK   - LOOK at a DOOR, KEY or CHEST by commanding its name (or direction *DOOR only). Examples: 'LOOK SOUTH DOOR', 'LOOK CHEST LESSER', 'LOOK KEY THREE'
`,
  walk: {
    attempt: "Attempting to walk",
    directions: {
      indexes: {'N': 0, 'NORTH': 0, 'S': 1, 'SOUTH': 1, 'E': 2, 'EAST': 2, 'W': 3, 'WEST': 3},
      values: ["North", "South", "East", "West"]
    },
    success: "You walk",
    failure: [
      "You pick out a spot on the wall and walk straight into it with a *slam*!",
      "You run full tilt at the wall and ricochet to the ground. From your present position, collapsed on the floor, you remember what it was like to have owned a compass and a map in a past life.",
      "With zero scruples you pursue your path like a Kamikaze pilot. Smacking against the wall, you're still alive...for now.",
      "You collide with the wall and wince. You cannot yet walk through walls."
    ]
  },
  gate: {
    msg: "As you walk you come upon a locked gate. Perhaps you did not 'UTTER' the incantation to proceed to this dimension.",
    success: "You pass through to another dimension."
  },
  feel: {
    success: [
      "You feel your way around, nothing of interest... Wait! There we go, just as you're retracting your palm, some force compels you to plunge it deep within your soul. Reaching within yourself the magic key appears windsthin your being.",
      "You feel your way around. The movement is so rapid, are you being whirled away to another dimension? Overwhelmed by dizzying torpor, your insides feel as if they're being ripped apart by some force of magic far greater than gravity. Seeking to latch onto something solid, you pick a spot on the ground and stare at it depraved. Then, when you've given up hope, inside that depravity, the magic key appears."
    ],
    failure: [
      "Feels good.",
      "You feel your way around. Nothing of interest here.",
      "You feel your way around. Err...what were you just doing? You seem to be confused.",
      "Feeling your way around is metaphysical, although you fail to see why...",
      "Feels sharp.",
      "Feels lonely.",
      "Feels great.",
      "Feels bumpy.",
      "You are overwhelmed by feelings of great loss."
    ],
    completed: "You are holding the KEY.",
    dizziness: [
      "You feel dizzy.",
      "The room is spinning.",
      "You are suffering from vertigo."
    ],
    madness: [
      "All this running around in circles. Who am I? Where is this? Are you tripping on LSD or something? IDLKjhiwhat's thedasf poin...oif it aill...",
      "You find yourself logging out from existence in a state of beleaguered hysteria.",
      "Your brain spirals into demented madness.",
      "Kox pef fa lrakwj fhlao kldaltll. Ltiv zykl ne wui wfp?",
      "Why is a raven like a writing-desk?"
    ]
  },
  dig: {
    success: [
      "*Chink-chink* you just struck pay dirt! After considerable effort, you upheave the magic chest but it's locked.",
      "At this point you've dug yourself a trench 6-feet deep. You lay inside it and begin covering yourself with soil and start the long involved process of 'letting-go'. What a minute, reaching into the soil your hand comes upon a small box, how could you have missed this? The box is locked."
    ],
    failure: [
      "You dig yourself deeper and deeper into the hollow earth's core, will you find any meaning there? Not yet, at least.",
      "Toiling, labouring, lethargy, even...muttering...incantations...to yourself, as it may be...exhausting...",
      "You dig a trench 6-feet deep. There's no chest in here, but you lie down in the hollow earth nevertheless."
    ],
    completed: "You are holding the CHEST.",
    fatigue: [
      "You are feeling fatigued.",
      "You are feeling very fatigued.",
      "You are feeling fatigued in every part of your mind, soul and body."
    ],
    disabled: "*Chink-chink* the magma has cooled and hardened here. You won't be able to dig.",
    exhaustion: [
      "You collapse in exhaustion.",
      "You simply give up.",
      "You fall asleep like a narcolept."
    ]
  },
  incantation: {
    success: [
      "Incantation succeeds.",
      "Your spell charms the room.",
      "You smile with schadenfreude as your abominable curse is released into the room."
    ],
    failure: [
      "Nothing happens.",
      "Good thing no one is around to hear this. You sound like a blathering idiot.",
      "Who are you talking to anyway?",
      "Is that supposed to be a song or something?",
      "You wave your hands (in what you presume to be a 'magical gesture'). The spell fails, take those diamond hands elsewehere."
    ]
  },
  death: {
    madness: "Madness",
    fatigue: "Fatigue"
  },
  open: {
    chest: {
      success: "The chest opens!",
      failure: "The chest remains locked."
    }
  },
  look: {
    door: {
      success: "You look at the door.",
      failure: "You look around for a door, but you see a wall."
    },
    chest: {
      success: "You look at the chest.",
      failure: "You don't have that chest."
    },
    key: {
      success: "You look at the key.",
      failure: "You don't have that key."
    },
    unknown: "You look at nothing."
  },
  gameover: {
    success: {
      msg: "You seem to have navigated your own personal hell, well done.\n\nGAME OVER.\n\nYou may continue to wander these shallow hallways as a God.",
      state: "You are victorious",
      reset: false,
      godlike: true
    },
    failure: {
      msg: "\n\nGAME OVER\n\n",
      state: "You lose",
      reset: true,
      godlike: false
    }
  },
  reset: {
    msg: "Press a key to play again"
  },
  error: "Error processing instruction",
  prompt: "What now?"
}

export default { Globals };