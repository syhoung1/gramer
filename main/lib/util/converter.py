import re

SI = 29.5735

VOLUME_UNITS = {
    "tsp" : "teaspoon",
    "teaspoon" : "teaspoon",
    "t" : "teaspoon",
    "tablespoon" : "tablespoon",
    "tbsp" : "tablespoon",
    "T" : "tablespoon",
    "fluid ounce" : "fluid ounce",
    "fl oz" : "fluid ounce",
    "cup" : "cup",
    "c" : "cup",
    "pint" : "pint",
    "pt" : "pint",
    "quart" : "quart",
    "qt" : "quart",
    "gallon" : "gallon",
    "gal" : "gallon",
    "cubic inch" : "cubic inch"
}

US_WEIGHTS = {
    "oz" : "ounce",
    "ounce" : "ounce",
    "lb" : "pound",
    "pound" : "pound",
}

# all ratios represent how many fl oz there are in 1 unit of vol.
# ex: for 1 cup, the ratio is (8 fl oz) / (1 cup), so "cup" : "8"
# ratio SI is the ratio of mL per fl oz
US_VOLUME_RATIOS = {
    "cm^3" : float(1/SI),
    "tsp" : float(1/6),
    "tbsp" : float(1/2),
    "in^3" : .5541,
    "fl oz" : 1,
    "c" : 8,
    "pt" : 16,
    "qt" : 32,
    "gal" : 128,
}

# returns amount and unit as a tuple
def get_amount_from(text):
    if type(text) == str:
        # searches for floats or integers followed by a target unit ex. "2.3 oz"
        description = re.search("(\d*\.?(?=\d)\d*)\s"
                                "("+'|'.join(US_UK_VOLUME_UNITS)+")", text)
        if description == None:
            return None
        else:
            amount = float(description.group(1))
            input_unit = US_UK_VOLUME_UNITS[description.group(2)]
        return (amount, input_unit)
