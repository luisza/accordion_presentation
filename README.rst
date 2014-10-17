accordion presentation
======================

It is a simple horizontal accordion for django cms 


Installation
-----------------------
Install from pypi 

	$ pip install accordion_presentation

or clone from with git 

	$ git clone https://github.com/luisza/accordion_presentation.git
	$ cd accordion_presentation
	$ python setup.py install

And put in your apps

    INSTALLED_APPS = (
        ...
        'accordion_presentation',
    )

Run syncdb

    $ python manage.py syncdb
    $ python manager.py migrate --fake

