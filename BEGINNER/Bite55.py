from collections import namedtuple

import feedparser

# cached version to have predictable results for testing
FEED_URL = "http://bit.ly/2IkFe9B"

Game = namedtuple('Game', 'title link')


def get_games():
    rss = feedparser.parse(FEED_URL)
    
    return [Game(post["title"], post["link"]) for post in rss.entries]
