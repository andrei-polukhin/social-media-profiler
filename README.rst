
SocialMediaProfiler
===================
.. image:: https://www.codefactor.io/repository/github/pandrey2003/social-media-profiler/badge?s=d4a6bd1bc17bc72d9ebc1e5d24876078a5319752
   :target: https://www.codefactor.io/repository/github/pandrey2003/social-media-profiler
   :alt: CodeFactor

.. image:: https://readthedocs.org/projects/social-media-profiler/badge/?version=latest
   :target: https://social-media-profiler.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

A GUI app to find social media information about any person on the world and put it into a neat PDF report.

Installation
------------
Clone this repository on your PC using git.

.. code-block:: bash

   git clone https://github.com/pandrey2003/dossier-builder.git

Usage
-----
1. Create the .env file into the ``app/scraping`` directory with the following credentials:

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

Where ``GOOGLE_DEVELOPER_KEY`` is the API key from the Google Developers platform, ``GOOGLE_CSE_ID`` is your Google Custom Search Engine ID (you have to set it up to search the info all around the web), ``IPSTACK_API_KEY`` is your API key from `ipstack <https://ipstack.com/>`_. LinkedIn and Instagram API access is authorized using your profile credentials. In addition, you have to create an app on the Twitter developers portal and get the API key, the API secret, the access token and the access token secret from there.

2. Install all the dependencies using ``pipenv``.

3. Run the ``run.py`` file from the pipenv environment (opens GUI).

4. Enter as much fields about the desired person as possible, choose the PDF output directory.

5. Click the submit button and observe the progress bar (normally takes 20-40 seconds to scrape, filter and visualize the data).

How does GUI look like?
-----------------------
The initial window looks like this:

.. image:: https://user-images.githubusercontent.com/64363269/101991905-6620b280-3cb8-11eb-953a-f29e98bd2b38.png

However, you may get confused about what you should write in each field, see below the explanations:

.. image:: https://user-images.githubusercontent.com/64363269/102231548-c2711580-3ef6-11eb-8e22-42fffd9402d0.png

Explanations on the red numbers:

- 1 - an ordinary input field, look at the label on the left to know which information you should enter. Fields "First name", "Last name" and "Location" are very recommended to be filled.
- 2 - the additional information selector (used for searching on Google Search), 3 - the additional information input. To put it simple for 2 and 3, let's say you want to find the profile *pandrey2003* on *GitHub*. In this case you write selector, "GitHub", into the field 2 and the profile name, "pandrey2003" to the field 3. *Note*: fields 2 and 3 are totally optional.
- Button 4 is used to choose the PDF output directory on your PC. Mandatory as visualization is the essential logical part of the app.
- Button 5 sends all your input data to the logical part of the project: scraping, analyzing and visualization. Press on it when you are sure you have entered all the information in the input fields and chose the PDF output directory.
- Progress bar 6 - reflects the progress of the logical part of the project (no your participations, just for you to see the progress). 2% means scraping has already started, 60% means scraping is done and your data is being analyzed, 75% indicates analysis is done and the data is being visualized, 100% - you can see the PDF file in the requested directory.


How does a final PDF report look like?
--------------------------------------

.. image:: https://user-images.githubusercontent.com/64363269/101992093-6c635e80-3cb9-11eb-9658-74677e10b019.png

.. image:: https://user-images.githubusercontent.com/64363269/101992113-869d3c80-3cb9-11eb-8137-dd88cabef31d.png

.. image:: https://user-images.githubusercontent.com/64363269/101992119-9452c200-3cb9-11eb-840c-259f8527aed8.png

.. image:: https://user-images.githubusercontent.com/64363269/102230902-14656b80-3ef6-11eb-86b4-5e4426075750.png

Note that, for your convenience, found profiles on Twitter, Instagram, LinkedIn and additional information from Google
Search go with links, so you can go to the found profiles straight from your PDF.
