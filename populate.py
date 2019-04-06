from lib import db
from lib.models import User, Post

u = User(username='john',
  first_name='John',
  last_name='Doe',
  email='john@example.com'
)
u.set_password('password')
db.session.add(u)
db.session.commit()

p = Post(
  title='Pugsley, a python user group webapp',
  body='Pugsley is a webapp written in Python',
  author=u
)
db.session.add(p)
db.session.commit()

u = User(
  username='susan',
  first_name='Susan',
  last_name='Smith',
  email='susan@example.com'
)
u.set_password('password')
db.session.add(u)
db.session.commit()

p = Post(
  title='Python is cool!',
  body='I love writing programs in Python',
  author=u
)
db.session.add(p)
db.session.commit()

users = User.query.all()
print(users)

posts = Post.query.all()
for p in posts:
  print(p.id, p.author.username, p.body)