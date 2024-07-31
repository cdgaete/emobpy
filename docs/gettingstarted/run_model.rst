*************************
Generate the time-series
*************************

After having created a project folder (previuos section), you are ready to run the model. This happens in four steps.

The information in this chapter can also be found in the Instruction.txt file that is created with the creation of a new project folder.

Base Case
==========

If not already done, change to project folder:

.. code-block:: bash

    $ cd my_evs

.. warning:: It is recommended to perform the following steps only if a conda environment has been installed and activated. Instructions can be found in the :ref:`installation` page.


Method 1: Jupyer Notebook
-------------------------

.. code-block:: bash

    $ jupyter notebook
    
Once the browser opens up, select and open ``Time-series_generation.ipynb``.


Method 2: Python interprreter
-----------------------------

Run the script in the following order:

.. code-block:: bash

    $ python Step1Mobility.py
    $ python Step2DrivingConsumption.py
    $ python Step3GridAvailability.py
    $ python Step4GridDemand.py


After finishing all the runs, open `Visualize_and_Export.ipynb` for visualization of results.


.. warning:: jupyter notebook must be installed, it can be installed ``conda install jupyter``.

