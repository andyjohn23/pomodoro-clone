from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required,current_user
from .forms import UpdateProfile,TaskForm
from ..models import User,Task

@main.route('/')
def index():
	"""
	view root page function that returns the index page and its data
	"""

	return render_template('index.html')

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        user_id = current_user
        new_task_object = Task(post=post,user_id=user_id,title=title)
        new_task_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('create_task.html', form = form)
