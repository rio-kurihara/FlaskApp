from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin


class User(UserMixin):
    ### add ###
    id = 'rio'
    username = 'rio'
    password_hash = generate_password_hash('password')
    ### add ###

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
