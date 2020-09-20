# ---------------------------------------------------------------------------------------------------------------------
#                                                       API Wars
#                                                      constants
#                                                        v 1.0
# ---------------------------------------------------------------------------------------------------------------------

# Topics to display.
class _Subject:
    PLANETS = 'planets'
    STARSHIPS = 'starships'
    VEHICLES = 'vehicles'


SUBJECT = _Subject()


# Key names for subject data.
class _Key:
    class Planets:
        CLIMATE = 'climate'
        DIAMETER = 'diameter'
        NAME = 'name'
        POPULATION = 'population'
        TERRAIN = 'terrain'
        WATER = 'surface_water'

    class Starships:
        ATSP = 'max_atmosphering_speed'
        CARGO = 'cargo_capacity'
        CLASS = 'starship_class'
        CREW = 'crew'
        LENGTH = 'length'
        MGLT = 'MGLT'
        MODEL = 'model'
        NAME = 'name'
        PASSENGERS = 'passengers'

    class Vehicles:
        ATSP = 'max_atmosphering_speed'
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


KEY = _Key()


# Constants for the column names and their sort order.
class _Data:
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
        KEY.STARSHIPS.ATSP,
        KEY.STARSHIPS.MGLT
    ]
    VEHICLES = [
        KEY.VEHICLES.NAME,
        KEY.VEHICLES.MODEL,
        KEY.VEHICLES.CLASS,
        KEY.VEHICLES.CREW,
        KEY.VEHICLES.PASSENGERS,
        KEY.VEHICLES.CARGO,
        KEY.VEHICLES.LENGTH,
        KEY.VEHICLES.ATSP
    ]


DATA = _Data()


class _NewColumnName:
    MGLT = 'Megalights'


NEW_COLUMN_NAME = _NewColumnName()
