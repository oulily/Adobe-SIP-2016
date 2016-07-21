import random
adj = ["Salty ", "Creamy ", "Crunchy ", "Sweet ", "Tangy ", "Juicy ", "Light ", "Bitter ", "Spicy ", "Thinly-sliced "]
cooking = ["Steamed ", "Fried ", "Baked ", "Raw ", "Stir-fried ", "Fresh ", "Barbacue ", "Fermented ", "Boiled ", "Grilled "]
food = ["Veggies", "Chicken", "Salmon", "Tilapia", "Noodles", "Steak", "Potatoes", "Pasta", "Sandwich", "Soup"]
number = ["1. ", "2. ", "3. ", "4. ", "5. ", "6. ", "7. ", "8. ", "9. ", "10. "]

for i in range(len(number)):
    random_adj = random.randint(0, len(adj) - 1)
    random_cooking = random.randint(0, len(cooking) - 1)
    random_food = random.randint(0, len(food) - 1)
    
    print(number[i] + adj[random_adj] + cooking[random_cooking] + food[random_food])



adj = ["Striking", "Crazy", "Funky", "Shiny", "Bouncy", "Ghastly", "Exploding", "Undulating", "Happy"]
noun = ["Duo", "Sharks", "Trio", "Heads", "Emeralds", "Ghostbusters", "Flintstones", "Gentlemen", "Ladies", "Surfers"]

random_adj = random.randint(0, len(adj))
random_noun = random.randint(0, len(noun))

print("The " + adj[random_adj] + " " + noun[random_noun])

    

five_syl = ["I love eating food", "Food food food food food", "Pizza is awesome", "Food is very good", "Gimme some food dude"
seven_syl = ["It puts me in a good mood", 
