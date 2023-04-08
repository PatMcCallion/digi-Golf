from flask import render_template, session, request, redirect, url_for
from flask_app import app

# MUST import model but make sure you change the name!!
from flask_app.models.model_tracker import Tracker

# display route


@app.route('/digiGolf/tracker')
def display_tracker():
    return render_template('tracker_create.html')


@app.route('/digiGolf/create_tracker', methods=['POST'])
def create_tracker():
    data = {
        **request.form,
        'user_id': session['uuid']
    }
    Tracker.create_tracker_holes_null(data)
    return redirect('/digiGolf/tracker/confirm')


@app.route('/digiGolf/tracker/confirm')
def confirm_tracker():

    data = {
        'user_id': session['uuid']
    }

    confirm = Tracker.get_most_recent(data)

    return render_template('tracker_confirm.html', confirm=confirm)


# Hole 1
@app.route('/digiGolf/tracker/<int:id>/1')
def display_hole_1(id):
    return render_template('tracker_hole_1.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_1', methods=['POST'])
def update_hole_1(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_1(data)
    return redirect(url_for('display_hole_2', id=id))
#


# Hole 2
@app.route('/digiGolf/tracker/<int:id>/2')
def display_hole_2(id):
    return render_template('tracker_hole_2.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_2', methods=['POST'])
def updated_hole_2(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_2(data)
    return redirect(url_for('display_hole_3', id=id))
#


# Hole 3
@app.route('/digiGolf/tracker/<int:id>/3')
def display_hole_3(id):
    return render_template('tracker_hole_3.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_3', methods=['POST'])
def update_hole_3(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_3(data)
    return redirect(url_for('display_hole_4', id=id))
#


# Hole 4
@app.route('/digiGolf/tracker/<int:id>/4')
def display_hole_4(id):
    return render_template('tracker_hole_4.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_4', methods=['POST'])
def update_hole_4(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_4(data)
    return redirect(url_for('display_hole_5', id=id))
#


# Hole 5
@app.route('/digiGolf/tracker/<int:id>/5')
def display_hole_5(id):
    return render_template('tracker_hole_5.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_5', methods=['POST'])
def update_hole_5(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_5(data)
    return redirect(url_for('display_hole_6', id=id))
#


# Hole 6
@app.route('/digiGolf/tracker/<int:id>/6')
def display_hole_6(id):
    return render_template('tracker_hole_6.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_6', methods=['POST'])
def update_hole_6(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_6(data)
    return redirect(url_for('display_hole_7', id=id))
#


# Hole 7
@app.route('/digiGolf/tracker/<int:id>/7')
def display_hole_7(id):
    return render_template('tracker_hole_7.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_7', methods=['POST'])
def update_hole_7(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_7(data)
    return redirect(url_for('display_hole_8', id=id))
#


# Hole 8
@app.route('/digiGolf/tracker/<int:id>/8')
def display_hole_8(id):
    return render_template('tracker_hole_8.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_8', methods=['POST'])
def update_hole_8(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_8(data)
    return redirect(url_for('display_hole_9', id=id))
#


# Hole 9
@app.route('/digiGolf/tracker/<int:id>/9')
def display_hole_9(id):
    return render_template('tracker_hole_9.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_9', methods=['POST'])
def update_hole_9(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_9(data)
    return redirect(url_for('display_hole_10', id=id))
#


# Hole 10
@app.route('/digiGolf/tracker/<int:id>/10')
def display_hole_10(id):
    return render_template('tracker_hole_10.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_10', methods=['POST'])
def update_hole_10(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_10(data)
    return redirect(url_for('display_hole_11', id=id))
#


# Hole 11
@app.route('/digiGolf/tracker/<int:id>/11')
def display_hole_11(id):
    return render_template('tracker_hole_11.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_11', methods=['POST'])
def update_hole_11(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_11(data)
    return redirect(url_for('display_hole_12', id=id))
#


# Hole 12
@app.route('/digiGolf/tracker/<int:id>/12')
def display_hole_12(id):
    return render_template('tracker_hole_12.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_12', methods=['POST'])
def update_hole_12(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_12(data)
    return redirect(url_for('display_hole_13', id=id))
#


# Hole 13
@app.route('/digiGolf/tracker/<int:id>/13')
def display_hole_13(id):
    return render_template('tracker_hole_13.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_13', methods=['POST'])
def update_hole_13(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_13(data)
    return redirect(url_for('display_hole_14', id=id))
#


# Hole 14
@app.route('/digiGolf/tracker/<int:id>/14')
def display_hole_14(id):
    return render_template('tracker_hole_14.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_14', methods=['POST'])
def update_hole_14(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_14(data)
    return redirect(url_for('display_hole_15', id=id))
#


# Hole 15
@app.route('/digiGolf/tracker/<int:id>/15')
def display_hole_15(id):
    return render_template('tracker_hole_15.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_15', methods=['POST'])
def update_hole_15(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_15(data)
    return redirect(url_for('display_hole_16', id=id))
#


# Hole 16
@app.route('/digiGolf/tracker/<int:id>/16')
def display_hole_16(id):
    return render_template('tracker_hole_16.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_16', methods=['POST'])
def update_hole_16(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_16(data)
    return redirect(url_for('display_hole_17', id=id))
#


# Hole 17
@app.route('/digiGolf/tracker/<int:id>/17')
def display_hole_17(id):
    return render_template('tracker_hole_17.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_17', methods=['POST'])
def update_hole_17(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_17(data)
    return redirect(url_for('display_hole_18', id=id))
#


# Hole 18
@app.route('/digiGolf/tracker/<int:id>/18')
def display_hole_18(id):
    return render_template('tracker_hole_18.html', id=id)


@app.route('/digiGolf/tracker/<int:id>/update_18', methods=['POST'])
def update_hole_18(id):

    data = {
        **request.form,
        'id': id
    }
    Tracker.updated_hole_18(data)
    return redirect(url_for('round_complete', id=id))
#


@app.route('/digiGolf/tracker/<int:id>/complete')
def round_complete(id):

    data = {
        'id': id
    }
    score = Tracker.get_one(data)
    return render_template('round_complete.html', score=score)
