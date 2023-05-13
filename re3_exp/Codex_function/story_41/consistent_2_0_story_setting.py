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
        self.Jennie_Mayfield = character('Jennie Mayfield')
        self.Aaron_Mayfield = character('Aaron Mayfield')
        self.Alex_Preston = character('Alex Preston')

    def story(self):
        self.after_a_car_crash_a_woman_starts_seeing_ghosts()
        self.the_ghosts_tell_her_she_has_to_right_the_wrongs_they_did_in_life_in_order_to_move_on()
        self.she_s_not_sure_if_she_s_going_crazy_or_if_this_is_really_happening()
        self.the_story_is_set_in_a_small_town_in_the_united_states()
        self.jennie_mayfield_is_a_young_woman_in_her_early_twenties()
        self.she_has_long_dark_hair_and_brown_eyes()
        self.she_is_of_average_height_and_build()
        self.aaron_mayfield_is_jennie_s_older_brother()
        self.he_is_in_his_late_twenties_and_has_short_blond_hair_and_blue_eyes()
        self.he_is_taller_than_jennie_and_has_a_muscular_build()
        self.alex_preston_is_a_young_man_in_his_early_twenties_who_is_jennie_s_boyfriend_and_aaron_s_best_friend()
        self.he_has_short_dark_hair_and_brown_eyes_and_is_of_average_height_and_build()
    def after_a_car_crash_a_woman_starts_seeing_ghosts(self):
        pass

    def the_ghosts_tell_her_she_has_to_right_the_wrongs_they_did_in_life_in_order_to_move_on(self):
        pass

    def she_s_not_sure_if_she_s_going_crazy_or_if_this_is_really_happening(self):
        pass

    def the_story_is_set_in_a_small_town_in_the_united_states(self):
        pass

    def jennie_mayfield_is_a_young_woman_in_her_early_twenties(self):
        self.Jennie_Mayfield.gender.append('female')
        self.Jennie_Mayfield.age.append('young')

    def she_has_long_dark_hair_and_brown_eyes(self):
        self.Jennie_Mayfield.appearance.append('long dark hair')
        self.Jennie_Mayfield.appearance.append('brown eyes')

    def she_is_of_average_height_and_build(self):
        self.Jennie_Mayfield.appearance.append('average height')
        self.Jennie_Mayfield.appearance.append('average build')

    def aaron_mayfield_is_jennie_s_older_brother(self):
        self.Jennie_Mayfield.relations['brother'] = 'Aaron_Mayfield'
        self.Aaron_Mayfield.relations['sister'] = 'Jennie_Mayfield'

    def he_is_in_his_late_twenties_and_has_short_blond_hair_and_blue_eyes(self):
        self.Aaron_Mayfield.age.append('late twenties')
        self.Aaron_Mayfield.appearance.append('short blond hair')
        self.Aaron_Mayfield.appearance.append('blue eyes')

    def he_is_taller_than_jennie_and_has_a_muscular_build(self):
        self.Aaron_Mayfield.appearance.append('taller than Jennie')
        self.Aaron_Mayfield.appearance.append('muscular build')

    def alex_preston_is_a_young_man_in_his_early_twenties_who_is_jennie_s_boyfriend_and_aaron_s_best_friend(self):
        self.Jennie_Mayfield.relations['boyfriend'] = 'Alex_Preston'
        self.Alex_Preston.relations['girlfriend'] = 'Jennie_Mayfield'
        self.Alex_Preston.age.append('early twenties')
        self.Aaron_Mayfield.relations['best friend'] = 'Alex_Preston'
        self.Alex_Preston.relations['best friend'] = 'Aaron_Mayfield'

    def he_has_short_dark_hair_and_brown_eyes_and_is_of_average_height_and_build(self):
        self.Alex_Preston.appearance.append('short dark hair')
        self.Alex_Preston.appearance.append('brown eyes')
        self.Alex_Preston.appearance.append('average height')
        self.Alex_Preston.appearance.append('average build')
## Create a world model state to track each character's appearance, personality, and relations with other characters.

