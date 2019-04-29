import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from pugsley import db
from pugsley.models.users import User
from pugsley.models.blog import Post
from pugsley.jwt import decode_auth_token

class PostNode(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (relay.Node, )


class PostConnection(relay.Connection):
    class Meta:
        node = PostNode

class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        summary = graphene.String()
        body = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, id, title, summary, body):
        print('mutate')
        # get the JWT
        # token = info.context.headers.get('Authorization')
        token = decode_auth_token(info.context)
        print(token)
        # post = Post.query.get(id)
        post = graphene.Node.get_node_from_global_id(info, id)
        print(post)
        post.title = title
        post.summary = summary
        post.body = body
        db.session.commit()
        ok = True

        return ok

class MyMutations(graphene.ObjectType):
    update_post = UpdatePost.Field()

class Query(graphene.ObjectType):
    # node = relay.Node.Field()
    post = relay.Node.Field(PostNode)
    all_posts = SQLAlchemyConnectionField(PostConnection)
