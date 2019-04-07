from pugsley import db
from pugsley.models import User, Post

users = User.query.all()
for u in users:
  db.session.delete(u)
posts = Post.query.all()
for p in posts:
  db.session.delete(p)
db.session.commit()