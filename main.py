from flask import Flask, render_template
from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'so secret tsh'

class PhoneForm(Form):
    name = StringField('Введите номер телефона', validators=[InputRequired()])
    submit = SubmitField('Отправить')


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/sushi')
def sushi():
    return render_template('sushi.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
