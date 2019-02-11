""" Quickstart script for FacebookPy usage """

# imports
from facebookpy import FacebookPy
from facebookpy import smart_run
from facebookpy import set_workspace

import random

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an FacebookPy session!
session = FacebookPy()

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    # session.like_by_tags(["natgeo"], amount=10)

    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=7500,
                                    max_following=3000,
                                    min_followers=25,
                                    min_following=25,
                                    min_posts=1)

    session.set_user_interact(amount=3, randomize=True, percentage=80,
                              media='Photo')
    # session.set_do_like(enabled=True, percentage=90)
    session.set_do_follow(enabled=True, percentage=40, times=1)


    """ Select users form a list of a predefined targets...
    """

    targets = ['ananya.mallik', 'Sushant.on']
    number = random.randint(3, 5)
    random_targets = targets

    if len(targets) <= number:
        random_targets = targets
    else:
        random_targets = random.sample(targets, number)

    session.follow_by_list(followlist=random_targets, times=1, sleep_delay=600, interact=False)

    session.follow_user_followers(random_targets,
                                  amount=random.randint(30, 60),
                                  randomize=True, sleep_delay=600,
                                  interact=True)

    session.follow_likers(random_targets, photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=False)

