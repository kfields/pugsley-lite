from flask import render_template, request, current_app
# from pugsley.graphql import schema
import pugsley.schemas as schemas
from flask_graphql import GraphQLView
from pugsley.graphql import bp
import os
import sys

path = os.path.join(os.path.dirname(__file__), "templates/playground.html")
templateFile = open(path)
TEMPLATE = templateFile.read()

bp.add_url_rule(
    '/graphql/',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schemas.schema,
        graphiql=True,
        graphiql_template=TEMPLATE
    )
)

@bp.route('/playground')
def playground():
    return render_template('playground.html')

