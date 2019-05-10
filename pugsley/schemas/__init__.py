import graphene
import pugsley.schemas.users
import pugsley.schemas.blog
import pugsley.schemas.images

class MyMutations(users.MyMutations, blog.MyMutations, images.MyMutations):
    pass
class Query(users.Query, blog.Query, images.Query):
    pass

schema = graphene.Schema(query=Query, mutation=MyMutations)
