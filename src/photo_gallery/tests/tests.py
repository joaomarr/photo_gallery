import requests
import graphene

from faker import Faker
from project.schema import Mutation
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from graphene_file_upload.django.testing import GraphQLFileUploadTestCase
from graphql_jwt.testcases import JSONWebTokenTestCase

class TestMutation(GraphQLFileUploadTestCase, JSONWebTokenTestCase):

    def setUp(self):
        fake = Faker()
        self.schema = graphene.Schema(mutation=Mutation)

        user = get_user_model().objects.create(username=fake.user_name(), password=fake.password(), email=fake.email())
        self.client.authenticate(user)

    def test_upload(self):
        fake_img = requests.get('https://picsum.photos/845/480')
        test_file = SimpleUploadedFile(name='test.jpg', content=fake_img.content, content_type='image/jpeg')

        result = self.client.execute(
            """
                mutation ($file: Upload!){
                    uploadPost(file: $file) {
                        success
                        errors
                    }
                }
            """,
            variables={'file': test_file},
        )
        
        # This validates the status code and if you get errors
        self.assertIsNone(result.errors)


