# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                      constants
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

# key names
KEY_PLANETS_CLIMATE = 'climate'
KEY_PLANETS_DIAMETER = "diameter"
KEY_PLANETS_NAME = "name"
KEY_PLANETS_POPULATION = 'population'
KEY_PLANETS_TERRAIN = 'terrain'
KEY_PLANETS_WATER = 'surface_water'


# Topics to display.
class Subject:
    PLANETS = 'planets'


# Constants for the names of the topic lists to display and their column sort order.
class Data:
    PLANETS = [
        KEY_PLANETS_NAME,
        KEY_PLANETS_DIAMETER,
        KEY_PLANETS_CLIMATE,
        KEY_PLANETS_TERRAIN,
        KEY_PLANETS_WATER,
        KEY_PLANETS_POPULATION
    ]


SUBJECT = Subject()
DATA = Data()

