from django.contrib.auth.models import AbstractUser
from django.db import models    
import uuid


class User(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )
    email = models.EmailField(
        max_length=256,
        unique=True,
    )
    first_name = models.CharField(
        max_length=20
    )
    last_name = models.CharField(
        max_length=30
    )
    # cpf = CPFField('cpf', max_length=11)

    # address = models.OneToOneField(
    #     "adresses.Address",
    #     null=True,
    #     on_delete=models.CASCADE,
    #     related_name='user'
    # )  

    registered_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )