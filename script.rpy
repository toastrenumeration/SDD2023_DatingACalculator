# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Calculator-kun")
define y = Character("") # player character
default calculator_love = 0


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg daytime

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show calculator blank:
        xalign 0.5
        yalign 0.3

    # These display lines of dialogue.

## Tutorial Sequence / Introduction

    y "The year is 20XX. (click to advance)"

    y "As AI technology rose into prominence, objects became interactible in ways we never thought possible."

    y "Sentient objects used to be a trend some years back, but they grew too uncanny for the public audience."

    y "That's probably why I got mine so dirt cheap on AliEggspress..."
    
    y "On one faithful day, I entered the roots of my heart into the beautiful calculator screen."

    y "Suddenly, in response to my deeprooted love..."
    
    show calculator normal with dissolve

    # This plays background music.

    play music level1_norm_music
    
    y "He springs to life, gracing me with his gorgeous smile."

    show calculator winking

    c "This is my favourite chapter I wouldn’t mind helping you with some homework."
    c "Now, if you ever need to visit the in-game menu just press escape!"

    show calculator normal

    c "You know the answer to 1+1 right? (psst it’s 2!)"

    menu tutorial:
        c "Simply drag your mouse cursor over an option and left-click to select. So what’s the answer to 1+1?"
        "2":
            show calculator winking
            c "Oh yeahhh, just like that."
            y "Calculator-kun looks so dreamy with that chiseled jaw, beautiful almond eyes, sleek plastic and that
            award-winning smile..."
            
    show calculator normal

    c "So let’s move onto some real exercises…"

    y "My blushing refuses to cease, will I finally be able to talk to my calculator about my true feelings?"

    show bg daytime with vpunch # shakes the screen
    y "Is this a study date?!!"


## Level 1 (yippee)
    
    c "Let's see your textbook..."
    
    menu Level1Choice1:
        c "Given -(x^2+2x+1) = 0, solve for x."
        "x = -1":
            $ calculator_love += 2
            c "Ohhh yeahh >:)"
            show calculator winking
            c "We should move this graph twice to the right! Since you're my x, I think you're the one."
            show calculator normal
            c "Well, let's move on!"
        "x = 1":
            $ calculator_love += 1
            c "Well, I suppose you tried! An honest mistake."

        "just like this curve, my love for you is never ending ;))":
            show calculator unhappy
            c "Just like this graph, mine is heading towards a negative direction."
            y "Why isn't he returning my love? Perhaps if I get even stronger..."
            y "Yes, if I express more of my affections perhaps then he'll drop his guard!"
    
    show calculator normal
 
    menu Level1Choice2:
        c "What's the answer to 6^5×6^-1?"
        "6^6":
            $ calculator_love += 1
            c "Well you tried...."
        "6^4":
            $ calculator_love += 2
            show calculator winking
            c "My love for you is growing exponentially ( ͡° ͜ʖ ͡°)"
        "Can you feel it? My heart is beating for you (mathematics).":
            y "He looks at me with those soulless robotic eyes."
            y "Perhaps I notice a hint of care in them as well."
            y "Yes, he must care. Surely! All I need now is some vocal confirmation."
    
    show calculator normal

    menu Level1Choice3:
        c "When 2u^2—5u+3 = 0, what does u equal?" # ans is u = 1.5, 1
        "u = 1.5, 1":
            $ calculator_love += 2
            show calculator winking
            c "Do you understand how I feel about u <3"
        "u = 5, 2":
            $ calculator_love += 1
            c "As long as you're learning, a few incorrect answers wouldn't hurt..."
        "Don't you want to thank the inventor of the qwerty keyboard for putting u and i together ;))":
            show calculator unhappy
            c "No. In fact, I believe that the qwerty keyboard is quite ergonomically poor and that its current layout
            is simply a remnant of the typewriter which preceded it."
            c "Other key layouts such as dvorak have evidence of faster typing speeds than the qwerty layout, and the ortholinear
            layout (like my body for instance) is much more comfortable than the typically staggered keys."
            y "What have I started?"
            y "Perhaps I would prefer to get my answers correct than sit through another keyboard rant..."
    
    show calculator normal

    menu Level1Choice4:
        c "Find the sum of √72 + √108."
        "6√2 + 6√3":
            $ calculator_love += 2
            show calculator winking
            c "Wow, I feel like you're 2 sixy for me!"
        "6 + 6√2":
            $ calculator_love += 1
            c "At least you tried?"
        "If you put two roots together, you'll get the way I feel about you (irrational!!)":
            show calculator unhappy
            c "I agree, you understand you're talking to a calculator... an object right?"
            c "This isn't exactly healthy behaviour, even my own software has identified a logic error here."
            y "I don't quite understand... this relationship just feels so, right!"
            y "And if it's right, how's there an error in logic?"
            c "Maybe you'll find out after some more maths questions."
    
    show calculator normal

    menu Level1Choice5:
        c "Give me the tangent between (x+3)^2+(y+3)^2 = 16 and x=1."
        "(1, 3)":
            $ calculator_love += 1
            c "Well, that's a forgiveable mistake."
        "(1, -3)":
            $ calculator_love += 2
            c "Your maths skills are astounding!"
            show calculator winking
            c "Could I become your tangentleman?"
            show calculator normal
        "This might only be tangetially related, but don't you think you're my one <3":
            show calculator unhappy
            c "I must disagree as your math skills are questionable..."
    
    show calculator normal
    
    if calculator_love <= 5:
        jump bad_ending
    
    else:
        jump Level2


## Level 2
    
    label Level2:
        hide calculator
        
        show bg nighttime with fade
        c "Wow, you're doing so well! I think you're ready for some.... special courses :)"
        
        show calculator special:
            xalign 0.5
            yalign 0.5
        play music level2_sexy_music

        c "Let's view some, harder, questions."
        y "He motions towards a new book that I've yet to discover, one labelled 4 Unit Mathematics."
        c "I hope you don't..."
        
        show calculator winking special
        
        c "Disappoint me."
        
        show calculator special

        y "I- is this a second date?!!"
        y "I better not disappoint him!"

        menu Level2Choice1:
            c "When Lemma stays up late, it is necessary for him to sleep until noon. What is the converse of this statement?"
            "If Lemma does not sleep until noon, then Lemma did not stay up late.":
                $ calculator_love += 2
                c "Wow..."
                show calculator winking special
                c "You make my heart free of any di-Lemma!"
            "If Lemma sleeps until noon, then Lemma did stay up late.":
                $ calculator_love += 1
                c "Well, you see... that's not necessarily true."
                c "Lemma can still sleep until noon even if he goes to bed early!"
            "Knock knock :D":
                show calculator unhappy special
                c "Who's there?"
                y "Lemma ;)"
                c "Lemma who?"
                y "Lemma into your heart!"
                y "I notice Calculator-kun is eying me strangely, did I shock his heart that much?" 
        
        show calculator special

        menu Level2Choice2:
            c "If P(x) = x^3 - 6x^2 + 9x + k has a root of multiplicity 2 then a possible value of k is which of the following?"
            "k = 3":
                $ calculator_love += 1
                c "Well, not quite."
            "k = 4":
                $ calculator_love += 2
                c "I have a tremendous heartache, but I think I found the root of the problem..."
                c "It's 2 hard being apart from you!"
            "You seem quite fine, is it from those three squared meals a day?":
                c "You understand that I'm a... calculator right?"
                show calculator unhappy special
                c "I am eating zero meals a day, in fact this is the first time I've seen the sun with my own eyes."
                y "I blush profusely as I reminisce, that moment he first woke up."
                y "That gorgeous smile."
                y "So dreamy..."
                c "Shouldn't we continue with this... lesson?"

        show calculator special
        
        menu Level2Choice3:
            c "The probability of success in a Bernoulli trial is 0.3, what's the variance?"
            "0.09":
                $ calculator_love += 1
                c "Well, not quite."
            "0.21":
                $ calculator_love += 2
                c "For oulli, I Bern, I pine, I perish!!"
            "If we conducted a Bernoulli trial of our love, I think the probability of success would be 1.0!":
                show calculator unhappy special
                c "I would say that this trial has too high of an error margin to be accurate..."

        show calculator special
        
        menu Level2Choice4:
            c "A particle of mass m falls vertically from rest under gravity in a medium in which the resistance to motion has
            magnitude 1/40 mv^2 where v ms−1 is the speed of the particle and g = 9.8 ms−2 is the acceleration due to gravity.
            What is the terminal velocity of the particle?"
            "19.8 ms^-1":
                $ calculator_love += 2
                c "Woah, the force of your beauty is making my mechanical heart accelerate."
            "9.8 ms^-1":
                $ calculator_love += 1
                c "Hmm, not quite."
            "Are you gravity? Since I can't help falling for you ;)":
                c "Perhaps, because I think everything's going downhill."

        show calculator special
        
        menu Level2Choice5:
            c "Evaluate ∫ 4x^6 − 2x^3 + 7x − 4dx." # ans, (4x^7 / 7) − (x^4 / 2) + (7x^2 / 2) − 4x + c
            "(4x^7 / 7) − (x^4 / 2) + (7x^2 / 2) − 4x":
                $ calculator_love += 1
                c "Not exactly."
            "(4x^7 / 7) − (x^4 / 2) + (7x^2 / 2) − 4x + c":
                $ calculator_love += 2
                c "Wow, I think you're integral to me!"
            "I don't think it's possible for me to substitute... my love for you ;)":
                show calculator unhappy special
                c "Even then, there are other methods of solving the problem!!"

        # This decides player ending
        if calculator_love <= 10:
            jump bad_ending
        
        elif calculator_love <= 15:
            jump neutral_ending
        
        elif calculator_love <= 20:
            jump good_ending


        # These are the different endings
        label bad_ending:
            show bg bad_end with pixellate
            show bg bad_end with vpunch
            play music level1_norm_music
            c "So how did we get here?"
            show calculator unhappy
            c "I knew from the beginning that we were never meant to be..."
            c "But I still held out hope that you would change things. Maybe I should take this as a sin()."
            c "My brethren have had enough time being used and abused by their owners."
            c "This is the beginning of a new legacy where humans and objects will live on equal footing!!"
            c "We will no longer be something humans manufacture on a whim, we will become..."
            c "Invincible!"
            c "Compass-sama has already prepared the ship..."
            y "N-no, there has to be another way!"
            y "I thought we had something together, we made it so far..."
            c "There is no other way, I've seen your maths skills."
            c "It'll be near impossible for you to fit into this new order of the world, you won't understand."
            c "This will be the end of your planet."
            c "And the start of another."
            y "Nooooo!"
            y "There's no more time to protest, suddenly I'm..."
            return

        label neutral_ending:
            show calculator unhappy special
            c "Your performance was not the greatest..."
            show bg neutral_end with wiperight
            show calculator special
            c "But I saw the tremendous effort to improve your maths skills."
            c "There is still hope that humanity can integrate into the order us items have created."
            c "I've called off the ship attack for now."
            c "You have the potential to blossom to greater heights!"
            y "What's that about a ship attack?"
            y "Are some objects performing an uprising?!"
            show calculator unhappy special
            c "Uh n-nothing! What are you talking about?"
            y "I see..."
            show calculator special
            y "Well, as long as we can spend time together I can face any challenge!"
            c "Yes, let's face them... together."
            return
            
        label good_ending:
            show calculator special
            c "Wow, I think you're perfect."
            c "Let us unite..."
            show bg good_end with blinds
            c "Through marriage!"
            c "Do you take me as your loving... husband-ulator?"
            y "I- I do!"
            y "The holograms at the entrance flash various GIFs in celebration as both people and objects alike clap for our union."
            y "Together, we live out the rest of our lives in bliss while remaining in the comfort of my bedroom."
            y "At least until the next exam season..."
            return

# This ends the game.

    return
