from controller.user_controller import uc
from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__)

    app.register_blueprint(uc)

    app.run(port=8080, debug=True)
