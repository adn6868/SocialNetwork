from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    like = db.Column(db.Integer, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __str__(self):
        return 'Blog: id: % s\ntitle: % s\nauthor: % s\nlike: % s' \
            % (self.id, self.title, self.author, self.like)

    def getContent(self):
        return self.content


if __name__ == "__main__":
    sampleBlog = Blog()
    print(str(sampleBlog))
