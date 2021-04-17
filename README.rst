SocialMediaProfiler
===================
.. image:: https://travis-ci.com/pandrey2003/social-media-profiler.svg?branch=master
   :target: https://travis-ci.com/pandrey2003/social-media-profiler

.. image:: https://www.codefactor.io/repository/github/pandrey2003/social-media-profiler/badge?s=d4a6bd1bc17bc72d9ebc1e5d24876078a5319752
   :target: https://www.codefactor.io/repository/github/pandrey2003/social-media-profiler
   :alt: CodeFactor

.. image:: https://readthedocs.org/projects/social-media-profiler/badge/?version=latest
   :target: https://social-media-profiler.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

A GUI app to find social media information about any person on the world and put it into a neat PDF report.


My dear visitor...
------------------
As you are reading this text, I can safely assume you're willing to find social media information about some person.

I have several questions for you. What if you could...

- spend only 20-40 secs to retrieve your information from Twitter, Instagram, LinkedIn and Google Search;
- get the information **you** need as you know there're pretty advanced sorting algorithms;
- get the information in a neat PDF file with according links and pictures

Sounds like a miracle, but that's exactly why we are here for you: to get, analyze and visualize the information you need.

How does it look in practice?
--------------------------------------

.. image:: https://user-images.githubusercontent.com/64363269/101992093-6c635e80-3cb9-11eb-9658-74677e10b019.png

.. image:: https://user-images.githubusercontent.com/64363269/101992113-869d3c80-3cb9-11eb-8137-dd88cabef31d.png

.. image:: https://user-images.githubusercontent.com/64363269/101992119-9452c200-3cb9-11eb-840c-259f8527aed8.png

.. image:: https://user-images.githubusercontent.com/64363269/102230902-14656b80-3ef6-11eb-86b4-5e4426075750.png

We all like to see in action, so check out the file `here <https://github.com/pandrey2003/social-media-profiler/files/6329254/KevinGoldsmith_2021-04-17T15_50_58.pdf>`_, if you want.


Installation
------------
Clone this repository on your PC using git.

.. code-block:: bash

   git clone https://github.com/pandrey2003/dossier-builder.git

Usage
-----
All this beauty takes several steps...
1. Create the ``.env`` file into the ``app/backend/scraping`` directory with the following credentials:

.. code-block:: python

   GOOGLE_DEVELOPER_KEY=
   GOOGLE_CSE_ID=
   IPSTACK_API_KEY=
   LINKEDIN_LOGIN=
   LINKEDIN_PASSWORD=
   INSTAGRAM_LOGIN=
   INSTAGRAM_PASSWORD=
   TWITTER_API_KEY=
   TWITTER_API_SECRET=
   TWITTER_ACCESS_TOKEN=
   TWITTER_ACCESS_SECRET=

Explanation on the provided credentials can be read on the bottom of the README. Take into account the setup happens only once.

*Note:* the caching algorithm has been enabled for Instagram interaction, which allows you to renew your cache settings only once per 2 months. LinkedIn throttling limit is 900 API calls/hour.

2. Install all the dependencies from ``Pipfile`` and ``Pipfile.lock`` using `pipenv <https://github.com/pypa/pipenv>`_:

.. code-block:: bash

   pipenv install

3. Activate the ``pipenv`` environment:

.. code-block:: bash

   pipenv shell

4. Run the ``run.py`` file (opens GUI).

5. Enter as many fields about the desired person as possible (below you can see more explanations if needed).

6. Choose the PDF output directory by clicking the according button.

7. Click the submit button and observe the progress bar (normally takes 20-40 seconds to scrape, filter and visualize
the data about the desired person).

How does it look interactively?
-------------------------------

Take a look at an example of finding information about Bill Gates:

.. image:: https://user-images.githubusercontent.com/64363269/111445458-1a94ff00-8714-11eb-8282-74268ccb55f4.gif

How does GUI look like?
-----------------------
The initial GUI window looks like this:

.. image:: https://user-images.githubusercontent.com/64363269/101991905-6620b280-3cb8-11eb-953a-f29e98bd2b38.png

However, you may get confused about what you should write in each field, see the explanation on the bottom of the README.

Explanations on environment variables
---------------------------------------

- ``GOOGLE_DEVELOPER_KEY`` is your API key from `the Google Developers platform <https://developers.google.com/>`_.
- ``GOOGLE_CSE_ID`` is your `Google Custom Search Engine <https://cse.google.com/>`_ ID (you have to set it up to search the info all around the web).
- ``IPSTACK_API_KEY`` is your API key from `ipstack <https://ipstack.com/>`_. If you do not have it, this is a 2-minute procedure.
- ``LINKEDIN_LOGIN`` and ``LINKEDIN_PASSWORD`` are the login and the password to your LinkedIn profile (no API-related credentials needed).
- ``INSTAGRAM_LOGIN`` and ``INSTAGRAM_PASSWORD`` are the login and the password to your Instagram profile (no API-related credentials needed).
- For the following Twitter credentials, you have to create an app at `Twitter Developers Portal <https://developer.twitter.com/en>`_. After this, you get ``TWITTER_API_KEY`` and ``TWITTER_API_SECRET`` from your app page. Your access token and access token secret can be received using the ``tweepy`` library. In case you do not know how to get it, watch this `tutorial <https://www.youtube.com/watch?v=dvAurfBB6Jk>`_ up to 12:45 minutes. The access token and the access token secret are *permanent*, so this set up happens only once.

Advanced explanation on GUI input
---------------------------------

.. image:: https://user-images.githubusercontent.com/64363269/102231548-c2711580-3ef6-11eb-8e22-42fffd9402d0.png

- The field 1 - an ordinary input field, look at the label on the left to know which information you should enter. Fields "First name", "Last name" and "Location" are very recommended to be filled.
- The field 2 - the additional information selector (used for searching on Google Search), the field 3 - the additional information input. To put it simple for 2 and 3, let's say you want to find the profile *pandrey2003* on *GitHub*. In this case, you write selector, "GitHub", into the field 2 and the profile name, "pandrey2003", into the field 3. *Note*: fields 2 and 3 are totally optional.
- The button 4 is used to choose the PDF output directory on your PC. Mandatory: visualization is an essential logical part of the app.
- The button 5 sends all your input data and the output directory to the logical part of the project. Press on it when you are sure you have entered all the necessary information.
- The progress bar 6 reflects the progress of the logical part of the project (no your interaction, just to see the progress). 2% means scraping has already started, 60% means scraping has been done and your data is being analyzed, 75% indicates analysis has been done and the data is being visualized, 100% - you can see the PDF file in the requested directory.
