# Remote Command Line Interface (CLI)

Mezzanine Client CLI is a **remote CLI** for [Mezzanine API](index.md). It enables a user or service to remotely read or write to [Mezzanine CMS](http://mezzanine.jupo.org/) using the command line. For example, you can write an article in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) on your laptop and type a simple command to automatically upload it and create a new blog post from it on your website.

## Installation

    $ pip install -U mezzanine-client

## Prerequisites

Refer to [Mezzanine Client Prerequisites](client.md#prerequisites).

## Configuration

Generally, you must set at least three configuration options: API URL, OAuth App ID, and OAuth App Secret. These settings correspond to the location of your Mezzanine API instance and your OAuth credentials to authenticate with it (as was discussed further in the above *Prerequisites* section).

```
$ mezzanine-cli config api_url http://127.0.0.1:8000/api
$ mezzanine-cli config client_id id
$ mezzanine-cli config client_secret secret
```

You can also see your current configuration and available options by issuing the `mezzanine-cli config` command without any arguments. Note that the `refresh_token` setting should not be altered.

## Authorize the app

Run a command that attempts to access the API:

    $ mezzanine-cli posts list

Then follow the guide to [authorize the app](client.md#authorize-the-app).

## Getting started

Some examples:

```
# List all posts (most recent first).
$ mezzanine-cli posts list

# Get the post with the ID of 2.
$ mezzanine-cli posts get 2

# Create a post from a Markdown file.
$ mezzanine-cli posts create \
  --title='Test Post from API Client' \
  --content-file=~/Desktop/test.md \
  --categories='Test,Fun' \
  --markdown
```

Just add `--help` to any command in order to get help on the command line:

```
# General help.
$ mezzanine-cli

# View available options for creating posts.
$ mezzanine-cli posts create --help
```

Finally, if you wish to clear the credentials and reset CLI configuration, you can do so by running:

    $ mezzanine-cli logout

## Community

Join us in the [Mezzanine API chat room](https://gitter.im/gcushen/mezzanine-api?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge) or leave a message and we will try to get back to you.

Feel free to [star](https://github.com/gcushen/mezzanine-client-python/) Mezzanine Client on Github to show your support and monitor updates.

Please file a [ticket](https://github.com/gcushen/mezzanine-client-python/issues) or contribute a pull request on GitHub for bugs or feature requests.

## Roadmap

- Add further CLI resources to interact with the API
