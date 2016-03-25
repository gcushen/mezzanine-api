# Release Notes

## Upgrading

To upgrade Mezzanine API to the latest version, use pip:

    pip install -U mezzanine-api

You can determine your currently installed version using `pip freeze`:

    $ pip freeze | grep mezzanine-api

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
