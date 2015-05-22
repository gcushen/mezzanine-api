# Release Notes

---

## Upgrading

To upgrade Mezzanine API to the latest version, use pip:

    pip install -U mezzanine-api

You can determine your currently installed version using `pip freeze`:

    $ pip freeze | grep mezzanine-api

## Version 0.3.0 (2015-05-17)

* Add superuser write access (POST and PUT) for categories
* Add site endpoint
* Add themes
* Update filters
* Update permission handling and security
* Update settings
* Expose more model fields to API
