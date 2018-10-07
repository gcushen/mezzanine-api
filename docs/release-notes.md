# Release Notes

## Upgrading

To upgrade Mezzanine API to the latest version, use pip:

    pip install -U mezzanine-api

You can determine your currently installed version using `pip freeze`:

    $ pip freeze | grep mezzanine-api

## Version 0.7.0 (2018-10-08)

This release brings a number of new features as well as adding compatibility for newer versions of dependencies and dropping support for older dependencies.

### What's New

* Add support for custom user models
* List child pages at page endpoint
* Support filtering pages by title
* Support filtering posts by multiple categories

### Fixes

* Add middleware compatibility for Django v1.11+
* Add compatibility for django-oauth-toolkit version 1.1.2+
* Add compatibility for django-filter v2+
* Update test environment to reflect updated dependencies
* Fix deprecation warnings from Mezzanine and Django

## Other

* Change license from BSD to MIT
* Drop support for older versions of dependencies
* Drop support for Python 2 (no longer tested on Python 2, but may still run)

## Version 0.6.1 (2017-10-30)

* Fix published blog posts queryset not updating
* Fix errors caused by latest versions of dependencies
* Update Setup, Tox, and Travis to support latest dependencies
* Add description field to post endpoint

## Version 0.6.0 (2017-01-30)

* Add `gallery_items` resource for pages
* Add support for latest Django Filters (v1)
* Add support for latest Swagger (v2)
* Update Tox and Travis for latest dependencies

## Version 0.5.0 (2016-04-15)

* Add API middleware (support CORS)
* Switch from Page Number to Limit Offset Pagination
* Add project_template for easy API project creation
* Add Material theme
* Add Order By filter
* Fix blog post Field filter
* Update default settings
* Advise importing `mezzanine_api.settings` prior to `local_settings.py` in Mezzanine's `settings.py`, as per revised installation docs

## Version 0.4.2 (2016-03-14)

* Fix Issue #3: `KeyError: 'context'`

## Version 0.4.1 (2016-03-07)

* Add logic for updating blog post categories
* No longer require title and content fields when updating a blog post
* Remove dependency on reverse URLs of Mezzanine views when deploying Mezzanine only as an API backend
* Add tests for creating and updating blog post categories
* Tidy up API template

## Version 0.4.0 (2016-03-02)

* Add superuser write access (POST and PUT) for blog posts
* Add support for Mezzanine 4.1.0, Django 1.9, and latest versions of other dependencies
* Switch test suite from factory to client based tests
* Add tests for blog posts
* Update docs

## Version 0.3.0 (2015-05-17)

* Add superuser write access (POST and PUT) for categories
* Add site endpoint
* Add themes
* Update filters
* Update permission handling and security
* Update settings
* Expose more model fields to API
