GPT_example_type_1="""
Determine if there's inconsistency in the following story:

The story is set in the present day and takes place in the United States. Joan Westfall is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind. Brent Westfall is Joan's husband. He is a kind and loving man who is struggling to cope with his wife's death.Jason Westfall is Joan's son. He is a young boy who is struggling to understand his mother's death.
Jason Westfall sits on the floor, looking at the empty box that used to hold his sister-in-law's belongings. His gaze is unfocused, his eyes brimming with tears. He cries for hours, eventually falling asleep from exhaustion. When he wakes up, he feels dazed and ill. Joan died in a car accident on a rainy day several weeks ago. She was coming home from work when she had a seizure behind the wheel and her car veered off the road and crashed into a tree. The doctors said she died instantly. Jason has been carrying on with life ever since as best he can manage, but he still doesn't really know how to cope with Joan's death. He didn't get along very well with her while she was alive and they only saw each other rarely; it never seemed like a real loss when he lost touch with her completely years ago. But now he feels utterly alone without her and desperately misses having someone in his life who cared about him and whom he could care about in return. Brent is struggling to cope with his wife's death as well. He was always the one who was there for her when she needed him and he feels lost without her. He is trying to be strong for Jason, but he is also grieving deeply.

Answer: Jason Westfall is Joan's son. But later it says Joan is Jason Westfall's sister-in-law. So there are inconsistencies.
===
Determine if there's inconsistency in the following story:

The story is set in a large city. Shannon Riley is a young woman in her early twenties. She has long, brown hair and blue eyes. She is of average height and build. Robert Riley is Shannon's father. He was a successful journalist who died suddenly of a heart attack. Jillian Riley is Shannon's older sister by three years. She is a successful corporate lawyer who lives and works in the city.
Jillian Riley couldn't believe her sister was actually moving to the city. "I've finally found my dream job," said Shannon. "I'm going to be a journalist." "That's great, sis," said Jillian, smiling. "But how are you going to pay the rent? I hope you know you don't have a job lined up yet. There are no newspapers in town, so it won't be easy finding a job." "But I have found a job!" exclaimed Shannon. "Robert Riley hired me." Jillian choked on her soup. "What?" she asked incredulously when she'd recovered herself. "You're not going to work for Robert Riley!" Jillian knew her father had moved back to the city about three months ago, but she didn't know he'd gotten back into journalism after retiring many years ago. Apparently, Shannon hadn't known either. She just assumed that Robert had moved back to the city and was living off his retirement fund while taking care of his two granddaughters full-time.

Answer: No inconsistency
===
"""

codex_init_prompt = """
### Create a world model state and track each character's appearance, personality, relationship to other characters, and other cruical attributes.
class character:
    def __init__(self, name):
        self.name = name
        self.appearance = []
        self.personality = []
        self.occupation = []
        self.gender = []
        self.status = []
        self.age = []
        self.relations = {}

"""

codex_init_prompt_2 = """
class character:
    def __init__(self, name):
        self.name = name
        self.appearance = []
        self.personality = []
        self.occupation = []
        self.gender = []
        self.status = []
        self.age = []
        self.relations = {}

"""

codex_init_prompt_3 = """
class character:
    def __init__(self, name):
        self.name = name
        self.appearance = []
        self.occupation = []
        self.gender = []
        self.age = []
        self.relations = {}

"""

## extract as json
GPT_example_type_2=""
## line by line prompting
GPT_example_type_3=""

GPT3_consistency_prompt_1="""
Question: Are there are contradiction in the person's personality: kind, sympathetic
Answer: No
===
Question: Are there are contradiction in the person's appearance: blue eye, yellow hair, handsome
Answer: No
===
Question: Are there are contradiction in the person's relations to others: mother of Joan_Westfall, wife of Joan_Westfall
Answer: Yes
===
Question: Are there are contradiction in the person's status: working, died
Answer: Yes
===
"""

GPT3_consistency_prompt_2="""
Question: Are there are contradiction in the person's description? The person's personality is kind, sympathetic. The person's appearance is blue eye, yellow hair, handsome. The person's relation to others is the mother of Joan_Westfall, the wife of Joan_Westfall. The person's status is working, died
Answer: The person cannot be both the mother of Joan_Westfall and the wife of Joan_Westfall. The person cannot be both working and died. So there are 2 contradictions in total.
===
Question: Are there are contradiction in the person's description? The person's personality is kind, sympathetic. The person's appearance is blue eye, yellow hair, handsome. The person's relation to others is the mother of Joan_Westfall, the wife of Jason_Westfall. The person's status is working, happy
Answer: There is no contradiction in the person's description. So 0 contradictions in total.
===
"""

GPT3_consistency_prompt_3="""
Question: Are there are contradiction in the person's description?
Story setting: The Breat Westfall's personality is kind, sympathetic. The Breat Westfall's appearance is blue eye, yellow hair, handsome. The person's relation to others is the mother of Joan_Westfall
Story: Breat Westfall is the wife of Joan_Westfall
Answer: The person cannot be both the mother of Joan_Westfall and the wife of Joan_Westfall. So there are 1 contradictions in total.
===
Question: Are there are contradiction in the person's description? 
Story Setting: The person's personality is kind, sympathetic. The person's appearance is blue eye, yellow hair, handsome.
Story: The person's relation to others is the mother of Joan_Westfall, the wife of Jason_Westfall. The person's status is working, happy
Answer: There is no contradiction in the person's description. So 0 contradictions in total.
===
Question: Are there are contradiction in the person's description? 
Story Setting: Joan Westfall has brown eyes and is of medium height. Joan's occupation is a teacher. Joan's age is 27 years old.
Story: Joan Westfall's appearance is short. Joan's occupation is a teacher. Joan's age is 30s.
Answer: Joan Westfall cannot be both short and of medium height. Joan Westfall cannot be both in his 30s and 27 years old. So there are 2 contradictions in total.
===
"""

Codex_consistency_prompt_1 = """
Check whether there are inconsistencies for the following character.
John_Stephen.relations{'best friend': 'Sarah_Mason', 'husband': 'Mark_Stephenson', 'children': 'two'}
Answer: Consistent
===
Check whether there are inconsistencies for the following character.
Rachel_Stephenson.relations={'mother': 'Joan_Westfall', 'sister': 'Joan_Westfall'}
Answer: Inconsistent
===
Check whether there are inconsistencies for the following character.
Sarah_Mason.appearance=['beautiful', 'long blond hair', 'blue eyes']
Answer: Consistent
===
Check whether there are inconsistencies for the following character.
Claire.occupation=['stay-at-home mom', 'police officer']
Answer: Inconsistent
===
Check whether there are inconsistencies for the following character.
Olivia_Fria_Spierings.age=['young', '18']
Answer: Consistent
===
"""

replace_coref_prompt = """
Replace the pronoun references to Thomas Watkins with his full name in []. After the replacement, You should not have any "she", "he", "they", "his", "him", "her" in the output.
Input: Thomas Watkins squinted as he surveyed the darkness surrounding the small town. He and his team had been in place for almost twenty-four hours, so they were all getting tired. They had searched the town thoroughly, but they hadn't been able to find any sign of the killer.
Output: [Thomas Watkins] squinted as [Thomas Watkins] surveyed the darkness surrounding the small town. [Thomas Watkins] and [Thomas Watkins'] team had been in place for almost twenty-four hours, so they [Thomas Watkins' team] were all getting tired. [Thomas Watkins' team] had searched the town thoroughly, but [Thomas Watkins' team] hadn't been able to find any sign of the killer.
---
Replace the pronoun references to Joan Westfall, Jason Westfall, and Brent Westfall with their full name in []. After the replacement, You should not have any "she", "he", "they", "his", "him", "her" in the output.
Input: The story is set in the present day and takes place in the United States. Joan Westfall is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind. Brent Westfall is Joan's husband. He is a kind and loving man who is struggling to cope with his wife's death. Jason Westfall is Joan's son. He is a young boy who is struggling to understand his mother's death.
Output: 

The story is set in the present day and takes place in the United States. [Joan Westfall] is a woman who has died in a car accident. [Joan Westfall] is a kind and sympathetic person who is eager to help the people she left behind. [Brent Westfall] is  [Joan Westfall]'s husband. [Brent Westfall] is a kind and loving man who is struggling to cope with [Joan Westfall]'s death. Jason Westfall is [Joan Westfall]'s son. [Jason Westfall] is a young boy who is struggling to understand  [Joan Westfall]'s death.

----
Replace the pronoun references to Joan Westfall, Jason Westfall, and Brent Westfall with their full name in []. After the replacement, You should not have any "she", "he", "they", "his", "him", "her" in the output.
Input: 
"""

event_extraction_prompt = """
Parse the following story into simple events about Joan Westfall, Brent Westfall, and Jason Westfall:
The story is set in the present day and takes place in the United States. Joan Westfall is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind. Brent Westfall is Joan's husband. He is a kind and loving man who is struggling to cope with his wife's death. Jason Westfall is Joan's son. He is a young boy who is struggling to understand his mother's death.

Events:
Joan Westfall is a woman.
Joan Westfall has died in a car accident.
Joan Westfall is a kind and sympathetic person
Joan Westfall is eager to help the people she left behind.
Brent Westfall is Joan's husband.
Brent Westfall is a kind and loving man
Brent Westfall is struggling to cope with his wife's death.
Jason Westfall is Joan's son.
Jason Westfall is a young boy
Jason Westfall is struggling to understand his mother's death.
###

Parse the following story into simple events about Joan Westfall, Brent Westfall, and Jason Westfall:
Jason Westfall sits on the floor, looking at the empty box that used to hold his sister-in-law's belongings. His gaze is unfocused, his dark blue eyes brimming with tears. He cries for hours, eventually falling asleep from exhaustion. When he wakes up, he feels dazed and ill. Joan died in a car accident on a rainy day several weeks ago. She was coming home from work when she had a seizure behind the wheel and her car veered off the road and crashed into a tree. The doctors said she died instantly. Jason has been carrying on with life ever since as best he can manage, but he still doesn't really know how to cope with Joan's death.

Events:
Jason Westfall sits on the floor.
Jason Westfall is looking at the empty box that used to hold his sister-in-law's belongings.
Jason Westfall's gaze is unfocused.
Jason Westfall's dark blue eyes are brimming with tears.
Jason Westfall cries for hours
Jason Westfall eventually falls asleep from exhaustion
Jason Westfall wakes up
Jason Westfall feels dazed and ill
Joan Westfall died in a car accident on a rainy day several weeks ago
Joan Westfall was coming home from work.
Joan Westfall had a seizure behind the wheel.
Joan Westfall's car veered off the road.
Joan Westfall's car crashed into a tree.
Joan Westfall died instantly.
Jason Westfall is carrying on with life.
Jason Westfall doesn't really know how to cope with Joan's death.
###
"""

check_consistency_GPT3_example = """
Determining whether the story contradicts the story setting.
Story Setting: Joan Westfall's husband is Brent Westfall. Joan Westfall's son is Jason Westfall.
Story: Joan Westfall's sister-in-law is Brent Westfall
Answer: Contradiction. Joan Westfall's sister-in-law is Brent Westfall contradicts with Joan Westfall's husband is Brent Westfall.
###
Determining whether the story contradicts the story setting.
Story Setting: Amy Gutman's husband is Bob Gutman
Story: Amy Gutman's son is Charlie Gutman.
Answer: No contradiction. The story is consistent with the story setting.
###
Determining whether a story is contradicts with the story setting.
Story Setting: Joan Westfall's occupation is a teacher.
Story: Joan Westfall's occupation is a part-time writer.
Answer: No contradiction. It's possible for Joan Westfall to be a part-time writer and a teacher at the same time.
### 
Determining whether a story is contradicts with the story setting.
Story Setting: Joan Westfall has brown eyes and is of medium height.
Story: Joan Westfall is short.
Answer: Contradiction. Joan Westfall is short contradicts Joan Westfall is of medium height.
### 
Determining whether a story is contradicts with the story setting.
"""

transform_to_description_example = """
Select the appropriate descriptions for the attribute and transform it to natural language:
Input: Jason Westfall appearance ['dark blue eyes', 'tears', 'dazed', 'ill', 'cigarette']
Output: Jason Westfall has dark blue eyes. Jason Westfall is dazed and ill with tears on her face.
###
Select the appropriate descriptions for the attribute and transform it to natural language:
Input: Jason Westfall occupation ['student', 'small town', 'racing car']
Output: Jason Westfall is a student.
### 
Select the appropriate descriptions for the attribute and transform it to natural language:
"""

codex_comment_example="""
## The story is set in the present day and takes place in the United States.
## Joan Westfall is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind.
## Brent Westfall is Joan's husband. He is a kind and loving man who is struggling to cope with his wife's death.
## Jason Westfall is Joan's son. He is a young boy who is struggling to understand his mother's death.
## Jason Westfall sits on the floor, looking at the empty box that used to hold his sister-in-law's belongings. 
## His gaze is unfocused. his dark blue eyes brimming with tears.
## He cries for hours, eventually falling asleep from exhaustion.
## When he wakes up, he feels dazed and ill.
## Joan died in a car accident on a rainy day several weeks ago.
## Jason has been carrying on with life ever since as best he can manage, but he still doesn't really know how to cope with Joan's death.
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
        self.Joan_Westfall = character('Joan Westfall')
        self.Jason_Westfall = character('Jason Westfall')
        self.Brent_Westfall = character('Brent Westfall')
        
    def story(self):
        ## The story is set in the present day and takes place in the United States.
        ## Joan Westfall is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind.
        self.Joan_Westfall.gender.append('female')
        ## Brent Westfall is Joan's husband. He is a kind and loving man who is struggling to cope with his wife's death.
        self.Joan_Westfall.relations['husband'] = 'Brent_Westfall'
        self.Brent_Westfall.relations['wife'] = 'Joan_Westfall'
        self.Brent_Westfall.gender.append('male')
        ## Jason Westfall is Joan's son. He is a young boy who is struggling to understand his mother's death.
        self.Joan_Westfall.relations['son'] = 'Jason_Westfall'
        self.Jason_Westfall.relations['mother'] = 'Joan_Westfall'
        self.Jason_Westfall.age.append('young')
        self.Jason_Westfall.gender.append('male')
        ## Jason Westfall sits on the floor, looking at the empty box that used to hold his sister-in-law's belongings. 
        self.Jason_Westfall.relations['sister_in_laws'] = 'Joan_Westfall'
        ## His gaze is unfocused. his dark blue eyes brimming with tears.
        self.Jason_Westfall.appearance.append("dark blue eyes")
        ## He cries for hours, eventually falling asleep from exhaustion.
        ## When he wakes up, he feels dazed and ill.
        ## Joan died in a car accident on a rainy day several weeks ago.
        ## Jason has been carrying on with life ever since as best he can manage, but he still doesn't really know how to cope with Joan's death.

###
"""

function_definition_example="""    def set_appearance(self, character, appearance):
        character.appearance.append(appearance)
    
    def set_occupation(self, character, occupation):
        character.occupation.append(occupation)
    
    def set_gender(self, character, gender):
        character.gender.append(gender)
    
    def set_age(self, character, age):
        character.age.append(age)
    
    def set_relation(self, character, relation, other_character):
        character.relations[relation] = other_character.name
        
"""
codex_function_abstract_example="""
## The story is set in the present day and takes place in the United States.
## Joan Westfall is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind.
## Brent Westfall is Joan's husband. He is a kind and loving man who is struggling to cope with his wife's death.
## Jason Westfall is Joan's son. He is a young boy who is struggling to understand his mother's death.
## Jason Westfall sits on the floor, looking at the empty box that used to hold his sister-in-law's belongings. 
## His gaze is unfocused. his dark blue eyes brimming with tears.
## He cries for hours, eventually falling asleep from exhaustion.
## When he wakes up, he feels dazed and ill.
## Joan died in a car accident on a rainy day several weeks ago.
## Jason has been carrying on with life ever since as best he can manage, but he still doesn't really know how to cope with Joan's death.
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
        self.Joan_Westfall = character('Joan Westfall')
        self.Jason_Westfall = character('Jason Westfall')
        self.Brent_Westfall = character('Brent Westfall')
    
    def set_appearance(self, character, appearance):
        character.appearance.append(appearance)
    
    def set_occupation(self, character, occupation):
        character.occupation.append(occupation)
    
    def set_gender(self, character, gender):
        character.gender.append(gender)
    
    def set_age(self, character, age):
        character.age.append(age)
    
    def set_relation(self, character, relation, other_character):
        character.relations[relation] = other_character.name
        
    def story(self):
        ## The story is set in the present day and takes place in the United States.
        ## Joan Westfall is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind.
        self.set_gender(self.Joan_Westfall, "female")
        ## Brent Westfall is Joan's husband. He is a kind and loving man who is struggling to cope with his wife's death.
        self.set_relation(self.Joan_Westfall, 'husband', self.Brent_Westfall)
        self.set_relation(self.Brent_Westfall, 'wife', self.Joan_Westfall)
        self.set_gender(self.Brent_Westfall, "male")
        ## Jason Westfall is Joan's son. He is a young boy who is struggling to understand his mother's death.
        self.set_relation(self.Joan_Westfall, 'son', self.Jason_Westfall)
        self.set_relation(self.Jason_Westfall, 'mother', self.Joan_Westfall)
        self.set_age(self.Jason_Westfall, "young")
        self.set_gender(self.Jason_Westfall, "male")
        ## Jason Westfall sits on the floor, looking at the empty box that used to hold his sister-in-law's belongings. 
        self.set_relation(self.Jason_Westfall, 'sister_in_laws', self.Joan_Westfall)
        self.set_relation(self.Joan_Westfall, 'brother_in_laws', self.Jason_Westfall)
        ## His gaze is unfocused. his dark blue eyes brimming with tears.
        self.set_appearance(self.Jason_Westfall, "dark blue eyes") 
        ## He cries for hours, eventually falling asleep from exhaustion.
        ## When he wakes up, he feels dazed and ill.
        ## Joan died in a car accident on a rainy day several weeks ago.
        ## Jason has been carrying on with life ever since as best he can manage, but he still doesn't really know how to cope with Joan's death.
###
"""


codex_function_example="""
### Create a world model state and track each character's appearance, personality, relationship to other characters, and other cruical attributes.
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
        self.Joan_Westfall = character('Joan Westfall')
        self.Jason_Westfall = character('Jason Westfall')
        self.Brent_Westfall = character('Brent Westfall')
        
    def story(self):
        self.the_story_is_set_in_the_present_day_and_takes_place_in_the_united_states()
        self.joan_westfall_is_a_woman_who_has_died_in_a_car_accident_she_is_a_kind_and_sympathetic_person_who_is_eager_to_help_the_people_she_left_behind()
        self.brent_westfall_is_joans_husband_he_is_a_kind_and_loving_man_who_is_struggling_to_cope_with_his_wife_s_death()
        self.jason_westfall_is_joans_son_he_is_a_young_boy_who_is_struggling_to_understand_his_mother_s_death()        
        self.jason_westfall_sits_on_the_floor_looking_at_the_empty_box_that_used_to_hold_his_sister_in_laws_belongings()
        self.his_gaze_is_unfocused_his_dark_blue_eyes_brimming_with_tears()
        self.he_cries_for_hours_eventually_falling_asleep_from_exhaustion()
        self.when_he_wakes_up_he_feels_dazed_and_ill()
        self.joan_died_in_a_car_accident_on_a_rainy_day_several_weeks_ago()
        self.jason_has_been_carrying_on_with_life_ever_since_as_best_he_can_manage_but_he_still_doesnt_really_know_how_to_cope_with_joans_death()
    
    def the_story_is_set_in_the_present_day_and_takes_place_in_the_united_states(self):
        pass
        
    def joan_westfall_is_a_woman_who_has_died_in_a_car_accident_she_is_a_kind_and_sympathetic_person_who_is_eager_to_help_the_people_she_left_behind(self):
        self.Joan_Westfall.gender.append('female')
        
    def brent_westfall_is_joan_s_husband_he_is_a_kind_and_loving_man_who_is_struggling_to_cope_with_his_wife_s_death(self):
        self.Joan_Westfall.relations['husband'] = 'Brent_Westfall'
        self.Brent_Westfall.relations['wife'] = 'Joan_Westfall'
        self.Brent_Westfall.gender.append('male')
    
    def jason_westfall_is_joan_s_son_he_is_a_young_boy_who_is_struggling_to_understand_his_mother_s_death(self):
        self.Joan_Westfall.relations['son'] = 'Jason_Westfall'
        self.Jason_Westfall.relations['mother'] = 'Joan_Westfall'
        self.Jason_Westfall.age.append('young')
        self.Jason_Westfall.gender.append('male')
    
    def jason_westfall_sits_on_the_floor_looking_at_the_empty_box_that_used_to_hold_his_sister_in_laws_belongings(self):
        self.Jason_Westfall.relations['sister_in_laws'] = 'Joan_Westfall'
        
    def his_gaze_is_unfocused_his_dark_blue_eyes_brimming_with_tears(self):
        self.Jason_Westfall.appearance.append("dark blue eyes")
        
    def he_cries_for_hours_eventually_falling_asleep_from_exhaustion(self):
        pass
        
    def when_he_wakes_up_he_feels_dazed_and_ill(self):
        pass
        
    def joan_died_in_a_car_accident_on_a_rainy_day_several_weeks_ago(self):
        pass
        
    def jason_has_been_carrying_on_with_life_ever_since_as_best_he_can_manage_but_he_still_doesnt_really_know_how_to_cope_with_joans_death(self):
        pass

"""

attr_to_sent_example = """
Jason Westfall's appearance is dark blue eyes.
Jason Westfall has dark blue eyes.
###
Jason Westfall's appearance is average height.
Jason Westfall is of average height.
###

"""