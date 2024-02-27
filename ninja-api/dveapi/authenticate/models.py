from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group, Permission
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class AccountUser(AbstractUser):
    pass

