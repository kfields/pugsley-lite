from pugsley import app, db
from pugsley.models.users import User
from pugsley.models.blog import Post
import arrow

@app.template_filter('humanize')
def humanize(d):
  return arrow.get(d).humanize()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

