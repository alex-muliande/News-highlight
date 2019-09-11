# from app import app
import urllib.request, json
from .models import News, Articles

# News = news.News
# Articles = news.Articles

# query = 'politics'
api_key = None
base_url = None
article_url = None

def configure_request(app):
    global api_key, base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['BASE_URL']
    article_url = app.config['ARTICLE_URL']

def get_news_source():
    '''
    Function that gets the json response to our url request
    '''

    get_news_url = base_url+api_key
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
    return news_results


def process_results(news_results_list):
    news_results= []
    for news_item in news_results_list:

        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if name:
            news_obj = News(id, name, description,url,category,language,country)
            news_results.append(news_obj)
    return news_results


def get_article(id):
    get_article_url = article_url.format(id)

    article_result= None
    with urllib.request.urlopen(get_article_url+api_key) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)
        print (get_article_data)
        if get_article_response['articles']:
            article_list = get_article_response['articles']
            article_result = process_article(article_list)

    return article_result


def process_article(article_list):
    article_res= []
    for article in article_list:
            id = article.get('id')
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            publishedAt = article.get('publishedAt')
            content = article.get('content')
            if urlToImage:
                article_result = Articles(id, author,title, description,url,urlToImage,publishedAt,content)
                article_res.append(article_result)
    return article_res
