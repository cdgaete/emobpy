Examples
===============

This section contains examples developed to help understand the features and functionalities of emobpy. To facilitate the implementation and execution of the examples, the tool enables us to create projects from templates that contain such examples. We expect to provide more examples further forward.

To obtain the template of an example we have to run the command line interface as follows:

.. code-block:: bash

   $ dieterpy create_project -n myproject -t eg1

In the above code snippet ``-n`` is an argument to provide the name of our project `myproject` and ``-t`` is the argument to provide the name of the template to obtain `eg1`. 

.. Hint:: If no template (-t) is provided ``dieterpy create_project -n myproject``, then the base case folder will be generated.

.. toctree::
   :hidden:
   :maxdepth: 1

   basecase
   eg1
