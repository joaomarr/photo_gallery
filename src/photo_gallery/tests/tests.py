import requests
import graphene

from project.schema import Mutation
from django.core.files.uploadedfile import SimpleUploadedFile
from graphene_file_upload.django.testing import GraphQLFileUploadTestCase

class MutationTestCase(GraphQLFileUploadTestCase):
   def test_upload(self):

        schema = graphene.Schema(mutation=Mutation)

        fake_img = requests.get('https://picsum.photos/845/480')
        test_file = SimpleUploadedFile(name='test.jpg', content=fake_img.content, content_type='image/jpeg')

        result = schema.execute(
            """
                mutation ($file: Upload!){
                    uploadPost(file: $file) {
                        success
                        errors
                    }
                }
            """,
            variables={'file': test_file}
        )
        
        # This validates the status code and if you get errors
        self.assertIsNone(result.errors)
