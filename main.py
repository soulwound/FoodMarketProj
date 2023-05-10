from flask import Flask, render_template, request
from wtforms import Form, validators
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Regexp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'so secret tsh'


class PhoneForm(Form):
    name = StringField("Телефон:", validators=[Regexp('/D')])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PhoneForm(request.form)
    return render_template('base.html', form=form)


@app.route('/sushi')
def sushi():
    return render_template('sushi.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
