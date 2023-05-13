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
        self.Shannon_Riley = character('Shannon Riley')
        self.Robert_Riley = character('Robert Riley')
        self.Jillian_Riley = character('Jillian Riley')

    def story(self):
        self.jillian_riley_couldn_not_believe_her_sister_was_actually_moving_to_the_city()
        self.i_ve_finally_found_my_dream_job_said_shannon()
        self.i_m_going_to_be_a_journalist()
        self.that_s_great_sis_said_jillian_smiling()
        self.but_how_are_you_going_to_pay_the_rent()
        self.i_hope_you_know_you_don_not_have_a_job_lined_up_yet()
        self.there_are_no_newspapers_in_town_so_it_won_not_be_easy_finding_a_job()
        self.but_i_have_found_a_job()
        self.exclaimed_shannon()
        self.robert_riley_hired_me()
        self.jillian_choked_on_her_soup()
        self.what()
        self.she_asked_incredulously_when_she_d_recovered_herself()
        self.you_re_not_going_to_work_for_robert_riley()
        self.jillian_knew_her_father_had_moved_back_to_the_city_about_three_months_ago_but_she_didn_not_know_he_d_gotten_back_into_journalism_after_retiring_many_years_ago()
        self.apparently_shannon_hadn_not_known_either()
        self.she_just_assumed_that_robert_had_moved_back_to_the_city_and_was_living_off_his_retirement_fund_while_taking_care_of_his_two_granddaughters_full_time()
    def jillian_riley_couldn_not_believe_her_sister_was_actually_moving_to_the_city(self):
        self.Jillian_Riley.relations['sister'] = 'Shannon_Riley'
        self.Shannon_Riley.relations['sister'] = 'Jillian_Riley'
    def i_ve_finally_found_my_dream_job_said_shannon(self):
        self.Shannon_Riley.occupation.append('journalist')
    def i_m_going_to_be_a_journalist(self):
        self.Shannon_Riley.occupation.append('journalist')
    def that_s_great_sis_said_jillian_smiling(self):
        self.Jillian_Riley.relations['sister'] = 'Shannon_Riley'
        self.Shannon_Riley.relations['sister'] = 'Jillian_Riley'
    def but_how_are_you_going_to_pay_the_rent(self):
        pass
    def i_hope_you_know_you_don_not_have_a_job_lined_up_yet(self):
        pass
    def there_are_no_newspapers_in_town_so_it_won_not_be_easy_finding_a_job(self):
        pass
    def but_i_have_found_a_job(self):
        self.Shannon_Riley.occupation.append('journalist')
    def exclaimed_shannon(self):
        pass
    def robert_riley_hired_me(self):
        self.Shannon_Riley.relations['father'] = 'Robert_Riley'
        self.Robert_Riley.relations['daughter'] = 'Shannon_Riley'
    def jillian_choked_on_her_soup(self):
        pass
    def what(self):
        pass
    def she_asked_incredulously_when_she_d_recovered_herself(self):
        pass
    def you_re_not_going_to_work_for_robert_riley(self):
        self.Jillian_Riley.relations['father'] = 'Robert_Riley'
        self.Robert_Riley.relations['daughter'] = 'Jillian_Riley'
    def jillian_knew_her_father_had_moved_back_to_the_city_about_three_months_ago_but_she_didn_not_know_he_d_gotten_back_into_journalism_after_retiring_many_years_ago(self):
        pass
    def apparently_shannon_hadn_not_known_either(self):
        pass
    def she_just_assumed_that_robert_had_moved_back_to_the_city_and_was_living_off_his_retirement_fund_while_taking_care_of_his_two_granddaughters_full_time(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

