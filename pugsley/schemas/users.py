import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from pugsley import db
from pugsley.models.users import User
from pugsley.models.blog import Post
from pugsley.jwt import decode_auth_token

class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):
    class Meta:
        node = UserNode

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()

    id = graphene.ID()

    def mutate(self, info, username, email):
        print('CreateUser')
        print(id)
        user = User(
            username='joe',
            first_name='Joe',
            last_name='Jackson',
            email='joe@example.com',
            role='Reader',
            about_me='I am a Reader'
        )
        user.set_password(password)
        db.session.add(u)
        db.session.commit()

        return user.id

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        username = graphene.String()
        email = graphene.String()

    ok = graphene.Boolean()

    def mutate(self, info, id, username, email):
        print('UpdateUser')
        print(id)
        user = graphene.Node.get_node_from_global_id(info, id)
        print(user)
        user.username = username
        user.email = email
        user.save()
        ok = True

        return ok

class MyMutations(graphene.ObjectType):
    update_user = UpdateUser.Field()

class Query(graphene.ObjectType):
    # node = relay.Node.Field()
    user = relay.Node.Field(UserNode)
    all_users = SQLAlchemyConnectionField(UserConnection)
