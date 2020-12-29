.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/pandrey2003/social-media-profiler/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug"
and "help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

``social-media-profiler`` could always use more documentation, whether as part of the
official ``social-media-profiler`` docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/pandrey2003/social-media-profiler/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Write more Google Search selectors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Google Search scraping part thoroughly depends on the selectors located in the ``app/backend/scraping/google_search/google_params.json`` file. In case you want to scrape information from more websites, you should add a dictionary into the file.

The key of the dictionary is the REGEX syntax, the website URL should meet.
Dictionary values should contain the following keys and values:

- the value of the key "service_name" will be displayed on your PDF.
- other keys and according values work on this principle: the key is just some text that will be visualized and the value is the XPATH selector to find on the needed webpage.

Let's see an exemplary object from the JSON file:

.. code-block:: json

   "https:\/\/github.com\/[a-zA-Z0-9`~!@#$^*()_+-.,|<>№]+": {
    "service_name": "GitHub Profile",
    "Full name: ": "//span[@class=\"p-name vcard-fullname d-block overflow-hidden\"]",
    "Nickname: ": "//span[@class=\"p-nickname vcard-username d-block\"]",
    "Popular repos: ": "//*[@id=\"js-pjax-container\"]/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li/div/div/div/a/span",
    "URLs of popular repos: ": {
      "https://github.com": "//*[@id=\"js-pjax-container\"]/div[2]/div/div[2]/div[2]/div/div[1]/div/ol/li/div/div/div/a/@href"
    },
    "img_url": "//*[@id=\"js-pjax-container\"]/div[2]/div/div[1]/div/div[2]/div[1]/a/img/@src",
    "Number of followers: ": "//*[@id=\"js-pjax-container\"]/div[2]/div/div[1]/div/div[5]/div[2]/div/div/a[1]/span",
    "Number of following: ": "//*[@id=\"js-pjax-container\"]/div[2]/div/div[1]/div/div[5]/div[2]/div/div/a[2]/span",
    "Location: ": "//*[@id=\"js-pjax-container\"]/div[2]/div/div[1]/div/div[5]/div[2]/ul/li[1]/span"
  }

The key of the object is ``https:\/\/github.com\/[a-zA-Z0-9`~!@#$^*()_+-.,|<>№]+``. The desired URL **must** meet this
REGEX syntax (in this case, any page on GitHub). After this, we create an other dictionary (as the value). There
we **must** include the ``service_name`` key, which value will be displayed as a subtitle on a PDF (in this case, it is
*"GitHub Profile"*). All other keys from that dictionary are XPATH selectors for the webpage. Keys are for a PDF, while
values are XPATH selectors per se.

Get Started!
------------

Ready to contribute? Here's how to set up ``social-media-profiler`` for local development.

1. Fork the ``social-media-profiler`` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name/social-media-profiler.git

3. Install your local copy into a ``pipenv``. Assuming you have it installed, this is how you set up your fork for local development::

    $ cd social-media-profiler
    $ pipenv install
    $ pipenv shell

4. Create a branch for local development::

    $ git checkout -b name-of-your-branch

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests::

    $ flake8 app/
    $ python -m unittest

   To get flake8, just pip install it into your pipenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Detailed description of your changes."
    $ git push origin name-of-your-branch

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. **The pull request should work for Python 3.7+**.

Tips
----

To run a subset of tests::

    $ python -m unittest

Bear in mind that you should set up your ``.env`` file for tests (see README).
