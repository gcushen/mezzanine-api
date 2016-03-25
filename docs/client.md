# Client SDK

Mezzanine client is a **Python SDK** and **remote CLI** for [Mezzanine API](index.md). It enables a user or service to remotely read or write to Mezzanine CMS using Python or the command line.

## Installation

    pip install --upgrade mezzanine-client

## Getting Started

Prerequisites: install [Mezzanine](http://mezzanine.jupo.org) and [Mezzanine API](index.md#installation) either locally or remotely, as we need an API to connect to.

1. Login to your Mezzanine CMS Admin Panel
2. In the menu, click OAuth > Applications
3. Create a new application with the following details:

        App Name: Mezzanine Python Client
        App Key: key
        App Secret: secret
        Client Type: Confidential
        Grant Type: Code

## Examples

Download the examples from <https://github.com/gcushen/mezzanine-client-python> .

Prior to running the examples, export your app key and secret to your terminal environment:

    $ export MN_KEY='key'
    $ export MN_SECRET='secret'


Then run an example:

    $ ./posts_list_recent.py

The first time the app attempts to access the API, it will ask you to click a link to authorize it. The web page will redirect you to a page with some data similar to below.

    "args": {
        "code": "vYQqcQSHmqkezX09xh8qflGVYUw6F8",
        "state": "Euf91j3H6uEE9VQ9mWsvFC5s3eEMJt"
    },

The code in this case is "vYQqcQSHmqkezX09xh8qflGVYUw6F8" *without* the speech marks and should be pasted back into the app within 1 minute to complete the authorization.

## Community

[Chat Room](https://gitter.im/gcushen/mezzanine-api?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) - if the room is quiet, feel free to leave a message and someone will try to get back to you.

[Report a bug or feature request](https://github.com/gcushen/mezzanine-client-python/issues) for the client.

## Roadmap

- Test suite
- Further documentation and examples
