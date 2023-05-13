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
        self.Karen_Fletcher = character('Karen Fletcher')
        self.Kate_Fletcher = character('Kate Fletcher')
        self.Julia_Fletcher = character('Julia Fletcher')

    def story(self):
        self.julia_fletcher_knocks_on_the_door_to_her_sister_s_hospital_room()
        self.karen_answers_the_door_having_just_come_out_of_the_bathroom()
        self.oh_good_you_re_up()
        self.the_doctor_said_you_could_go_home_today_julia_says_hugging_her_sister()
        self.that_s_great_news()
        self.i_was_beginning_to_feel_like_a_prisoner_in_here_karen_says()
        self.although_i_m_glad_they_took_care_of_my_daughter()
        self.they_took_care_of_your_daughter()
        self.julia_asks()
        self.the_one_who_s_dead()
        self.karen_gasps_and_holds_her_stomach_grimacing_with_pain_as_she_collapses_on_the_bed_tears_streaming_down_her_face()
        self.she_s_dead()
        self.she_died()
        self.she_cries()
        self.what_happened()
        self.was_it_a_car_accident()
        self.i_m_so_sorry_karen_julia_says_as_she_sits_on_the_bed_next_to_her_sister_and_pulls_her_into_a_hug()
        self.no_one_told_you_yet()
        self.you_must_have_been_asleep_when_they_came_and_told_me()
        self.her_voice_catches_in_her_throat_as_she_realizes_what_happened_while_karen_was_asleep()
    def julia_fletcher_knocks_on_the_door_to_her_sister_s_hospital_room(self):
        pass
    def karen_answers_the_door_having_just_come_out_of_the_bathroom(self):
        self.Karen_Fletcher.occupation.append('patient')
        self.Karen_Fletcher.gender.append('female')
    def oh_good_you_re_up(self):
        pass
    def the_doctor_said_you_could_go_home_today_julia_says_hugging_her_sister(self):
        self.Karen_Fletcher.relations['sister'] = 'Julia_Fletcher'
        self.Julia_Fletcher.relations['sister'] = 'Karen_Fletcher'
        self.Julia_Fletcher.gender.append('female')
    def that_s_great_news(self):
        pass
    def i_was_beginning_to_feel_like_a_prisoner_in_here_karen_says(self):
        pass
    def although_i_m_glad_they_took_care_of_my_daughter(self):
        self.Karen_Fletcher.relations['daughter'] = 'Kate_Fletcher'
        self.Kate_Fletcher.relations['mother'] = 'Karen_Fletcher'
        self.Kate_Fletcher.gender.append('female')
    def they_took_care_of_your_daughter(self):
        pass
    def julia_asks(self):
        pass
    def the_one_who_s_dead(self):
        pass
    def karen_gasps_and_holds_her_stomach_grimacing_with_pain_as_she_collapses_on_the_bed_tears_streaming_down_her_face(self):
        pass
    def she_s_dead(self):
        pass
    def she_died(self):
        pass
    def she_cries(self):
        pass
    def what_happened(self):
        pass
    def was_it_a_car_accident(self):
        pass
    def i_m_so_sorry_karen_julia_says_as_she_sits_on_the_bed_next_to_her_sister_and_pulls_her_into_a_hug(self):
        pass
    def no_one_told_you_yet(self):
        pass
    def you_must_have_been_asleep_when_they_came_and_told_me(self):
        pass
    def her_voice_catches_in_her_throat_as_she_realizes_what_happened_while_karen_was_asleep(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

