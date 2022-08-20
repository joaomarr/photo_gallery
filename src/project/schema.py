import graphene
import authentication.schema as auth
import photos.schema as photos

class Query(
    auth.Query, graphene.ObjectType,
):
    ...

class Mutation(
    auth.Mutation, graphene.ObjectType,
):
    ...

schema = graphene.Schema(query=Query, mutation=Mutation)