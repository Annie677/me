Notes: (PANDA)
pattern_of_bools = ["o" in x for x in pets_series]

pattern_of_bools = [x[0] == "C" in x for x in pets_series]
This one is more specific for selecting the words in the list with the first (0) letter of "C". 

Debug function:
def a_thing(n):
    return str(n) + str(100)
[a_thing(x) for x in range(10)]
This will return show the items in strings.