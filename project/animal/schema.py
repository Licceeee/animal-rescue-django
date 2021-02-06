import graphene
from graphene_django.types import DjangoObjectType

from .models import Animal, AnimalType, AnimalCondition


# ============================================================= >> ANIMAL NODES
class AnimalNode(DjangoObjectType):
    class Meta:
        model = Animal


class AnimalTypeNode(DjangoObjectType):
    class Meta:
        model = AnimalType


class AnimalConditionNode(DjangoObjectType):
    class Meta:
        model = AnimalCondition


# ================================================================ >> MUTATIONS
class CreateAnimalCondition(graphene.Mutation):
    condition = graphene.Field(AnimalConditionNode)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        cond = AnimalCondition(name=name)
        cond.save()
        return CreateAnimalCondition(condition=cond)