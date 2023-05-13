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
        self.Sarah_Mason = character('Sarah Mason')
        self.Rachel_Stephenson = character('Rachel Stephenson')
        self.John_Mason = character('John Mason')

    def story(self):
        self.rachel_stephenson_was_a_happy_person()
        self.she_had_her_best_friend_sarah_mason_her_perfect_husband_mark_stephenson_and_two_perfect_children()
        self.she_woke_up_at_six_every_morning()
        self.as_soon_as_she_got_out_of_bed_she_did_fifteen_minutes_of_yoga_to_loosen_her_muscles_and_help_them_relax()
        self.after_the_yoga_routine_she_went_downstairs_to_make_breakfast_for_herself_and_her_husband()
        self.while_they_ate_breakfast_in_the_kitchen_they_discussed_their_plans_for_the_day()
        self.after_breakfast_was_done_she_headed_upstairs_to_give_each_of_their_two_kids_a_bath_while_mark_took_out_the_trash_and_checked_his_email_on_his_computer_in_the_den()
        self.their_kids_were_like_little_angels_because_they_never_caused_any_trouble_they_were_quiet_when_they_were_eating_they_were_always_dressed_in_impeccable_outfits_when_they_left_the_house_and_there_was_no_yelling_in_their_household_because_everyone_was_kind_to_one_another()
        self.they_would_go_out_for_walks_after_breakfast_but_by_eight_thirty_am_rachel_already_had_her_work_clothes_on_as_well_as_her_makeup_done_at_nine_am_she_was_usually_working_on_a_canvas_or_painting_at_one_of_three_coffee_shops_that_all_opened_at_eight_am_in_lake_bloomfield_illinois_where_she_lived_with_her_family()
    def rachel_stephenson_was_a_happy_person(self):
        self.Rachel_Stephenson.relations['husband'] = 'Mark_Stephenson'
        self.Rachel_Stephenson.gender.append('female')
        self.Rachel_Stephenson.appearance.append('happy')

    def she_had_her_best_friend_sarah_mason_her_perfect_husband_mark_stephenson_and_two_perfect_children(self):
        self.Rachel_Stephenson.relations['best_friend'] = 'Sarah_Mason'
        self.Rachel_Stephenson.relations['husband'] = 'Mark_Stephenson'
        self.Rachel_Stephenson.relations['children'] = 'two'
        self.Sarah_Mason.relations['best_friend'] = 'Rachel_Stephenson'
        self.Mark_Stephenson.relations['wife'] = 'Rachel_Stephenson'
        self.Mark_Stephenson.relations['children'] = 'two'

    def she_woke_up_at_six_every_morning(self):
        self.Rachel_Stephenson.appearance.append('woke up at six')

    def as_soon_as_she_got_out_of_bed_she_did_fifteen_minutes_of_yoga_to_loosen_her_muscles_and_help_them_relax(self):
        self.Rachel_Stephenson.appearance.append('did fifteen minutes of yoga')

    def after_the_yoga_routine_she_went_downstairs_to_make_breakfast_for_herself_and_her_husband(self):
        self.Rachel_Stephenson.appearance.append('went downstairs')

    def while_they_ate_breakfast_in_the_kitchen_they_discussed_their_plans_for_the_day(self):
        self.Rachel_Stephenson.appearance.append('ate breakfast')

    def after_breakfast_was_done_she_headed_upstairs_to_give_each_of_their_two_kids_a_bath_while_mark_took_out_the_trash_and_checked_his_email_on_his_computer_in_the_den(self):
        self.Rachel_Stephenson.appearance.append('gave their kids a bath')
        self.Mark_Stephenson.appearance.append('took out the trash')
        self.Mark_Stephenson.appearance.append('checked his email')

    def their_kids_were_like_little_angels_because_they_never_caused_any_trouble_they_were_quiet_when_they_were_eating_they_were_always_dressed_in_impeccable_outfits_when_they_left_the_house_and_there_was_no_yelling_in_their_household_because_everyone_was_kind_to_one_another(self):
        self.Rachel_Stephenson.relations['children'].append('quiet when they were eating')
        self.Rachel_Stephenson.relations['children'].append('dressed in impeccable outfits')
        self.Rachel_Stephenson.relations['children'].append('kind to one another')
        self.Mark_Stephenson.relations['children'].append('quiet when they were eating')
        self.Mark_Stephenson.relations['children'].append('dressed in impeccable outfits')
        self.Mark_Stephenson.relations['children'].append('kind to one another')

    def they_would_go_out_for_walks_after_breakfast_but_by_eight_thirty_am_rachel_already_had_her_work_clothes_on_as_well_as_her_makeup_done_at_nine_am_she_was_usually_working_on_a_canvas_or_painting_at_one_of_three_coffee_shops_that_all_opened_at_eight_am_in_lake_bloomfield_illinois_where_she_lived_with_her_family(self):
        self.Rachel_Stephenson.relations['children'].append('went out for walks')
        self.Mark_Stephenson.relations['children'].append('went out for walks')
        self.Rachel_Stephenson.appearance.append('had work clothes on')
        self.Rachel_Stephenson.appearance.append('makeup done')
        self.Rachel_Stephenson.occupation.append('painting')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

