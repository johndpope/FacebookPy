# FacebookPy

[![MIT license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/socialbotspy/FacebookPy/blob/master/LICENSE)
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://travis-ci.org/socialbotspy/FacebookPy)

### Tooling that automates your social media interactions to “farm” Likes, Comments, and Followers on Facebook

Implemented in Python using the Selenium module.

**Have an issue?**
If you should encounter any issue, please first [search for similar issues](https://github.com/socialbotspy/FacebookPy/issues)

## **Installation**

It is recomended to use via pyenv
We will be supporting python 3.6.0 and above going forward

```
curl https://pyenv.run | bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
pyenv install 3.6.0
pyenv local 3.6.0
pip install --upgrade git+https://github.com/socialbotspy/SocialCommons.git
pip install -r requirements.txt
```

<br />

Now all you need is a **quickstart** script into your computer, go ahead and run it in the command prompt as:

```elm
python quickstart.py --username abc@gmail.com --userid abc.pqr --password 123
```

> **PRO**:
> Read about difference between username and userid for facebook: https://www.facebook.com/help/211813265517027?helpref=faq_content

> **PRO**:
> Read more about passing arguments from the command line interface in the section - [Pass arguments by CLI](#pass-arguments-by-cli).

<br />

##### 🚁 You can provide _username_ & _password_ inside the **quickstart** script, too!

```python
# inside quickstart script

session = FacebookPy(username="abc",
                  password="123")
```

<br />

🛸 Also, if you like to run _FacebookPy_ in **background**, just enable the **headless** mode!

```erlang
python quickstart.py -u abc -p 123 --headless-browser
```

Or do it right inside the **quickstart** script.

```python
# inside quickstart script

session = FacebookPy(username="abc",
                  password="123",
                  headless_browser=True)  
```

_Until you enable the **headless** mode, FacebookPy will run in the **graphical** mode where you can watch the ongoing automation in your web browser_.

> If you've used _FacebookPy_ before installing it by **pip**, you have to move your _old_ data to the new **workspace** folder for once.
[Read how to do this here](#migrating-your-data-to-the-workspace-folder).

<br />

---

### Social

#### [Twitter of FacebookPy](https://twitter.com/FacebookPy) | [Twitter of Ishan](https://twitter.com/ishandutta2007) | [Talk about doing Open-Source work](https://www.youtube.com/watch?v=A_UtST302Og&t=0s&list=PLa4P1NPX9hthXV-wko0xyxFpbhYZFkW7o) | [Listen to the "Talk Python to me"-Episode](https://talkpython.fm/episodes/show/142/automating-the-web-with-selenium-and-facebookpy)

### Do you want to support us ?

<a href="https://opencollective.com/facebookpy/donate" target="_blank">
  <img align="left" hspace="10" src="https://opencollective.com/facebookpy/contribute/button@2x.png?color=blue" width=300 />
</a>

<a href="https://www.paypal.me/supportFacebookPy">
  <img hspace="14" alt="paypalme" src="http://codeinpython.com/tutorials/wp-content/uploads/2017/09/PayPal-ME-300x300.jpg.png" width=100 />
</a>

**Help build FacebookPy!**
Head over to https://github.com/socialbotspy/FacebookPy/wiki/How-to-Contribute to find out how you can help.

---

### Guides

#### Written Guides:

**[How to Ubuntu (64-Bit)](./docs/How_To_DO_Ubuntu_on_Digital_Ocean.md) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**

**[How to RaspberryPi](./docs/How_to_Raspberry.md) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**

**[How to Windows](./docs/How_to_Windows.md)**

# Documentation

### Table of Contents

#### NOTE: Checked are the ones that have been migrated and tested for Facedbook, while the rest are yet to be migrated or investigated the scope of.

* [FacebookPy Available Features](#facebookpy-available-features)
  * [Following](#following)  ✔
  * [Following by a list](#following-by-a-list)  ✔
  * [Follow someone else's followers](#follow-someone-elses-followers)  ✔
  * [Follow the likers of posts of users](#follow-the-likers-of-photos-of-users)   ✔
  * [Friending](#friending)  ✔
  * [Friending by a list](#friending-by-a-list)  ✔
  * [Restricting Likes](#restricting-likes)  ✔
  * [Ignoring Users](#ignoring-users)  ✔
  * [Ignoring Restrictions](#ignoring-restrictions)
  * [Excluding friends](#excluding-friends)  ✔
  * [Blacklist Campaign](#blacklist-campaign)  ✔
  * [Quota Supervisor](#quota-supervisor)  ✔

<br />

## FacebookPy Available Features

### Following

```python
# default enabled=False, follows ~ 10% of the users from the images, times=1
# (only follows a user once (if unfollowed again))

session.set_do_follow(enabled=True, percentage=10, times=2)
```

### Following by a list

##### This will follow each account from a list of facebook nicknames

```python
follow_by_list(followlist=['samantha3', 'larry_ok'], times=1, sleep_delay=600, interact=False)
```

_only follows a user once (if unfollowed again) would be useful for the precise targeting_  
`sleep_delay` is used to define break time after some good following (_averagely ~`10` follows_)  
For example, if one needs to get followbacks from followers of a chosen account/group of accounts.

```python
accs = ['therock','natgeo']
session.follow_by_list(accs, times=1, sleep_delay=600, interact=False)
```

* You can also **interact** with the followed users by enabling `interact=True` which will use the configuration of `set_user_interact` setting:  

```python
session.set_user_interact(amount=4,
                 percentage=50,
                  randomize=True,
                   media='Photo')
session.follow_by_list(followlist=['samantha3', 'larry_ok'], times=2, sleep_delay=600, interact=True)
```

### Follow someone else's followers

```python
# Follows the followers of each given user
# The usernames can be either a list or a string
# The amount is for each account, in this case 30 users will be followed
# If randomize is false it will pick in a top-down fashion

session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False)

# default sleep_delay=600 (10min) for every 10 user following, in this case
# sleep for 60 seconds

session.follow_user_followers(['friend1', 'friend2', 'friend3'], amount=10, randomize=False, sleep_delay=60)
```

> **Note**: [simulation](#simulation) takes place while running this feature.

### Follow the likers of posts(only non video/non-photo) of users

##### This will follow the people those liked photos of given list of users

```python
session.follow_likers(['user1' , 'user2'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=False)
```

_in this case 2 random photos from each given user will be analyzed and 3 people who liked them will be followed, so 6 follows in total_
The `usernames` can be any list
The `photos_grab_amount` is how many photos will I grat from users profile and analyze who liked it
The `follow_likers_per_photo` is how many people to follow per each photo
`randomize=False` will take photos from newes, true will take random from first 12
`sleep_delay` is used to define break time after some good following (_averagely ~`10` follows_)

* You can also **interact** with the followed users by enabling `interact=True` which will use the configuration of `set_user_interact` setting:  

```python
session.set_user_interact(amount=2,
                    percentage=70,
                    randomize=True,
                    media='Photo')
session.follow_likers(['user1' , 'user2'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=True)
```

### Friending

```python
session.friend('user1', daysold=365, max_pic = 100, sleep_delay=600, interact=False)
```

### Friending by a list

##### This will add as friend each account from a list of facebook userids

```python
friend_by_list(friendlist=['samantha3', 'larry_ok'], times=1, sleep_delay=600, interact=False)
```

### Restricting Likes

```python
session.set_dont_like(['#exactmatch', '[startswith', ']endswith', 'broadmatch'])
```

`.set_dont_like` searches the description and owner comments for hashtags and
won't like the image if one of those hashtags are in there

You have 4 options to exclude posts from your FacebookPy session:

* words starting with `#` will match only exact hashtags (e. g. `#cat` matches `#cat`, but not `#catpic`)
* words starting with `[` will match all hashtags starting with your word (e. g. `[cat` matches `#catpic`, `#caturday` and so on)
* words starting with `]` will match all hashtags ending with your word (e. g. `]cat` matches `#mycat`, `#instacat` and so on)
* words without these prefixes will match all hashtags that contain your word regardless if it is placed at the beginning, middle or end of the hashtag (e. g. `cat` will match `#cat`, `#mycat`, `#caturday`, `#rainingcatsanddogs` and so on)

### Ignoring Users

```python
# completely ignore liking images from certain users

session.set_ignore_users(['random_user', 'another_username'])
```

### Ignoring Restrictions

```python
# will ignore the don't like if the description contains
# one of the given words

session.set_ignore_if_contains(['glutenfree', 'french', 'tasty'])
```

### Excluding friends

```python
# will prevent commenting on and unfollowing your good friends (the images will
# still be liked)

session.set_dont_include(['friend1', 'friend2', 'friend3'])
```

### Follow/Unfollow/exclude not working?

If you notice that one or more of the above functionalities are not working as expected - e.g. you have specified:

```python
session.set_do_follow(enabled=True, percentage=10, times=2)
```

but none of the profiles are being followed - or any such functionality is misbehaving - then one thing you should check is the position/order of such methods in your script. Essentially, all the ```set_*``` methods have to be before ```like_by_tags``` or ```like_by_locations``` or ```unfollow```. This is also implicit in all the exmples and quickstart.py

### Bypass Suspicious Login Attempt

If you're having issues with the "we detected an unusual login attempt" message,
you can bypass it setting FacebookPy in this way:

```python
session = FacebookPy(username=facebook_username, password=facebook_password, bypass_suspicious_attempt=True)
```

```bypass_suspicious_attempt=True``` will send the verification code to your
email, and you will be prompted to enter the security code sent to your email.
It will login to your account, now you can set bypass_suspicious_attempt to False
```bypass_suspicious_attempt=False``` and FacebookPy will quickly login using cookies.

If you want to bypass suspicious login attempt with your phone number, set `bypass_with_mobile` to `True`

```python
FacebookPy(username=facebook_username, password=facebook_password, bypass_suspicious_attempt=True, bypass_with_mobile=True)
```

### Quota Supervisor

###### Take full control of the actions with the most sophisticated approaches

```python
  session.set_quota_supervisor(
                      Settings, enabled=True,
                      sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                      sleepyhead=True,
                      stochastic_flow=True,
                      notify_me=True,
                      peak_likes=(57, 585),
                      peak_comments=(21, 182),
                      peak_follows=(48, None),
                      peak_unfollows=(35, 402),
                      peak_server_calls=(None, 4700))
```

#### Parameters:

`enabled`: put `True` to **activate** or `False` to **deactivate** supervising any time

`peak_likes`: the **first value** indicates the **hourly** and the **second** indicates the **daily** peak value

* _e.g._ in `peak_likes=(66, 700)` - `66` is the **hourly**, and `700` is the **daily** peak value  
_such as_,
  * `peak_server_calls=(500, 4745)` will _supervise_ server calls with **hourly** peak of `500` and **daily** peak of `4745`
  * `peak_likes=(70, None)` will _supervise_ only hourly likes with the peak of `70`
  * `peak_unfollows=(None, 350)` will _supervise_ only daily unfollows with the peak of `350`
  * `peak_comments=(None, None)` will not _supervise_ comments at all

If you **don't want to** _supervise_ likes **at all**, simply **remove** `peak_likes` parameter **OR** use `peak_likes=(None, None)`.  
_Once_ likes **reach** peak, it will **jump** every other like, _yet_, **will do all available actions** (_e.g. follow or unfollow_).

* Only `server calls` **does not** jump, it exits the program **once reaches the peak**.

> Although, you can put server calls to sleep once reaches peak, read `sleep_after` parameter.

* _Every action_ will be **jumped** separately after reaching it's peak, _except_ comments. Cos commenting without a like isn't welcomed that's why as like peak is reached, it will jump comments, too.

**Notice**: `peak_likes=(50)` will not work, use `peak_likes=(50, None)` to supervise **hourly** peak and `peak_likes=(None, 50)` for **daily** peak.  
>_Same **form**_ **applies** to **all** actions. Just specify the peaks in desired intervals- **hourly** or **daily** you want to _supervise_.

`sleep_after`: is used to put **FacebookPy** to _sleep_ **after reaching peak** _rather than_ **jumping the action** (_or exiting- **for** server calls_)  
_Any action_ can be included `["likes", "comments", "follows", "unfollows", "server_calls"]`.  
_As if_ you want to put _sleep_ **only after** reaching **hourly** like peak, put `"likes_h"` **OR** put `"likes_d"` for _sleeping_ **only after** reaching **daily** like peak.  
_such as_,

* `sleep_after=['follows_h']` will _sleep_ after reaching **hourly** follow peak  
* `sleep_after=['likes_d', 'follows', 'server_calls_h']` will _sleep_ after reaching **daily** like peak, follow peaks (_**hourly** and **daily**_) and **hourly** server call peak.  

**Notice**: there can be _either_ `"likes"` (_for both **hourly** and **daily** sleep_) **OR** `"likes_h"` (_for **hourly** sleep only_) **OR** `"likes_d"` (_for **daily** sleep only_).  
>_Once_ gone to sleep, it will **wake up** as _new_ **hour**/**day** (_according to the interval_) arrives AND **continue** the activity.

`sleepyhead`: can help to _sound_ **more humanly** which will **wake up a little bit later** in a randomly chosen time interval around accurate wake up time.
>_e.g._, if remaining time is `17` minutes, it will sleep `20` minutes instead (_random values each time_)..

`stochastic_flow`: can provide _smooth_ peak value generation by your original values.

* Every ~**hour**/**day** it will generate peaks **at close range** _around_ your **original peaks** (_but below them_).

> _e.g._, your peak likes **hourly** is `45`, next hour that peak will be `39`, the next `43`, etc.

`notify_me`: sends **toast notifications** (_directly to your OS_) _about_ the **important states of** _supervisor_- **sleep**, **wake up** and **exit** messages.

#### Mini-Examples:

* Claudio has written **a new 😊 quickstart** script where it **mostly** _put likes and comments_. He wants the program to **comment safely** cos he is _afraid of exceeding_ **hourly** & **daily** comment limits,

```python
session.set_quota_supervisor(Settings, enabled=True, peak_comments=(21, 240))
```

>_That's it! When it reaches the comments peak, it will just jump all of the comments and will again continue to put comments when is available [in the next  hour/day]_.

* Alicia has a **24**/**7** 🕦 working **quickstart** script and **would like to** keep _server calls_ in control to AVOID **excessive amount of requests** to the _server_ in **hourly** basis, also,
  * **wants** the program to **sleep after** reaching **hourly** _server calls_ peak: **adds** `"server_calls_h"` into `sleep_after` parameter
  * **wants** the program to **wake up** _a little bit later_ than real sleep time [once reaches the peaks]: **uses** `sleepyhead=True` parameter

```python
session.set_quota_supervisor(Settings, enabled=True, peak_server_calls=(490, None), sleep_after=["server_calls_h"], sleepyhead=True)
```

>_It will sleep after **hourly** server calls reaches its peak given - `490` and **never allow** one more extra request to the server out of the peak and **wake up** when **new hour** comes in WHILST **daily** server calls **will not be** supervised at all- as Alicia wishes_.

* features and he wants to **do it safely**, also,
  * is **gonna** run on local computer and **wants** to receive **toast notifications** 😋 on _supervising states_: **uses** `notify_me` parameter
  * **wants** QS to _randomize_ his `pre-defined` peak values [at close range] each new _hour_/_day_: **uses** `stochastic_flow=True` parameter
  * **wants** the program to sleep after reaching **hourly** _follow_ peak and **daily** _unfollow_ peak: **adds** `"follows_h"` and `"unfollows_d"`into `sleep_after` parameter

```python
session.set_quota_supervisor(Settings, enabled=True, peak_follows=(56, 660), peak_unfollows=(49, 550), sleep_after=["follows_h", "unfollows_d"], stochastic_flow=True, notify_me=True)
```

---
>**Big Hint**: _Find your NEED_ 🤔 _and supervise it!_

* _EITHER_ **fully** configure QS to supervise **all** of the _actions_ all time  
* _OR_ **just** supervise the desired _action_(_s_) in desired _interval_(_s_) [**hourly** and/or **daily**] per your need

## Relationship tools

### Grab Followers of a user

###### Gets and returns `followers` of the given user in desired amount, also can save locally

```python
popeye_followers = session.grab_followers(username="Popeye", userid="Popeye", amount="full", live_match=True, store_locally=True)
##now, `popeye_followers` variable which is a list- holds the `Followers` data of "Popeye" at requested time
```

#### Parameters:

`username`:  
A desired username to grab its followers

* It can be your `own` username **OR** a _username of some `non-private` account._

`amount`:  
Defines the desired amount of usernames to grab from the given account

* `amount="full"`:
  * Grabs followers **entirely**
* `amount=3089`:
  * Grabs `3089` usernames **if exist**, _if not_, grabs **available** amount

`live_match`:  
Defines the method of grabbing `Followers` data
> **Knowledge Base**:  
Every time you grab `Followers` data in `"full"` range of **any** user, it is also gonna be _stored in some corner_ of `FacebookPy` **for that session**.

* `live_match=False`:
  * If the user **already do have** a `Followers` data loaded _earlier_ in the **same** session, it will run a _smart_ `data-matching` _algorithm_.  
  And **there**, it will **load only the new data** _from the server_ and then **return a compact result** of _current data_.  
  The _algorithm_ **works like**: _load the usernames **until hits the** ones from the **previous query** at certain amount_.  
  * **Also if** the `live_match` is `False` and the user has **no any** _sessional_ `Followers` data, **then** it will load `live` data at _requested range_.
  * As a **result**, `live_match=False` saves lots of `precious time` and `server requests`.  
* `live_match=True`:  
  * It will **always** load `live` data from the server at _requested range_.

`store_locally`:  
Gives the _option_ to `save` the loaded `Followers` data in a **local storage**  
The files will be saved _into_ your **logs folder**, `~/FacebookPy/logs/YourOwnUsername/relationship_data/Popeye/followers/` directory.  
Sample **filename** `14-06-2018~full~6874.json`:

* `14-06-2018` means the **time** of the data acquisition.
* `"full"` means the **range** of the data acquisition;  
_If the data is requested at the range **else than** `"full"`, it will write **that** range_.
* `6874` means the **count** of the usernames retrieved.
* `json` is the **filetype** and the data is stored as a `list` in it.

There are **several** `use cases` of this tool for **various purposes**.  
_E.g._, inside your **quickstart** script, you can **do** _something like this_:

```python
#get followers of "Popeye" and "Cinderella"
popeye_followers = session.grab_followers(username="Popeye", userid="Popeye", amount="full", live_match=True, store_locally=True)
sleep(600)
cinderella_followers = session.grab_followers(username="Cinderella", userid="Cinderella", amount="full", live_match=True, store_locally=True)

#find the users following "Popeye" WHO also follow "Cinderella" :D
popeye_cinderella_followers = [follower for follower in popeye_followers if follower in cinderella_followers]
```

#### `PRO`s:

You can **use** this tool to take a **backup** of _your_ **or** _any other user's_ **current** followers.

### Grab Following of a user

###### Gets and returns `following` of the given user in desired amount, also can save locally

```python
lazySmurf_following = session.grab_following(username="lazy.smurf", amount="full", live_match=True, store_locally=True)
##now, `lazySmurf_following` variable which is a list- holds the `Following` data of "lazy.smurf" at requested time
```

#### Parameters:

`username`:  
A desired username to grab its following

* It can be your `own` username **OR** a _username of some `non-private` account._

`amount`:  
Defines the desired amount of usernames to grab from the given account

* `amount="full"`:
  * Grabs following **entirely**
* `amount=3089`:
  * Grabs `3089` usernames **if exist**, _if not_, grabs **available** amount

`live_match`:  
Defines the method of grabbing `Following` data
> **Knowledge Base**:  
Every time you grab `Following` data in `"full"` range of **any** user, it is also gonna be _stored in some corner_ of `FacebookPy` **for that session**.

* `live_match=False`:
  * If the user **already do have** a `Following` data loaded _earlier_ in the **same** session, it will run a _smart_ `data-matching` _algorithm_.  
  And **there**, it will **load only the new data** _from the server_ and then **return a compact result** of _current data_.
  The _algorithm_ **works like**: _load the usernames **until hits the** ones from the **previous query** at certain amount_.  
  * **Also if** the `live_match` is `False` and the user has **no any** _sessional_ `Following` data, **then** it will load `live` data at _requested range_.
  * As a **result**, `live_match=False` saves lots of `precious time` and `server requests`.  
* `live_match=True`:  
  * It will **always** load `live` data from the server at _requested range_.

`store_locally`:  
Gives the _option_ to `save` the loaded `Following` data in a **local storage**  
The files will be saved _into_ your **logs folder**, `~/FacebookPy/logs/YourOwnUsername/relationship_data/lazy.smurf/following/` directory.  
Sample **filename** `15-06-2018~full~2409.json`:

* `15-06-2018` means the **time** of the data acquisition.
* `"full"` means the **range** of the data acquisition;  
_If the data is requested at the range **else than** `"full"`, it will write **that** range_.
* `2409` means the **count** of the usernames retrieved.
* `json` is the **filetype** and the data is stored as a `list` in it.

There are **several** `use cases` of this tool for **various purposes**.  
_E.g._, inside your **quickstart** script, you can **do** _something like this_:

```python
##as we know that all lazy Smurf care is to take some good rest, so by mistake, he can follow somebody WHOM Gargamel also follow!
#so let's find it out to save Smurfs from troubles! :D

#get following of "lazy.smurf" and "Gargamel"
lazySmurf_following = session.grab_following(username="lazy.smurf", amount="full", live_match=True, store_locally=True)
sleep(600)
gargamel_following = session.grab_following(username="Gargamel", amount="full", live_match=True, store_locally=True)

#find the users "lazy.smurf" is following WHOM "Gargamel" also follow :D
lazySmurf_gargamel_following = [following for following in lazySmurf_following if following in gargamel_following]
```

#### `PRO`s:

You can **use** this tool to take a **backup** of _your_ **or** _any other user's_ **current** following.

### Pick Unfollowers of a user

###### Compares the `followers` stored in a local storage against current followers and returns absent followers

```python
all_unfollowers, active_unfollowers = session.pick_unfollowers(username="Bernard_bear", compare_by="month", compare_track="first", live_match=True, store_locally=True, print_out=True)
##now, `all_unfollowers` and `all_unfollowers` variables which are lists- hold the `Unfollowers` data of "Bernard_bear" at requested time
#`all_unfollowers` holds all of the unfollowers WHILST `active_unfollowers` holds the unfollowers WHOM "Bernard_bear" is still following
```

#### Parameters:
`username`:  
A desired username to pick its unfollowers

* It can be your `own` username **OR** a _username of some `non-private` account._

`compare_by`:
Defines the `compare point` to pick unfollowers

* Available **value**s are:
  * `"latest"` chooses the very latest record from the existing records in the local folder
  * `"earliest"` chooses the very earliest record from the existing records in the local folder

  The compare points below needs a **compare track** defined, too:
  * `"day"` chooses from the existing records of today in the local folder
  * `"month"` chooses from the existing records of this month in the local folder
  * `"year"` chooses from the existing records of this year in the local folder

`compare_track`:
Defines the track to choose a file to compare for `"day"`, `"month"` and `"year"` compare points

* Available **value**s are:
  * `"first"` selects the first record from the given `day`, `month` or `year`
  * `"median"` selects the median (_the one in the middle_) record from the given `day`, `month` or `year`
  * `"last"` selects the last record from the given `day`, `month` or `year`

`live_match`:  
Defines the method of grabbing **new** `Followers` data to compare with **existing** data
> **Knowledge Base**:  
Every time you grab `Followers` data in `"full"` range of **any** user, it is also gonna be _stored in some corner_ of `FacebookPy` **for that session**.

* `live_match=False`:
  * If the user **already do have** a `Followers` data loaded _earlier_ in the **same** session, it will run a _smart_ `data-matching` _algorithm_.  
  And **there**, it will **load only the new data** _from the server_ and then **return a compact result** of _current data_.  
  The _algorithm_ **works like**: _load the usernames **until hits the** ones from the **previous query** at certain amount_.  
  * **Also if** the `live_match` is `False` and the user has **no any** _sessional_ `Followers` data, **then** it will load `live` data at _requested range_.
  * As a **result**, `live_match=False` saves lots of `precious time` and `server requests`.  
* `live_match=True`:  
  * It will **always** load `live` data from the server at _requested range_.

`store_locally`:  
Gives the _option_ to `save` the loaded `Unfollowers` data in a **local storage**  
There will be 2 files saved in their own directory:

* `all_unfollowers`:
  * Will store all of the unfollowers in there  
  * Its files will be saved at **logs folder**, `~/FacebookPy/logs/YourOwnUsername/relationship_data/Bernard_bear/unfollowers/all_unfollowers/` directory.
* `active_unfollowers`:
  * Will store only the unfollowers WHOM you are currently following.  
  * Its files will be saved at **logs folder**, `~/FacebookPy/logs/YourOwnUsername/relationship_data/Bernard_bear/unfollowers/active_unfollowers/` directory.

Sample **filename** `03-06-2018~all~75.json`:

* `03-06-2018` means the **time** of the data acquisition.
* `"all"` means that it is all of the unfollowers data;  
_*`"active"` unfollowers files will have `"active"` written in there_.
* `75` means the **count** of the unfollowers retrieved.
* `json` is the **filetype** and the data is stored as a `list` in it.

`print_out`:  
Use this parameter if you would like the `see` those unfollowers **printed** into the **console output** _right after finding them_.

There are **several** `use cases` of this tool for **various purposes**.

* You can the get the unfollowers you have had from the **start of the** _year_, or from the **middle of the** _year_ or from the start of the **month**, etc.

And then, e.g. do some `useful` **analysis** with that _generated unfollowers data_.

* _And_ you can also **find** the unfollowers to `block` them **all**.
* Also, you can **unfollow back** those `active unfollowers` _right away_:

```python
#find all of the active unfollowers of Bernard bear
all_unfollowers, active_unfollowers = session.pick_unfollowers(username="Bernard_bear", compare_by="earliest", compare_track="first", live_match=True, store_locally=True, print_out=True)
sleep(200)
#let's unfollow them immediately cos Bernard will be angry if heards about those unfollowers! :D
session.unfollow_users(amount=len(active_unfollowers), customList=(True, active_unfollowers, "all"), style="RANDOM", unfollow_after=None, sleep_delay=600)
```

### Pick Nonfollowers of a user

###### Compares the `Followers` data against `Following` data of a user and returns the `Nonfollowers` data

```python
scoobyDoo_nonfollowers = session.pick_nonfollowers(username="ScoobyDoo", live_match=True, store_locally=True)
#now, `scoobyDoo_nonfollowers` variable which is a list- holds the `Nonfollowers` data of "ScoobyDoo" at requested time
```

#### Parameters:

`username`:  
A desired username to pick its nonfollowers

* It can be your `own` username **OR** a _username of some `non-private` account._

`live_match`:  
Defines the method of grabbing `Followers` and `Following` data to compare with each other to find **nonfollowers**
> **Knowledge Base**:  
Every time you grab `Followers` and/or `Following` data in `"full"` range of **any** user, it is also gonna be _stored in some corner_ of `FacebookPy` **for that session**.

* `live_match=False`:
  * If the user **already do have** a `Followers` and/or `Following` data loaded _earlier_ in the **same** session, it will run a _smart_ `data-matching` _algorithm_.  
  And **there**, it will **load only the new data** _from the server_ and then **return a compact result** of _current data_.  
  The _algorithm_ **works like**: _load the usernames **until hits the** ones from the **previous query** at certain amount_.  
  * **Also if** the `live_match` is `False` and the user has **no any** _sessional_ `Followers` and/or `Following` data, **then** it will load `live` data at _requested range_.
  * As a **result**, `live_match=False` saves lots of `precious time` and `server requests`.  
* `live_match=True`:  
  * It will **always** load `live` data from the server at _requested range_.

`store_locally`:  
Gives the _option_ to `save` the loaded `Nonfollowers` data in a **local storage**  
The files will be saved _into_ your **logs folder**, `~/FacebookPy/logs/YourOwnUsername/relationship_data/ScoobyDoo/nonfollowers/` directory.  
Sample **filename** `01-06-2018~[5886-3575]~2465.json`:

* `01-06-2018` means the **time** of the data acquisition.
* `5886` means the **count** of the followers retrieved.
* `3575` means the **count** of the following retrieved.
* `2465` means the **count** of the nonfollowers picked.
* `json` is the **filetype** and the data is stored as a `list` in it.

There are **several** `use cases` of this tool for **various purposes**.

* You can get the nonfollowers of several users and then do analysis.  
  * _e.g., in this example Scooby Do used it like this_:

  ```python
  ##Scooby Doo always wonders a lot and this time he wonders if there are people Shaggy is following WHO do not follow him back...
  shaggy_nonfollowers = session.pick_nonfollowers(username="Shaggy", live_match=True, store_locally=True)

  #now Scooby Doo will tell his friend Shaggy about this, who knows, maybe Shaggy will unfollow them all or even add to block :D
  ```  

### Pick Fans of a user

###### Returns Fans data- all of the accounts who do follow the user WHOM user itself do not follow back

```python
smurfette_fans = session.pick_fans(username="Smurfette", live_match=True, store_locally=True)
#now, `smurfette_fans` variable which is a list- holds the `Fans` data of "Smurfette" at requested time
```

#### Parameters:

`username`:  
A desired username to pick its fans

* It can be your `own` username **OR** a _username of some `non-private` account._

`live_match`:  
Defines the method of grabbing `Followers` and `Following` data to compare with each other to find **fans**
> **Knowledge Base**:  
Every time you grab `Followers` and/or `Following` data in `"full"` range of **any** user, it is also gonna be _stored in some corner_ of `FacebookPy` **for that session**.

* `live_match=False`:
  * If the user **already do have** a `Followers` and/or `Following` data loaded _earlier_ in the **same** session, it will run a _smart_ `data-matching` _algorithm_.  
  And **there**, it will **load only the new data** _from the server_ and then **return a compact result** of _current data_.  
  The _algorithm_ **works like**: _load the usernames **until hits the** ones from the **previous query** at certain amount_.  
  * **Also if** the `live_match` is `False` and the user has **no any** _sessional_ `Followers` and/or `Following` data, **then** it will load `live` data at _requested range_.
  * As a **result**, `live_match=False` saves lots of `precious time` and `server requests`.  
* `live_match=True`:  
  * It will **always** load `live` data from the server at _requested range_.

`store_locally`:  
Gives the _option_ to `save` the loaded `Fans` data in a **local storage**  
The files will be saved _into_ your **logs folder**, `~/FacebookPy/logs/YourOwnUsername/relationship_data/Smurfette/fans/` directory.  
Sample **filename** `05-06-2018~[4591-2575]~3477.json`:

* `05-06-2018` means the **time** of the data acquisition.
* `4591` means the **count** of the followers retrieved.
* `2575` means the **count** of the following retrieved.
* `3477` means the **count** of the fans picked.
* `json` is the **filetype** and the data is stored as a `list` in it.

There are **several** `use cases` of this tool for **various purposes**.

* You can get the fans of several users and then do analysis.  
  * _e.g., in this example Smurfette used it like this_:

  ```python
  ##Smurfette is so famous in the place and she wonders which smurfs is following her WHOM she doesn't even know of :D
  smurfette_fans = session.pick_fans(username="Smurfette", live_match=True, store_locally=True)
  #and now, maybe she will follow back some of the smurfs whom she may know :P
  ```  

### Pick Mutual Following of a user

###### Returns `Mutual Following` data- all of the accounts who do follow the user WHOM user itself **also** do follow back

```python
Winnie_mutualFollowing = session.pick_mutual_following(username="WinnieThePooh", live_match=True, store_locally=True)
#now, `Winnie_mutualFollowing` variable which is a list- holds the `Mutual Following` data of "WinnieThePooh" at requested time
```

#### Parameters:

`username`:  
A desired username to pick its mutual following

* It can be your `own` username **OR** a _username of some `non-private` account._

`live_match`:  
Defines the method of grabbing `Followers` and `Following` data to compare with each other to find **mutual following**
> **Knowledge Base**:  
Every time you grab `Followers` and/or `Following` data in `"full"` range of **any** user, it is also gonna be _stored in some corner_ of `FacebookPy` **for that session**.

* `live_match=False`:
  * If the user **already do have** a `Followers` and/or `Following` data loaded _earlier_ in the **same** session, it will run a _smart_ `data-matching` _algorithm_.  
  And **there**, it will **load only the new data** _from the server_ and then **return a compact result** of _current data_.  
  The _algorithm_ **works like**: _load the usernames **until hits the** ones from the **previous query** at certain amount_.  
  * **Also if** the `live_match` is `False` and the user has **no any** _sessional_ `Followers` and/or `Following` data, **then** it will load `live` data at _requested range_.
  * As a **result**, `live_match=False` saves lots of `precious time` and `server requests`.  
* `live_match=True`:  
  * It will **always** load `live` data from the server at _requested range_.

`store_locally`:  
Gives the _option_ to `save` the loaded `Mutual Following` data in a **local storage**  
The files will be saved _into_ your **logs folder**, `~/FacebookPy/logs/YourOwnUsername/relationship_data/WinnieThePooh/mutual_following/` directory.  
Sample **filename** `11-06-2018~[3872-2571]~1120.json`:

* `11-06-2018` means the **time** of the data acquisition.
* `3872` means the **count** of the followers retrieved.
* `2571` means the **count** of the following retrieved.
* `1120` means the **count** of the mutual following picked.
* `json` is the **filetype** and the data is stored as a `list` in it.

There are **several** `use cases` of this tool for **various purposes**.

* You can get the mutual following of several users and then do analysis.
  * _e.g., in this example Winnie The Pooh used it like this_:

  ```python
  #Winnie The Pooh is a very friendly guy and almost everybody follows him back, but he wants to be sure about it :D
  Winnie_mutual_following = session.pick_mutual_following(username="WinnieThePooh", live_match=True, store_locally=True)
  ##now, he will write a message to his mutual followers to help him get a new honey pot :>
  ```  

## Text Analytics

### Yandex Translate API

<img src="https://yastatic.net/www/_/Q/r/sx-Y7-1azG3UMxG55avAdgwbM.svg" width="196" align="right">

<img src="https://yastatic.net/s3/home/logos/services/1/translate.svg" width="66" align="left">

###### Offers excellent language detection and synchronized translation for over 95 languages 😎 worldwide

_This service currently is supported only by the [Interact by Comments](#interact-by-comments) feature_.

#### Usage

Go [**sign up**](https://translate.yandex.com/developers/keys) on [_translate.yandex.com_](https://translate.yandex.com) and get a _free_ `API_key`;  
_Then configure its usage at your **quickstart** script_,

```python
session.set_use_yandex(enabled=True,
                       API_key='',
                       match_language=True,
                       language_code="en")
```

#### Parameters

`enabled`
: Put `True` to **activate** or `False` to **deactivate** the service usage;  

`API_key`
: The _key_ which is **required** to authenticate `HTTP` _requests_ to the **API**;  

`match_language`
: **Enable** if you would like to match the language of the text;

`language_code`
: **Set** your desired language's code to **match language** (_if it's enabled_);
>You can get the list of all supported languages and their codes at [_tech.yandex.com_](https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/#api-overview__languages).

#### Rate Limits

In its _free_ plan, the **daily** request _limit_ is `1,000,000` characters and the **monthly** _limit_ is `10,000,000` characters.
>To increase the request limit, you can **switch** to the `fee-based` version of the service (_$`15`/million chars_)..

#### Examples

**1**-) Matching language;

```python
session.set_use_yandex(enabled=True, API_key='', match_language=True, language_code="az")
```

Target text
: "_your technique encourages📸 me_"  

_Now that text is gonna be labeled **inappropriate** COS its language is `english` rather than the desired `azerbaijani`_..

**2**-) Enabling the **Yandex** service _but NOT_ matching language;
Since **Yandex** Translate is being used [internally] by the **MeaningCloud** service, you can just provide the API key of **Yandex** and enable it without enabling the `match_language` parameter what will be sufficient for the **MeaningCloud** to work..

```python
session.set_use_yandex(enabled=True, API_key='', match_language=False)
```

>And yes, you can enable **Yandex** service to make it be available for **MeaningCloud** and then also _match language_ if you like, in the same setup just by turning the `match_language` parameter on..

#### Legal Notice

[Powered by Yandex.Translate](http://translate.yandex.com/)

### MeaningCloud Sentiment Analysis API

<img src="https://www.meaningcloud.com/developer/img/LogoMeaningCloud210x85.png" width="210" align="right">

###### Offers a detailed, multilingual analysis of all kind of unstructured content determining its sentiment ⚖

_This service currently is supported only by the [Interact by Comments](#interact-by-comments) feature_.

Determines if text displays _positive_, _negative_, or _neutral_ sentiment - or is _not possible_ to detect.  
Phrases are identified with the _relationship between_ them evaluated which identifies a _global polarity_ value of the text.

#### Usage

**1**-) Go [**sign up**](https://www.meaningcloud.com/developer/login) (_offers **sign in** with_ 😎 _**Github**_) on [_meaningcloud.com_](https://www.meaningcloud.com) and get a _free_ `license_key`;  
_Then configure its usage at your **quickstart** script_,

```python
session.set_use_meaningcloud(enabled=True,
                             license_key='',
                             polarity="P",
                             agreement="AGREEMENT",
                             subjectivity="SUBJECTIVE",
                             confidence=94)
```

**2**-) Install its _package_ for **python** by `pip`;

```powershell
pip install MeaningCloud-python
```

**3**-) Turn on **Yandex** _Translate_ service which is a **requirement** for the language _detection_ & _translation_ at request;  
_To have it configured, read its [documentation](#yandex-translate-api)_.

#### Parameters

`enabled`
: Put `True` to **activate** or `False` to **deactivate** the service usage;  

`license_key`
: The license key is **required** to do _calls_ to the API;  

`polarity`
: It indicates the polarity found (_or not found_) in the text and applies to the **global** polarity of the text;  
_It's a **graduated** polarity - rates from **very** negative to **very** positive_.

| `score_tag` |                   definition                    |  
| ----------- | ----------------------------------------------- |
|    `"P+"`   |       match if text is _**strong** positive_    |  
|    `"P"`    |       match if text is _positive_ or above      |
|    `"NEU"`  |       match if text is _neutral_ or above       |  
|    `"N"`    |       match if text is _negative_ or above      |
|    `"N+"`   | match if text is _**strong** negative_ or above |  
|    `None`   |     do not match per _polarity_ found, at all   |  

  > By "_or above_" it means- _e.g._, if you set `polarity` to `"P"`, and text is `"P+"` then it'll also be appropriate (_as it always leans towards positivity_) ..

`agreement`
: Identifies **opposing** opinions - _contradictory_, _ambiguous_;  
_It marks the agreement **between** the sentiments detected in the text, the sentence or the segment it refers to_.

|    `agreement`   |                            definition                                     |  
| ---------------- | ------------------------------------------------------------------------- |
|   `"AGREEMENT"`  |       match if the different elements have **the same** polarity          |  
| `"DISAGREEMENT"` | match if there is _disagreement_ between the different elements' polarity |
|      `None`      |              do not match per _agreement_ found, at all                   |

`subjectivity`
: Identification of _opinions_ and _facts_ - **distinguishes** between _objective_ and _subjective_;  
_It marks the subjectivity of the text_.

| `subjectivity` |                          definition                           |  
| -------------- | ------------------------------------------------------------- |
| `"SUBJECTIVE"` |           match if text that has _subjective_ marks           |  
| `"OBJECTIVE"`  | match if text that does not have **any** _subjectivity_ marks |
|     `None`     |         do not match per _subjectivity_ found, at all         |

`confidence`
: It represents the _confidence_ associated with the sentiment analysis **performed on the** text and takes an integer number in the _range of_ `(0, 100]`;  
>If you **don't want to** match per _confidence_ found, at all, use the value of `None`.

#### Rate Limits

It gives you `20 000` single API calls per each month (_starting from the date you have **signed up**_).  
It has _no daily limit_ but if you hit the limit set for number of requests can be carried out concurrently (_per second_) it'll return with error code of `104` rather than the result 😉

#### Language Support

**MeaningCloud** currently supports a generic sentiment model (_called general_) in these languages: _english_, _spanish_, _french_, _italian_, _catalan_, and _portuguese_.  
>You can define your own sentiment models using the user sentiment models console and work with them in the same way as with the sentiment models it provides.  

But **no need to worry** IF your _language_ or _target audience's language_ is NONE of those **officially** supported.  
Cos, to **increase the coverage** and support **all other** languages, as well, **Yandex** _Translate_ service comes to rescue!  
It detects the text's langugage before passing it to **MeaningCloud**, and, if its language is not supported by **MeaningCloud**, it translates it into english and only then passes it to **MeaningCloud** _Sentiment Analysis_..

#### Examples

**a** -) Match **ONLY** per `polarity` and `agreement`

```python
session.set_use_meaningcloud(enabled=True, license_key='', polarity="P", agreement="AGREEMENT")
```

Target text
: "_I appreciate your innovative thinking that results, brilliant images_"  

_Sentiment Analysis_ results for the text:

| `score_tag` |  `agreement`  | `subjectivity` | `confidence` |
| ----------- | ------------- | -------------- | ------------ |
|   `"P+"`    | `"AGREEMENT"` | `"SUBJECTIVE"` |     `100`    |

_Now that text is gonna be labeled **appropriate** COS its polarity is `"P+"` which is more positive than `"P"` and `agreement` values also do match_..  

**b** -) Match **FULLY**

```python
session.set_use_meaningcloud(enabled=True, license_key='', polarity="P+", agreement="AGREEMENT", subjectivity="SUBJECTIVE", confidence=98)
```

Target text
: "_truly fantastic but it looks sad!_"  

_Sentiment Analysis_ results for the text:

| `score_tag` |    `agreement`   | `subjectivity` | `confidence` |
| ----------- | ---------------- | -------------- | ------------ |
|    `"P"`    | `"DISAGREEMENT"` | `"SUBJECTIVE"` |     `92`    |

_Now that text is gonna be labeled **inappropriate** COS its polarity is `"P"` which is less positive than `"P+"` and also, `agreement` values also **do NOT** match, and **lastly**, `confidence` is **below** user-defined `98`_..

#### Legal Notice

This project uses MeaningCloud™ (http://www.meaningcloud.com) for Text Analytics.

### Use a proxy

You can use FacebookPy behind a proxy by specifying server address and port

```python
session = FacebookPy(username=facebook_username, password=facebook_password, proxy_address='8.8.8.8', proxy_port=8080)
```

To use proxy with authentication you should firstly generate proxy chrome extension (works only with headless_browser=False unless using FF where it works with headless_browser=True).

```python
from proxy_extension import create_proxy_extension

proxy = 'login:password@ip:port'
proxy_chrome_extension = create_proxy_extension(proxy)

session = FacebookPy(username=facebook_username, password=facebook_password, proxy_chrome_extension=proxy_chrome_extension, nogui=True)
```

### Switching to Firefox

Chrome is the default browser, but FacebookPy provides support for Firefox as well.

```python
session = FacebookPy(username=facebook_username, password=facebook_password, use_firefox=True)
```

### Emoji Support

To use an emoji just add an `u` in front of the opening apostrophe:

```python
session.set_comments([u'This post is 🔥',u'More emojis are always better 💯',u'I love your posts 😍😍😍'])
# or
session.set_comments([u'Emoji text codes are also supported :100: :thumbsup: :thumbs_up: \u2764 💯💯'])
```

Emoji text codes are implemented using 2 different naming codes. A complete list of emojis codes can be found on the [Python Emoji Github](https://github.com/carpedm20/emoji/blob/master/emoji/unicode_codes.py), but you can use the alternate shorted naming scheme found for Emoji text codes [here](https://www.webpagefx.com/tools/emoji-cheat-sheet). Note: Every Emoji has not been tested. Please report any inconsistencies.

> **Legacy Emoji Support**
>
> You can still use Unicode strings in your comments, but there are some limitations.
>
> 1. You can use only Unicode characters with no more than 4 characters and you have to use the unicode code (e. g. ```\u1234```). You find a list of emoji with unicode codes on [Wikipedia](https://en.wikipedia.org/wiki/Emoji#Unicode_blocks), but there is also a list of working emoji in ```/assets```
>
> 2. You have to convert your comment to Unicode. This can safely be done by adding an u in front of the opening apostrophe: ```u'\u1234 some comment'```

## Clarifai ImageAPI

<img src="https://clarifai.com/cms-assets/20180311184054/Clarifai_Pos.svg" width="200" align="right">

###### Note: Head over to [https://developer.clarifai.com/signup/](https://developer.clarifai.com/signup/) and create a free account, once you're logged in go to [https://developer.clarifai.com/account/applications/](https://developer.clarifai.com/account/applications/) and create a new application. You can find the client ID and Secret there. You get 5000 API-calls free/month.

If you want the script to get your CLARIFAI_API_KEY for your environment, you can do:

```python
export CLARIFAI_API_KEY="<API KEY>"
```

### Example with Imagecontent handling

```python
session.set_do_comment(True, percentage=10)
session.set_comments(['Cool!', 'Awesome!', 'Nice!'])
session.set_use_clarifai(enabled=True)
session.clarifai_check_img_for(['nsfw'])
session.clarifai_check_img_for(['food', 'lunch', 'dinner'], comment=True, comments=['Tasty!', 'Nice!', 'Yum!'])

session.end()
```

### Enabling Imagechecking

```python
# default enabled=False , enables the checking with the Clarifai API (image
# tagging) if secret and proj_id are not set, it will get the environment
# variables 'CLARIFAI_API_KEY'.

session.set_use_clarifai(enabled=True, api_key='xxx')
```

### Using Clarifai Public Models and Custom Models

If not specified by setting the `models=['model_name1']` in `session.set_use_clarifai`, `models` will be set to `general` by default.

If you wish to check against a specific model or multiple models (see Support for Compound Model Queries below), you can specify the models to be checked as shown below.

To get a better understanding of the models and their associated concepts, see the Clarifai [Model Gallery](https://clarifai.com/models) and [Developer Guide](https://clarifai.com/developer/guide/)

**NOTE ON MODEL SUPPORT**: At this time, the support for the`Focus`, `Face Detection`, `Face Embedding`, and `General Embedding` has not been added.

```python
# Check image using the NSFW model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['nsfw'])

# Check image using the Apparel model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['apparel'])

# Check image using the Celebrity model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['celebrity'])

# Check image using the Color model
session.set_use_clarifai(enabled=True, api_key=‘xxx’, models=[‘model’])

# Check image using the Demographics model
session.set_use_clarifai(enabled=True, api_key=‘xxx’, models=[‘demographics’])

# Check image using the Food model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['food'])

# Check image using the Landscape Quality model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['landscape quality'])

# Check image using the Logo model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['logo'])

# Check image using the Moderation model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['moderation'])

# Check image using the Portrait Quality model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['portrait quality'])

# Check image using the Textures and Patterns model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['textures'])

# Check image using the Travel model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['travel'])

# Chaeck image using the Weddings model
session.set_use_clarifai(enabled=True, api_key='xxx', models=['weddings'])

# Check image using a custom model where model_name is name of your choosing (see Clarifai documentation for using custom models)
session.set_use_clarifai(enabled=True, api_key='xxx', models=['your-model-name'])
```

### Filtering Inappropriate Images

```python
# uses the clarifai api to check if the image contains nsfw content
# by checking against Clarifai's NSFW model
# -> won't comment if image is nsfw

session.set_use_clarifai(enabled=True, api_key='xxx', models=['nsfw'])
session.clarifai_check_img_for(['nsfw'])
```

```python
# uses the clarifai api to check if the image contains inappropriate content
# by checking against Clarifai's Moderation model
# -> won't comment if image is suggestive or explicit

session.set_use_clarifai(enabled=True, api_key='xxx', models=['moderation'])
session.clarifai_check_img_for(['suggestive', 'explicit'])

# To adjust the threshold for accepted concept predictions and their
# respective score (degree of confidence) you can set the default probability
# parameter for Clarifai (default 50%). For example, you could set probability to 15%.
# -> any image with a nsfw score of 0.15 of higher will not be commented on

session.set_use_clarifai(enabled=True, api_key='xxx', probability= 0.15, models=['nsfw'])
session.clarifai_check_img_for(['nsfw'])
```

### Filtering by Keyword

```python
# uses the clarifai api to check if the image concepts contain the keyword(s)
# -> won't comment if image contains the keyword

session.clarifai_check_img_for(['building'])
```

### Specialized Comments for Images with Specific Content

```python
# checks the image for keywords food and lunch. To check for both, set full_match in
# in session.set_use_clarifia to True, and if both keywords are found,
# FacebookPy will comment with the given comments. If full_match is False (default), it only
# requires a single tag to match Clarifai results.

session.set_use_clarifai(enabled=True, api_key='xxx', full_match=True)
session.clarifai_check_img_for(['food', 'lunch'], comment=True, comments=['Tasty!', 'Yum!'])

# If you only want to accept results with a high degree of confidence, you could
# set a probability to a higher value, like 90%.

session.set_use_clarifai(enabled=True, api_key='xxx', probability=0.90, full_match=True)
session.clarifai_check_img_for(['food', 'lunch'], comment=True, comments=['Tasty!', 'Yum!'])
```

### Querying Multiple Models with Workflow (Single API Call)

You can query multiple Clarifai models with a single API call by setting up a custom workflow.  Using a `workflow` is the recommended way to query multiple models. Alternatively, it is possible to query multiple models separately (see Querying Multiple Models (Multiple API Calls) below).

To setup a workflow, see the [Workflow Documentation](https://www.clarifai.com/developer/guide/workflow#workflow).

**NOTE** :As mentioned above, the `Focus`, `Face Detection`, `Face Embedding`, and `General Embedding` models are not current supported.

Once you have a workflow setup, you can use FacebookPy to check images with the Clarifai Image API by setting the `workflow` parameter in `session.set_use_clarifai` to the name of your custom workflow.

Let's say you want to comment 'Great shot!' on images of men or women with the hashtag `#selfie`, but you want to make sure not to comment on images which might contain inappropriate content. To get general concepts, e.g. `woman`, you would setup your workflow using `General` and to check the image for the concepts `nsfw` and `explicit` you would also want to add NSFW and Moderation models to your workflow.

For example:

```python
session.set_use_clarifai(enabled=True, api_key='xxx', workflow=['your-workflow'], proxy='123.123.123.123:5555')
session.clarifai_check_img_for(['woman', 'man'], ['nsfw', 'explicit', 'suggestive'], comment=True, comments=['Great shot!'])
```

If Clarifai's response includes the concepts of either `woman` or `man` but also includes at least `nsfw`, `explicit`, or `suggestive`, FacebookPy will not comment. On the other hand, if Clarifai's response includes the concepts of either `woman` or `man` but does not include any of the concepts `nsfw`, `explicit`, or `suggestive`, FacebookPy will add the comment `Great shot!`

### Querying Multiple Models (Multiple API Calls)

In the event that you do not want to set up a workflow, you can also query multiple models using multiple API calls.

**WARNING**: If you are using a free account with Clarifiai, be mindful that the using compound API queries could greatly increase your chances of exceeding your allotment of free 5000 operations per month. The number of Clarifai billable operations per image check equals the number of models selected. For example, if you check 100 images against `models=['general', 'nsfw', 'moderation']`, the total number of billable operations will be 300.

Following the example above, to get general concepts, e.g. `woman`, you would use the model `general` and to check the image for the concepts `nsfw` and `explicit` you would also want to check the image against the NSFW and Moderation models.

For example:

```python
session.set_use_clarifai(enabled=True, api_key='xxx', models=['general', 'nsfw', 'moderation'], proxy=None)
session.clarifai_check_img_for(['woman', 'man'], ['nsfw', 'explicit', 'suggestive'], comment=True, comments=['Great shot!'])
```

Using proxy to access clarifai:
We have 3 options:

1. ip:port
2. user:pass@ip:port
3. None

### Checking Video

**WARNING**: Clarifai checks one frame of video for content for every second of video. **That is, in a 60 second video, 60 billable operations would be run for every model that the video is being checked against.** Running checks on video should only be used if you have special needs and are prepared to use a large number of billable operations.

To have Clarifai run a predict on video posts, you can set the `check_video` argument in `session.set_use_clarifai` to `True`. By default, this argument is set to `False`. Even if you do not choose to check the entire video, Clarifai will still check the video's keyframe for content.

For example:

```python
session.set_use_clarifai(enabled=True, api_key='xxx', check_video=True)
```

With video inputs, Clarifai's Predict API response will return a list of concepts at a rate of one frame for every second of a video.

Be aware that you cannot check video using a `workflow` and that only a select number of public models are currently supported. Models currently supported are: Apparel, Food, General, NSFW, Travel, and Wedding. In the event that the models being used do not support video inputs or you are using a workflow, the video's keyframe will still be checked for content.

##### Check out [https://clarifai.com/demo](https://clarifai.com/demo) to see some of the available tags.</h6>

## Running on a Server

Use the `nogui` parameter to interact with virtual display

```python
session = FacebookPy(username='test', password='test', nogui=True)
```

## Running on a Headless Browser

**Note:** Chrome only! Must use chromedriver v2.9+

Use `headless_browser` parameter to run the bot via the CLI. Works great if running the scripts locally, or to deploy on a server. No GUI, less CPU intensive. [Example](http://g.recordit.co/BhEgXANLhJ.gif)

```python
session = FacebookPy(username='test', password='test', headless_browser=True)
```

## Running Multiple Accounts

Use the multi_logs parameter if you are going to use multiple accounts and want the log files stored per account.

```python
session = FacebookPy(username='test', password='test', multi_logs=True)
```

## Running with Docker microservices manual

Docker allows very easy and fast run of the facebookpy bot without any pain and tears.

### 0. Preparations

Install docker from the official website [https://www.docker.com/](https://www.docker.com/)

Install VNC viewer if you do not have one. For windows, a good program is  [http://www.tightvnc.com/](http://www.tightvnc.com/)

### 1. Set your facebook login and password

Open `docker_quickstart.py` and fill the quotes after facebook_username and facebook_password with your credentials.

Don't forget to make other changes for the file as you want to. Read the documentation above for info.

### 2. Run and build containers with docker-compose

First you need to open your terminal, move to the root folder (usually with the `cd` command) of facebookpy project and then type:

```bash
docker-compose up -d --build
```

That's all! At this step, you are already successfully running your personal bot!

### 3. See what your bot can do right now

Run your VNC viewer, and type address and port `localhost:5900`. The password is `secret`.

### 4. Stop your facebookpy bot

Use your terminal again, type in the same window:

```bash
docker-compose down
```

Your bot is stopped!

### 5. Further steps

Those are just basic steps to run facebookpy bot on your PC with docker. There are other docker-compose settings file in the root of project.

#### Development environment to run, test and debug by SSH

Use it to help us with development and test facebookpy! `docker-dev.yml` file.

```bash
docker-compose -f docker-dev.yml up -d
```

After striking this command, you can access your bot by VNC on the adress  `localhost:5901`, the password is `secret`.

But there is more! There is a fully accessible bash console with all code mounted at the path `/code`. When you hack some files they are dynamically updated inside your container.

To access yor container console to run bot type `localhost:22` in your favorite ssh client. The User is `root` and the password is `root` also.

#### Run in production without opened VNC port

Suitable to run in a remote server. Attention! You can not view what happened through VNC on this configuration `docker-prod.yml` file.

```bash
docker-compose -f docker-prod.yml up -d
```

## Running all-in-one with Docker (legacy)

### 1. Build the Image

First you need to build the image by running this in the Terminal:

```bash
docker build -t facebookpy ./docker_conf/all_in_one
```

Make sure to use the `nogui` feature:

```python
# you can use the nogui parameter to use a virtual display

session = FacebookPy(username='test', password='test', nogui=True)
```

### 2. Run in a Container

After the build succeeds, you can simply run the container with:

```bash
docker run --name=facebookpy -e FACEBOOK_USER=<your-user> -e FACEBOOK_PW=<your-pw> -d --rm facebookpy
```

## Automate FacebookPy

### [Windows Task Scheduler](https://msdn.microsoft.com/en-us/library/windows/desktop/aa383614(v=vs.85).aspx)

You can use Window's built in Task Scheduler to automate FacebookPy, using a variety of trigger types: time, login, computer idles, etc. To schedule a simple daily run of an Facebookpy script follow the below directions

1. Open [Windows Task Scheduler](https://msdn.microsoft.com/en-us/library/windows/desktop/aa383614(v=vs.85).aspx)
2. Select "Create Basic Task"
3. Fill out "Name" and "Description" as desired, click "Next"
4. On "Trigger" screen select how frequently to run, click "Next" (Frequency can be modified later)
5. On "Daily" screen, hit "Next"
6. "Action Screen" select "Start a program" and then click "Next"
7. "Program/script" enter the path, or browse to select the path to python. ([How to find python path on Windows](https://stackoverflow.com/questions/647515/how-can-i-get-python-path-under-windows))
8. "Add arguments" input the FacebookPy script path you wish to run. (Example: C:\Users\USER_NAME\Documents\GitHub\FacebookPy\craigquick.py)
9. "Start in" input Facebookpy install location (Example: C:\Users\USER_NAME\Documents\GitHub\FacebookPy\). Click "Next"
10. To finish the process, hit "Finish"

### `cron`

You can add FacebookPy to your crontab, so that the script will be executed regularly. This is especially useful for servers, but be sure not to break Facebooks follow and like limits.

```shell
# Edit or create a crontab
crontab -e
# Add information to execute your FacebookPy regularly.
# With cd you navigate to your FacebookPy folder, with the part after &&
# you execute your quickstart.py with python. Make sure that those paths match
# your environment.
45 */4 * * * cd /home/user/FacebookPy && /usr/bin/python ./quickstart.py
```

### [Schedule](https://github.com/dbader/schedule)

> Schedule is an in-process scheduler for periodic jobs that uses the builder pattern for configuration. Schedule lets you run Python functions periodically at pre-determined intervals using a simple, human-friendly syntax.

```shell
pip install schedule
```

```python
from facebookpy import FacebookPy
import schedule
import time

def job():
    try:
        session = FacebookPy(selenium_local_session=False) # Assuming running in Compose
        session.set_selenium_remote_session(selenium_url='http://selenium:4444/wd/hub')
        session.login()
        session.set_do_comment(enabled=True, percentage=20)
        session.set_comments(['Well done!'])
        session.set_do_follow(enabled=True, percentage=5, times=2)
        session.like_by_tags(['love'], amount=100, media='Photo')
        session.end()
    except:
        import traceback
        print(traceback.format_exc())

schedule.every().day.at("6:35").do(job)
schedule.every().day.at("16:22").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## Workspace folders

###### _FacebookPy_ stores user's data files inside the **workspace** folder.

By default, it is gonna be the **FacebookPy** folder at your home folder.  
Such as, if your username is `Cherry`, let's show where your FacebookPy folder would be,

|   OS    |       home folder     | _FacebookPy_ **workspace** folder |
| ------- | --------------------- | ------------------------------ |
| Windows | `C:\\Users\\Cherry\\` | `C:\\Users\\Cherry\\FacebookPy\\` |
|   Mac   |    `/Users/Cherry/`   |    `/Users/Cherry/FacebookPy/`    |
|  Linux  |    `/home/Cherry/`    |    `/home/Cherry/FacebookPy/`     |

Note that, at the start of each run, it shows you the **workspace** folder in use.

<br /> 

<details>
  <summary>
    <b>
      What will be stored at the <b>workspace</b> folder? 🔍
    </b>
  </summary>

Anything that is _user's **data file**_ will be stored in there.  
Such as,

* **logs** folder - _log and other storage files_
* **assets** folder - _e.g. user chosen chromedriver executable(s)_
* **db** folder - _databases_
* etc.

</details>

### Migrating your data to the workspace folder

After installing FacebookPy with pip, you have to run it once by calling `python quickstart.py`. Once the web browser opens, you can abort the session by closing the browser or your terminal.

You will now find an `FacebookPy` folder located at the above mentioned home folder.
Simply copy and paste the content of your logs folder into that workspace folder in order to assure that all your data is migrated.

> Please note that you only have to do this once. After that, you can get rid of your old, downloaded version of this repository since the FacebookPy folder in your home folder will now be the default location for your data.

### Set a _custom_ workspace folder

You can use `set_workspace(Settings)` function to set a custom **workspace** folder,

```python
from facebookpy import FacebookPy
from facebookpy import set_workspace

set_workspace("C:\\My\\Custom\\Path\\FacebookPy\\")

session = FacebookPy(...)
```

<details>
  <summary>
    <b>
      Rules 🔎
    </b>
  </summary>

**1**-) You have to set your custom **workspace** folder before instantiates _FacebookPy_.
**2**-) Your custom **workspace** folder must have `FacebookPy` (*_case sensitive_) word in its name.

* If your path does not have it,  
`set_workspace("C:\\Other\\Path\\InstaPie\\")`  
then your **workspace** folder will be named and made as,  
`"C:\\Other\\Path\\InstaPie\\FacebookPy\\"`  
👆🏼 `FacebookPy` directory will be added as a new subdirectory in there, and be your **workspace** folder.

* If your custom **workspace** folder name has a case-insensitive default name in it- `Facebookpy`, `facebookpy`, `instaPY`, etc.,  
`set_workspace("C:\\Other\\Path\\facebookpy2\\")`  
then your **workspace** folder will be,
`"C:\\Other\\Path\\FacebookPy2\\"`
as you can see, it normalizes name and sets the **workspace** folder.

##### _Why naming is so important?_

* It will help to easily adapt to the flexible _FacebookPy_ usage with that default formal name.

</details>

### Set a custom **workspace** folder _permanently_ with ease

If you want to set your custom **workspace** folder permanently and more easily, add a new environmental variable named `FACEBOOKPY_WORKSPACE` with the value of the path of the desired **workspace** folder to your operating system.  
Then that will be the default **workspace** folder in all sessions [unless you change it using `set_workspace(Settings)` or so].

### _Get_ the location of the workspace folder in use

If you ever want to **get** the _location_ of your **workspace** folder, you can use
the `get_workspace(Settings)` function,

```python
from facebookpy import FacebookPy
from facebookpy import smart_run
from facebookpy import set_workspace
from isntapy import get_workspace

set_workspace(path="C:\\Custom\\Path\\FacebookPy_super\\")

session = FacebookPy(username="abc", password="123")

with smart_run(session, Settings):
    # lots of code
    workspace_in_use = get_workspace(Settings)
    print(workspace_in_use["path"])
    # code code
```

Note that, `get_workspace(Settings)` is a function used _internally_ and makes a **workspace** folder [by default at home folder] if not exists.  
It means, you must use only the `set_workspace(Settings")` feature to set a custom **workspace** folder and not try to use `get_workspace(Settings)` for that purpose..

### Set a custom _location_

You can set any of the **custom** _locations_ you like, **any time**!  
E.g. setting the _location_ of the **database** file,

```python
from facebookpy import FacebookPy
from facebookpy import set_workspace


set_workspace(...)   # if you will set a custom workspace, set it before anything
Settings.db_location = "C:\\New\\Place\\DB\\facebookpy.db"

session = FacebookPy(...)
# code code
```

<details>
  <summary>
    <b>
      Restrictions 🔎
    </b>
  </summary>

**a**-) You cannot set a custom **workspace** folder after _FacebookPy_ has been instantiated;
_E.g. while instantiating _FacebookPy_, you make a logger at that given location and trying to change the_ `log_location` _really needs to restart the LOGGER adapter and make another logger instance, but it can be achieved in future_.

**b**-) If you set a custom **workspace** once and then set it again then your data locations will still use the previous locations:

```python
from facebookpy import FacebookPy
from facebookpy import set_workspace

# first time settings custom workspace folder
set_workspace("C:\\Users\\MMega\\Desktop\\My_FacebookPy\\")
# second time settings custom workspace folder
set_workspace("C:\\Users\\MMega\\Documents\\My_FacebookPy\\")

# locations of data files, e.g. chromedriver executable, logfolder, db will use first custom workspace locations.
# if you still want to change their location to second one, then do this one by one:
Settings.log_location = "C:\\Users\\MMega\\Documents\\My_FacebookPy\\logs\\"
DATABASE_LOCATION = "C:\\Users\\MMega\\Documents\\My_FacebookPy\\db\\facebookpy.db"
Settings.chromedriver_location = "C:\\Users\\MMega\\Documents\\My_FacebookPy\\logs\\chromedriver.exe"
```

As you can see, you have to use `set_workspace(Settings)` only once.
Why it is so difficult in those 👆🏼 regards?

* It's to preserve custom location assignments alive (`Settings.*`) cos otherwise setting another **workspace** would override any previously _manually_ assigned location(s).

</details>

## Extensions

[1. Session scheduling with Telegram](https://github.com/Tkd-Alex/Telegram-FacebookPy-Scheduling)

## Extra Information

### Custom chromedriver version

By default, FacebookPy downloads the latest version of the chromedriver.
Unless you need a specific version of the chromdriver, you're ready to go.

You have two options to install the version you want to have:

1. You can get the desired version of chromedriver binary by installing the same version of instapy-chromedriver package by pip [per their python version].
2. You can manually download and put the chromedriver binary into the assets folder [at their workspace] and then FacebookPy will always use it. You can find the specific versions of **chromedriver** for your OS [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Extract the .**zip** file and put it into the **assets** folder [at your **workspace** folder].

### Using one of the templates

If you're interested in what other users setup looks like, feel free to check out the `quickstart_templates` folder which includes several working setups with different features.

In order to use them, just copy the desired file and put it next to the `quickstart.py` file in the, what is called root, directory.

Finally simply adjust the username and any tags or firend lists before executing it.
That's it.

### How not to be banned

Built-in delays prevent your account from getting banned. 
However, excessive use of this tool may result in action blocks or permanent bans.
Use the Quota Supervisor feature to set some fixed limits for the bot for maximum safety.

### Chrome Browser

64-bit system is a requirement for current versions of chrome browser.

### Simulation

##### During indirect data retrieval, **simulation** happens to provide a _genuine_ activity flow triggered by a wise algorithm.

To **turn off** simulation or to **decrease** its occurrence frequency, use `set_simulation` setting:

```python
#use the value of `False` to permanently turn it off
session.set_simulation(enabled=False)

#use a desired occurrence percentage
session.set_simulation(enabled=True, percentage=66)
```

### Disable Image Loading

If you want to save some bandwidth, you can simply disable the image/video loading. This will lead to, if you watch FacebookPy running, not downloading and displaying any more images and videos.

> Note: This can save a tremendous amount of data. This is turned off by default (`False`).

To do this simply pass the `disable_image_load=True` parameter in the FacebookPy constructor like so:

```python
session = FacebookPy(username=facebook_username,
                  password=facebook_password,
                  headless_browser=False,
                  disable_image_load=True,
                  multi_logs=True)
```

### Using Multiple Chromedrivers

If you need multiple os versions of chromedriver just rename it like:

```bash
chromedriver_linux
chromedriver_osx
chromedriver_windows
```

### Changing DB or Chromedriver locations

If you want to change the location/path of either the DB or the chromedriver, simply head into the `facebookpy/settings.py` file and change the following lines.
Set these in facebookpy/settings.py if you're locating the library in the /usr/lib/pythonX.X/ directory.

```python
DATABASE_LOCATION = '/path/to/facebookpy.db'
Settings.chromedriver_location = '/path/to/chromedriver'
```

### Custom action delays

###### _After doing each action- like, comment, follow or unfollow, there is a sleep delay to provide smooth activity flow_.

##### But you can set a _custom_ sleep delay for each action yourself by using the `set_action_delays` setting!

```python
session.set_action_delays(enabled=True,
                           like=3,
                           comment=5,
                           follow=4.17,
                           unfollow=28)
```

_Now it will sleep `3` seconds **after putting every single like**, `5` seconds for every single comment and similarly for the others.._

You can also customize the sleep delay of _e.g._ **only the likes**:

```python
session.set_action_delays(enabled=True, like=3)
```

##### Wanna go smarter? - use `random_range(min, max)`

By just enabling `randomize` parameter, you can **enjoy** having random sleep delays at desired range, e.g.,

```python
session.set_action_delays(enabled=True, like=5.2, randomize=True, random_range=(70, 140))
```

_There, it will have a **random sleep delay between** `3.64` (_`70`% of `5.2`_) and `7.28`(_`140`% of `5.2`_) seconds _each time_ **after putting a like**._
* You can also put **only the max range** as- `random_range=(None, 200)`  
Then, the _min range will automatically be_ `100`%- the same time delay itself.  
And the random sleep delays will be between `5.2` and `10.4` seconds.  
* If you put **only the min range** as- `random_range=(70, None)`  
Then, the _max range will automatically be_ `100`%- the same time delay itself.  
And the random sleep delays will be between `3.64` and `5.2` seconds.  
* But if you **put `None` to both** min & max ranges as- `random_range=(None, None)`  
Then no randomization will occur and the sleep delay will always be `5.2` seconds.
* Heh! You **mistakenly put** min range instead of max range as- `random_range=(100, 70)`?  
No worries. It will automatically take the smaller number as min and the bigger one as max.
* Make sure to use the values **bigger than `0`** for the `random_rage` percentages.  
E.g. `random_range=(-10, 140)` is an invalid range and no randomization will happen.
* You can provide **floating point numbers** as percentages, too!  
`random_range=(70.7, 200.45)` will work greatly.

###### Note: There is a _minimum_ **default** delay for each action and if you enter a smaller time of delay than the default value, then it will **pick the default value**. You can turn that behaviour off with `safety_match` parameter.

```python
session.set_action_delays(enabled=True, like=0.15, safety_match=False)
```

_It has been held due to safety considerations. Cos sleeping a respective time after doing actions- for example ~`10` seconds after an unfollow, is very important to avoid possible temporary blocks and if you might enter e.g. `3` seconds for that without realizing the outcome..._

### How to avoid _python_ & **pip** confusion

Sometimes you have **multiple** _python_ installations in your system.  
Then you'll obviously have crazy aliases linked to _python_ and **pip** commands.  

For example, let's assume you have _python_ 2.7 & _python_ 3.7 installed in your system,  

| _python_ version | _python_ alias | **pip** alias |  
| ---------------- | -------------- | ------------- |
|       2.7        |     `py2`      |     `pip`     |
|       3.7        |    `python`    |     `pip3`    |

And once you install a package by the `pip` command and try to run it with `python` command, it will confuse you.  

Why? - cos,

* `pip` command is for _python_ 2.7  
* `python` command is for _python_ 3.7  

As you can see, it is,  
`python -m pip ...`  
rather than,  
`pip ...`

Using this style, you will never have to worry about what is the correct alias of the **pip** for you specific _python_ installation and all you have to know is just the _python_'s alias you use.  

### Pass arguments by CLI

###### It is recommended to pass your credentials from command line interface rather than storing them inside quickstart scripts.

Note that, arguments passed from the CLI has higher priorities than the arguments inside a **quickstart** script.  
E.g., let's assume you have,

```python
# inside quickstart script

session = FacebookPy(username="abc")
```

and you start that **quickstart** script as,

```erlang
python quickstart.py -u abcdef -p 12345678
```

Then, your _username_ will be set as `abcdef` rather than `abc`.  
_And obviously, if you don't pass the flag, it'll try to get that argument from the **quickstart** script [if any]_.

#### Currently these _flags_ are supported:

🚩 `-u` abc, `--username` abc

* Sets your username.

🚩 `-p` 123, `--password` 123

* Sets your password.

🚩 `-pd` 25, `--page-delay` 25

* Sets the implicit wait.

🚩 `-pa` 192.168.1.1, `--proxy-address` 192.168.1.1

* Sets the proxy address.

🚩 `-pp` 8080, `--proxy-port` 8080

* Sets the proxy port.

🚩 `-uf`, `--use-firefox`

* Enables Firefox.

🚩 `-hb`, `--headless-browser`

* Enables headless mode.

🚩 `-dil`, `--disable-image-load`

* Disables image load.

🚩 `-bsa`, `--bypass-suspicious-attempt`

* Bypasses suspicious attempt.

🚩 `-bwm`, `--bypass-with-mobile`

* Bypasses with mobile phone.

To get the list of available commands, you can type,

```erlang
python quickstart.py -h
# or
python quickstart.py --help
```

#### Examples

⚽ Let's quickly set your username and password right by CLI,

```erlang
python quickstart.py -u Toto.Lin8  -p 4X27_Tibor
# or
python quickstart.py --username Toto.Lin8  --password 4X27_Tibor
# or
python quickstart.py -u "Toto.Lin8"  -p "4X27_Tibor"
```

⚽ Enable Firefox,

```erlang
python quickstart.py -uf
# or
python quickstart.py --use-firefox
```

<details>
<summary>
  <b>
    Advanced 🔎
  </b>
</summary>

You can **pass** and then **parse** the **_custom_** CLI arguments you like right inside the **quickstart** script.  
To do it, open up your **quickstart** script and add these lines,

```python
# inside quickstart script

import argparse

my_parser = argparse.ArgumentParser()
# add the arguments as you like WHICH you will pass
# e.g., here is the simplest example you can see,
my_parser.add_argument("--my-data-files-name")
args, args_unknown = my_parser.parse_known_args()

filename = args.my_data_files_name

# now you can print it
print(filename)

# or open that file
with open(filename, 'r') as f:
    my_data = f.read()
```

After adding your custom arguments to the **quickstart** script, you can now **pass** them by CLI, comfortably,

```erlang
python quickstart.py --my-data-files-name "C:\\Users\\Anita\\Desktop\\data_file.txt"
```

> **NOTE**:  
Use **dash** in flag and parse them with **underscores**;  
E.g., we have used the flag as **`--my-data-files-name`** and parsed it as `args.`**`my_data_files_name`** ...

> **PRO**:
See `parse_cli_args()` function [used internally] inside the **util.py** file to write & parse more advanced flags.  
You can also import that function into your **quickstart** script and parse the **formal** flags into there to be used, as well.

```python
# inside quickstart script

from facebookpy.util import parse_cli_args


cli_args = parse_cli_args()
username = cli_args.username

print(username)
```

👆🏼👉🏼 as you will pass the _username_ like,

```erlang
python quickstart.py -u abc
```

</details>

<br />

---

## Credits

### Contributors

This project exists thanks to all the people who contribute.

### Backers

Thank you to all our backers! 🙏

### Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website.
