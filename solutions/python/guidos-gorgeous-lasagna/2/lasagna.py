"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
print(EXPECTED_BAKE_TIME)

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

bake_time_remaining(30)


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - the number of layesr in the lasagna
    :return: int - number of layers * 2
    This function takes the number of layers in the lasagna, and each layer takes 2 minutes to be prepared, so 
    we multiply the number of layers by 2, and we got the preparation time in minutes.
    """
    return number_of_layers * 2
    
    

preparation_time_in_minutes(2)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapseb_bake_time: int - elapsed cooking time.
    :return: int: total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the time already
    spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return number_of_layers * 2 + elapsed_bake_time
    

elapsed_time_in_minutes(3, 20)

