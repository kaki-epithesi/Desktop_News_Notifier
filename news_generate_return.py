
import requests
import xml.etree.ElementTree as ET

# url of news rss feed
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

#function to load rss feed
def loadRSS():
# creating HTTP request response object
    resp = requests.get(RSS_FEED_URL)
# returning response content
    return resp.content
#function to parse xml format rss feed
def parseXML(rss):
    # create element tree root object
    root = ET.fromstring(rss)
    # create empty list for news items
    newsitems = []
    # iterate news items
    for item in root.findall('./channel/item'):
        news = {}
        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            elif child.text is not None:
                news[child.tag] = child.text.encode('utf8')
        newsitems.append(news)

    # return news items list
    return newsitems
#function generating and returning news items
def topStories():
    
    # load rss feed
    rss = loadRSS()

    # parse XML
    newsitems = parseXML(rss)
    return newsitems
