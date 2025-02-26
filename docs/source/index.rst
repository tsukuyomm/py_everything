.. _py_everything: http://github.com/pybash1/py_everything
.. _Python: http://www.python.org/

******************************************
Welcome to py_everything_'s Documentation!
******************************************

Welcome to the Documentation for py_everything_.
You can find all the modules and how to use them here.

py_everything_ hopes to become a Python_ package that helps you write **everything** much faster and in a easier way.
Without importing many libraries for different tasks. Do them with the help of one.

Power of py_everything_ - 
^^^^^^^^^^^^^^^^^^^^^^^^^

The basic usage for this package is given below::

   >>> import py_everything
   >>> from py_everything import search
   >>> search.searchFiles('python', 'C:\Programming\\')
   C:\Programming\python.txt
   C:\Programming\projectpython.py
   C:\Programming\py_everything-python.docx
   >>> my_list = [2, 4, 5, 3, 7, 5, 6, 3 , 12 , 9, 6]
   >>> py_everything.maths.avg(my_list)
   5.636363636363637


Contributors - 
^^^^^^^^^^^^^^

People who have contributed to this project - 

* `pybash(Creator and Maintainer) <https://github.com/pybash1>`_
* `Farid(Contributor) <https://github.com/mfaridn03>`_
* `Morgan-Phoenix(Contributor and Collaborator) <https://github.com/Morgan-Phoenix>`_


.. toctree::
   :caption: Basic:
   :maxdepth: 2
   
   index

.. toctree::
   :caption: Modules:
   :maxdepth: 2
   
   py_everything
   py_everything.automation
   py_everything.conversion
   py_everything.dateUtils
   py_everything.error
   py_everything.fileIO
   py_everything.htmlXml
   py_everything.maths
   py_everything.mensuration
   py_everything.search
   py_everything.sencrypt
   py_everything.units
   py_everything.web

.. toctree::
   :caption: setupPyGen:
   :maxdepth: 2

   setupPyGen
   setupPyGen Changelog

.. toctree::
   :caption: gitIt:
   :maxdepth: 2

   gitIt
   gitIt Changelog

.. toctree::
   :caption: About the Project:
   :maxdepth: 2
   
   Dependencies & Dependents
   License


.. 
   Indices
   =======
   * :ref:`genindex`
