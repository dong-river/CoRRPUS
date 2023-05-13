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
        self.harold_martinez_a_19_year_old_hispanic_boy_was_working_at_the_gas_station_when_he_noticed_a_customer_who_looked_like_he_needed_some_help()
        self.the_man_had_a_gun_in_his_hand_and_looked_pretty_desperate()
        self.hey_you()
        self.the_customer_yelled()
        self.don_not_move()
        self.harold_stepped_out_from_behind_the_counter_and_got_on_his_knees()
        self.the_customer_grabbed_him_by_the_collar_of_his_shirt_and_pulled_him_close_to_him()
        self.listen_very_carefully_he_said_in_a_whisper_that_was_almost_a_growl_give_me_all_the_money_from_the_register_and_nobody_gets_hurt()
        self.he_pulled_out_a_stack_of_twenty_dollar_bills_from_his_pocket_and_set_them_on_the_counter()
        self.he_had_some_long_greasy_hair_that_stuck_out_everywhere_on_his_head()
    def harold_martinez_a_19_year_old_hispanic_boy_was_working_at_the_gas_station_when_he_noticed_a_customer_who_looked_like_he_needed_some_help(self):
        self.Harold_Martinez.age.append('19')
        self.Harold_Martinez.occupation.append('gas station attendant')
        self.Harold_Martinez.gender.append('male')
        self.Harold_Martinez.appearance.append('hispanic')
    def the_man_had_a_gun_in_his_hand_and_looked_pretty_desperate(self):
        self.David_Garcia.appearance.append('desperate')
    def hey_you(self):
        pass
    def the_customer_yelled(self):
        pass
    def don_not_move(self):
        pass
    def harold_stepped_out_from_behind_the_counter_and_got_on_his_knees(self):
        pass
    def the_customer_grabbed_him_by_the_collar_of_his_shirt_and_pulled_him_close_to_him(self):
        pass
    def listen_very_carefully_he_said_in_a_whisper_that_was_almost_a_growl_give_me_all_the_money_from_the_register_and_nobody_gets_hurt(self):
        pass
    def he_pulled_out_a_stack_of_twenty_dollar_bills_from_his_pocket_and_set_them_on_the_counter(self):
        pass
    def he_had_some_long_greasy_hair_that_stuck_out_everywhere_on_his_head(self):
        self.David_Garcia.appearance.append('greasy hair')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

