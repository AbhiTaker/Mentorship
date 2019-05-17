from django.db import models
from neomodel import StructuredNode, StringProperty, UniqueIdProperty, Relationship, RelationshipTo
from django_neomodel import DjangoNode

# Create your models here.

class Person(DjangoNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)

    mentors = RelationshipTo('Person', 'IS_MENTOR_OF')

    def get_mentee(self):
        results, columns = self.cypher("MATCH (n)-[:IS_MENTOR_OF]->(m) WHERE id(n) = {self} RETURN m")
        return [self.inflate(row[0]) for row in results]


