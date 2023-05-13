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
        self.Karen_Fletcher = character('Karen Fletcher')
        self.Kate_Fletcher = character('Kate Fletcher')
        self.Julia_Fletcher = character('Julia Fletcher')

    def story(self):
        self.the_last_thing_karen_remembers_before_she_blacks_out_is_the_sound_of_her_daughter_crying_for_help()
        self.when_she_comes_to_she_s_in_the_hospital_with_no_recollection_of_what_happened()
        self.the_police_are_at_her_bedside_telling_her_that_her_daughter_is_dead_and_that_she_is_the_prime_suspect()
        self.the_story_is_set_in_a_hospital_room()
        self.karen_fletcher_is_a_middle_aged_woman_with_blonde_hair_and_blue_eyes()
        self.she_is_of_average_height_and_build()
        self.kate_fletcher_is_karen_s_teenage_daughter()
        self.she_is_tall_and_slender_with_dark_hair_and_brown_eyes()
        self.julia_fletcher_is_karen_s_younger_sister()
        self.she_is_shorter_than_karen_with_light_brown_hair_and_green_eyes()
    def the_last_thing_karen_remembers_before_she_blacks_out_is_the_sound_of_her_daughter_crying_for_help(self):
        pass
    def when_she_comes_to_she_s_in_the_hospital_with_no_recollection_of_what_happened(self):
        pass
    def the_police_are_at_her_bedside_telling_her_that_her_daughter_is_dead_and_that_she_is_the_prime_suspect(self):
        pass
    def the_story_is_set_in_a_hospital_room(self):
        pass
    def karen_fletcher_is_a_middle_aged_woman_with_blonde_hair_and_blue_eyes(self):
        self.Karen_Fletcher.appearance.append('blonde hair')
        self.Karen_Fletcher.appearance.append('blue eyes')
        self.Karen_Fletcher.age.append('middle-aged')
        self.Karen_Fletcher.gender.append('female')
    def she_is_of_average_height_and_build(self):
        pass
    def kate_fletcher_is_karen_s_teenage_daughter(self):
        self.Karen_Fletcher.relations['daughter'] = 'Kate_Fletcher'
        self.Kate_Fletcher.relations['mother'] = 'Karen_Fletcher'
        self.Kate_Fletcher.age.append('teenage')
        self.Kate_Fletcher.gender.append('female')
    def she_is_tall_and_slender_with_dark_hair_and_brown_eyes(self):
        self.Kate_Fletcher.appearance.append('dark hair')
        self.Kate_Fletcher.appearance.append('brown eyes')
    def julia_fletcher_is_karen_s_younger_sister(self):
        self.Karen_Fletcher.relations['younger_sister'] = 'Julia_Fletcher'
        self.Julia_Fletcher.relations['older_sister'] = 'Karen_Fletcher'
        self.Julia_Fletcher.age.append('younger')
        self.Julia_Fletcher.gender.append('female')
    def she_is_shorter_than_karen_with_light_brown_hair_and_green_eyes(self):
        self.Julia_Fletcher.appearance.append('light brown hair')
        self.Julia_Fletcher.appearance.append('green eyes')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

