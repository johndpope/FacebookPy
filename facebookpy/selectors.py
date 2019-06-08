"""
Global variables

By design, import no any other local module inside this file.
Vice verse, it'd produce circular dependent imports.
"""

# from sys import platform
# from os import environ as environmental_variables
# from os.path import join as join_path
# from os.path import exists as path_exists

class Selectors:
    """
    Store XPath, CSS, and other element selectors to be used at many places
    """

    likes_dialog_body_xpath = \
        ('//*[@id="facebook"]/body/div[10]/div[2][@role="dialog"]')

    # likes_dialog_close_xpath = '//a[@title="Close"]'

    # default_profile_pic_facebook = [
    #     "https://facebook.flas1-2.fna.fbcdn.net/vp"
    #     "/a8539c22ed9fec8e1c43b538b1ebfd1d/5C5A1A7A/t51.2885-19"
    #     "/11906329_960233084022564_1448528159_a.jpg",
    #     "https://scontent-yyz1-1.cdnfacebook.com/vp"
    #     "/a8539c22ed9fec8e1c43b538b1ebfd1d/5C5A1A7A/t51.2885-19"
    #     "/11906329_960233084022564_1448528159_a.jpg",
    #     "https://facebook.faep12-1.fna.fbcdn.net/vp"
    #     "/a8539c22ed9fec8e1c43b538b1ebfd1d/5C5A1A7A/t51.2885-19"
    #     "/11906329_960233084022564_1448528159_a.jpg",
    #     "https://facebook.fbts2-1.fna.fbcdn.net/vp"
    #     "/a8539c22ed9fec8e1c43b538b1ebfd1d/5C5A1A7A/t51.2885-19"
    #     "/11906329_960233084022564_1448528159_a.jpg",
    #     "https://scontent-mia3-1.cdnfacebook.com/vp"
    #     "/a8539c22ed9fec8e1c43b538b1ebfd1d/5C5A1A7A/t51.2885-19"
    #     "/11906329_960233084022564_1448528159_a.jpg"]