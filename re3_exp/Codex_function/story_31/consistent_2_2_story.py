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
        self.Riley_Harper = character('Riley Harper')
        self.Chase_Elliott = character('Chase Elliott')
        self.Jonas_Harper = character('Jonas Harper')

    def story(self):
        self.chase_elliott_is_your_average_guy_who_works_at_the_local_gas_station()
        self.he_lives_in_a_small_town_called_grandview_and_he_has_been_there_for_his_entire_life()
        self.jonas_harper_was_a_rich_man_who_owned_his_own_business_and_drove_a_nice_car()
        self.he_came_from_a_small_town_called_resting_ridge_and_he_loved_to_drive_on_country_roads()
        self.jonas_harper_died_in_a_car_accident()
        self.his_daughter_riley_lives_far_away_from_grandview_but_she_comes_for_her_father_s_funeral()
    def chase_elliott_is_your_average_guy_who_works_at_the_local_gas_station(self):
        self.Chase_Elliott.occupation.append('gas station')
    def he_lives_in_a_small_town_called_grandview_and_he_has_been_there_for_his_entire_life(self):
        self.Chase_Elliott.appearance.append('small town')
    def jonas_harper_was_a_rich_man_who_owned_his_own_business_and_drove_a_nice_car(self):
        self.Jonas_Harper.occupation.append('rich man')
        self.Jonas_Harper.appearance.append('nice car')
    def he_came_from_a_small_town_called_resting_ridge_and_he_loved_to_drive_on_country_roads(self):
        self.Jonas_Harper.appearance.append('small town')
    def jonas_harper_died_in_a_car_accident(self):
        pass
    def his_daughter_riley_lives_far_away_from_grandview_but_she_comes_for_her_father_s_funeral(self):
        self.Riley_Harper.relations['father'] = 'Jonas_Harper'
        self.Jonas_Harper.relations['daughter'] = 'Riley_Harper'

## Create a world model state to track each character's appearance, personality, and relations with other characters.

