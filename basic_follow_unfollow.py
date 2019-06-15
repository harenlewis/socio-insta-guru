# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = "Haren Lewis, harenlewis@gmail.com"


"""
This template was written by @cormo1990. Modified to cater to our needs.
What does this quickstart script aim to do?
- Basic follow/unfollow activity.
NOTES:
- Follow users, then after following step, I start unfollowing
the user that didn't follow me back.
- At the end I clean my account unfollowing all the users followed with
InstaPy.

Useful Links:
The python library on which this script built on
https://github.com/timgrossmann/InstaPy

It's documentation
https://github.com/timgrossmann/InstaPy/blob/master/DOCUMENTATION.md


https://instavast.com/faq/instagram-bot/auto-follow-does-not-work/
"""

# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
# Replace with credentials of account to be used 
insta_username = 'liamitchel1892@gmail.com'
insta_password = 'liamitcheL@1892'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
# This will open a chrome browser and run it in automation
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_skip_users(skip_private=True, private_percentage=100)

    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=10,
                                    min_following=10)

    """
    First Step: Follow Users
    The below code will follow all the followers of the account 
    solotraverlstale and cool_kid_bantai
    If we have more accounts we just add to the list, comma separated
    """
    list_of_users_whose_followers_i_want_to_follow = ['solotraverlstale', 'cool_bantai_kid']

    session.follow_user_followers(
        list_of_users_whose_followers_i_want_to_follow,
        amount=800,
        randomize=True,
        interact=True,
        sleep_delay=60
    )

    """ Second Step: Unfollow users who dont follow back
    """
    session.unfollow_users(
        amount=500, 
        InstapyFollowed=(True, "nonfollowers"),
        style="FIFO",
        unfollow_after=12 * 60 * 60, 
        sleep_delay=60
    )

    """ Clean all followed user - Unfollow all users followed by InstaPy...
    """
    session.unfollow_users(
        amount=500, 
        InstapyFollowed=(True, "all"),
        style="FIFO", 
        unfollow_after=3 * 24 * 60 * 60,
        sleep_delay=60
    )

    """ Joining Engagement Pods...
    Add code for liking, commenting etc
    """

    session.join_pods()