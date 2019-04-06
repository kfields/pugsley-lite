from lib import db
from lib.models import User, Post

users = User.query.all()
print(users)

posts = Post.query.all()
for p in posts:
  print(p.id, p.author.username, p.body)