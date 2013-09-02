% How To Create Amazing Open Source Modules
% Kumar McMillan
% September, 2013

# ![temple](images/temple.jpg) How To Create Amazing Open Source Modules
[github.com/ kumar303/ build-open-source](https://github.com/kumar303/build-open-source)
# Newbies or seasoned hackers

# Topics:

* scaffolding that works today
* essential tools
* docs
* stability
* community

# [Mozilla](https://github.com/mozilla/) <3 open source
# Mozilla: 45+ Django modules

* [django-aesfield](https://github.com/andymckay/django-aesfield)
* [django-browserid](https://github.com/mozilla/django-browserid/)
* [django-cache-machine](https://github.com/jbalogh/django-cache-machine)
* [django-memcached-pool](https://github.com/mozilla/django-memcached-pool)
* [django-nose](https://github.com/jbalogh/django-nose)
* [django-paranoia](https://github.com/andymckay/django-paranoia/)
* [django-statsd](https://github.com/jsocol/django-statsd)
* [django-waffle](https://github.com/jsocol/django-waffle/)

# Useless modules are OK
# Open by default
# ![Creepy mustache](images/mustache_cropped.jpg) I want to use your module

# When should you create a module?
#

    TODO: liberate
#

    from distutils.core import setup

    setup(name='yourmodule',
          version='1.0.0',
          ...)

#

    from setuptools import (setup,
                            find_packages)

    setup(name='yourmodule',
          packages=find_packages(exclude=['tests']),
          ...)

# Publish to [PyPI](https://pypi.python.org/pypi)

    python setup.py sdist \
                    register \
                    upload

# ![double rainbow](images/double-rainbow.jpg)

    pip install yourmodule

# ![double rainbow](images/double-rainbow.jpg)

34,347 packages

#

    yourmodule/__init__.py:

    __version__ = '1.0.0'

#

    import re, sys

    version = None
    for line in open("./yourmodule/__init__.py"):
        m = re.search("__version__\s*=\s*(.*)", line)
        if m:
            version = m.group(1).strip()[1:-1]
            break
    assert version

#

    setup(...,
          classifiers=[
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
          ])

# Support Python 2 and 3 with [six](https://pypi.python.org/pypi/six/)
# Use [check-manifest](https://pypi.python.org/pypi/check-manifest) to validate MANIFEST.in
# setup.cfg will solve all your problems (I think)
#

    setup(...,
          license='Apache 2')

# ![Good Guy](images/good-guy.png)[WTFPL](http://en.wikipedia.org/wiki/WTFPL) - Do What the Fuck You Want to Public License
# Write documentation (it's ok to be lazy)
# Add a README.rst file
# Say anything in the README, just say something
# Crucial docs:

1. what your module does
2. how to install it
3. how to use it
4. how to hack on it

# When you are AWESOME:

* switch to [Sphinx](http://sphinx-doc.org/)
  * README.rst converts nicely
* deploy to [readthedocs.org](https://readthedocs.org/) from git

# Usage docs:

* show code, examples
* use [doctest](http://docs.python.org/2/library/doctest.html) (but be careful)
* document settings

#

    .. doctest::
        :hide:

        >>> fudge.clear()

    .. doctest::

        >>> from fudge import Fake
        >>> do_login = Fake()

# Do not hide import paths. Thx.
#

    def login(user, passwd):
        """
        Logs in the user

        :param user: string
        :param passwd: string
        :rtype: boolean
        """

    .. autofunction:: yourmodule.login

# Tell a story about your module. Fallback to the API reference.
# Newbies vs. power users
# How to test...

* test environment
* running tests
* running partial tests

# Nice docs:

* where to get help
* changelog
  * backwards incompatible
  * migration guide
* roadmap?

# Use [tox](http://tox.readthedocs.org/en/latest/) to test your module
#

    [testenv]
    commands=
        python manage.py test

    [testenv:py27]
    basepython=python2.7

    [testenv:py32]
    basepython=python3.2

#

    [django14]
    deps=
        Django >= 1.4, < 1.5

    [django15]
    deps=
        Django >= 1.5, < 1.6

#

    [base]
    deps=
        M2Crypto >= 0.21.1

    [django14]
    deps=
        Django >= 1.4, < 1.5
        {[base]deps}

# Run tests continuously with [TravisCI](https://travis-ci.org/)
#

    language: python
    python:
      - "2.7"

    install:
      - pip install tox
    script: tox

# Accepting patches

* choose your criteria
  * require tests
  * require docs
  * review patches

# Open source governance

* meritocracy
* experts emerge
* contributors come and go

# Bikeshedding

* don't let it slow you down
* working code trumps all

# Maintenance?!

* chores, release management
* quit at will
* maintain modules you care about

# How did Ian Bicking do it?
# "I have no idea ..."
# Ian says...

* low quality project, more engagement
  * pip needed a lot of work
  * release early
* if the module is useful ... ?
* appreciate and empower others

# ![earth](images/earth.jpg) That's it

* make amazing modules
  * try to patch other modules first
* questions?
* [@kumar303](https://twitter.com/kumar303)
