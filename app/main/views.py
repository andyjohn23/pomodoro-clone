from flask import render_template,redirect,url_for
from flask_login import login_required,current_user
from . import main
from .forms import UpdateProfile,TaskForm
from ..models import User,Task

@main.route('/')
def index():
    Task = Task.query.all()
    return render_template('index.html', task = Task)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_task():
    form = TaskForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        user_id = current_user
        new_pitch_object = Task(post=post,user_id=current_user._get_current_object().id,title=title)
        new_pitch_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('create_task.html', form = form)		
