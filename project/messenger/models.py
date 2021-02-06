from django.db import models


class Message(models.Model):
    """model for group of animals:
            mammals, birds, reptiles, amphibians, fish, invertebrates.
    """
    content = models.TextField()
    sender = models.ForeignKey('user.Customuser', related_name='sender',
                               on_delete=models.PROTECT)
    receiver = models.ForeignKey('user.Customuser', related_name='receiver',
                                 on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.content}"
