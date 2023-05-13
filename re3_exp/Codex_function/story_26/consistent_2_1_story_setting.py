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
        self.Lettie_Hanson = character('Lettie Hanson')
        self.Bob_Hanson = character('Bob Hanson')
        self.Karen_Hanson = character('Karen Hanson')

    def story(self):
        self.after_a_woman_s_husband_dies_she_realizes_that_she_is_now_invisible_to_the_world()
        self.she_tries_to_go_on_with_her_life_but_finds_that_without_anyone_acknowledging_her_existence_she_might_as_well_not_exist_at_all()
        self.the_story_is_set_in_a_small_town_in_the_united_states()
        self.lettie_hanson_is_a_middle_aged_woman_who_is_struggling_to_cope_with_the_death_of_her_husband()
        self.she_is_kind_hearted_and_gentle_but_feels_lost_and_alone_in_the_world_without_him()
        self.bob_hanson_is_lettie_s_late_husband()
        self.he_was_a_kind_and_loving_man_who_was_always_there_for_her()
        self.karen_hanson_is_lettie_s_niece_who_comes_to_visit_her_after_bob_s_death()
    def after_a_woman_s_husband_dies_she_realizes_that_she_is_now_invisible_to_the_world(self):
        self.Lettie_Hanson.relations['husband'] = 'Bob_Hanson'
        self.Bob_Hanson.relations['wife'] = 'Lettie_Hanson'
        
    def she_tries_to_go_on_with_her_life_but_finds_that_without_anyone_acknowledging_her_existence_she_might_as_well_not_exist_at_all(self):
        pass
        
    def the_story_is_set_in_a_small_town_in_the_united_states(self):
        pass
        
    def lettie_hanson_is_a_middle_aged_woman_who_is_struggling_to_cope_with_the_death_of_her_husband(self):
        self.Lettie_Hanson.age.append('middle-aged')
        
    def she_is_kind_hearted_and_gentle_but_feels_lost_and_alone_in_the_world_without_him(self):
        pass
        
    def bob_hanson_is_lettie_s_late_husband(self):
        pass
        
    def he_was_a_kind_and_loving_man_who_was_always_there_for_her(self):
        pass
        
    def karen_hanson_is_lettie_s_niece_who_comes_to_visit_her_after_bob_s_death(self):
        self.Lettie_Hanson.relations['niece'] = 'Karen_Hanson'
        self.Karen_Hanson.relations['aunt'] = 'Lettie_Hanson'

## Create a world model state to track each character's appearance, personality, and relations with other characters.

