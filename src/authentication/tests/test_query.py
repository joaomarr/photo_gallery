from project.schema import Query
from django.test.testcases import TestCase
import graphene

class TestQuery(TestCase):

    def test_users(self):
        schema = graphene.Schema(query=Query)
        
        query = """
            query {
                users {
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

    def test_users_filter(self):
        schema = graphene.Schema(query=Query)

        query = """
            query {
                users(isActive: true) {
                    edges {
                        node {
                            isActive
                        }
                    }
              }
            }
        """

        result = schema.execute(query)
        print(result)
        users = result.data['users']['edges']
        for user in users:
            self.assertEqual(user.node.isActive, True)
        self.assertIsNone(result.errors)