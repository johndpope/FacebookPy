""" Quickstart script for FacebookPy usage """

# imports
from facebookpy import FacebookPy
from facebookpy import smart_run
from facebookpy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an FacebookPy session!
session = FacebookPy()

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    session.like_by_tags(["natgeo"], amount=10)
