# This Python file uses the following encoding: utf-8

from flask import Flask, render_template, request
from StockInfo import StockInfo
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
# configure your application before initializing any extensions
app.debug = True
app.config['SECRET_KEY'] = 'secret'  # required for session cookies to work
app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
toolbar = DebugToolbarExtension(app)



@app.route('/')
def hello_world():
    return 'Hello My blog!'

@app.route('/search/', methods=['get', 'post'])
def hello_good():
    titles = [u'股票名称',
        u'今开盘', u'昨收盘',
        u'当前价', u'今最高', u'今最低',
        u'买入价', u'卖出价',
        u'成交量', u'成交额',
        u'买一', u'买一价', u'买二', u'买二价', u'买三', u'买三价', u'买四', u'买四价', u'买五', u'买五价',
        u'卖一', u'卖一价', u'卖二', u'卖二价', u'卖三', u'卖三价', u'卖四', u'卖四价', u'卖五', u'卖五价',
        u'日期', u'时间']

    if request.method == 'POST':
        StockCode = request.form["StockCode"]
        stock = StockInfo(StockCode)
        contents = stock.getInfo().split(",")
        del contents[-1]
        if contents:
            return render_template("index.html", titles=titles, contents=contents)
    return render_template("index.html", titles=titles, contents=None)

if __name__ == '__main__':
    app.debug = True
    app.run()
