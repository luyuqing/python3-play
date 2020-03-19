from flask import Flask, render_template, flash, request
from flask.ext.wtf import Form
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'well-secret-password'


class MyForm(Form):
    name = StringField(label='Name', validators=[DataRequired()])
    starting = SubmitField(label='Starting')
    ending = SubmitField(label='Ending')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()

    if form.validate_on_submit():
        print("Starting data Value : {value}".format(value=form.starting.data))
        print("Ending data Value : {value}".format(value=form.ending.data))
        flash(
            "You submitted name {name} via button {button}".format(
                name=form.name.data,
                button="Starting" if form.starting.data else "Ending"
            )
        )

        return render_template('index.html', form=form)

    if form.errors:
        for error_field, error_message in form.errors.iteritems():
            flash("Field : {field}; error : {error}".format(field=error_field, error=error_message))

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)