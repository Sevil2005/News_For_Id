from flask import Flask, render_template
from db import News, all_news
app = Flask(__name__)

@app.route('/')
@app.route('/news')
def news():
    return render_template('all_news.html', data = all_news)

@app.route('/news/<id>')
def one_news(id):
    return render_template('one_news.html', data = all_news, news_id = id)


if __name__ == '__main__':
    app.run(debug=True)