# -*- coding: utf-8 -*-

from sys import argv, exit

script = argv

items = []

yes = ["Yes", "y", "Y", "yes"]
no = ['no', 'n', 'No', 'N']
forward = ['forward', 'Foward', 'front', 'Front', 'F', 'f', '#1', '1']
left = ['left', 'Left', 'l', 'L', '#2', '2']
right = ['right', 'Right', 'r', 'R', '#3', '3']
behind = ['behind', 'Behind', 'b', 'B', '#4', '4']
mirror_select = ['m', 'M', 'mirror', 'Mirror', 'touch mirror', 'Touch mirror']
tension_mirror = "You tap it and feel a small tension force, like water. \nYou try to lick it. It tastes like 'mirror'. \nThen you stick your arm in and, like an insect pulled into a drop of water, \nare pulled into the mirror."
tension_painting = "\nYou tap it and feel a small tension force, like water. \nYou try to lick it. It tastes like 'painting'.\nThen you stick your arm in and, like an insect pulled into a drop of water, \nare pulled into the painting."

def no_sense():
    print "That doesn't make sense.... \nPick a better answer %s!" %name
    print "Enter a direction or number like below:\n"
    print left
    print right
    print forward
    print behind
    print mirror_select, "\n\nNow the game will reboot as punishment."
    items[:] = []
    start()

def ending():
    print "Congrats on finding one of the true endings in the game!"

    raw_input()

    print "Play again to find all 3 true endings!"

    exit()

def lttp():
    print "Learn to type %s!" %name
    print "Enter a variation of 'yes' or 'no' like below:"
    print yes, no, "\nNow the game will reboot as punishment."
    items[:] = []
    start()

def walking():
    print "\nYou walk towards the painting."
    print "Upon further examination, you see more details."

def no_touch():
    print "\nOk."
    print "You go back to where you were, in the center of the room."
    start()

def death():
    print "You died! Good job!"
    items[:] = []
    exit(0)

def painting_1():
    #Finished!!!!
    """This takes you into the first painting"""
    raw_input()

    print "You land hard on concrete."
    print "Dazed, you look around as you feel a rhythmic thundering."
    print "The pelting rain only adds to your frustration."

    raw_input()

    print "You use the umbrella as you try to figure out what's happened."
    print "You now see the cause of all the thundering."
    print "The titan-looking monster is smashing his way through the city."

    raw_input()

    print "You notice the hero is wearing this metal equipment."
    print "It seems to enable them to move around easily."
    print "You notice one beside you. It's labled as 'VME'."
    print "Do you want to grab it?"

    grab = raw_input('\n>')

    if grab in yes:
        VME = 'VME'
        items.append(VME)
        print "\nYou added the VME to your items!!!"


        raw_input()

        print "Items:", items

        raw_input()

        print 'You also see a pair of swords. They look cool.'
        print "You decide to grab them as well."
        print "You added 'cool swords' to your items too!"
        items.append('cool swords')

        raw_input()

        print "Items:", items

        raw_input()

        print "Nice. You're feeling pretty prepared to help fight the titan."
        print "Do you want to go help the hero and kill a titan?"

        kill_titan = raw_input('\n>')

        if kill_titan in yes:
            print "\nThe titan sees you and starts charging at you."
            print "You use the VME to quickly navigate away and dodge their tackle."
            print "You realize how big the titan is and wonder if you're in over your head."

            raw_input()

            print "The hero tells you that you need to cut the titan at their neck to defeat them."
            print "The titan starts charging towards the hero."
            print "You take advantage in the titan's shift in focus."
            print "You swiftly go for the titan's neck and use your swords."
            print "You successfully kill the titan but break your swords."

            raw_input()

            items.pop(1)
            print "Items: ", items

            print "\nThe titan falls and, other than the thud it makes, there's silence."
            print "The hero nods in thanks and acknowledgement."
            print "You nod back."
            print "All of a sudden, you hear a ringing sound."

            raw_input()

            print "You wake up. It dawns on you that this was a dream."
            print "You realize you're late for school."
            print "You check if you still have the VME."

            raw_input()

            print "Items: ", items

            raw_input()

            print "Nice, you still do."
            print "You use it to make it to school on time!"

            raw_input('\n')

            ending()

        elif kill_titan in no:
            print "You realize this is outside your capabilities."
            print "You see the titan suddenly grab the hero. It doesn't look good."

            raw_input()

            print "You see the titan then look at you."
            print "You use the VME to run."
            print "The titan follows, right on your tail."
            print "You decide to use your cool swords to attack the titan."

            raw_input()

            print "You successfully cut the titan, but it seems to regnerate any damage done."
            print "You realize you don't know how to kill the titan...."

            raw_input()

            print "You run away as the titan gives chase again."
            print "The titan swats at you. You realize that you can't dodge."
            print "You see its giant hand coming for you."
            print "Your heart beats intensely as you know you've only a few beats left."

            raw_input()

            print "You suddenly hear an alarm ringing...."

            raw_input()

            print "You wake up. You realize it was all a dream."
            print "You also notice you're late for school!"

            items[:] = []

            print "You check if you've still the VME to help you get to school."

            raw_input()

            print "Items: ", items

            print "You do not....you arrive late to school"
            print "Your homeroom teacher gives you detention. For life."

            raw_input()

            death()

        else:
            lttp()

    elif grab in no:
        print "You pass on the VME."

        raw_input()

        print "You see the titan battling the hero a few meters away."
        print "You decide to check your items to see if you have anything that can help."

        regret = 'regret'
        items.append(regret)

        raw_input()

        print items
        print "You realize that you're pretty much useless in this situation..."

        raw_input()

        print "The titan swats the hero towards you."
        print "You look at the hero. They're a mess. They also look pretty dead."
        print "The titan now starts charging in your direction."
        print "The hero manages to murmur to you, 'run...'"
        print "You do exactly that."

        raw_input()

        print "You notice that for every step the titan takes, you take 20."
        print "You check your items one last time."

        reset = 'reset button'
        items.append(reset)

        raw_input()

        print items
        print "You notice the new item."
        print "Where did that come from?"
        print "Probably from some benevolant programmer."

        raw_input()

        print "You decide to use the reset button."

        items[:] = []

        print "(The game will now reset.)"

        raw_input()

        start()

    else:
        lttp()

def painting_2():
    #Finished!!!!
    """This takes you into the second painting"""
    print "\nYou touching the painting smudged it."
    print "You have ruined the painting. You are filled with shame."

    raw_input()

    print "You quickly look around to see if anyone saw what you did."
    print "No one did. You quickly walk back to the middle of the room."

    smudged_painting()

def painting_3():
    #Finished!!!!
    """This takes you into the third painting"""
    print "\nYou wake up a few meters outside the castle entrance."
    print "You see this strange flower that seems to almost be on fire."
    print "You reach out to grab it."

    raw_input()

    print "It burns you. You grab it by the stem this time."

    fire_flower = 'fire flower'

    items.append(fire_flower)

    print "\nYou've added 'fire flower' to your items!"

    raw_input()

    print "Items: ", items

    raw_input()

    print "You make your way to the castle."
    print "As you walk through the entrance, you notice the chubby person's no longer here."
    print "You start to remember the smug turtle creature and decide to look for it."
    print "You want to rub the fire flower in its smug face."

    raw_input()

    print "You see a staircase near the entrance."
    print "The only path behind it is a dead end, so you decide to climb it."
    print "You are still filled with determination."

    raw_input()

    print "After climbing for about 10 minutes and many, many stairs, you see the top \nof the stairs."
    print "You hear what sounds like an intense battle above."
    print "You also see a feather and two mushrooms just at the top of the stairs."
    print "Do you grab them?"

    grab = raw_input('\n>')

    if grab in yes:
        mushroom = 'mushroom'
        feather = 'feather'
        items.append(mushroom)
        items.append(mushroom)
        items.append(feather)

        print "\nYou added 2 mushrooms and a feather to your items!"

        print "\nItems: ", items

        raw_input()

        print "You come out of the stairs."
        print "You see the chubby person running around."
        print "The smug turtle monster is breathing fire."
        print "You now reconsider your plan of rubbing the flower in its face."

        raw_input()

        print "The chubby person calls out to you."
        print "They ask if you've any mushrooms."
        print "You nod and toss one over to them."

        items.pop(2)

        raw_input()

        print "Items: ", items

        raw_input()

        print "You see the person  eat the mushroom and instantly double in size."
        print "You decide to eat a mushroom too."

        items.pop(2)

        print "You trip. Insanely."
        print "You have a very short, but very intense episode."
        print "You contemplate the direction in your life and question where you're going."
        print "You have several epiphanies."

        raw_input()

        print "Items: ", items

        raw_input()

        print "After about 10 minutes, your trip ends."
        print "You see the plumber still struggling and yelling at you."
        print "You ground yourself in reality and focus on the fight."
        print "You are filled with determination."

        raw_input()

        determination = 'determination x2'
        items[:] = []

        items.append(determination)
        items.append(fire_flower)
        items.append(feather)

        print "Items: ", items

        raw_input()

        print "The chubby person asks for a fire flower."
        print "You take yours out."
        print "The turtle monster sees this and starts targeting their flames at you."
        print "You dodge to the right."

        raw_input()

        print "The heat is insanely hot."
        print "The chubby person jumps over the flame and reaches out for your fire flower."
        print "You manage to hand it off."

        raw_input()

        items.pop(1)
        print "Items: ", items

        raw_input()

        print "The chubby person further changes."
        print "Now they've a white and red overall outfit."
        print "It looks much more fashionable than before."

        raw_input()

        print "The turtle monster becomes enraged."
        print "They target youa again with their flames."
        print "The plumber rolls in front of you and uses their gloved hands to absorb the flames."
        print "They then send the flames back to the monster. They strafe away to keep you safe."""

        raw_input()

        print "You then show the chubby person the feather."
        print "They throw fireballs at the monster as they make their way back to you."
        print "They grab the feather and in a cloud of smoke transforms."

        raw_input()

        items.pop(1)
        print "Items: ", items

        raw_input()

        print "They now have the same outfit as before except with the addition of a yellow cape."
        print "It looks stupid."

        raw_input()

        print "The chubby person now flies over and upper cuts the monster."
        print "There's silence."

        raw_input()

        print "They nod at you in respect."
        print "You return the nod."
        print "They then pull out a whistle and quickly blow."

        raw_input()

        print "A gale comes through."
        print "The wind is strong and you can faintly hear the note of the whistle in the \nwind storm."
        print "It carries you away and the tone gets louder."
        print "You close your eyes."

        raw_input()

        print "All of the sudden you realize you stopped moving."
        print "You open your eyes and find youself in bed."
        print "You check your items to see if what happened was true."

        raw_input()

        print "Items: ", items

        raw_input()

        print "You sit and wonder. Then you realize you've school that day."
        print "You tap into your determination and the epiphanies of that mushroom trip \n to get you out of bed."

        items.pop(0)
        print "Items: ", items

        raw_input()

        print "With your newfound clarity in life, you make moves and accomplish everything you \n set your mind too."

        raw_input()

        ending()

    elif grab in no:
        print "You think for a while and decide to pass on the items."

        raw_input()

        print "You hear a boom and decide to exit the staircase to explore what that was."
        print "As you exit the stair case, you are hit by a giant bullet bill."

        death()

    else:
        lttp()

def painting_4():
    #Finished!!!
    """This takes you into the fourth painting"""
    print "\nYou land face first."
    print "You stand up and compose yourself."
    print "You suddenly hear yelling."

    raw_input()

    print "\"Damn you All Might!!!!\" booms a voice."
    print "You scan the area and see a person with a disfigured face."
    print "They are being blown away by the punch of a person with a disfigured arm."
    print "You instantly put together that this is All Might defeating All For One."

    raw_input('\n(SPOILERS)!\n')

    print "The rest of the chapter from the manga plays out in front of you."
    print "As it wraps up, you notice 50,000 ₩ on the floor; score!"
    print "You decide to take it since there's no other people around at all."

    raw_input()

    money = '50,000 KRW'
    items.append(money)
    print "Items: ", items

    raw_input()

    print "You decide to go to that Purie store now."
    print "You are greeted by the nicest family of sister."
    print "They offer to sell you some jam. Do you buy some?\n"

    jam = raw_input('>')

    if jam in yes:

        coco = 'Coconut Jam'
        rose = "Rose Jam"
        wine = "Wine Jam"
        mango = "Mango Jam"

        print "You tell them yes and they show you their samples."
        print "After sampling many different jams for free, you find your favorites!"
        print "It comes out to exactly %s. Lucky!" % money

        raw_input()

        items.append(coco)
        items.append(rose)
        items.append(wine)
        items.append(mango)
        items.pop(0)

        print "Items: ", items

        raw_input()

        print "The Jam Fam thanks you for your patronage and they give you a gift as 'service'."
        print "Apparently, they've connects in the airline industry."
        print "It's a flight ticket home."

        raw_input()

        print "Nice! You instantly go home.\n"

        ending()

    elif jam in no:

        print "You stumble around and fall on a knife."

        death()

    else:
        lttp()

    exit(0)

def mirror():
    """This restarts the game"""
    print "You touch the mirror and a ripple spreads across its surface like a small pond."
    print "It's cool to the touch."

    raw_input()

    print tension_mirror

    raw_input()

    print "Once on the other side, you immediately start falling."
    print "You land on the floor hard. You look around."

    start()

def start():
    """This is the story that starts the game and offers you what world to explore"""

    raw_input()
    print "You're in a wide room with red carpeting, white walls."
    print "There's a painting on each of the 4 walls."
    print"Each painting is unique, depicting a distinctive scene."

    raw_input()

    print "The painting directly in front of you (#1) shows modern day Tokyo (東京)."
    print "You can't tell the season but it's raining."
    print "You notice you don't have an umbrella."
    print "You also notice that there's an umbrella under the painting."

    raw_input()
    print "There's some humanoid looking giant attacking the city."
    print "Some hero seems to be battling it. The hero is normal sized."
    print "You guess that the hero might lose, given the size difference. \nSucks to suck."

    raw_input()

    print "The picture to your left (#2) shows a forest in mid autumn."
    print "There's no animals or people in the picture."
    print "It's just of trees slowly losing their leaves."
    print "A slight breeze seems to be playing through the branches at that \nvery moment. It looks peaceful."

    raw_input()

    print "The picture to your right (#3) shows some kind of castle."
    print "It's spring and cherry blossoms seem to be falling slowly."

    print "\nThe castle stands tall and alone in the background."
    print "In the foreground of the painting, there's a path leading to it."
    print "The castle is easily accesible."

    raw_input()

    print "The painting behind you (#4) shows modern day Seoul (서울), in Hyehwa (혜화)."
    print "It looks like a hot summer day, the kind where cicadas don't shut up."
    print "You see people in brightly colored uniforms fighting."
    print "They have hairstyles only slightly less ridiculous than their clothing."

    raw_input()

    print "You can't tell who's winning or losing. Or who's good or evil (because \nwhat does good/evil even look like?). All you can see is that, aside "
    print "from the heroes, the city looks empty and only partially destroyed."

    raw_input()

    print "Above you is a super relfective mirror."
    print "There's no glare or anything at all in it."
    print "It looks unlike any other mirror you've ever seen before."
    print "You almost want to touch it. There is a ladder nearby....."

    raw_input()

    print "\tYou can go check out in detail any painting you want."
    print "\tOr you could go touch the mirror if that's your thing."
    print "\tYou can choose where to go from here. \n\tWhat do you want to do %s?" % name

    choice = raw_input('\n>')

    #painting_1 is finished
    if choice in forward :
        walking()
        print "The monster seems to be eating something human looking."
        print "The hero also looks like they've unresolved childhood trauma."

        raw_input()

        print "You also look at the umbrella. It's a nice umbrella."
        print "You decide to take it."

        umbrella = 'umbrella'
        items.append(umbrella)

        print "\nItems: ", items

        print "\nWhile gazing at the picture, you find yourself wanting to touch it. \nDo you?"

        touch = raw_input('\n>')

        if touch in yes:
            print tension_painting
            painting_1()

        elif touch in no:
            no_touch()

        else:
            lttp()

    #mirror is finished
    elif choice in mirror_select:
        print "\nYou grab the ladder and prop it up against a blank portion of one of the walls."
        print "You start climbing it. Hopefully you're not afraid of heights."
        print "As you climb, you notice the red carpeting in the room is really distasteful."

        raw_input()
        mirror()

    #painting_2 finished
    elif choice in left:
        walking()
        print "You now notice the cute squirrels in the background."
        print "You almost want to touch the picture. Do you?"


        touch = raw_input('\n>')

        if touch in yes:
            painting_2()

        elif touch in no:
            no_touch()

        else:
            lttp()

    #painting_3
    elif choice in right:
        walking()
        print "You notice a short looking, chubby person with really bad fashion taste."
        print "He's standing at the entrance of the castle."
        print "You are filled with determination by looking at them."

        raw_input()

        determination = 'determination'
        items.append(determination)

        print "Items: ", items

        raw_input()

        print "You also see some huge turtle-looking creature with an even bigger nose."
        print "It looks smug."
        print "You automatically side with the short person because who likes smugness."

        raw_input()

        print "You want to touch the picture to see if it's really oil-based paint. \nDo you?"

        touch = raw_input('\n>')

        if touch in yes:
            painting_3()

        elif touch in no:
            print "You've just lost all determination for some reason."

            raw_input()

            items[:] = []
            print "\nItems: ", items
            no_touch()

        else:
            lttp()

    #painting_4
    elif choice in behind:
        walking()

        raw_input()

        print "You notice all the bulding names are blurred except for one."
        print "It says 'PURIE'."
        print "You debate if you should touch the picture or not. Do you?"

        touch = raw_input('\n>')

        if touch in yes:
            print tension_painting
            painting_4()

        elif touch in no:
            no_touch()

        else:
            lttp()

    else:
        no_sense()

#copy painting_4 here when finished in start()
def smudged_painting():
    """This is the the same as start() but now painting_2 is smudged"""

    raw_input()
    print "You're in a wide room with red carpeting, white walls."
    print "There's a painting on each of the 4 walls."
    print"Each painting is unique, depicting a distinctive scene."

    raw_input()

    print "The painting directly in front of you (#1) shows modern day Tokyo (東京)."
    print "You can't tell the season but it's raining."
    print "You notice you don't have an umbrella."
    print "You also notice that there's an umbrella under the painting."

    raw_input()
    print "There's some humanoid looking giant attacking the city."
    print "Some hero seems to be battling it. The hero is normal sized."
    print "You guess that the hero might lose, given the size difference. \nSucks to suck."

    raw_input()

    print "The picture to your left (#2) shows a forest in mid autumn."
    print "There's no animals or people in the picture."
    print "It's just of trees slowly losing their leaves."
    print "A slight breeze seems to be playing through the branches at that \nvery moment. It looks peaceful."

    raw_input()

    print "The picture to your right (#3) shows some kind of castle."
    print "It's spring and cherry blossoms seem to be falling slowly."

    print "\nThe castle stands tall and alone in the background."
    print "In the foreground of the painting, there's a path leading to it."
    print "The castle is easily accesible."

    raw_input()

    print "The painting behind you (#4) shows modern day Seoul (서울), in Hyehwa (혜화)."
    print "It looks like a hot summer day, the kind where cicadas don't shut up."
    print "You see people in brightly colored uniforms fighting."
    print "They have hairstyles only slightly less ridiculous than their clothing."

    raw_input()

    print "You can't tell who's winning or losing. Or who's good or evil (because \nwhat does good/evil even look like?). All you can see is that, aside "
    print "from the heroes, the city looks empty and only partially destroyed."

    raw_input()

    print "Above you is a super relfective mirror."
    print "There's no glare or anything at all in it."
    print "It looks unlike any other mirror you've ever seen before."
    print "You almost want to touch it. There is a ladder nearby....."

    raw_input()

    print "\tYou can go check out in detail any painting you want."
    print "\tOr you could go touch the mirror if that's your thing."
    print "\tYou can choose where to go from here. \n\tWhat do you want to do %s?" % name

    choice = raw_input('\n>')

    #painting_1 is finished
    if choice in forward :
        walking()
        print "The monster seems to be eating something human looking."
        print "The hero also looks like they've unresolved childhood trauma."

        raw_input()

        print "You also look at the umbrella. It's a nice umbrella."
        print "You decide to take it."

        umbrella = 'umbrella'
        items.append(umbrella)

        print "\nItems: ", items

        print "\nWhile gazing at the picture, you find yourself wanting to touch it. \nDo you?"


        touch = raw_input('\n>')

        if touch in yes:
            print tension_painting
            painting_1()

        elif touch in no:
            no_touch()

        else:
            lttp()

    #mirror is finished
    elif choice in mirror_select:
        print "\nYou grab the ladder and prop it up against a blank portion of one of the walls."
        print "You start climbing it. Hopefully you're not afraid of heights."
        print "As you climb, you notice the red carpeting in the room is really distasteful."

        raw_input()
        mirror()

    #painting_2 finished
    elif choice in left:
        print "\nYou walk towards the painting with your head down."
        print "You see how you've ruined an otherwise nice painting."
        print "You are filled with shame."

        raw_input()

        print "You walk back to the center of the room."
        smudged_painting()

    #painting_3
    elif choice in right:
        walking()
        print "You notice a short looking, chubby person with really bad fashion taste."
        print "He's standing at the entrance of the castle."
        print "You are filled with determination by looking at them."

        raw_input()

        determination = 'determination'
        items.append(determination)

        print "Items: ", items

        raw_input()

        print "You also see some huge turtle-looking creature with an even bigger nose."
        print "It looks smug."
        print "You automatically side with the short person because who likes smugness."

        raw_input()

        print "You want to touch the picture to see if it's really oil-based paint. \nDo you?"

        touch = raw_input('\n>')

        if touch in yes:
            painting_3()

        elif touch in no:
            print "You've just lost all determination for some reason."

            raw_input()

            items[:] = []
            print "\nItems: ", items
            no_touch()

        else:
            lttp()

    #Paste painting_4 HERE:
    elif choice in behind:
        walking()

        raw_input()

        print "You notice all the bulding names are blurred except for one."
        print "It says 'PURIE'."
        print "You debate if you should touch the picture or not. Do you?"

        touch = raw_input('\n>')

        if touch in yes:
            print tension_painting
            painting_4()

        elif touch in no:
            no_touch()

        else:
            lttp()

    else:
        no_sense()

print "Welcome to the game My Attack on Super Paintings!"
name = raw_input("What's your name? \n\n>")

print "\nWelcome %s!!!" % name

start()
exit(0)
