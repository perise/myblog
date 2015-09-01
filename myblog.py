# This Python file uses the following encoding: utf-8

from flask import Flask, render_template, request, session
from StockInfo import StockInfo
from flask_debugtoolbar import DebugToolbarExtension
from wtforms import Form, StringField, validators
from wtforms.csrf.session import SessionCSRF

app = Flask(__name__)
# configure your application before initializing any extensions
app.debug = True
app.config['SECRET_KEY'] = 'security'
app.config['CSRF_SECRET_KEY'] = 'pleasedonttellanyone'  # required for session cookies to work
app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
toolbar = DebugToolbarExtension(app)



class CSRFEnabledForm(Form):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = app.config['CSRF_SECRET_KEY']
        @property
        def csrf_context(self):
            return session

@app.route('/')
def hello_world():
    return 'Hello My blog!'

def stockcodecheck():
    def _stockcodecheck(form, field):
        if not str.isdigit(field.data.encode("ascii")) or len(field.data.encode("ascii")) is not 6:
            raise validators.ValidationError('Field must equal to six digital number')
    return _stockcodecheck

class LoginForm(CSRFEnabledForm):
    stockcode = StringField(u'股票代码', [validators.input_required(), stockcodecheck()])



@app.route('/search/', methods=['GET', 'POST'])
def hello_good():
    titles = [u'股票名称',
        u'今开盘', u'昨收盘',
        u'当前价', u'今最高', u'今最低',
        u'买入价', u'卖出价',
        u'成交量', u'成交额',
        u'买一', u'买一价', u'买二', u'买二价', u'买三', u'买三价', u'买四', u'买四价', u'买五', u'买五价',
        u'卖一', u'卖一价', u'卖二', u'卖二价', u'卖三', u'卖三价', u'卖四', u'卖四价', u'卖五', u'卖五价',
        u'日期', u'时间']
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        stock = StockInfo(form.stockcode.data)
        contents = stock.getInfo().split(",")
        del contents[-1]

        if contents:
            return render_template("index.html", titles=titles, contents=contents, form=form)
    return render_template("index.html", titles=titles, contents=None, form=form)

if __name__ == '__main__':
    app.debug = True
    app.run()
