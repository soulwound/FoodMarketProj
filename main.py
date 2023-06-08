import os
from flask import Flask, render_template, request, session, g, make_response
from wtforms import Form, validators
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Regexp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'so secret tsh'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "data.sqlite")}'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)


class PhoneForm(Form):
    name = StringField("Телефон:", validators=[Regexp('/D')])
    submit = SubmitField("Submit")


class Category(db.Model):  # таблица категорий
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), unique=True)
    product = db.relationship('Product', backref='category')

    def __repr__(self):
        return '<Categoty %r>' % self.name


class Product(db.Model):  # таблицы для продуктов
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), unique=True)
    price = db.Column(db.Numeric)
    sale_price = db.Column(db.Numeric)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))  #  вторичный ключ, ссылающийся на таблицу категорий
    calories = db.Column(db.Integer)
    proteins = db.Column(db.Numeric)
    fats = db.Column(db.Numeric)
    carbohydrates = db.Column(db.Numeric)
    weight = db.Column(db.Integer)
    ingredients = db.Column(db.String(128))

    def __repr__(self):
        return '<Product %r>' % self.title


@app.route('/set-cookie')
def set_cookie():
    context = {}
    context['text'] = 'Привет Мир!'
    name = 'nsjgjdskg'
    # получаем объект ответа
    resp = make_response(render_template('basic.html', content=context))
    # устанавливаем cookie 'user' со
    # значением user в объект ответа
    resp.set_cookie('user', name)
    # возвращаем измененный ответ
    return resp


@app.route('/get-cookie')
def get_cookie():
   # читаем cookie с именем 'user'
   name = request.cookies.get('phone')
   return f'<h1>Cookie user={name}</h1>'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PhoneForm(request.form)
    resp = make_response(render_template('base.html', form=form))
    if request.form.get('name') is not None:
        phone = request.form.get('name')
        resp.set_cookie('phone', phone)
    return resp


@app.route('/sushi', methods=['GET', 'POST'])
def sushi():
    form = PhoneForm(request.form)
    resp = make_response(render_template('sushi.html', form=form))
    if request.form.get('name') is not None:
        phone = request.form.get('name')
        resp.set_cookie('phone', phone)
    return resp

@app.route('/pizza', methods=['GET', 'POST'])
def pizza():
    form = PhoneForm(request.form)
    resp = make_response(render_template('pizza.html', form=form))
    if request.form.get('name') is not None:
        phone = request.form.get('name')
        resp.set_cookie('phone', phone)
    return resp


@app.errorhandler(404)
def page_not_found(e):
    form = PhoneForm(request.form)
    resp = make_response(render_template('404.html', form=form), 404)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')
