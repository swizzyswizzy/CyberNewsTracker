import feedparser
from flask import Flask
import json

app = Flask(__name__)


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

@app.route('/rssParser', methods=['GET'])
def rssfeed():
    articles = parseRssArticles(rssUrl)
    return articles

def main():
    app.run("0.0.0.0", "9000")


if __name__ == "__main__":
    main()
