import feedparser
from flask import Flask
import json

app = Flask(__name__)

# Run
# sudo flask --app app run --debug -p 80

#TODO 
# https://flask.palletsprojects.com/en/2.3.x/deploying/proxy_fix/

rssUrl = "https://www.lovemeow.com/feeds/feed.rss"

rssFeed = feedparser.parse(rssUrl)
def parseRssArticles(url, limit=None) -> dict:
    if limit == None:
        parsedArticles = []

        for article in rssFeed.entries:
            print("Title: ", article.title, "\n\n")
            print("Url: ", article.link, "\n\n")

            temp = article.summary_detail
            temp = temp['value']
            temp = temp.split('\n')
            temp = temp[0]
            print(temp)
            parsedArticles.append([article.link, article.title, temp])

        print(len(parsedArticles))
        parsedArticles = json.dumps(parsedArticles)
        return parsedArticles


def convertArticleListToHtml(article: list) -> str:
   ... 

@app.route('/rssfeed', methods=['GET'])
def rssfeed():
    articles = parseRssArticles(rssUrl)
    return articles



