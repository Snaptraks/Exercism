# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME = 40
# TODO: define the 'PREPARATION_TIME' constant
PREPARATION_TIME = 2

# TODO: define the 'bake_time_remaining()' function


def bake_time_remaining(elapsed_bake_time):
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Return the preparation time in minutes, based on the number of layers.
    """
    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return the total number of minutes you've been cooking, or the sum of
    your preparation time and the time the lasagna has already spent
    baking in the oven.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
