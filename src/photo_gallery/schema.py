import graphene

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.decorators import login_required
from graphene_file_upload.scalars import Upload
from authentication.schema import UserType

from photos.models import Photo
from photo_gallery.models import Post, Comment


class PostType(DjangoObjectType):
    """ Post type object """

    id = graphene.ID(required=True)
    likes = graphene.List(UserType)

    @staticmethod
    def resolve_likes(post, *args, **kwargs):
        return post.likes.all()

    class Meta:
        model = Post
        filter_fields = [
            'id',
            'owner',
            'is_approved',
        ]
        interfaces = (graphene.relay.Node, )


class CommentType(DjangoObjectType):
    """ Comment type object """
    
    class Meta:
        model = Comment
        interfaces = (graphene.relay.Node, )



class UploadPost(graphene.Mutation):
    """ Upload a Post """
    
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        file = Upload(required=True)

    def mutate(self, info, file, **kwargs):
        try:
            photo = Photo.objects.create(file=file)
            photo.save()

            post = Post.objects.create(file=photo, owner=info.context.user)
            post.save()
        except Exception as e:
            errors = [e]
            return UploadPost(errors=errors, success=False)

        return UploadPost(success=True)

class ToggleLikePost(graphene.Mutation):
    """ Toggle like in a post """
    
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        post_id = graphene.ID(required=True)

    def mutate(self, info, post_id, **kwargs):

        try:
            post = Post.objects.get(id=post_id)
            post_likes = post.likes.all()

            if info.context.user in post_likes:
                post.likes.remove(info.context.user)
                post.save()

                return ToggleLikePost(success=True)
            else:
                post.likes.add(info.context.user)
                post.save()
                return ToggleLikePost(success=True)
        except Exception as e:
            errors = [e]
            return ToggleLikePost(success=False, errors=errors)

class CommentPost(graphene.Mutation):
    """ Post a comment in the given post """
    
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        post_id = graphene.ID(required=True)
        text = graphene.String(required=True)

    def mutate(self, info, post_id, text, **kwargs):

        try:
            post = Post.objects.get(id=post_id)

            post.comments.add(info.context.user, through_defaults={'text': text})
            post.save()
            return CommentPost(success=True)
        except Exception as e:
            errors = [e]
            return CommentPost(success=False, errors=errors)

class PostApproval(graphene.Mutation):
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        post_id = graphene.ID(required=True)
        approve = graphene.Boolean(required=True)

    def mutate(self, info, post_id, approve, **kwargs):

        if info.context.user.is_staff:
            try:
                post = Post.objects.get(id=post_id)

                if approve == True:
                    post.is_approved = True
                    post.save()
                else:
                    post.delete()

                return PostApproval(success=True)
            except Exception as e:
                errors = [e]
                return PostApproval(success=False, errors=errors)

        errors = ['userIsNotStaff']
        return PostApproval(success=False, errors=errors)
        
class Mutation:
    upload_post = UploadPost.Field()
    toggle_like_post = ToggleLikePost.Field()
    comment_post = CommentPost.Field()
    post_approval = PostApproval.Field()

class Query:
    posts = DjangoFilterConnectionField(PostType)
    comments = graphene.List(CommentType)

    @login_required
    @staticmethod
    def resolver_posts(cls, info, **kwargs):
        return Post.objects.all()

