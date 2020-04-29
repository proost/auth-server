from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    email = StringField('Email Address', [validators.Email(), validators.Required()])
    password = PasswordField('New Password', [validators.Required()])

class Registration(Form):
    name = StringField('Username', [validators.Required()])
    email = StringField('Email Address', [validators.Email(), validators.Required()])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
