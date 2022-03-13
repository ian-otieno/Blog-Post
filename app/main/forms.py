from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField("Update you bio info.", validators=[Required()])  
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    name = StringField('Name')
    comment = TextAreaField('Leave your comment', validators=[Required()])
    submit = SubmitField("Comment")

class PostForm(FlaskForm):
    title = StringField("Title", validators=[Required()])
    content = TextAreaField("Write your blog..", validators=[Required()])
    submit = SubmitField("Submit Blog")

class SubscriptionForm(FlaskForm):
    email= StringField("Enter your valid email address", validators=[Required()])
    submit = SubmitField('Subscribe')


