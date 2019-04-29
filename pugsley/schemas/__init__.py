import graphene
import pugsley.schemas.blog
import pugsley.schemas.users

class MyMutations(users.MyMutations, blog.MyMutations):
    pass
class Query(users.Query, blog.Query):
    pass

schema = graphene.Schema(query=Query, mutation=MyMutations)
