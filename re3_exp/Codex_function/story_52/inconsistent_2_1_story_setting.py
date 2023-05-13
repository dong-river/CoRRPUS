## Create a world model state to track each character's appearance, personality, and relations with other characters.

class character:
    def __init__(self, name):
        self.name = name
        self.appearance = []
        self.occupation = []
        self.gender = []
        self.age = []
        self.relations = {}

class World:
    def __init__(self):
        self.Sarah_Mason = character('Sarah Mason')
        self.Rachel_Stephenson = character('Rachel Stephenson')
        self.John_Mason = character('John Mason')

    def story(self):
        self.the_grass_is_always_greener_on_the_other_side()
        self.this_is_a_lesson_that_john_learns_the_hard_way_when_he_cheated_on_his_wife_with_her_best_friend()
        self.when_he_tries_to_reconcile_with_his_wife_he_realizes_that_she_has_been_cheating_on_him_with_her_best_friend_s_husband()
        self.the_story_is_set_in_a_small_town_in_the_midwest()
        self.sarah_mason_is_a_beautiful_woman_with_long_blond_hair_and_blue_eyes()
        self.she_is_the_wife_of_john_mason_and_the_mother_of_two_children()
        self.rachel_stephenson_is_sarah_s_best_friend_and_the_wife_of_richard_stevenson()
        self.john_mason_is_sarah_s_husband_and_the_father_of_two_children()
        self.he_is_a_successful_businessman_who_has_a_wandering_eye()
    def the_grass_is_always_greener_on_the_other_side(self):
        pass
    
    def this_is_a_lesson_that_john_learns_the_hard_way_when_he_cheated_on_his_wife_with_her_best_friend(self):
        pass
    
    def when_he_tries_to_reconcile_with_his_wife_he_realizes_that_she_has_been_cheating_on_him_with_her_best_friend_s_husband(self):
        pass
    
    def the_story_is_set_in_a_small_town_in_the_midwest(self):
        pass
    
    def sarah_mason_is_a_beautiful_woman_with_long_blond_hair_and_blue_eyes(self):
        self.Sarah_Mason.appearance.append("beautiful")
        self.Sarah_Mason.appearance.append("long blond hair")
        self.Sarah_Mason.appearance.append("blue eyes")
        self.Sarah_Mason.gender.append("female")
        
    def she_is_the_wife_of_john_mason_and_the_mother_of_two_children(self):
        self.Sarah_Mason.relations['husband'] = 'John_Mason'
        self.Sarah_Mason.relations['children'] = 2
        self.John_Mason.relations['wife'] = 'Sarah_Mason'
        self.John_Mason.relations['children'] = 2
        
    def rachel_stephenson_is_sarah_s_best_friend_and_the_wife_of_richard_stevenson(self):
        self.Sarah_Mason.relations['best_friend'] = 'Rachel_Stephenson'
        self.Rachel_Stephenson.relations['best_friend'] = 'Sarah_Mason'
        self.Rachel_Stephenson.relations['husband'] = 'Richard_Stephenson'
        
    def john_mason_is_sarah_s_husband_and_the_father_of_two_children(self):
        self.John_Mason.gender.append("male")
        
    def he_is_a_successful_businessman_who_has_a_wandering_eye(self):
        self.John_Mason.occupation.append("successful businessman")
        self.John_Mason.personality.append("wandering eye")
        

## Create a world model state to track each character's appearance, personality, and relations with other characters.

