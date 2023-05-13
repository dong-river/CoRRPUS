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
        self.Julie_Christensen = character('Julie Christensen')
        self.Tommy_Foster = character('Tommy Foster')
        self.Beth_Christensen = character('Beth Christensen')

    def story(self):
        self.a_young_woman_finds_out_that_she_is_pregnant_and_decides_to_abort_the_pregnancy_even_though_it_goes_against_her_religious_beliefs()
        self.the_story_is_set_in_a_small_town_in_the_midwest()
        self.julie_christensen_is_a_young_woman_in_her_early_twenties()
        self.she_is_pretty_and_blonde_and_is_the_daughter_of_a_prominent_family_in_the_town()
        self.julie_is_a_student_at_the_local_college_and_is_active_in_her_church()
        self.tommy_foster_is_a_young_man_in_his_early_twenties()
        self.he_is_the_son_of_a_poor_family_in_the_town_and_has_been_involved_in_a_lot_of_trouble_in_his_life()
        self.tommy_is_julie_s_boyfriend_and_the_father_of_her_unborn_child()
        self.beth_christensen_is_julie_s_best_friend_since_childhood_and_her_confidante_in_this_matter()
    def a_young_woman_finds_out_that_she_is_pregnant_and_decides_to_abort_the_pregnancy_even_though_it_goes_against_her_religious_beliefs(self):
        self.Julie_Christensen.age.append('young')
        self.Julie_Christensen.gender.append('female')
        self.Julie_Christensen.relations['boyfriend'] = 'Tommy_Foster'
        self.Tommy_Foster.relations['girlfriend'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['best_friend'] = 'Beth_Christensen'
        self.Beth_Christensen.relations['best_friend'] = 'Julie_Christensen'
        self.Beth_Christensen.relations['sister'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['sister'] = 'Beth_Christensen'
    def the_story_is_set_in_a_small_town_in_the_midwest(self):
        pass
    def julie_christensen_is_a_young_woman_in_her_early_twenties(self):
        self.Julie_Christensen.age.append('young')
        self.Julie_Christensen.age.append('twenty')
    def she_is_pretty_and_blonde_and_is_the_daughter_of_a_prominent_family_in_the_town(self):
        self.Julie_Christensen.appearance.append('pretty')
        self.Julie_Christensen.appearance.append('blonde')
    def julie_is_a_student_at_the_local_college_and_is_active_in_her_church(self):
        self.Julie_Christensen.occupation.append('student')
        self.Julie_Christensen.occupation.append('church')
    def tommy_foster_is_a_young_man_in_his_early_twenties(self):
        self.Tommy_Foster.age.append('young')
        self.Tommy_Foster.age.append('twenty')
        self.Tommy_Foster.gender.append('male')
    def he_is_the_son_of_a_poor_family_in_the_town_and_has_been_involved_in_a_lot_of_trouble_in_his_life(self):
        self.Tommy_Foster.occupation.append('trouble')
    def tommy_is_julie_s_boyfriend_and_the_father_of_her_unborn_child(self):
        self.Tommy_Foster.relations['girlfriend'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['boyfriend'] = 'Tommy_Foster'
    def beth_christensen_is_julie_s_best_friend_since_childhood_and_her_confidante_in_this_matter(self):
        self.Beth_Christensen.relations['best_friend'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['best_friend'] = 'Beth_Christensen'
        self.Beth_Christensen.relations['sister'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['sister'] = 'Beth_Christensen'

## Create a world model state to track each character's appearance, personality, and relations with other characters.

