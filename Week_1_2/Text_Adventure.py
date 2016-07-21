print("Your plane has crashed and you find yourself in the middle of a forest.  You are alse very hungry.")

print("BEGIN")

print("Type 'left' to go left or 'right' to go right.")
user_input = input()

while (user_input != "left") and (user_input != "right"):
    print("Type 'left' to go left or 'right' to go right.")
    user_input = input()
if user_input == "left":
    print("You decide to go left and you find a bush filled with berries. Will you eat the berries?")
    user_input == input()   
    while (user_input != "yes") and (user_input != "no"):
        print("Will you eat the berries?")
        user_input = input()
    if user_input == "yes":
        print("You start eating the berries and they taste amazing.  Then you see a skunk coming out from under the bush.  It sees you as well and turns so that its tail is flaired up and facing you. Are you going to run?")
        user_input == input()
        while (user_input != "yes") and (user_input != "no"):
            print("Are you going to run?")
            user_input = input()
        if user_input == "yes":
            print("You turn to run but the quick movement startles the skunk, and it sprays you in the face.  Although your eyes are burning, you see a pond nearby. Will you jump into the pond?")
            user_input == input()
            while (user_input != "yes") and (user_input != "no"):
                print("Will you jump into the pond?")
                user_input = input()
            if user_input == "yes":
                print("You jump into the pond, and while you are rinsing your eyes, an alligater attacks you and you die.")
                print("The end")
            elif user_input == "no":
                print("You are glad you did not jump into the pond, because and a few seconds later, an alligator pops its head out of the water. Your eye still hurts but it goes away eventually.  You keep walking until you find a clearing.  A helicoptor spots you and you are saved.")
                print("The end")
        elif user_input == "no":
            print("The skunk ignores you and proceeds to leave.  You suddenly feel sick and then throw up on the ground.  It turns out the berries were poisonous. You feel thirsty and dehydrated so you keep walking until you find a stream nearby.  Are you going to drink from the stream?")
            user_input = input()
            while (user_input != "yes") and (user_input != "no"):
                print("Are you going to drink from the stream?")
                user_input = input()
            if user_input == "yes":
                print("Luckily, the water is clean, and you take a long sip of water.  Then you continue walking and finally reach civilization.")
                print("The end")
            elif user_input == "no":
                print("You decide not risk drinking dirty water, so you keep walking.  You cannot find another water source so you eventually die of dehydration.")
                print("The end")
    elif user_input == "no":
        print("As you walk past the berries, your stomach growls loudly, and you feel deteriorated.  Do you want to rest?")
        user_input = input()
        while (user_input != "yes") and (user_input != "no"):
            print("Do you want to rest?")
            user_input = input()
        if user_input == "yes":
            print("You lie down on the ground and proceed to take a nap.  Sudddenly, you feel a painful sting on your leg.  You are surrounded by fireants! You stand up immediately.  Do you stomp on the ants to get revenge?")
            user_input = input()
            while (user_input != "yes") and (user_input != "no"):
                print("Do you stomp on the ants to get revenge?")
                user_input = input()
            if user_input == "yes":
                print("The more you stomp on the ants, the more ants appear.  They start crawling up your body and you have an extreme allergic reaction to their vemon and you die.")
                print("The end")
            elif user_input == "no":
                print("You run away from the swarm of ants and fall into a trap hole.  You are discovered by a group of researchers and you are saved.")
                print("The end")
        elif user_input == "no":
            print("As you keep walking, you start feeling dizzy.  You accidentally hit your head really hard on a tree and you faint.  When you wake up there is a bear 2 feet away.  Do you stand up to run?")
            user_input = input()
            while (user_input != "yes") and (user_input != "no"):
                print("Do you stand up to run?")
                user_input = input()
            if user_input == "yes":
                print("You stand up too quickly, and you feel dizzy again.  You fall again, this time on a hard rock and you die.")
                print("The end")
            elif user_input == "no":
                print("You stay still and the bear ignores you.  Once the bear leaves and you are fully conscious, you eventually find your way back to civilization.")
                print("The end")
           

elif user_input == "right":
    print("You choose to go right and you come across quicksand that's 9 feet across.  Are you going to try to jump across?") 
    user_input = input()
    while (user_input != "yes") and (user_input != "no"):
        print("Are you going to jump across?")
        user_input = input()
    if user_input == "yes":
        print("Because of your strong legs, you make it across easily.  You take another step and realize you just crushed an ostrich egg.  The mother sees you and starts running towards you.  Do you choose to run or fight?")
        user_input = input()
        while (user_input != "run") and (user_input != "fight"):
            print("Do you choose to run or fight?")
            user_input = input()
        if user_input == "run":
            print("You turn and run as fast as you can. The ostrich almost catches up when you see a tree with a branch that is just within your reach.  Are you going to climb the tree?")
            user_input = input()
            while(user_input != "yes") and (user_input != "no"):
                print("Are you going to climb the tree?")
                user_input = input()
            if user_input == "yes":
                print("You climb 30 feet up the tree, but then the branch you are holding onto breaks, and you fall to your death.")
                print("The end")
            elif user_input == "no":
                print("You keep running and start zigzagging between the trees and bushes.  You eventually lose the ostrich and then come upon a clearing.  You are spotted by a helicopter and you are saved.")
                print("The end")
        elif user_input == "fight":
            print("You grab all the rocks you can and throw it at the ostrich.  Now it is even more aggravated.  It tramples over you and then runs away.  You're left with a broken rib and bruises all over your body.  Your eyes become very heavy. Are you gonna take a nap?")
            user_input = input()
            while(user_input != "yes") and (user_input != "no"):
                print("Are you gonna take a nap?")
                user_input = input()
            if user_input == "yes":
                print("You close your eyes, but unfortunately, you never wake up.")
                print("The end")
            elif user_input == "no":
                print("You push on and start crawling.  Eventually you come across a wooden shed.  You knock on the door and is greeted by a team of scienists.  You are saved.")
                print("The end")
    elif user_input == "no":
        print("You start backing up, but apparently there was a monkey behind you and it shoves you face first into the quicksand.  You are drowning and you see a vine covered with poison oak that's just out of your reach.  Do you grab it?")
        user_input = input()
        while (user_input != "yes") and (user_input != "no"):
            print("Do you grab the poison oak vine?")
            user_input = input()
        if user_input == "yes":
            print("You get out of the quicksand, but your hand is covered with poison oak. You see a plant and you're not sure if it'll sooth your hand. Do you pick it up?")
            user_input = input()
            while (user_input != "yes") and (user_input != "no"):
                print("Will you pick up the plant?")
                user_input = input()
            if user_input == "yes":
                print("You pick up the plant and it intensified the pain.  You get a deadly infection and you die.")
                print("Game over")
            elif user_input == "no":
                print("You decide not to take the risk and move on.  Finally, you reach the edge of the forest and find your way back to civilization.")
                print("The end")
        elif user_input == "no":
            print("You continue flailing and then realize the quicksand is only 4 feet deep.  You climb out and you are face to face with a venomous snake.  Do you try to hit it with a rock?")
            user_input = input()
            while (user_input != "yes") and (user_input != "no"):
                print("Will you hit the snake with a rock?")
                user_input = input()
            if user_input == "yes":
                print("You slam the rock on the head of the snake and it dies immediately.  You climb out of the quicksand and is saved by the rescue team.")
                print("The end")
            elif user_input == "no":
                print("The snake is startled by you and bites you.  You die within 30 seconds.")
                print("The end")
