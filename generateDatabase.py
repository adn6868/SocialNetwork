from DB import User, Blog
from Module0 import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app=app)

currentUser = User(name='Anh', email='anh@anh.com',
                   phoneNumber='123456789', employment='CEO')
db.session.add(currentUser)
