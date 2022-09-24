=============
Mezzanine API: Transform Mezzanine into a Headless CMS
=============

.. image:: https://img.shields.io/pypi/v/mezzanine-api.svg
   :target: `PyPi`_
.. image:: https://travis-ci.org/gcushen/mezzanine-api.svg?branch=master
   :target: https://travis-ci.org/gcushen/mezzanine-api
.. image:: https://img.shields.io/github/license/gcushen/mezzanine-api.svg
   :target: https://github.com/gcushen/mezzanine-api/blob/master/LICENSE

No longer maintained - use Wagtail CMS instead
================

**Mezzanine CMS and Mezzanine API are no longer maintained.**

**To deploy a new CMS with Python, it's recommended to use Wagtail CMS:** https://wagtail.org/

Mezzanine API
================

Mezzanine API is a **RESTful web API** for the popular `Mezzanine`_ content management platform.
It is built upon the `Django`_ framework, using **JSON** for serialization and **OAuth2** for secure authentication.
The API empowers developers to **automate, extend and combine Mezzanine with other services** such as mobile apps.

Why use the API?
================
* **Freedom**: build mobile, web, or server apps and use whatever programming language you want
* **Speed**: harness a significant speed advantage over Mezzanine's Python based page views

Features
========
* Intuitive REST API resources for posts, categories, comments, pages, users, and site/app metadata. Retrieving or updating data involves simply sending a HTTP request.
* Easily filter and search content
* Industry standard OAuth2 API authentication allows users to authorize and revoke access to third party applications
* Web browsable API
* Interactive API resource documentation

Installation, Documentation and Roadmap
=======================================
Check out the `docs` folder

Screenshot
==========
.. image:: http://gcushen.github.io/mezzanine-api/img/api_resources_scaled.png

Created by `George Cushen <https://twitter.com/GeorgeCushen>`_

.. _`Mezzanine`: http://mezzanine.jupo.org/
.. _`Django`: http://djangoproject.com/
.. _`Django Rest Framework`: http://www.django-rest-framework.org/
.. _`pip`: http://www.pip-installer.org/
.. _`PyPi`: https://pypi.python.org/pypi/mezzanine-api
.. _`GitHub`: https://github.com/gcushen/mezzanine-api
.. _`GitHub issue tracker`: https://github.com/gcushen/mezzanine-api/issues
.. _`mezzanine-users`: http://groups.google.com/group/mezzanine-users/topics
