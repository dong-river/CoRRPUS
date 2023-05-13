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
        self.Jenny_Anderson = character('Jenny Anderson')
        self.Jimmy_Jackson = character('Jimmy Jackson')
        self.Principal_Stevens = character('Principal Stevens')

    def story(self):
        self.jenny_s_life_changed_forever_the_day_she_discovered_her_ability_to_turn_invisible()
        self.at_first_it_was_a_fun_game_to_play_with_her_friends_but_soon_jenny_realized_that_she_could_use_her_power_for_more_than_just_pranks()
        self.when_she_starts_using_it_to_take_the_town_s_corrupt_mayor_down_she_realizes_that_being_invisible_is_more_than_just_a_gift_it_s_a_way_of_life()
        self.the_story_is_set_in_the_small_town_of_shepherdstown()
        self.jenny_anderson_is_a_young_girl_with_blonde_hair_and_blue_eyes()
        self.she_is_small_for_her_age_and_is_often_rebel_without_a_cause()
        self.jimmy_jackson_is_jenny_s_boyfriend_and_the_star_quarterback_of_the_football_team_at_their_school()
        self.principal_stevens_is_the_principal_of_jenny_s_school()
        self.he_is_a_middle_aged_man_with_graying_hair_and_glasses()
        self.he_is_a_fair_and_just_man_but_is_also_very_strict()
    def jenny_s_life_changed_forever_the_day_she_discovered_her_ability_to_turn_invisible(self):
        pass
    def at_first_it_was_a_fun_game_to_play_with_her_friends_but_soon_jenny_realized_that_she_could_use_her_power_for_more_than_just_pranks(self):
        pass
    def when_she_starts_using_it_to_take_the_town_s_corrupt_mayor_down_she_realizes_that_being_invisible_is_more_than_just_a_gift_it_s_a_way_of_life(self):
        pass
    def the_story_is_set_in_the_small_town_of_shepherdstown(self):
        pass
    def jenny_anderson_is_a_young_girl_with_blonde_hair_and_blue_eyes(self):
        self.Jenny_Anderson.appearance.append('blonde hair')
        self.Jenny_Anderson.appearance.append('blue eyes')
        self.Jenny_Anderson.gender.append('female')
    def she_is_small_for_her_age_and_is_often_rebel_without_a_cause(self):
        self.Jenny_Anderson.appearance.append('small')
    def jimmy_jackson_is_jenny_s_boyfriend_and_the_star_quarterback_of_the_football_team_at_their_school(self):
        self.Jenny_Anderson.relations['boyfriend'] = 'Jimmy_Jackson'
        self.Jimmy_Jackson.relations['girlfriend'] = 'Jenny_Anderson'
        self.Jimmy_Jackson.occupation.append('quarterback')
    def principal_stevens_is_the_principal_of_jenny_s_school(self):
        self.Principal_Stevens.occupation.append('principal')
    def he_is_a_middle_aged_man_with_graying_hair_and_glasses(self):
        self.Principal_Stevens.appearance.append('middle aged')
        self.Principal_Stevens.appearance.append('graying hair')
        self.Principal_Stevens.appearance.append('glasses')
        self.Principal_Stevens.gender.append('male')
    def he_is_a_fair_and_just_man_but_is_also_very_strict(self):
        self.Principal_Stevens.appearance.append('fair and just')
        self.Principal_Stevens.appearance.append('strict')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

