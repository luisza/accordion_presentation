accordion presentation
======================

It is a simple horizontal accordion for django cms 


Installation
-----------------------

Not pypi version yet, clone de repository 

    $ git clone https://github.com/luisza/accordion_presentation.git

Please read https://github.com/mlavin/django-responsive

And put in your apps

    INSTALLED_APPS = (
        ...
        'accordion_presentation',
    )

Put in middleware 

    MIDDLEWARE_CLASSES = (
        ...
        'responsive.middleware.DeviceInfoMiddleware',
    )

Put in template context processors:

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...,
         'responsive.context_processors.device_info',
    )

Run syncdb

    $ python manage.py syncdb
    $ python manager.py migrate --fake

