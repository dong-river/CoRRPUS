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
        self.jillian_riley_always_wanted_to_be_a_writer()
        self.her_husband_robert_had_always_been_an_artist_at_heart()
        self.when_they_married_and_began_their_life_together_they_believed_they_would_both_achieve_their_dreams()
        self.instead_robert_lived_his_life_vicariously_through_his_wife_s_stories_and_articles()
        self.he_died_before_he_had_the_chance_to_be_published_himself()
        self.jillian_s_first_story_was_published_in_a_national_newspaper_shortly_after_his_death()
        self.she_took_on_part_time_work_as_a_sales_assistant_at_a_small_bookshop_to_help_support_herself_and_her_daughter()
        self.with_money_tight_jillian_relied_on_her_writing_skills_to_pay_for_shannon_s_education_and_living_expenses()
        self.she_taught_shannon_how_to_appreciate_the_printed_word_and_provided_a_broad_range_of_reading_material_from_romance_novels_to_classics_such_as_shakespeare_and_dickens()
        self.as_shannon_grew_older_she_began_writing_her_own_stories_for_her_mother_to_read_each_night_before_bedtime()
        self.the_story_is_set_in_a_small_city_in_new_england_where_an_exciting_artistic_environment_exists_beside_an_old_mill_that_was_converted_into_shops_selling_various_art_supplies()
    def the_story_is_set_in_a_small_city_in_new_england_where_an_exciting_artistic_environment_exists_beside_an_old_mill_that_was_converted_into_shops_selling_various_art_supplies(self):
        pass

    def jillian_riley_always_wanted_to_be_a_writer(self):
        self.Jillian_Riley.occupation.append('writer')
        self.Jillian_Riley.gender.append('female')

    def her_husband_robert_had_always_been_an_artist_at_heart(self):
        self.Jillian_Riley.relations['husband'] = 'Robert_Riley'
        self.Robert_Riley.relations['wife'] = 'Jillian_Riley'
        self.Robert_Riley.occupation.append('artist')
        self.Robert_Riley.gender.append('male')

    def when_they_married_and_began_their_life_together_they_believed_they_would_both_achieve_their_dreams(self):
        pass

    def instead_robert_lived_his_life_vicariously_through_his_wife_s_stories_and_articles(self):
        pass

    def he_died_before_he_had_the_chance_to_be_published_himself(self):
        pass

    def jillian_s_first_story_was_published_in_a_national_newspaper_shortly_after_his_death(self):
        pass

    def she_took_on_part_time_work_as_a_sales_assistant_at_a_small_bookshop_to_help_support_herself_and_her_daughter(self):
        self.Jillian_Riley.relations['daughter'] = 'Shannon_Riley'
        self.Shannon_Riley.relations['mother'] = 'Jillian_Riley'
        self.Jillian_Riley.occupation.append('sales assistant')
        self.Shannon_Riley.gender.append('female')

    def with_money_tight_jillian_relied_on_her_writing_skills_to_pay_for_shannon_s_education_and_living_expenses(self):
        pass

    def she_taught_shannon_how_to_appreciate_the_printed_word_and_provided_a_broad_range_of_reading_material_from_romance_novels_to_classics_such_as_shakespeare_and_dickens(self):
        pass

    def as_shannon_grew_older_she_began_writing_her_own_stories_for_her_mother_to_read_each_night_before_bedtime(self):
        pass


## Create a world model state to track each character's appearance, personality, and relations with other characters.

