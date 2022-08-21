import graphene
import authentication.schema as auth
import photos.schema as photos
import photo_gallery.schema as photo_gallery 

class Query(
    auth.Query, photos.Query, photo_gallery.Query, graphene.ObjectType,
):
    ...

class Mutation(
    auth.Mutation, photos.Mutation, photo_gallery.Mutation, graphene.ObjectType,
):
    ...

schema = graphene.Schema(query=Query, mutation=Mutation)