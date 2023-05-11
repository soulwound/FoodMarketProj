from flask import Flask, render_template, request, session
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
    if 'phone-number' not in session:
        session['phone-number'] = request.form.get('name')
        session.modified = True
    else:
        session['phone-number'] = request.form.get('name')
        session.modified = True
        session.permanent = True
    print(session['phone-number'])
    return render_template('base.html', form=form)


@app.route('/sushi', methods=['GET', 'POST'])
def sushi():
    form = PhoneForm(request.form)
    if 'phone-number' not in session:
        session['phone-number'] = request.form.get('name')
    else:
        session['phone-number'] = request.form.get('name')
    print(session['phone-number'])
    return render_template('sushi.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
