import pdb
import re

class IterRecipe(type):
    def __iter__(cls):
        return iter(cls._AllRecipes)


class Recipe:
    AllRecipes = []

    carb_options = []
    veg_options = []
    protein_options = []
    
    def __init__(self, name, protein, carb, veg, time, difficulty):
        self.name = name.title()
        self.protein = protein.title()
        self.carb = carb.title()
        self.veg = veg
        self.time = time
        self.difficulty = difficulty.title()
        self.other_ingredients = []
        self.method = {}
        Recipe.AllRecipes.append(self)
        for v in self.veg:
            if v not in Recipe.veg_options:
                Recipe.veg_options.append(v)
        if self.carb not in Recipe.carb_options:
            Recipe.carb_options.append(self.carb)
        if self.protein not in Recipe.protein_options:
            Recipe.protein_options.append(self.protein)    

    def __ref__(self): self.name

    def print_recipeMethod(self):
        i = 1
        for key in self.method.keys():
            print("{num}: {method}".format(num = i, method = self.method[key]))
            i += 1
    
    def print_ingredients(self):
        print("\n {carb} \n{protein}".format(carb = self.carb, protein = self.protein))
        for v in self.veg:
            print("\n{} ".format(v))
        for ing in self.other_ingredients:
            print("\n {}".format(ing))

    def assign_recipe(user):
         for recipe in Recipe.AllRecipes:
             AllVeg = True 
             for v in recipe.veg:
                 if v not in user.veg:
                     AllVeg = False
             if AllVeg == True and recipe.protein == user.protein and recipe.carb == user.carb and recipe.time <= user.time and recipe.difficulty == user.competency:
                 print("Today you will be cooking {}".format(recipe.name))
                 print("To cook {recipe_} you will need the following ingredients:".format(recipe_ = recipe.name))
                 recipe.print_ingredients()
                 while True:
                    try:
                        go_ahead = input("\nDo you have everything you need and want to proceed? [y][n] \n")
                        if go_ahead == "y": 
                            print(recipe.print_recipeMethod())
                            break
                        elif go_ahead == "n": 
                            print("Okay, we'll start again and try find another.")
                            break
                        else: print("Please only input 'y' or 'n'")
                    except: continue
                 assigned_recipe = recipe
         return assigned_recipe
         

stir_fry = Recipe('Stir Fry', 'Tofu', 'Noodles', ['Carrots', 'Onion', 'Cabbage', 'Bell Pepper'], 15, 'Easy')
stir_fry.other_ingredients = ['soy sauce', 'peanut butter', 'honey', 'chilli flakes', 'spring onion (optional)']
stir_fry.method = {1: 'Heat the pan up to high with a tablespoon of oil', 2: 'Chuck in all the veg. Fry on high for 5 mins. Meanwhile cook the noodles', 3: 'Add it all together in a pan with soy sauce, peanut butter, honey and chilli flakes. Save some water from the noodles to add if needed', 4: 'Chop the spring onion and sprinkle on too', 5: 'Eat!'}

chilli_sausage_pasta = Recipe('Sausage Chilli Pasta','Sausages', 'Lasagne Sheets', ['Carrots', 'Onion', 'Celery', 'Mushrooms', 'Bell Pepper'], 30, 'Hard')
chilli_sausage_pasta.other_ingredients = ['Gochujang Paste or Chillis', 'Cream or Yogurt', 'Spring Onions', 'Salt & Pepper', 'Dried Basil']
chilli_sausage_pasta.method = {1: 'Heat the pan up to high with a teaspoon of oil and chop your veg', 2: 'Chop the sausages into chunks then fry on high till all golden brown', 3: 'Remove the sausages into a bowl, and fry the chopped veg in the residual fat', 4: 'Now get the pasta on for 10 mins. Meanwhile add the sausage back in with a tablespoon of gochujang paste', 5: 'Spoon in a couple ladles of the pasta water to loosen, and then add the pasta', 6: 'Take off the heat and add in the cream or yogurt', 7: 'Eat!'}


chilli_sin_carne = Recipe('Chilli sin Carne', 'Kidney Beans', 'Rice', ['Bell Pepper', 'Carrot', 'Tomatoes', 'Sweet Potatoes'], 60, 'Medium')
chilli_sin_carne.other_ingredients = ['Paprika', 'Chilli', 'Cumin', 'Cinnamon', 'Ground Coriander', 'Lime Juice', 'Soy Sauce', 'Garlic', 'Bay Leaf']
chilli_sin_carne.method = {1: 'Heat the pan up to high with a tablespoon of oil and chop your veg', 2: 'Put your rice on', 3: 'Chuck in all the veg. Fry on high for 5 mins.', 4: 'Add all the spices till you can really smell them - usually no more than a minute', 5: 'Chuck the tomatoes in with some water and a tablespoon of soy sauce', 6: 'Let simmer for a while until the rice is cooked', 7: 'Eat!'}


stuffed_aubergine = Recipe('Stuffed Aubergine', 'Chickpeas', 'None', ['Aubergine', 'Onion', 'Ginger', 'Tomatoes'], 40, 'Hard')
stuffed_aubergine.other_ingredients = ['Curry Powder', 'Yoghurt', 'Harissa Paste']
stuffed_aubergine.method = {1: 'Heat the oven up and the pan to high with a tablespoon of oil', 2: 'Prime the aubergine by pricking it with a fork and rubbing it with curry powder and oil', 3: 'Put the aubergine in the oven and the other veg in the pan', 4: 'When the veg in the pan is cooked, add in chickpeas with harissa paste and curry powder. Fry till aromatic', 5:'Add in the tomatoes and simmer', 6: 'When the aubergine is done, remove and cut in half. Fill with the contents of your pan'}

carbs_available = 'The carbs avaiable are:'
for i in range(0,len(Recipe.carb_options)):
    if Recipe.carb_options[-1] != Recipe.carb_options[i]:
        carbs_available += '\n[{number}]: {carb}'.format(number = i+1, carb = Recipe.carb_options[i])
    else: 
        carbs_available += '\n[{number}]: {carb} \n Please pick the number you wish to have:\n'.format(number = len(Recipe.carb_options), carb = Recipe.carb_options[-1])

protein_available = 'The proteins avaiable are:'
for i in range(0,len(Recipe.protein_options)):
    if Recipe.protein_options[-1] != Recipe.protein_options[i]:
        protein_available += '\n[{number}]: {protein}'.format(number = i+1, protein = Recipe.protein_options[i])
    else: 
        protein_available += '\n[{number}]: {protein} \n Please pick the number you wish to have: \n'.format(number = len(Recipe.protein_options), protein = Recipe.protein_options[-1])

veg_available = 'The veg avaiable are:'
for i in range(0,len(Recipe.veg_options)):
    if Recipe.veg_options[-1] != Recipe.veg_options[i]:
        veg_available += '\n[{number}]: {veg}'.format(number = i+1, veg = Recipe.veg_options[i])
    else: 
        veg_available += '\n[{number}]: {veg} \n Please pick the numbers you wish to not have, seperated by spaces:\n'.format(number = len(Recipe.veg_options), veg = Recipe.veg_options[-1])


class User:
    def __init__(self, name) -> None:
        self.name = name
        self.carb = ''
        self.protein = ''
        self.veg = []
        self.dislikes = []
        self.time = 0
        self.competency = 'Hard'

    def assign_name(self):
        print("Welcome to the cook assist. Let's start.")
        self.name = input('What is your name?')
        print("Hello {name}, we're going to find out what to cook".format(name = self.name))
    
    def assign_attributes(self):

    # --- Name Input ----
        # self.name = input('\nWhat is your name?\n')
        # print("\nHello {name}, we're going to find out what to cook\n".format(name = self.name))

    # --- Carb Choice Input ---
        while True:
            try:    
                choice_carb_number = int(input(carbs_available))
                if choice_carb_number > 0 and choice_carb_number <= len(carbs_available):
                    self.carb = Recipe.carb_options[choice_carb_number-1]
                    print("\nWe'll get that sorted\n")
                    break
                else:
                    print("\nPlease input only the numbers above\n")
                    continue
            except ValueError: 
                continue
                
     # --- Protein Choice Input ---    
        while True:
            try:
                choice_protein_number = int(input(protein_available))
                if choice_protein_number > 0 and choice_protein_number <= len(protein_available):
                    self.protein = Recipe.protein_options[choice_protein_number-1]
                    print("\nOkay nice one!\n")
                    break
                else: 
                    print("\nPlease input only the numbers above\n")
                    continue
            except ValueError: 
                continue    
        
    # --- Veg starts here ---
        bad_veg = []
        new_veg = Recipe.veg_options
        # START Input test
        while True:
            try:
                choice_veg_numbers = input(veg_available)
                veg_numbers_split = choice_veg_numbers.split()
                veg_int_nums = []
                good_input = True
                for veg_num in veg_numbers_split:
                    int_veg = int(veg_num)
                    veg_int_nums.append(int_veg)
                for veg_num in veg_int_nums:
                    if veg_num > 0 and veg_num <= len(Recipe.veg_options): 
                        continue
                    else: 
                        print("Try again")
                        good_input = False
                        continue
                if good_input == False: continue
                else: 
                    print("")
                    break   
            except SyntaxError:
                continue
        #END Input test
        #Remove unliked veg from the list
        for veg_num in veg_int_nums: 
             bad_veg.append(Recipe.veg_options[veg_num-1])
        for veg in bad_veg:
            new_veg.remove(veg)                   
        self.veg = new_veg
        statement_of_veg = "\nThanks we won't include the following veg in your recipe:"
        for veg in bad_veg:
            statement_of_veg += "\n {}".format(veg)
        print(statement_of_veg)
    # --- End of the veg escapade ---


        dislikes = input("\nType in anything you don't like, seperated by commas:\n")
        dislikes_split = dislikes.split(',')

        for dislikes in dislikes_split:
            self.dislikes.append(dislikes.strip())

        while True:
            try:
                time = int(input("\nHow much time do you have to make this (in minutes):\n"))
                if time >= 0 and time <240:
                    self.time = time
                    print("\nTime entered successfully!\n")
                    break
                else: 
                    print("\nERROR: Time must be greater than 0 minutes and less than 240 minutes (4hrs)")
            except ValueError:
                print("\nERROR: Provide an integer value...\n")
                continue

        while True:
            try:
                competency_num = int(input("How good are you at cooking? \n[1]: Really Bad \n[2]: Average \n[3]: I taught Ratatouille \nType number:\n"))
                if competency_num == 1: 
                    self.competency = 'Easy'
                    print("\nNoted! We'll go with an easy recipe\n")
                    break
                elif competency_num == 2: 
                    self.competency = 'Medium'
                    print("\nOkay! We'll go for a medium difficulty dish\n")
                    break
                elif competency_num == 3: 
                    self.competency = 'Hard'
                    print("\nOkay buddy! Polish off those Michelen stars and let's get a difficult one on the burner\n")
                    break
                else: print("\nERROR: Response must be between 1 and 3\n")
            except ValueError:
                print("\nERROR: Please either type the interger 1, 2 or 3\n")
            
# --- Add Recipe function ---
recipe_dict = {}
def create_newVar(var_name, var_value):
    globals()[var_name] = var_value

def addRecipe():
    print("\nLet's put your recipe into the system \n")
# ask name of recipe:
    new_name = input("What is the name of your recipe\n")
# get main protein
    protein_input = input("\nWhat is the main protein in your recipe?\n")
    stripped_protein = re.sub("[^A-Za-z]", "", protein_input)
    new_protein = stripped_protein.title()
#get carb base
    carb_input = input("\nWhat is the main carb in your recipe. If none, type 'None' \n")
    stripped_carb = re.sub("[^A-Za-z]", "", carb_input)
    new_carb = stripped_carb.title()
# get veg needed
    new_veg =[]
    veg_input = input("What veg goes into your recipe? Seperate each instance by commmas.\n")
    split_veg_input = veg_input.split(',')
    for v in split_veg_input:
        stripped_v = re.sub("[^A-Za-z]", "", v)
        titleCase_v = stripped_v.title()
        new_veg.append(titleCase_v)
# get length it takes
    while True:
        try:
            new_time = int(input("\nHow long does it take to cook? Input the number of minutes\n"))
            if isinstance(new_time, int) and new_time > 0:
                break
            else: 
                print("\nERROR: Please only input positive numbers.\n")
        except ValueError:
            print("\nERROR: Please only input numbers.\n")
            continue
# get difficulty 
    while True:
        try:        
            new_difficulty = int(input("\nHow hard is it to cook?:\n [1] Easy [2] Medium [3] Hard\n"))
            if new_difficulty == 1 or new_difficulty == 2 or new_difficulty == 3:
                break
            else: 
                print("Please input only the values 1, 2 or 3")
        except ValueError:
            print("Please input only the values 1, 2 or 3") 
            continue
# create new recipe instance
    recipe_value = new_name.replace(" ", "_")
    recipe_dict[recipe_value] = Recipe(new_name, new_protein, new_carb, new_veg, new_time, new_difficulty)

# ---- ADD USER FUNCTION ----

# users_dict = {}

# def new_user():
#     user_value = user_name.replace(" ", "_")
#     users_dict[user_value] = User(user_name)
    


# --- START PROGRAM --- 
user_name = input("Hi there! Welcome to the CodeCook. What's your name?\n")

newUser = User(user_name)


print("\nHi there {}! Welcome. First let's figure what you're here to do.".format(user_name))

while True:
    try:
        addRecipeQs = int(input("\nWould you like to add a new recipe or find something to cook?: New Recipe [1], Find something to cook [2], or Exit the program [3]?\n"))
        if addRecipeQs == 1:
            print("\nOkay! Let's add a recipe to the program\n")
            addRecipe()
            continue
        elif addRecipeQs == 2:
            print("Okay, let's figure what to cook")
            newUser.assign_attributes()
            assignedRecipe = Recipe.assign_recipe(newUser)
            continue
        elif addRecipeQs == 3:
            print("See you later!")
            break
        else:
            print("Please only input values '1','2', or '3'")
    except:
        continue
            


