
Created by `George Cushen <https://github.com/gcushen>`_

========
Overview
========
Mezzanine API is a RESTful web API built using the `Django`_
framework which extends the `Mezzanine`_ content management platform. 
It gives you freedom to interact with the Mezzanine backend via innovative 
frontends such as an Angular Javascript based one or mobile app.

Features
========
* Endpoints for posts, pages, users, and categories
* Web browserable API
* Well documented endpoints
* Leverages Django Rest Framework
* Highly efficient
* Easy to use
* Clean code

Roadmap
========
* More endpoints
* Refinement
* Token based authentication
* Writeable API access
* Test Suite

Installation
============
1. In your terminal, run `pip`_::

    $ pip install mezzanine-api

2. Add the following three apps to INSTALLED_APPS in your Mezzanine settings.py::

    INSTALLED_APPS = (
        ...
        'mezzanine_api',
        'rest_framework',
        'rest_framework_swagger',
    )

3. Also, put the following code in your Mezzanine settings.py::

    #####################
    # REST API SETTINGS #
    #####################
    try:
        from mezzanine_api.settings import *
    except ImportError as e:
        pass

4. Put the following code in your Mezzanine urls.py::

    # REST API URLs
    urlpatterns += patterns("",
        ("^api/", include("mezzanine_api.urls")),
    )

5. Start the server::

    $ python manage.py runserver

6. Visit http://127.0.0.1:8000/api/ to view the documentation and query the API.


Contributing
============

Mezzanine API is an open source project managed using the Git version control system. The repository is hosted on
 `GitHub`_ , so contributing is as easy as forking the project and committing back your enhancements.

Support
=======

For support, feel free to ask on the `mezzanine-users`_ mailing list. 

Otherwise, if you have found a bug, please use the `GitHub issue tracker`_ and include the steps necessary to reproduce it. 

.. _`Mezzanine`: http://mezzanine.jupo.org/
.. _`Django`: http://djangoproject.com/
.. _`pip`: http://www.pip-installer.org/
.. _`GitHub`: https://github.com/gcushen/mezzanine-api
.. _`GitHub issue tracker`: https://github.com/gcushen/mezzanine-api/issues
.. _`mezzanine-users`: http://groups.google.com/group/mezzanine-users/topics
