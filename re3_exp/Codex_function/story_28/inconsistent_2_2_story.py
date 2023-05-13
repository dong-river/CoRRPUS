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
        self.Payton_Dupree = character('Payton Dupree')
        self.Amanda_Dupree = character('Amanda Dupree')
        self.Olivia_Dupree = character('Olivia Dupree')

    def story(self):
        self.olivia_dupree_is_now_5_years_old()
        self.her_mother_amanda_died_suddenly_five_years_ago_and_she_was_left_in_the_care_of_her_godmother_payton()
        self.hiya_livie()
        self.payton_calls_from_the_hallway_of_her_apartment()
        self.is_your_homework_done()
        self.i_m_playing_a_game_olivia_yells_back_to_her()
        self.come_on_in()
        self.payton_smiles_and_enters_the_living_room()
        self.olivia_is_sitting_cross_legged_on_the_floor_with_an_ipad_propped_up_on_a_pillow()
        self.she_grins_up_at_payton_and_waves()
        self.hello()
        self.she_says_cheerfully()
        self.what_have_you_been_doing_today()
        self.not_much_payton_says_bending_down_to_hug_olivia_and_steal_a_kiss_on_her_cheek()
        self.she_sits_down_beside_her_niece_and_kisses_her_forehead_tenderly_before_ruffling_her_hair()
        self.i_had_a_lot_of_work_to_do_at_the_office_today()
        self.i_want_to_go_there_sometime_olivia_tells_her_seriously_putting_down_the_ipad_and_reaching_for_a_toy_purse_instead()
    def olivia_dupree_is_now_5_years_old(self):
        self.Olivia_Dupree.age.append('5')

    def her_mother_amanda_died_suddenly_five_years_ago_and_she_was_left_in_the_care_of_her_godmother_payton(self):
        self.Amanda_Dupree.relations['mother'] = 'Olivia_Dupree'
        self.Olivia_Dupree.relations['mother'] = 'Amanda_Dupree'
        self.Payton_Dupree.relations['godmother'] = 'Olivia_Dupree'
        self.Olivia_Dupree.relations['godmother'] = 'Payton_Dupree'

    def hiya_livie(self):
        pass

    def payton_calls_from_the_hallway_of_her_apartment(self):
        pass

    def is_your_homework_done(self):
        pass

    def i_m_playing_a_game_olivia_yells_back_to_her(self):
        pass

    def come_on_in(self):
        pass

    def payton_smiles_and_enters_the_living_room(self):
        pass

    def olivia_is_sitting_cross_legged_on_the_floor_with_an_ipad_propped_up_on_a_pillow(self):
        pass

    def she_grins_up_at_payton_and_waves(self):
        pass

    def hello(self):
        pass

    def she_says_cheerfully(self):
        pass

    def what_have_you_been_doing_today(self):
        pass

    def not_much_payton_says_bending_down_to_hug_olivia_and_steal_a_kiss_on_her_cheek(self):
        pass

    def she_sits_down_beside_her_niece_and_kisses_her_forehead_tenderly_before_ruffling_her_hair(self):
        pass

    def i_had_a_lot_of_work_to_do_at_the_office_today(self):
        pass

    def i_want_to_go_there_sometime_olivia_tells_her_seriously_putting_down_the_ipad_and_reaching_for_a_toy_purse_instead(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

