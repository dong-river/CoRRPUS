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
        self.Jane_Doe = character('Jane Doe')
        self.Mister_Snuggles = character('Mister Snuggles')
        self.Jessica_Brown = character('Jessica Brown')

    def story(self):
        self.jessica_brown_woke_up_at_her_usual_time()
        self.today_was_saturday_which_meant_she_could_sleep_in()
        self.but_something_was_not_right()
        self.she_sat_up_in_bed_and_glanced_around_the_room()
        self.what_is_going_on()
        self.she_thought_to_herself()
        self.the_room_was_identical_to_how_it_had_been_last_night()
        self.it_seemed_to_be_unchanged_except_for_her_sister_jane_s_side_of_the_room_which_looked_like_a_bomb_had_hit_it()
        self.clothes_and_books_were_scattered_all_over_the_floor_as_if_there_had_been_a_windstorm_while_jane_slept_on_peacefully_as_though_nothing_was_wrong_unaware_of_the_havoc_that_had_occurred_just_hours_earlier()
    def jessica_brown_woke_up_at_her_usual_time(self):
        self.Jessica_Brown.age.append('teenage')
        self.Jessica_Brown.gender.append('female')
    def today_was_saturday_which_meant_she_could_sleep_in(self):
        pass
    def but_something_was_not_right(self):
        pass
    def she_sat_up_in_bed_and_glanced_around_the_room(self):
        pass
    def what_is_going_on(self):
        pass
    def she_thought_to_herself(self):
        pass
    def the_room_was_identical_to_how_it_had_been_last_night(self):
        pass
    def it_seemed_to_be_unchanged_except_for_her_sister_jane_s_side_of_the_room_which_looked_like_a_bomb_had_hit_it(self):
        self.Jessica_Brown.relations['sister'] = 'Jane_Doe'
        self.Jane_Doe.relations['sister'] = 'Jessica_Brown'
    def clothes_and_books_were_scattered_all_over_the_floor_as_if_there_had_been_a_windstorm_while_jane_slept_on_peacefully_as_though_nothing_was_wrong_unaware_of_the_havoc_that_had_occurred_just_hours_earlier(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.
