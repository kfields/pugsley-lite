import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from pugsley.models import User, Post


class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):
    class Meta:
        node = UserNode


class PostNode(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (relay.Node, )


class PostConnection(relay.Connection):
    class Meta:
        node = PostNode


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_users = SQLAlchemyConnectionField(UserConnection)
    # Disable sorting over this field
    all_posts = SQLAlchemyConnectionField(PostConnection, sort=None)

schema = graphene.Schema(query=Query)
