from pugsley import app, db
from pugsley.models import User, Post
import arrow

@app.template_filter('humanize')
def humanize(d):
  return arrow.get(d).humanize()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}

