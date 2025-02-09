emobpy
======

.. image:: https://img.shields.io/pypi/v/emobpy.svg
   :target: https://pypi.org/project/emobpy/
   :alt: emobpy Status Badge

.. image:: https://img.shields.io/pypi/pyversions/emobpy.svg
   :target: https://pypi.org/project/dieterpy/
   :alt: emobpy Python Versions

.. image:: https://img.shields.io/pypi/l/emobpy.svg
   :target: https://pypi.org/project/emobpy/
   :alt: emobpy license

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3675456.svg
   :target: https://doi.org/10.5281/zenodo.3675456
   :alt: Code DOI

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3931663.svg
   :target: https://doi.org/10.5281/zenodo.3931663
   :alt: Dataset DOI

.. image:: https://static.pepy.tech/personalized-badge/emobpy?period=total&units=none&left_color=black&right_color=orange&left_text=Downloads
   :target: https://pepy.tech/project/emobpy
   :alt: emobpy pypi downloads

.. image:: https://img.shields.io/badge/chat-Slack-orange.svg
   :target: https://emobpy.slack.com
   :alt: Use our chat for issues


emobpy is a Python tool that can create battery electric vehicle time series. Four different time series can be created: vehicle mobility time series, driving electricity consumption time series, grid availability time series and grid electricity demand time series. The vehicles mobility time series are created based on mobility statistics. For driving electricity consumption time series, the properties of vehicles can be selected from a database with several actual battery electric vehicles models. `emobpy` is developed by the research group `Transformation of the Energy Economy <https://twitter.com/transenerecon>`_ at `DIW Berlin <https://www.diw.de/en/diw_01.c.604205.en/energy__transportation__environment_department.html>`__ (German Institute of Economic Research).

.. Note::
   **Cite this article:** Gaete-Morales, C., Kramer, H., Schill, WP. et al. An open tool for creating battery-electric vehicle time series from empirical data, emobpy. Sci Data 8, 152 (2021). https://doi.org/10.1038/s41597-021-00932-9

.. raw:: html

    <img src="https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41597-021-00932-9/MediaObjects/41597_2021_932_Fig1_HTML.png" height="400px">


Announcement
------------

Join our webinar and do-a-thon on 25/03/2022 at 10am CET. |open_pdf|. Register your attendance here: https://www.eventbrite.com/e/265898719227


Communication channels
----------------------

Please use the following channels to share ideas, propose enhancements or ask for support:

* Slack: https://emobpy.slack.com (Use our `invite link`_ )
* Gitlab issue: https://gitlab.com/emobpy/emobpy/issues

Instructions
------------

This tool has been tested in window 7, Ubuntu 18.04, Ubuntu 19.04 and Suse Linux. It is recommended to install the package in an dedicated Python environment with Python version 3.6+.

Installation:

.. code-block:: console

   pip install emobpy

Usage
-----
You can use our project template. It is a folder that contains files with mobility probabilities, assumptions in a rules file and python scripts that show different python classes and functions to start generating the time series.
To get a copy of the template folder, we create a project folder. For instance, as shown below, our project name is `my_evs`.

.. code-block:: console

   emobpy create -n my_evs

.. Hint:: When we create a project folder for the first time, emobpy also copies files to our system user folder. In windows is usually located in `c:/users/your_win_user/AppData/Local/emobpy`, while for Linux is `/home/your_linux_user/.local/share/emobpy`. The files hosted contain actual battery electric vehicle models, weather time series hourly across a year for different countries, and driving cycles divided on urban, rural, and highways.

Then by using the command line, we access to project folder `my_evs`:

.. code-block:: console

   cd my_evs

We can run the python script that enables us to generate examples of time series.

.. code-block:: console

   python Step1Mobility.py

read the instruction file in my_evs folder

Jupyter notebook offers a more interactive learning. You can open the ``Time-series_generation.ipynb`` by running jupyter in your console.

.. code-block:: console

   jupyter notebook

In the example section of the documentation, the code is clearly explained. Go directly to the example here_.

Remove library:

.. code-block:: console

   pip uninstall emobpy

***************
Links
***************

* Documentation: https://emobpy.readthedocs.io/
* Source code: https://gitlab.com/diw-evu/emobpy/emobpy
* PyPI releases: https://pypi.org/project/emobpy
* License: http://opensource.org/licenses/MIT
* Code DOI: https://doi.org/10.5281/zenodo.3675456
* Dataset DOI: https://doi.org/10.5281/zenodo.3931663
* Issues: https://gitlab.com/diw-evu/emobpy/emobpy/issues
* Slack chat: https://emobpy.slack.com (Use our `invite link`_ )

***************
Authors
***************

The developers are `Carlos Gaete-Morales (lead) <mailto:cdgaete@gmail.com>`_ and Lukas Trippe.


Changelog:
-----------

v0.6.2 (2021-12-05)

* Fix: Solved updating custom dataset issue. BEV database and weather data are now updated.
* Fix: Logging issue. Messages are now logged in the correct order.
* Fix: Insulation data had an incorrect key `steel` and was not recognized. Heating and cooling calculations are more accurate now.

v0.6.1 (2021-12-02)

* Fix: Availability class had an inadequate allocation of states (locations), causing faulty availability and charging time-series.
* Fix: Add seed to a random number generator (get_seed(seed)).
* Improved message for short hours time series that may cause empty time series.

v0.6.0 (2021-12-01)

* Implemented 1-minute time-step (see template eg3)
* Implemented 1-second time-step (see template eg4)
* Added average power in W per time-step for driving consumption time-series
* Added instant power in W per time-step for driving consumption time-series
* Improved logging. Now the logging is done in a file, while the console can be suppressed
* Results can be exported to "DIETERpy" https://diw-evu.gitlab.io/dieter_public/dieterpy/
* Results can be exported to "SimSES" https://www.ei.tum.de/ees/simses/

*************
Description
*************

Vehicle mobility time series
-----------------------------------------

The vehicle mobility time series contains the location of a vehicle at each point in time. The locations vary according to the mobility of drivers. Possible locations are at home, workplace, shopping, errands, escort, leisure, or driving. When "Driving", the distance travelled is also provided in the time series. The time resolution can be established initially (our examples contains 15 minutes time steps). The daily number of trips, the departure time, the trip purpose, distance travelled, and duration of the trips are determined based on statistics of mobility surveys. Other considerations can also be set up. For instance, the number of working hours per day, the first and last destination of the day, can be established as "at home". The "driving" will always be placed in between two different locations.

Driving electricity consumption time series
-------------------------------------------

The previous time series is used as input to the creation of driving electricity consumption time series. The energy required for every trip is calculated based on the ambient temperature and traction effort for the vehicle's movement. To simulate the travel conditions, driving cycles are taken into account. The tool counts with battery electric vehicle models that are currently in the market. A vehicle's model has to be selected to include the model's parameters and characteristics.


Grid availability time series
-----------------------------

Grid availability time series consists of taking a driving electricity consumption time series and based on the locations. The model assigns charging stations. Different charging stations can be available for a vehicle, and they are chosen based on a probability distribution that adds up 100% for each location. The charging stations defined in this tool are "home", "public", "maker", "workplace", "fast" and "none", although more user-defined charging stations can be established. The charging stations have an associated capacity per time interval, and "none" has zero capacity. Different scenarios of grid availability can be modelled.

Grid electricity demand time series
-----------------------------------

While a grid availability time series contains at each interval information of the charging stations available, such as the maximum power rating allocated to them, a grid electricity demand time series is the one that indicates the actual consumption of electricity from the grid to charge the battery of a vehicle according to its driving needs and grid availability. There are different options available to create a grid electricity demand time series. For example, "Immediate-Full capacity" is an option that informs the energy drawn from the grid at a maximum power rating of a respective charging station until the battery is fully charged or "Immediate-Balanced" option that creates a time series taking into account the duration of a vehicle is connected to a charging station and the energy required to get the battery fully charged, allowing to charge the battery at a lower capacity than the maximum capacity available.




.. _here: https://diw-evu.gitlab.io/emobpy/emobpy/examples/basecase.html#method-1-using-jupyter-notebook

.. _`invite link`: https://join.slack.com/t/emobpy/shared_invite/zt-tiatky76-cx0C4ss566Zb_z4p1QthMg



.. |open_pdf| raw:: html

    <a href="https://www.diw.de/de/diw_01.c.837535.de/veranstaltungen/emobpy__a_tool_for_time_series_generation_of_battery_electric_vehicles.html" target="_blank">Webinar program here</a>


.. <a href="_static/0/webinar22/emobpy_webinar_program.pdf" target="_blank">Webinar program here</a>