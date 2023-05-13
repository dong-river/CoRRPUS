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
        self.Nina_Harman = character('Nina Harman')
        self.Jake_Ryan = character('Jake Ryan')
        self.Karen_Hartman = character('Karen Hartman')

    def story(self):
        self.nina_an_unassuming_pre_teen_discovers_she_has_the_ability_to_astral_project_outside_of_her_body()
        self.she_soon_learns_that_she_is_not_the_only_one_with_this_ability_and_that_there_are_others_who_would_use_this_power_for_evil()
        self.nina_must_use_her_new_found_abilities_to_stop_them()
        self.the_story_is_set_in_a_small_town_in_the_united_states()
        self.nina_harman_is_a_small_delicate_looking_pre_teen_with_long_dark_hair_and_brown_eyes()
        self.she_is_shy_and_withdrawn_but_has_a_kind_heart()
        self.jake_ryan_is_a_handsome_teenage_boy_who_is_popular_at_school()
        self.he_is_athletic_and_outgoing_but_can_be_arrogant_at_times()
        self.he_is_also_nina_s_crush()
        self.karen_hartman_is_nina_s_best_friend_who_is_outgoing_and_energetic_with_a_quick_wit_and_sharp_tongue()
    def the_story_is_set_in_a_small_town_in_the_united_states(self):
        pass
    def nina_harman_is_a_small_delicate_looking_pre_teen_with_long_dark_hair_and_brown_eyes(self):
        self.Nina_Harman.appearance.append('small')
        self.Nina_Harman.appearance.append('delicate')
        self.Nina_Harman.appearance.append('long dark hair')
        self.Nina_Harman.appearance.append('brown eyes')
        self.Nina_Harman.age.append('pre-teen')
    def she_is_shy_and_withdrawn_but_has_a_kind_heart(self):
        self.Nina_Harman.personality.append('shy')
        self.Nina_Harman.personality.append('withdrawn')
        self.Nina_Harman.personality.append('kind hearted')
    def jake_ryan_is_a_handsome_teenage_boy_who_is_popular_at_school(self):
        self.Jake_Ryan.appearance.append('handsome')
        self.Jake_Ryan.age.append('teenage')
        self.Jake_Ryan.occupation.append('popular')
    def he_is_athletic_and_outgoing_but_can_be_arrogant_at_times(self):
        self.Jake_Ryan.personality.append('athletic')
        self.Jake_Ryan.personality.append('outgoing')
        self.Jake_Ryan.personality.append('arrogant')
    def he_is_also_nina_s_crush(self):
        self.Nina_Harman.relations['crush'] = 'Jake_Ryan'
        self.Jake_Ryan.relations['crush'] = 'Nina_Harman'
    def karen_hartman_is_nina_s_best_friend_who_is_outgoing_and_energetic_with_a_quick_wit_and_sharp_tongue(self):
        self.Nina_Harman.relations['best friend'] = 'Karen_Hartman'
        self.Karen_Hartman.relations['best friend'] = 'Nina_Harman'
        self.Karen_Hartman.personality.append('outgoing')
        self.Karen_Hartman.personality.append('energetic')
        self.Karen_Hartman.personality.append('quick wit')
        self.Karen_Hartman.personality.append('sharp tongue')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

