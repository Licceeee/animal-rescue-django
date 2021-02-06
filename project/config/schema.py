import graphene
from graphene_django.types import DjangoObjectType

from animal.models import Animal, AnimalType, AnimalCondition
from animal.schema import (AnimalNode, AnimalTypeNode, AnimalConditionNode,
                           CreateAnimalCondition)

from user.models import CustomUser
from user.schema import UserNode


class Query(graphene.ObjectType):
    animals = graphene.List(AnimalNode)
    animal_types = graphene.List(AnimalTypeNode)
    animal_conditions = graphene.List(AnimalConditionNode)

    users = graphene.List(UserNode)

    def resolve_animals(self, info, **kwargs):
        return Animal.objects.all()

    def resolve_animal_types(self, info, **kwargs):
        return AnimalType.objects.all()

    def resolve_animal_condistions(self, info, **kwargs):
        return AnimalCondition.objects.all()

    def resolve_users(self, info, **kwargs):
        return CustomUser.objects.all()


class Mutation(graphene.ObjectType):
    create_condition = CreateAnimalCondition.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)


# """
#     query {
#         animals {
#             id
#             name
#             image
#             Type {
#                 name
#             }
#             conditions {
#                 name
#             }
#         }
#     }
# """
