headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

one_character = {"name": "a"}

maximum_characters = {"name": "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdab"
                              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}


empty_string = {"name": ""}

higher_character_plus_one = {"name": "Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                     "cdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                                     "abcdabcdabcD"}

special_characters = {"name": '"№%@",'}

characters_with_space = {"name": " A Aaa "}

characters_with_number = {"name": "123"}

empty_characters = {}

without_string_character = {"name": 123}