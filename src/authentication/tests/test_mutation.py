from faker import Faker
import graphene

from project.schema import Mutation
from django.contrib.auth import get_user_model
from graphene_file_upload.django.testing import GraphQLFileUploadTestCase
from graphql_jwt.testcases import JSONWebTokenTestCase

class TestMutation(JSONWebTokenTestCase):

    def register(self):
        fake = Faker()
        self.email = fake.email()

        schema = graphene.Schema(mutation=Mutation)
        result = schema.execute(
            """
                mutation ($username: String!, $email: String!, $password1: String!, $password2: String!) {
                    register(username: $username, password1: $password1, password2: $password2, email: $email) {
                        success,
                        errors,
                        token
                    }
                }
            """,
            variables={'username': fake.user_name(), 'email': self.email, 'password1': 'password', 'password2': 'password'}
        )

        self.assertIsNone(result.errors)
        try:
            self.user = get_user_model().objects.get(email=self.email)
            self.token = result.token
        except Exception as e:
            print(e)
        print(get_user_model().objects.all())

    def token_auth(self):
        result = self.schema.execute(
            """
                mutation ($email: String!, $password: String!) {
                    register(username: $username, password1: $password1, password2: $password2, email: $email) {
                        success,
                        errors,
                        token
                    }
                }
            """,
            variables={'email': self.email, 'password': 'password'}
        )

        self.assertIsNone(result.errors)
        self.assertEquals(result.token, self.token)

