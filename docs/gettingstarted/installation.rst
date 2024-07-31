.. _installation:

************************
Installation
************************

To run emobpy, you should have a functioning installation of Python.
It is a good idea to install emobpy within a conda environment. The result can best be visualized in a jupyter notebook. However, it is also possible to run emobpy through other python interpreter.

The following instructions describes in detail how to install Python, how to create a ``conda`` environment, and finally how to install emobpy and its dependencies.

This tool has been tested in window 7, Ubuntu 18.04, Ubuntu 19.04 and Suse Linux. Python version 3.6+.


Installation of Python with Conda
==================================

The easiest and most convenient way to install Python is to install Anaconda (or Miniconda). Download the latest version from their website_ and install it.

During the installation of Anaconda on **Windows**, you will be asked to specify several options. We recommend you to choose the following ones so that emobpy will run smoothly:

* Install Anaconda to a custom directory (such as ``C:/Anaconda`` or ``D:/Anaconda``) and do not install it in the default folder, because this might increase the log-in and log-out out time;
* Do not use ``C:/Programs/`` or ``C:/Program Files/`` because this will require admin rights (recommended for permission restricted computers);
* During the installation, select "advanced option" and check both boxes (despite not recommended by the application). This will add this Conda Python Installation to the path and enables it as default python.

.. _website: https://www.anaconda.com/products/individual

Create a new Conda environment
--------------------------------

An conda environment is an isolated Python space. Different environments can contain different Python packages of different versions. In order to have reproducible and stable "working space", it is useful to create a new environment for emobpy.

Anaconda offers different ways to create a new environment:

**1. Anaconda Navigator**

Start the Anaconda Navigator and go on *Environments* and then *create*. Choose a name, tick the box next to *Python* and choose a Python version compatible with your GAMS installation (see box above).

**2. Console**

Open a console (Anaconda Prompt, CMD, PowerShell, Windows Terminal) and create a new conda environment with the name *yourenvname* and the exemplary Python version *X.X* (we recommend 3.6) with the following command:

.. code-block:: bash

    $ conda create -n yourenvname python=X.X


.. note:: To verify the successful creation of your environment, type ``conda info --envs`` in your console.

For further information on how to edit and delete conda environments, we refer to the `conda documentation`_.

.. _GAMS Documentation: https://www.gams.com/latest/docs/
.. _conda documentation: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html


Installation of emobpy
=========================

Now, your are ready to install emobpy. Make sure you have activated the correct environment:

.. code-block:: bash

    $ conda activate yourenvname

You can install emobpy easily from PyPI_:

.. code-block:: bash

    $ pip install emobpy

Installing emobpy from PyPI ensures that all necessary linked packages are downloaded and installed.

.. note:: You can uninstall emobpy, while having activated the *yourenvname* environment, simply by executing ``$ pip uninstall emobpy`` in the console.

.. _PyPI: https://pypi.org/project/emobpy/

