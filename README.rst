Accordion presentation
======================

It is a simple horizontal (cycle2) accordion for django cms 3.0.6 and django 1.7.

Installation
-----------------------

Install from pypi 

.. code:: bash

	$ pip install accordion_presentation

or clone from with git 

.. code:: bash

	$ git clone https://github.com/luisza/accordion_presentation.git
	$ cd accordion_presentation
	$ python setup.py install

Setup
-------

And put in your apps

.. code:: python
	
    INSTALLED_APPS = (
        ...
        'accordion_presentation',
        'paintstore'
    )

Run migrate

.. code:: bash

    $ python manager.py migrate 

