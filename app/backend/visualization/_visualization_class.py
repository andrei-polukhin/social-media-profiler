# -*- coding: utf-8 -*-
"""The visualization multiple-inheritance class."""

from app.backend.visualization._facebook import FacebookVisualize
from app.backend.visualization._google_search import GoogleSearchVisualize
from app.backend.visualization._instagram import InstagramVisualize
from app.backend.visualization._linkedin import LinkedinVisualize
from app.backend.visualization._twitter import TwitterVisualize


class Visualization(
        FacebookVisualize, GoogleSearchVisualize, InstagramVisualize,
        LinkedinVisualize, TwitterVisualize
):
    """Gather all visualization classes together to call visualization methods from one place."""
