# Client SDK

Mezzanine client is a **Python SDK** and **remote CLI** for [Mezzanine API](index.md). It enables a user or service to remotely read or write to Mezzanine CMS using Python or the command line.

## Installation

    pip install --upgrade mezzanine-client

[*Star* the Client on Github](https://github.com/gcushen/mezzanine-client-python/) to help support further development. You can also *watch* it on Github to keep track of updates.

## Getting Started

Prerequisites: install [Mezzanine API](index.md#installation) either locally or remotely, as we need an API to connect to.

1. Login to your Mezzanine CMS Admin Panel (e.g. [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/))
2. In the menu, click *OAuth* > *Applications*
3. Create a new application with the following details:

        App Name: Mezzanine Python Client
        App ID: id
        App Secret: secret
        Client Type: Confidential
        Grant Type: Code
        Redirect URI: https://httpbin.org/get

## Examples

The client's `Mezzanine` class in the `api` module contains a set of methods for accessing the API. Some of the most common methods are demonstrated in the following command line interface examples:

- `posts_list.py` List published blog posts
- `posts_retrieve.py <post_id>` Retrieve the specified blog post
- `posts_create.py` Create a new blog post

Start by downloading the examples included in <https://github.com/gcushen/mezzanine-client-python/archive/master.zip> , or directly with `wget`:

    $ mkdir mezzanine-client-examples && cd $_ && wget https://raw.githubusercontent.com/gcushen/mezzanine-client-python/master/examples/posts_list.py \
    https://raw.githubusercontent.com/gcushen/mezzanine-client-python/master/examples/posts_retrieve.py \
    https://raw.githubusercontent.com/gcushen/mezzanine-client-python/master/examples/posts_create.py

Allow examples to be executed without explicit `python` command:

    $ chmod u+x posts_*.py

Prior to running the examples, export your app key and secret to your terminal environment:

    $ export MN_ID='id'
    $ export MN_SECRET='secret'

Then run an example:

    $ ./posts_list.py

The first time the app attempts to access the API, it will ask you to click a link to authorize it. The web page will redirect you to a page with some data similar to below.

    "args": {
        "code": "vYQqcQSHmqkezX09xh8qflGVYUw6F8",
        "state": "Euf91j3H6uEE9VQ9mWsvFC5s3eEMJt"
    },

The code in this case is "vYQqcQSHmqkezX09xh8qflGVYUw6F8" *without* the speech marks and should be pasted back into the app within one hour to complete the authorization.

## Community

[Chat Room](https://gitter.im/gcushen/mezzanine-api?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) - if the room is quiet, feel free to leave a message and someone will try to get back to you.

[Report a bug or feature request](https://github.com/gcushen/mezzanine-client-python/issues) for the client.

## Roadmap

- Test suite
- Further documentation and examples
