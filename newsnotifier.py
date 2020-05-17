#!/usr/bin/env python3

from time import sleep
import notify2
#importing the module which we just created
import news_generate_return

# fetching news items
all_news = news_generate_return.topStories()

# initialise the d-bus connection
notify2.init("News Notifier")

# creating Notification object
#give icon image path icon=""
n = notify2.Notification(None, icon = "/")

# seting urgency level
n.set_urgency(notify2.URGENCY_NORMAL)

# seting timeout for a notification
n.set_timeout(10000)

for newsitem in all_news:

    # update notification data for Notification object
    n.update(newsitem['title'], newsitem['description'])

    # show notification on screen
    n.show()

    # short delay between notifications
    sleep(20)
