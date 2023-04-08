from flask_app import app
# import ****ALL**** controller files!!
from flask_app.controllers import controller_user
from flask_app.controllers import controller_tracker
from flask_app.controllers import controller_routes
# MUST BE AT BOTTOM
if __name__ == "__main__":
    app.run(debug=True)
