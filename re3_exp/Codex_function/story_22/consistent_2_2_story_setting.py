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
        self.it_was_supposed_to_be_a_quiet_night_shift_at_the_gas_station_but_when_a_disheveled_man_walks_in_and_demands_all_the_money_in_the_register_it_turns_into_a_nightmare()
        self.the_man_is_armed_and_clearly_desperate_and_the_clerk_has_no_choice_but_to_complied()
        self.but_when_the_police_arrive_minutes_later_the_customer_is_long_gone_leaving_the_clerk_as_the_only_suspect()
        self.the_story_is_set_in_a_gas_station_at_night()
        self.harold_martinez_is_a_young_hispanic_man_who_is_the_gas_station_attendant_who_is_held_up_at_gunpoint_by_a_customer_and_is_forced_to_give_him_all_the_money_in_the_register_david_garcia_is_a_young_hispanic_man_who_is_the_customer_who_robs_the_gas_station()
        self.he_is_armed_and_dangerous_and_is_clearly_desperate()
    def it_was_supposed_to_be_a_quiet_night_shift_at_the_gas_station_but_when_a_disheveled_man_walks_in_and_demands_all_the_money_in_the_register_it_turns_into_a_nightmare(self):
        self.David_Garcia.occupation.append('customer')
        self.David_Garcia.appearance.append('disheveled')
        self.Harold_Martinez.occupation.append('gas station attendant')
    def the_man_is_armed_and_clearly_desperate_and_the_clerk_has_no_choice_but_to_complied(self):
        self.David_Garcia.appearance.append('armed')
        self.David_Garcia.appearance.append('desperate')
        self.Harold_Martinez.appearance.append('forced')
    def but_when_the_police_arrive_minutes_later_the_customer_is_long_gone_leaving_the_clerk_as_the_only_suspect(self):
        pass
    def the_story_is_set_in_a_gas_station_at_night(self):
        pass
    def harold_martinez_is_a_young_hispanic_man_who_is_the_gas_station_attendant_who_is_held_up_at_gunpoint_by_a_customer_and_is_forced_to_give_him_all_the_money_in_the_register_david_garcia_is_a_young_hispanic_man_who_is_the_customer_who_robs_the_gas_station(self):
        self.Harold_Martinez.age.append('young')
        self.Harold_Martinez.gender.append('male')
        self.David_Garcia.age.append('young')
        self.David_Garcia.gender.append('male')
    def he_is_armed_and_dangerous_and_is_clearly_desperate(self):
        self.David_Garcia.appearance.append('armed')
        self.David_Garcia.appearance.append('dangerous')
        self.David_Garcia.appearance.append('desperate')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

