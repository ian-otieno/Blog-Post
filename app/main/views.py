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

@main.route('/new_post/new', methods=['GET','POST'])
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        title = post_form.title.data
        content = post_form.content.data
        user_id = current_user._get_current_object().id
        new_post = Post(user_id=user_id, title=title, content=content)
        new_post.save_post()

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('main.index'))

    return render_template ('new_post.html', post_form = post_form )

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
def new_Comment(id):
    comment_form = CommentsForm()
    post =Post.query.filter_by(id=id).all()
    comments = Comment.query.filter_by(post_id=id).all()
    if comment_form.validate_on_submit():
        comment=comment_form.comment.data
        name= comment_form.name.data
        new_comment=Comment(comment = comment,name=name, post_id=id)
        new_comment.save_comment()

        db.session.add(new_comment)
        db.session.commit()

    return render_template('comment.html', comment_form=comment_form, comments=comments,post=post)

@main.route('/update_post/<int:id>', methods=['GET', 'POST'])
@login_required
def updatePost(id):
    post = Post.query.get_or_404(id)
    post_form = PostForm()
    if post_form.validate_on_submit():
        post.title = post_form.title.data
        post.content = post_form.content.data
        user_id = current_user._get_current_object().id
       
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('main.index',user_id=user_id))
    elif request.method == 'GET':
        post_form.title.data = post.title
        post_form.content.data = post.content
       
    return render_template('edit_post.html',post=post, post_form=post_form)

