from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phoneNumber = db.Column(db.String(13), nullable=False)
    employment = db.Column(db.String(22), nullable=False)

    def __str__(self):
        return 'User: id: % s\nname: % s\nemail: % s\nphoneNumber: % s\nemployment: % s' \
            % (self.id, self.name, self.email, self.phoneNumber, self.employment)


# if __name__ == "__main__":
#     bob = User()
#     print(str(bob))
