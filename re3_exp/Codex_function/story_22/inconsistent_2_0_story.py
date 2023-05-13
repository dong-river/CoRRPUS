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
        self.Harold_Martinez = character('Harold Martinez')
        self.David_Garcia = character('David Garcia')

    def story(self):
        self.harold_martinez_works_at_the_gas_station_as_a_clerk()
        self.he_works_every_night_from_10pm_to_7am()
        self.he_is_a_middle_aged_hispanic_man_with_dark_brown_hair_dark_eyes_and_a_medium_build()
        self.tonight_was_supposed_to_be_a_quiet_night_shift_with_few_customers_visiting_the_gas_station()
        self.the_shift_started_on_time_at_10pm_and_there_were_no_customers_during_the_first_hour()
        self.then_at_around_11_45pm_there_was_a_customer_who_walked_into_the_gas_station_with_bags_under_his_eyes()
        self.he_seemed_to_be_disheveled_and_his_hair_was_messy()
        self.his_clothes_were_dirty_and_he_looked_like_he_hadn_t_shaved_in_days()
        self.as_he_looked_at_harold_his_eyes_seem_ed_like_they_haven_t_seen_the_light_of_day_for_weeks_they_look_dead_somehow()
        self.when_he_walked_up_to_harold_and_said_give_me_all_your_money_it_took_a_moment_for_harold_to_process_what_the_man_said_because_the_voice_that_came_out_was_not_the_one_he_expected_to_hear()
        self.instead_of_hearing_an_angry_or_aggressive_voice_what_came_out_of_this_man_s_mouth_is_monotone_and_flat_like_there_s_no_emotion_behind_it()
        self.i_m_sorry_harold_said_immediately_after_processing_what_happened()
        self.i_m_not_joking_around()
    def harold_martinez_works_at_the_gas_station_as_a_clerk(self):
        self.Harold_Martinez.occupation.append('clerk')
    def he_works_every_night_from_10pm_to_7am(self):
        pass
    def he_is_a_middle_aged_hispanic_man_with_dark_brown_hair_dark_eyes_and_a_medium_build(self):
        self.Harold_Martinez.appearance.append('dark brown hair')
        self.Harold_Martinez.appearance.append('dark eyes')
        self.Harold_Martinez.appearance.append('medium build')
        self.Harold_Martinez.gender.append('male')
        self.Harold_Martinez.age.append('middle aged')
    def tonight_was_supposed_to_be_a_quiet_night_shift_with_few_customers_visiting_the_gas_station(self):
        pass
    def the_shift_started_on_time_at_10pm_and_there_were_no_customers_during_the_first_hour(self):
        pass
    def then_at_around_11_45pm_there_was_a_customer_who_walked_into_the_gas_station_with_bags_under_his_eyes(self):
        self.David_Garcia.appearance.append('bags under eyes')
    def he_seemed_to_be_disheveled_and_his_hair_was_messy(self):
        self.David_Garcia.appearance.append('disheveled')
        self.David_Garcia.appearance.append('messy hair')
    def his_clothes_were_dirty_and_he_looked_like_he_hadn_t_shaved_in_days(self):
        self.David_Garcia.appearance.append('dirty clothes')
        self.David_Garcia.appearance.append('unshaven')
    def as_he_looked_at_harold_his_eyes_seem_ed_like_they_haven_t_seen_the_light_of_day_for_weeks_they_look_dead_somehow(self):
        self.David_Garcia.appearance.append('dead eyes')
    def when_he_walked_up_to_harold_and_said_give_me_all_your_money_it_took_a_moment_for_harold_to_process_what_the_man_said_because_the_voice_that_came_out_was_not_the_one_he_expected_to_hear(self):
        self.Harold_Martinez.relations['customer'] = 'David_Garcia'
        self.David_Garcia.relations['clerk'] = 'Harold_Martinez'
    def instead_of_hearing_an_angry_or_aggressive_voice_what_came_out_of_this_man_s_mouth_is_monotone_and_flat_like_there_s_no_emotion_behind_it(self):
        self.David_Garcia.appearance.append('monotone voice')
        self.David_Garcia.appearance.append('flat voice')
    def i_m_sorry_harold_said_immediately_after_processing_what_happened(self):
        pass
    def i_m_not_joking_around(self):
        pass

world = World()
world.story()

for attribute in world.David_Garcia.appearance:
    print(attribute)

for attribute in world.Harold_Martinez.appearance:
    print(attribute)
    
for attribute in world.Harold_Martinez.relations:
    print(attribute)
    
for attribute in world.David_Garcia.relations:
    print(attribute)

for attribute in world.David_Garcia.gender:
    print(attribute)

for attribute in world.Harold_Martinez.gender:
    print(attribute)

for attribute in world.David_Garcia.age:
    print(attribute)

for attribute in world.Harold_Martinez.age:
    print(attribute)

for attribute in world.David_Garcia.occupation:
    print(attribute)

for attribute in world.Harold_Martinez.occupation:
    print(attribute)

