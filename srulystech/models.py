from srulystech import db
from datetime import datetime

class Post(db.Model):
    postId  =db.Column(db.Integer,primary_key=True) 
    picture = db.Column(db.String(30))
    title = db.Column(db.String(120), nullable= False)
    description = db.Column(db.String(400))
    datePosted = db.Column(db.DateTime,nullable= False,default=datetime.utcnow)
    color = db.Column(db.String(20),default='primary')
    link = db.Column(db.String(120))

    def __repr__(self):
        return f"Post('{self.picture}','{self.title}','{self.description[:20]}..',{self.link})"
    