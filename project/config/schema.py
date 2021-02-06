import graphene

import animal.schema


class Query(animal.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
