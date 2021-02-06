import graphene
from graphene_django import DjangoObjectType

from .models import Animal, AnimalType, AnimalCondition


class AnimalAPI(DjangoObjectType):
    class Meta:
        model = Animal


class AnimalTypeAPI(DjangoObjectType):
    class Meta:
        model = AnimalType


class AnimalConditionAPI(DjangoObjectType):
    class Meta:
        model = AnimalCondition


class Query(graphene.ObjectType):
    animals = graphene.List(AnimalAPI)
    animal_types = graphene.List(AnimalTypeAPI)
    animal_conditions = graphene.List(AnimalConditionAPI)

    def resolve_animals(self, info, **kwargs):
        return Animal.objects.all()


schema = graphene.Schema(query=Query)


"""
    query {
        animals {
            id
            name
            image
            Type {
                name
            }
            conditions {
                name
            }
        }
    }
"""
