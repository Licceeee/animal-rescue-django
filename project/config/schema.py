import graphene

from animal.models import (Animal, AnimalGroup, AnimalType, AnimalCondition)
from animal.schema import (AnimalNode, AnimalGroupNode, AnimalTypeNode,
                           AnimalConditionNode)
from animal.schema import (CreateAnimalCondition, CreateAnimal)

from user.models import CustomUser
from user.schema import UserNode, CreateUser

# https://django-graphql-jwt.domake.io/en/latest/quickstart.html#installation


class Query(graphene.ObjectType):
    animals = graphene.List(AnimalNode)
    animal_types = graphene.List(AnimalTypeNode)
    animal_groups = graphene.List(AnimalGroupNode)
    animal_conditions = graphene.List(AnimalConditionNode)

    users = graphene.List(UserNode)

    def resolve_animals(self, info, **kwargs):
        return Animal.objects.all()

    def resolve_animal_types(self, info, **kwargs):
        return AnimalType.objects.all()

    def resolve_animal_groups(self, info, **kwargs):
        return AnimalGroup.objects.all()

    def resolve_animal_conditions(self, info, **kwargs):
        return AnimalCondition.objects.all()

    def resolve_users(self, info, **kwargs):
        return CustomUser.objects.all()


class Mutation(graphene.ObjectType):
    create_animal = CreateAnimal.Field()
    create_condition = CreateAnimalCondition.Field()
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


# query {
#     animals {
#         id
#         name
#         image
#         Type {
#             name
#         }
#         conditions {
#             name
#         }
#     }
# }
# mutation {
#     createCondition(name: "freak") {
#         condition {
#             id
#             name
#         }
#     }
# }
