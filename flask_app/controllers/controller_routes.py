from flask import render_template, session, request, redirect
from flask_app import app

# MUST import model but make sure you change the name!!
from flask_app.models.model_user import User
from flask_app.models.model_history import History
from flask_app.models.model_tracker import Tracker


@app.route('/digiGolf/history')
def show_history():

    if 'uuid' not in session:
        return redirect('/')

    history = Tracker.get_all_trackers_user({'user_id': session['uuid']})
    single_user = User.get_one_by_id({'id': session['uuid']})
    return render_template('user_history.html', history=history, single_user=single_user)


@app.route('/digiGolf/locator')
def show_courses():

    if 'uuid' not in session:
        return redirect('/')

    return render_template('course_locator.html')


@app.route('/digiGolf/edit/<int:id>')
def show_edit_form(id):

    single_round = Tracker.get_one({'id': id})
    return render_template('round_edit.html', single_round=single_round)


@app.route('/digiGolf/create_tracker', methods=['POST'])
def process_update():

    Tracker.update_edit_form(request.form)
    return redirect('/digiGolf/history')
