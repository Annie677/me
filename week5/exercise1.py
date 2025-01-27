# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    for i in range (9,0,-1):
        print("Getting ready to strat in {}".format(i))
        continue
    print ("Let's go!")

    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"] ** 2 + triangle["height"] ** 2
    base = triangle["base"]
    height = triangle["height"]
    hypotenuse = triangle["hypotenuse"]
    print("area = " + str((base * height) / 2))
    print("side lengths are:")
    print("base: {}".format(base))
    print("height: {}".format(height))
    print("hypotenuse: {}".format(hypotenuse))

    another_hyp = 5 ** 2 + 6 ** 2
    print(another_hyp)

    yet_another_hyp = 40 ** 2 + 30 ** 2
    print(yet_another_hyp)
    return 


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    countdown_list = []
    for i in range (start, stop-1, -1):
        if start == start:
            countdown_list.append(message + str(start))
            print("{message} {number}".format(message=message, number=str(start)))
            start = start -1
            if start <= stop-1:
                countdown_list.append(completion_message)
                print (completion_message)
    return countdown_list


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    hypotenuse = (base ** 2 + height ** 2) ** 0.5
    return hypotenuse


def calculate_area(base, height):
    area = (base * height) / 2 
    return area


def calculate_perimeter(base, height):
    hypotenuse = (base ** 2 + height ** 2) ** 0.5
    perimeter = base + height + hypotenuse
    return perimeter

def calculate_aspect(base, height):
    if base == height:
        aspect = "equal"
    elif base < height:
        aspect = "tall"
    elif base > height:
        aspect = "wide"
    return aspect


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    triangle_fact= {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }
    return triangle_fact


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}""".format(height =facts_dictionary["height"],
                                base= facts_dictionary["height"],
                                hypotenuse= facts_dictionary["hypotenuse"])
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}""".format(height =facts_dictionary["height"],
                                base= facts_dictionary["height"],
                                hypotenuse= facts_dictionary["hypotenuse"])
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}""".format(height =facts_dictionary["height"],
                                base= facts_dictionary["height"],
                                hypotenuse= facts_dictionary["hypotenuse"])

    pattern = (
        "This triangle is {area}{units}²\n".format(area=facts_dictionary["area"],
                                                                    units="mm") +
        "It has a perimeter of {perimeter}{units}\n".format(perimeter=facts_dictionary["perimeter"],
                                                                            units="mm") +
        "This is a {aspect} triangle.\n".format(aspect= facts_dictionary["aspect"])
    )

    facts = pattern.format(**facts_dictionary)

    if facts_dictionary["aspect"] == "tall":
        print(tall + pattern)
        triangle = tall
        
    elif facts_dictionary["aspect"]== "wide":
        print(wide + pattern)
        triangle = wide

    else:
        print (equal+pattern)
        triangle = equal
    return facts + triangle
    

#python3 ../course/week5/tests.py


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    triangle = get_triangle_facts(base, height, units="mm")
    diagram = tell_me_about_this_right_triangle(triangle)
    if return_diagram and return_dictionary:
        return str(diagram) + str(triangle)
    elif return_diagram:
        return str(diagram)
    elif return_dictionary:
        return str(triangle)
    else:
        print("You're an odd one, you don't want anything!")

#"http://api.wordnik.com/v4/words.json/randomWords?" is replaced by the 
# https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}
def wordy_pyramid():
    import requests

    baseURL = (
        "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}"
        "&minLength={length}"
        "&maxLength={length}"
        "&limit=1"
    )
    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL.format(base = baseURL, length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    for i in range(20, 3, -2):
        url = baseURL.format(base = baseURL, length=i)
        r = requests.get(url)
        if r.status_code is 200:
            message = r.json()[0]["word"]
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
    return pyramid_list


def get_a_word_of_length_n(length):
    import requests
    length_list = []
    limit = 1
    template = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length} "
    for i in range (limit):
        url = template.format(base= template, length= i)
        r = requests.get(url)
        if r.status_code is 200:
            word = r.json()[0]["word"]
            length_list.append(word)
            return length_list
        else:
            print ("error?")



def list_of_words_with_lengths(list_of_lengths):
    import requests

    length_list = []
    template = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length} "
    for i in range(3,21, 2):
        url = template.format(base=template, length = list_of_lengths)
        r = requests.get(url)
        if r.status_code is 200:
            words = r.json()[0]["word"]
            length_list.append(words)
    return length_list
        

if __name__ == "__main__":
    do_bunch_of_bad_things()
    wordy_pyramid("a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
