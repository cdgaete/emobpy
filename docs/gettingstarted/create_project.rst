.. _start-create-project:

******************************
Creating a project folder
******************************

Before start creating time-series we have to create a new project folder. By creating a project we will copy all required files from a template folder. These files can be modified according to our research purpose.

In our example, we want to create a new project called *my_evs* and use the console to create the project folder. Open the console (or terminal) where you want to create the project folder (e.g. in Windows by right-clicking and shift and choosing *Open Windows Terminal here*), or navigate to the desired folder within the console.

Once you are in the desired folder and if emobpy was installed correctly, type the following command:

.. code-block:: bash

    $ emobpy create -n my_evs

or:

.. code-block:: bash

    $ emobpy create --name my_evs

.. warning:: The name of the project must not contain any blanks. This can lead to errors.

Further options
===============

In addition, further settings can be made. For example, a seed can be set. This allows that the same calculations are always executed in the same way. This makes it easy to compare projects and simplifies further development. If no seed is given, it will be randomly generated.

.. list-table::
   :widths: 15 15 15 70
   :header-rows: 1

   * - Argument
     - Shortcut
     - Optional
     - Description
   * - --name
     - -n
     - Required
     - Name of the project folder.
   * - --template
     - -t
     - Optional
     - Select a specific example project.
   * - --seed
     - -s
     - Optional
     - Set a seed to make calculations reproducible.

This will create a folder and file structure as follows.

.. code-block:: bash

    ├── my_evs
    │   └── config_files
    │       ├── DepartureDestinationTrip.csv
    │       ├── DistanceDurationTrip.csv
    │       ├── TripsPerDay.csv
    │       ├── rules.yml
    │   ├── Time-series_generation.ipynb
    │   ├── Step1Mobility.py
    │   ├── Step2DrivingConsumption.py
    │   ├── Step3GridAvailability.py
    │   ├── Step4GridDemand.py
    │   ├── Visualize_and_Export.ipynb



To start creating the time series, follow the instructions on the next page.
