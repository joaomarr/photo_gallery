import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload
from graphql_jwt.decorators import login_required

from photos.models import Photo

class PhotoType(DjangoObjectType):
    """ Photo type object """

    class Meta:
        model = Photo
        fields = [
            'id',
            'file',
            'uploaded_at',
        ]

class UploadPhoto(graphene.Mutation):
    """ Upload Photo to S3 """
    
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        file = Upload(required=True)

    def mutate(self, info, file, **kwargs):
        try:
            photo_file = Photo.objects.create(file=file)
            photo_file.save()
        except:
            errors = ['unableToUploadFile']
            return UploadPhoto(errors=errors, success=False)

        return UploadPhoto(success=True)

class Mutation:
    upload_photo = UploadPhoto.Field()

class Query:
    photo = graphene.List(PhotoType)

    @staticmethod
    def resolve_photo(cls, info, **kwargs):
        return Photo.objects.all()