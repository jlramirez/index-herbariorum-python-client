index-herbariorum-python-client
=====================

A python client library for the `Index Herbariorum https://github.com/nybgvh/IH-API/wiki` API.

To contribute code to this project, please submit a pull request to the repo on github:

https://github.com/jlramirez/index-herbariorum-python-client

Installation
------------

.. code-block::

    pip install indexherbariorum

Usage
-----------

Get all available countries

.. code-block:: python

    import indexherbariorum
	
    ih = indexherbariorum.init()
    countries_result = ih.countries()
	
Search for an institution by code

.. code-block:: python

    import indexherbariorum
	
    ih = indexherbariorum.init()
    institution_result = ih.institution('ala')
	
Search institutions by matching a specified query

.. code-block:: python

    import indexherbariorum
	
    ih = indexherbariorum.init()
    institutions_result = ih.institutions(rq={'state': 'california', 'city': 'los angeles'})

Search staff by matching a specified query

.. code-block:: python

    import indexherbariorum
	
    ih = indexherbariorum.init()
    staff_result = ih.staff(rq={'state': 'new york', 'correspondent': 'yes'})
	
Get number of countries

.. code-block:: python

    import indexherbariorum
	
    ih = indexherbariorum.init()
    count = ih.count_countries()
	
Get number of institution records based on search

.. code-block:: python

    import indexherbariorum
	
    ih = indexherbariorum.init()
    count = ih.count_institutions(rq={'country': 'colombia', 'city': 'medellin'})

Get number of staff records based on search

.. code-block:: python

    import indexherbariorum
	
    ih = indexherbariorum.init()
    count = ih.count_staff(rq={'state': 'texas', 'correspondent': 'yes'})
	
Download CSV file

.. code-block:: python

    import indexherbariorum
	
    ih = indexherbariorum.init()
    ih.download('staff', rq={'state': 'new york', 'correspondent': 'yes'}, filename='ny_staff.csv')






