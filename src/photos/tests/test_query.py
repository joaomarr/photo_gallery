from project.schema import Query
from django.test.testcases import TestCase
import graphene

class TestQuery(TestCase):

    def test_photo(self):
        schema = graphene.Schema(query=Query)
        
        query = """
            query {
                photo {
                    id
                    file
                    uploadedAt
                }
            }
        """
        result = schema.execute(query)
        self.assertIsNone(result.errors)