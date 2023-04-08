from flask import render_template, session, request, redirect
from flask_app import app, bcrypt

# MUST import model but make sure you change the name!!
from flask_app.models.model_user import User

# display route


@app.route('/')
def hello_user():
    return render_template('user_login.html')


@app.route('/digiGolf/register')
def user_create_display():
    return render_template('user_register.html')


@app.route('/user/process_create', methods=['POST'])
def user_create():
    # validate first
    if not User.validator(request.form):
        return redirect('/digiGolf/register')

    hash_pw = bcrypt.generate_password_hash(request.form['reg_password'])

    data = {
        **request.form,
        'password': hash_pw
    }

    id = User.create(data)
    session['uuid'] = id
    return redirect('/')


@app.route('/user/process_login', methods=['POST'])
def user_process_login():
    if not User.validator_login(request.form):
        return redirect('/')

    if 'uuid' not in session:
        return redirect('/')

    return redirect('/digiGolf/dashboard')


@app.route('/user/logout')
def logout_user():
    session.clear()
    return redirect('/')


@app.route('/digiGolf/dashboard')
def show_dashboard():
    if 'uuid' not in session:
        return redirect('/')

    single_user = User.get_one_by_id({'id': session['uuid']})

    return render_template('dashboard.html', single_user=single_user)
