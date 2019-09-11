from flask import render_template, request,redirect, url_for
from . import main
from ..request import get_news_source, process_results, get_article
from ..models import News,Articles

@main.route('/')
def index():
    results = get_news_source()
    return render_template('index.html', results = results)

@main.route('/news/<id>')
def news(id):
    article = get_article(id)
    print(article)
    return render_template('article.html',article =article)
