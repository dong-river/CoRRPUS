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
        self.Valerie_Russo = character('Valerie Russo')
        self.Carl_Russo = character('Carl Russo')
        self.Antoinette_Russo = character('Antoinette Russo')

    def story(self):
        self.valerie_is_a_high_school_senior_who_has_always_been_a_good_student()
        self.she_s_been_told_her_whole_life_that_she_s_going_to_be_a_great_doctor_just_like_her_mother()
        self.but_when_she_starts_to_doubt_her_abilities_she_decides_to_take_a_gap_year_to_travel_the_world_and_find_herself()
        self.the_story_is_set_in_the_present_day_in_the_small_town_of_valerie_s_childhood_home()
        self.valerie_russo_is_a_young_woman_of_italian_descent()
        self.she_has_dark_hair_and_brown_eyes()
        self.she_is_average_height_and_build()
        self.carl_russo_is_valerie_s_father()
        self.he_is_a_large_man_with_dark_hair_and_brown_eyes()
        self.he_is_a_retired_police_officer_who_now_works_as_a_security_guard_at_the_local_hospital()
        self.antoinette_russo_is_valerie_s_mother()
        self.she_is_a_petite_woman_with_dark_hair_and_brown_eyes()
        self.she_is_a_successful_surgeon_who_owns_her_own_practice()
    def valerie_is_a_high_school_senior_who_has_always_been_a_good_student(self):
        self.Valerie_Russo.age.append('high school senior')
        self.Valerie_Russo.occupation.append('student')
    def she_s_been_told_her_whole_life_that_she_s_going_to_be_a_great_doctor_just_like_her_mother(self):
        self.Valerie_Russo.relations['mother'] = 'Antoinette_Russo'
        self.Antoinette_Russo.relations['daughter'] = 'Valerie_Russo'
    def but_when_she_starts_to_doubt_her_abilities_she_decides_to_take_a_gap_year_to_travel_the_world_and_find_herself(self):
        pass
    def the_story_is_set_in_the_present_day_in_the_small_town_of_valerie_s_childhood_home(self):
        pass
    def valerie_russo_is_a_young_woman_of_italian_descent(self):
        self.Valerie_Russo.gender.append('female')
    def she_has_dark_hair_and_brown_eyes(self):
        self.Valerie_Russo.appearance.append('dark hair')
        self.Valerie_Russo.appearance.append('brown eyes')
    def she_is_average_height_and_build(self):
        self.Valerie_Russo.appearance.append('average height')
        self.Valerie_Russo.appearance.append('average build')
    def carl_russo_is_valerie_s_father(self):
        self.Valerie_Russo.relations['father'] = 'Carl_Russo'
        self.Carl_Russo.relations['daughter'] = 'Valerie_Russo'
    def he_is_a_large_man_with_dark_hair_and_brown_eyes(self):
        self.Carl_Russo.gender.append('male')
        self.Carl_Russo.appearance.append('dark hair')
        self.Carl_Russo.appearance.append('brown eyes')
        self.Carl_Russo.appearance.append('large')
    def he_is_a_retired_police_officer_who_now_works_as_a_security_guard_at_the_local_hospital(self):
        self.Carl_Russo.occupation.append('retired police officer')
        self.Carl_Russo.occupation.append('security guard at the local hospital')
    def antoinette_russo_is_valerie_s_mother(self):
        self.Valerie_Russo.relations['mother'] = 'Antoinette_Russo'
        self.Antoinette_Russo.relations['daughter'] = 'Valerie_Russo'
    def she_is_a_petite_woman_with_dark_hair_and_brown_eyes(self):
        self.Antoinette_Russo.gender.append('female')
        self.Antoinette_Russo.appearance.append('dark hair')
        self.Antoinette_Russo.appearance.append('brown eyes')
        self.Antoinette_Russo.appearance.append('petite')
    def she_is_a_successful_surgeon_who_owns_her_own_practice(self):
        self.Antoinette_Russo.occupation.append('successful surgeon')
        self.Antoinette_Russo.occupation.append('owns her own practice')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

