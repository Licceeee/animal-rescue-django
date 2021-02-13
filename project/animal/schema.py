import graphene
from graphene_django.types import DjangoObjectType

from .models import Animal, AnimalType, AnimalCondition, AnimalGroup


# ============================================================= >> ANIMAL NODES
class AnimalNode(DjangoObjectType):
    class Meta:
        description = "Representation of an animal"
        model = Animal


class AnimalGroupNode(DjangoObjectType):
    class Meta:
        description = "Representation of an animal group"
        model = AnimalGroup


class AnimalTypeNode(DjangoObjectType):
    class Meta:
        model = AnimalType
        only_fields = [
            "name",
            "icon",
            'animal_set',
            'get_animal_numbers'
        ]


class AnimalConditionNode(DjangoObjectType):
    class Meta:
        model = AnimalCondition


# ================================================================ >> MUTATIONS
class CreateAnimalCondition(graphene.Mutation):
    condition = graphene.Field(AnimalConditionNode)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, **data):
        cond = AnimalCondition(**data)
        cond.save()
        return CreateAnimalCondition(condition=cond)


class CreateAnimal(graphene.Mutation):
    animal = graphene.Field(AnimalNode)

    class Arguments:
        name = graphene.String()
        is_chipped = graphene.Boolean()
        chip = graphene.String()
        age_years = graphene.Int()
        age_months = graphene.Int()
        neutered = graphene.Boolean()
        # location
        # _type
        # post_type
        # conditions
        # image
        # gender

    @classmethod
    def mutate(self, info, **data):
        a = Animal(**data)
        a.save()
        return CreateAnimal(animal=a)
