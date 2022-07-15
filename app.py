from controller.user_controller import uc
from controller.reimbursement_controller import rc
from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(uc)
    app.register_blueprint(rc)

    app.run(port=8080, debug=True)
