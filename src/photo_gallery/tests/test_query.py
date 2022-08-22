from faker import Faker
from project.schema import Query
from django.contrib.auth import get_user_model
from django.test.testcases import TestCase
import graphene

class TestQuery(TestCase):

    def setUp(self):
        fake = Faker()
        self.schema = graphene.Schema(query=Query)

        user = get_user_model().objects.create(username=fake.user_name(), password=fake.password(), email=fake.email())
        self.client.authenticate(user)

    def test_query_posts(self):
        schema = graphene.Schema(query=Query)
        
        query = """
            query {
                posts {
                    edges {
                        node {
                            id
                            username
                        }
                    }
              }
            }
        """
        result = schema.execute(query)
        self.assertIsNone(result.errors)

    def test_posts_filter(self):
        schema = graphene.Schema(query=Query)

        query = """
            query {
                posts(isApproved: false) {
                    edges {
                        node {
                            isApproved
                        }
                    }
              }
            }
        """

        result = schema.execute(query)
        self.assertIsNone(result.errors)