# FacebookPy

[![MIT license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/socialbotspy/FacebookPy/blob/master/LICENSE)
[![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://travis-ci.org/socialbotspy/FacebookPy)

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
