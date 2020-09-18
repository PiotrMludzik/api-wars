# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                      constants
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

# Topics to display.
class Subject:
    PLANETS = 'planets'


SUBJECT = Subject()


# Key names for subject data.
class Key:
    class Planets:
        CLIMATE = 'climate'
        DIAMETER = "diameter"
        NAME = "name"
        POPULATION = 'population'
        TERRAIN = 'terrain'
        WATER = 'surface_water'

    PLANETS = Planets()


KEY = Key()


# Constants for the names of the topic lists to display and their column sort order.
class Data:
    PLANETS = [
        KEY.PLANETS.NAME,
        KEY.PLANETS.DIAMETER,
        KEY.PLANETS.CLIMATE,
        KEY.PLANETS.TERRAIN,
        KEY.PLANETS.WATER,
        KEY.PLANETS.POPULATION
    ]


DATA = Data()
