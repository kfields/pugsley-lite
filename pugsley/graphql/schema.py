import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from pugsley import db
from pugsley.models import User, Post


class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):
    class Meta:
        node = UserNode

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        username = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, id, username, email):
        print('mutate')
        print(id)
        user = graphene.Node.get_node_from_global_id(info, id)
        print(user)
        user.username = username
        user.email = email
        user.save()
        ok = True

        return ok

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
        body = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, id, title, body):
        print('mutate')
        print(id)
        # post = Post.query.get(id)
        post = graphene.Node.get_node_from_global_id(info, id)
        print(post)
        post.title = title
        post.body = body
        db.session.commit()
        ok = True

        return ok

class MyMutations(graphene.ObjectType):
    update_user = UpdateUser.Field()
    update_post = UpdatePost.Field()

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    user = relay.Node.Field(UserNode)
    post = relay.Node.Field(PostNode)
    all_users = SQLAlchemyConnectionField(UserConnection)
    all_posts = SQLAlchemyConnectionField(PostConnection)

schema = graphene.Schema(query=Query, mutation=MyMutations)
