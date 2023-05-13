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
        self.harold_martinez_is_a_middle_aged_hispanic_man_who_works_as_a_gas_station_clerk()
        self.he_is_a_hardworking_and_honest_man_who_has_been_working_at_the_gas_station_for_years()
        self.david_garcia_is_a_young_hispanic_man_who_is_the_customer_who_robs_the_gas_station()
        self.he_is_armed_and_dangerous_and_is_clearly_desperate()
    def it_was_supposed_to_be_a_quiet_night_shift_at_the_gas_station_but_when_a_disheveled_man_walks_in_and_demands_all_the_money_in_the_register_it_turns_into_a_nightmare(self):
        pass
    def the_man_is_armed_and_clearly_desperate_and_the_clerk_has_no_choice_but_to_complied(self):
        pass
    def but_when_the_police_arrive_minutes_later_the_customer_is_long_gone_leaving_the_clerk_as_the_only_suspect(self):
        pass
    def the_story_is_set_in_a_gas_station_at_night(self):
        pass
    def harold_martinez_is_a_middle_aged_hispanic_man_who_works_as_a_gas_station_clerk(self):
        self.Harold_Martinez.occupation.append('gas station clerk')
        self.Harold_Martinez.age.append('middle_aged')
        self.Harold_Martinez.gender.append('male')
    def he_is_a_hardworking_and_honest_man_who_has_been_working_at_the_gas_station_for_years(self):
        pass
    def david_garcia_is_a_young_hispanic_man_who_is_the_customer_who_robs_the_gas_station(self):
        self.David_Garcia.occupation.append('customer')
        self.David_Garcia.age.append('young')
        self.David_Garcia.gender.append('male')
    def he_is_armed_and_dangerous_and_is_clearly_desperate(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

