from django.test import TestCase

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any additional fields here
    pass

# Create your tests here.
