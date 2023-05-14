from flask import Flask, render_template, request, session, g, make_response
from wtforms import Form, validators
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'so secret tsh'

class PhoneForm(Form):
    name = StringField("Телефон:", validators=[Regexp('/D')])
    submit = SubmitField("Submit")


@app.route('/setcookie')
def setcookie():
    context = {}
    context['text'] = 'Привет Мир!'
    name = 'penis'
    # получаем объект ответа
    resp = make_response(render_template('basic.html', content=context))
    # устанавливаем cookie 'user' со
    # значением user в объект ответа
    resp.set_cookie('user', name)
    # возвращаем измененный ответ
    return resp


@app.route('/getcookie')
def getcookie():
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
    if 'phone-number' not in session:
        session['phone-number'] = request.form.get('name')
    else:
        session['phone-number'] = request.form.get('name')
    return render_template('sushi.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    form = PhoneForm(request.form)
    resp = make_response(render_template('404.html', form=form), 404)
    return resp


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0')
