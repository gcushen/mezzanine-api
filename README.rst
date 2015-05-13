.. image:: https://pypip.in/version/mezzanine-api/badge.svg
 :target: `PyPi`_
.. image:: https://pypip.in/license/mezzanine-api/badge.svg
 :target: `PyPi`_

Created by `George Cushen <https://github.com/gcushen>`_

========
Overview
========
Mezzanine API is a RESTful web API built using the `Django`_ framework which extends the `Mezzanine`_ content
management platform. The API empowers developers to automate, extend and combine Mezzanine with other services such as
Ember.js or a mobile app.

Features
========
* REST API resources for posts, pages, users, and categories
* OAuth 2.0 allows users to authorize and revoke access to third party applications without the need for those
  applications to request the user's credentials
* Endpoints documented with `Swagger UI`_
* Leverages `Django Rest Framework`_
* Web browsable API
* Highly efficient
* Easy to use

Roadmap
========
* More endpoints
* Refinement
* Writeable API access
* Test Suite

Installation
============
1. Install from PyPI::

    $ pip install mezzanine-api

2. Add the following apps to INSTALLED_APPS in your Mezzanine settings.py::

    INSTALLED_APPS = (
        ...
        'mezzanine_api',
        'rest_framework',
        'rest_framework_swagger',
        'oauth2_provider',
    )

3. Also, add the following lines at the end of your settings.py module::

    #####################
    # REST API SETTINGS #
    #####################
    try:
        from mezzanine_api.settings import *
    except ImportError as e:
        pass

4. Add the following code in your Mezzanine urls.py somewhere after the ``urlpatterns = []`` line::

    # REST API URLs
    urlpatterns += patterns("",
        ("^api/", include("mezzanine_api.urls")),
    )

5. Migrate the database to support Oauth2::

    $ python manage.py migrate

6. Start the server::

    $ python manage.py runserver

7. Visit http://127.0.0.1:8000/api/docs/ to view the endpoint documentation and query the API.


Contributing
============

Mezzanine API is an open source project managed using the Git version control system. The repository is hosted
on `GitHub`_ , so contributing is as easy as forking the project and committing back your enhancements.

Support
=======

If you have questions about the API, consider discussing it on the `mezzanine-users`_ mailing list.

Otherwise, if you have found a bug, please use the `GitHub issue tracker`_ and include the steps necessary to reproduce
it.

.. _`Mezzanine`: http://mezzanine.jupo.org/
.. _`Django`: http://djangoproject.com/
.. _`Django Rest Framework`: http://www.django-rest-framework.org/
.. _`pip`: http://www.pip-installer.org/
.. _`PyPi`: https://pypi.python.org/pypi/mezzanine-api
.. _`GitHub`: https://github.com/gcushen/mezzanine-api
.. _`GitHub issue tracker`: https://github.com/gcushen/mezzanine-api/issues
.. _`mezzanine-users`: http://groups.google.com/group/mezzanine-users/topics
.. _`Swagger UI`: http://swagger.io/
