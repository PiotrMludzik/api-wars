# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                      constants
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

# Topics to display.
class Subject:
    PLANETS = 'planets'
    STARSHIPS = 'starships'
    VEHICLES = 'vehicles'


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
        CARGO = 'cargo_capacity'
        CLASS = 'starship_class'
        CREW = 'crew'
        LENGTH = 'length'
        MEGALIGHTS = 'MGLT'
        MODEL = 'model'
        NAME = 'name'
        PASSENGERS = 'passengers'

    class Vehicles:
        ATSPEED = 'max_atmosphering_speed'
        CARGO = 'cargo_capacity'
        CLASS = 'vehicle_class'
        CREW = 'crew'
        LENGTH = 'length'
        MODEL = 'model'
        NAME = 'name'
        PASSENGERS = 'passengers'

    PLANETS = Planets()
    STARSHIPS = Starships()
    VEHICLES = Vehicles()


KEY = Key()


# Constants for the column names and their sort order.
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
        KEY.STARSHIPS.CARGO,
        KEY.STARSHIPS.LENGTH,
        KEY.STARSHIPS.ATSPEED,
        KEY.STARSHIPS.MEGALIGHTS
    ]
    VEHICLES = [
        KEY.VEHICLES.NAME,
        KEY.VEHICLES.MODEL,
        KEY.VEHICLES.CLASS,
        KEY.VEHICLES.CREW,
        KEY.VEHICLES.PASSENGERS,
        KEY.VEHICLES.CARGO,
        KEY.VEHICLES.LENGTH,
        KEY.VEHICLES.ATSPEED
    ]


DATA = Data()
