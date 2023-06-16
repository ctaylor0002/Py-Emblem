import random

class Character:
    def __init__(self, level, character_class, character_race):
        self.level = level
        self.character_class = character_class
        self.character_race = character_race
        self.stats = [10, 10, 10, 10]


    # def level_up(self):

    #     # Create 4 variable to hold the chance to increase each stat based on class and race
    #     strength_modifier = 70 #(self.character_class.strength_growth_rate) + (self.character_race.strength_growth_rate)
    #     agility_modifier =  20 #(self.character_class.agility_growth_rate) + (self.character_race.agility_growth_rate)
    #     constitution_modifier = 55 # (self.character_class.constitution_growth_rate) + (self.character_race.constitution_growth_rate)
    #     intellect_modifier = 10 #(self.character_class.intellect_growth_rate) + (self.character_race.intellect_growth_rate)
        
    #     stat_modifiers = [strength_modifier, agility_modifier, constitution_modifier, intellect_modifier]
    #     counter = 0

    #     for i in self.stats:
    #         rand_number = random.randint(1, 100)
    #         if rand_number < stat_modifiers[counter]:
    #             self.stats[counter] += 1
    #         counter += 1  



