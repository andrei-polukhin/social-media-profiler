SocialMediaProfiler
===================
.. image:: https://www.codefactor.io/repository/github/pandrey2003/social-media-profiler/badge?s=d4a6bd1bc17bc72d9ebc1e5d24876078a5319752
   :target: https://www.codefactor.io/repository/github/pandrey2003/social-media-profiler
   :alt: CodeFactor

A GUI app to find social media information about any person on the world and put it into a neat PDF report.

Installation
------------
Clone this repository on your PC using git.

.. code-block:: bash

   git clone https://github.com/pandrey2003/dossier-builder.git

Usage
-----
1. Create the .env file into the ``scraping`` directory with the following credentials:

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

2. Run the ``run.py`` file to get the visual interface.

3. Enter as much fields about the desired person as possible, choose the PDF output directory.

4. Click the submit button and observe the progress bar (normally takes 30-40 seconds to scrape, filter and visualize the data).
