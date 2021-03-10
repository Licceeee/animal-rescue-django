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
            "icon_name",
            'animal_set',
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
        print(data)
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
        animal_type = graphene.Int()
        # post_type
        # conditions
        # image
        # gender

    def mutate(self, info, **data):
        data['animal_type'] = AnimalType.objects.get(id=data['animal_type'])
        new_animal = Animal(**data)
        new_animal.save()
        return CreateAnimal(animal=new_animal)
