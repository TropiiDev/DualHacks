from website import create_app
from flask_login import login_user, login_required, logout_user, current_user

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

def get_current_user():
    return current_user