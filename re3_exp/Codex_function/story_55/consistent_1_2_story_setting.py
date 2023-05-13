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
        self.Emma_Saunders = character('Emma Saunders')
        self.Jackson_Cooper = character('Jackson Cooper')
        self.Olivia_Saunders = character('Olivia Saunders')

    def story(self):
        self.emma_is_your_typical_high_school_girl_until_she_starts_seeing_ghosts()
        self.at_first_she_think_she_s_going_crazy_but_she_soon_realizes_that_the_ghosts_are_trying_to_tell_her_something()
        self.with_the_help_of_her_new_ghost_friends_emma_has_to_uncover_a_dark_secret_that_is_haunting_her_school()
        self.the_story_is_set_in_a_small_town_in_the_united_states()
        self.emma_saunders_is_a_teenage_girl_with_long_curly_hair_and_brown_eyes()
        self.she_s_of_average_height_and_build()
        self.jackson_cooper_is_a_teenage_boy_with_short_brown_hair_and_blue_eyes()
        self.he_s_of_average_height_and_build()
        self.olivia_saunders_is_emma_s_mother()
        self.she_s_a_tall_woman_with_blonde_hair_and_green_eyes()
    def emma_is_your_typical_high_school_girl_until_she_starts_seeing_ghosts(self):
        self.Emma_Saunders.age.append('teenage')
        self.Emma_Saunders.occupation.append('high school girl')
        
    def at_first_she_think_she_s_going_crazy_but_she_soon_realizes_that_the_ghosts_are_trying_to_tell_her_something(self):
        pass
        
    def with_the_help_of_her_new_ghost_friends_emma_has_to_uncover_a_dark_secret_that_is_haunting_her_school(self):
        pass
        
    def the_story_is_set_in_a_small_town_in_the_united_states(self):
        pass
        
    def emma_saunders_is_a_teenage_girl_with_long_curly_hair_and_brown_eyes(self):
        self.Emma_Saunders.gender.append('female')
        self.Emma_Saunders.appearance.append('long curly hair')
        self.Emma_Saunders.appearance.append('brown eyes')
        
    def she_s_of_average_height_and_build(self):
        self.Emma_Saunders.appearance.append('average height')
        self.Emma_Saunders.appearance.append('average build')
        
    def jackson_cooper_is_a_teenage_boy_with_short_brown_hair_and_blue_eyes(self):
        self.Jackson_Cooper.gender.append('male')
        self.Jackson_Cooper.age.append('teenage')
        self.Jackson_Cooper.appearance.append('short brown hair')
        self.Jackson_Cooper.appearance.append('blue eyes')
        
    def he_s_of_average_height_and_build(self):
        self.Jackson_Cooper.appearance.append('average height')
        self.Jackson_Cooper.appearance.append('average build')
        
    def olivia_saunders_is_emma_s_mother(self):
        self.Olivia_Saunders.relations['mother'] = 'Emma_Saunders'
        self.Emma_Saunders.relations['daughter'] = 'Olivia_Saunders'
        
    def she_s_a_tall_woman_with_blonde_hair_and_green_eyes(self):
        self.Olivia_Saunders.gender.append('female')
        self.Olivia_Saunders.appearance.append('tall')
        self.Olivia_Saunders.appearance.append('blonde hair')
        self.Olivia_Saunders.appearance.append('green eyes')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

