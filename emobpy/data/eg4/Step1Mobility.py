from emobpy import Mobility

# Initialize seed
from emobpy.tools import set_seed
set_seed()

hrs = 24 # short period, otherwise, it would take ages, because of one second timestep
steps = 1/3600 # 1 second

if __name__ == '__main__':

    m = Mobility()
    m.set_params("This_is_a_file_name_prefix", hrs, steps, "user_defined", "01/01/2020")
    m.set_stats(
        "TripsPerDay.csv",
        "DepartureDestinationTrip.csv",
        "DistanceDurationTrip.csv",
    )
    m.set_rules("user_defined")
    m.run()
    m.save_profile("db")
