import graphene
import authentication.schema as auth
import photos.schema as photos

class Query(
    auth.Query, photos.Query, graphene.ObjectType,
):
    ...

class Mutation(
    auth.Mutation, photos.Mutation, graphene.ObjectType,
):
    ...

schema = graphene.Schema(query=Query, mutation=Mutation)