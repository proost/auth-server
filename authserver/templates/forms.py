from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    email = StringField('Email Address', [validators.Email(), validators.Required()])
    password = PasswordField('Password', [validators.Required()])
