from pugsley import db
from pugsley.models.users import User
from pugsley.models.blog import Post

users = User.query.all()
print(users)

posts = Post.query.all()
for p in posts:
  print(p.id, p.author.username, p.body)