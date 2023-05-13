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
        self.beth_christensen_is_julie_s_mother()
        self.she_is_a_well_respected_member_of_the_community_and_is_very_involved_in_her_church()
        self.beth_is_not_happy_about_her_daughter_s_situation_and_is_strongly_opposed_to_the_idea_of_abortion()
    def a_young_woman_finds_out_that_she_is_pregnant_and_decides_to_abort_the_pregnancy_even_though_it_goes_against_her_religious_beliefs(self):
        pass
    def the_story_is_set_in_a_small_town_in_the_midwest(self):
        pass
    def julie_christensen_is_a_young_woman_in_her_early_twenties(self):
        self.Julie_Christensen.age.append('early twenties')
        self.Julie_Christensen.gender.append('female')
    def she_is_pretty_and_blonde_and_is_the_daughter_of_a_prominent_family_in_the_town(self):
        self.Julie_Christensen.appearance.append('pretty')
        self.Julie_Christensen.appearance.append('blonde')
    def julie_is_a_student_at_the_local_college_and_is_active_in_her_church(self):
        self.Julie_Christensen.occupation.append('student')
        self.Julie_Christensen.occupation.append('church')
    def tommy_foster_is_a_young_man_in_his_early_twenties(self):
        self.Tommy_Foster.age.append('early twenties')
        self.Tommy_Foster.gender.append('male')
    def he_is_the_son_of_a_poor_family_in_the_town_and_has_been_involved_in_a_lot_of_trouble_in_his_life(self):
        self.Tommy_Foster.relations['father'] = 'poor family'
    def tommy_is_julie_s_boyfriend_and_the_father_of_her_unborn_child(self):
        self.Tommy_Foster.relations['boyfriend'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['boyfriend'] = 'Tommy_Foster'
    def beth_christensen_is_julie_s_mother(self):
        self.Beth_Christensen.relations['mother'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['mother'] = 'Beth_Christensen'
    def she_is_a_well_respected_member_of_the_community_and_is_very_involved_in_her_church(self):
        self.Beth_Christensen.occupation.append('church')
    def beth_is_not_happy_about_her_daughter_s_situation_and_is_strongly_opposed_to_the_idea_of_abortion(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

