import graphene
import pugsley.schemas.users
import pugsley.schemas.blog
import pugsley.schemas.gallery

class MyMutations(users.MyMutations, blog.MyMutations, gallery.MyMutations):
    pass
class Query(users.Query, blog.Query, gallery.Query):
    pass

schema = graphene.Schema(query=Query, mutation=MyMutations)
