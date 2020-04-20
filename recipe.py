import random, time, sys, pygame



class Beer:
    def __init__(self, ingredients, volume):
        self.ingredients = ingredients
        self.volume = volume
        self.age = 0
        self.bottled = False
        self.bottle = None
        self.name = None
        self.quality = 10

    class Recipe:
        # Initializes recipe to Cincinnati Pale Ale
        # Hops amount is in tenths of an ounce. 10 = 1 oz.
        def __init__(self, name, grain_type=ingredients.Pale,
                     grain_amount=4,
                     hops_helpings=
                     [ingredients.HopsHelping(ingredients.Nugget, 10, 0),
                      ingredients.HopsHelping(ingredients.Cascade, 10, 45)],
                     yeast=2, extras=[], boil_time=60,
                     temp_range=(65, 70)):
            self.name = name
            self.grain_type = grain_type
            self.grain_amount = grain_amount
            self.hops_helpings = hops_helpings
            self.yeast = yeast
            self.extras = extras
            self.boil_time = boil_time
            self.temp_range = temp_range

        # adds hops to the recipe, takes an argument "hops"
        # "hops" is a 3-item list: a Hops instance, an amount, and a time
        def add_hops(self, hops_helping):
            self.hops_helpings.append(hops_helping)

        def get_ingredients(self):
            self.hops = set([])
            # TODO: put in caveat that finds duplicate hops_helpings attributes.
            # and just doubles that item's aau value in the set. Whew.
            for i in range(len(self.hops_helpings)):
                self.hops.add(self.hops_helpings[i].get_attributes())
            ingredients = dict(zip([self.grain_type.name, "Hops", "Yeast",
                                    "Extras"],
                                   [self.grain_amount, self.hops, self.yeast,
                                    self.extras]))
            return ingredients

        def brewed_me(self, brewed):
            return self.get_ingredients() == brewed.get_ingredients()

    CPA = Recipe("Cincinnati Pale Ale")
    recipes = [CPA]
    discovered_recipes = [CPA]

    class Grain:
        def __init__(self, name, grain_type="Syrup Extract"):
            self.name = name
            self.type = grain_type

    class Hops:
        def __init__(self, name, aa=12):
            self.name = name
            self.aa = aa

    class HopsHelping:
        def __init__(self, hops, amount, time):
            self.hops = hops
            self.amount = amount
            self.time = time
            # alpha acid units: a measurement of bitterness/flavor
            # used to determine if a recipe has been made
            self.aau = hops.aa * amount * 0.1

        def get_attributes(self):
            return (self.aau, self.time)

    Pale = Grain("Pale")
    Wheat = Grain("Wheat", "Grain")
    Nugget = Hops("Nugget")
    Cascade = Hops("Cascade", 5)

    def check_if_num(input_string):
        input_list = list(input_string)
        if len(input_list) > 0:
            for i in range(len(input_list)):
                if input_list[i] not in NUMBERS_0_TO_9:
                    return False
            return True

    is_playing = True
    while is_playing:
        print
        "It's brewing time!"
        print
        "What is your beer's name?"
        name = raw_input()
        brewing = recipes.Recipe(name)
        ingredient_names = [brewing.malt_type.name, brewing.bitters_type.name,
                            brewing.hops_type.name, "yeast"]
        ingredient_types = ['syrup', 'bitters', 'hops', '']
        ingredient_amounts = [brewing.malt_syrup, brewing.bitters, brewing.hops,
                              brewing.yeast]
        for i in range(4):
            print("How much " + ingredient_names[i] +
                  " " + ingredient_types[i] + " do you want to use?")
            while True:
                amount = raw_input()
                if not check_if_num(amount):
                    print
                    "Please enter a number. (0 is acceptable)"
                else:
                    ingredient_amounts[i] = int(amount)
                    break
        brewing.malt_syrup = ingredient_amounts[0]
        brewing.bitters = ingredient_amounts[1]
        brewing.hops = ingredient_amounts[2]
        brewing.yeast = ingredient_amounts[3]

        print
        "Your beer has been brewed!"
        time.sleep(1)
        for i in range(3):
            print
            "Analyzing..."
            time.sleep(1)
        brewed_something = False
        for recipe in recipes.recipes:
            if recipe.brewed_me(brewing):
                brewed_something = True
                print("You brewed " + brewing.name + ", a "
                      + recipe.name +
                      "! Congratulations!")

        if not brewed_something:
            print
            "Your beer didn't turn out right (or perhaps"
            print
            "the world just isn't ready for it yet)!"
        print
        "Brew again? Y/N"
        decision = raw_input()
        if list(decision)[0].lower() != 'y':
            is_playing = False
            print
            "Thanks for playing!"
            break

def main():
    Brew = Beer()
    Brew.check_if_num()
