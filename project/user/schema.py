import graphene
from graphene_django.types import DjangoObjectType

from .models import CustomUser


# =============================================================== >> USER NODES
class UserNode(DjangoObjectType):
    class Meta:
        model = CustomUser


# # ================================================================ >> MUTATIONS
# class CreateUser(graphene.Mutation):
#     user = graphene.Field(UserNode)

#     class Arguments:
#         name = graphene.String()

#     def mutate(self, info, name):
#         cond = CustomUser(name=name)
#         cond.save()
#         return CreateUser(condition=cond)
