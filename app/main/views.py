from ..request import get_random_quote
from flask import render_template, request, redirect ,url_for ,abort,flash
from . import main
from .. import db, photos
from flask_login import login_required, current_user
from app.models import Post, User,Comment, Subscriber
from .forms import PostForm,CommentsForm, SubscriptionForm, UpdateProfile
from  ..email import mail_message


@main.route('/')
@main.route('/index')
def index():
    '''
    view root page that returns the view index page and its data
    '''
    
    posts = Post.get_all_posts()
    quote = get_random_quote()
    title = 'Bloggers'
    return render_template('index.html', posts = posts, current_user = current_user, quote=quote, title=title)

