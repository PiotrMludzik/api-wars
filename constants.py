# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                      constants
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

# Topics to display.
class Subject:
    PLANETS = 'planets'
    STARSHIPS = 'starships'


SUBJECT = Subject()


# Key names for subject data.
class Key:
    class Planets:
        CLIMATE = 'climate'
        DIAMETER = 'diameter'
        NAME = 'name'
        POPULATION = 'population'
        TERRAIN = 'terrain'
        WATER = 'surface_water'

    class Starships:
        ATSPEED = 'max_atmosphering_speed'
        CAPACITY = 'cargo_capacity'
        CLASS = 'starship_class'
        CREW = 'crew'
        LENGTH = 'length'
        MEGALIGHTS = 'MGLT'
        MODEL = 'model'
        NAME = 'name'
        PASSENGERS = 'passengers'

    PLANETS = Planets()
    STARSHIPS = Starships()


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
    STARSHIPS = [
        KEY.STARSHIPS.NAME,
        KEY.STARSHIPS.MODEL,
        KEY.STARSHIPS.CLASS,
        KEY.STARSHIPS.CREW,
        KEY.STARSHIPS.PASSENGERS,
        KEY.STARSHIPS.CAPACITY,
        KEY.STARSHIPS.LENGTH,
        KEY.STARSHIPS.ATSPEED,
        KEY.STARSHIPS.MEGALIGHTS
    ]


DATA = Data()
